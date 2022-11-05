import argparse
import logging
import multiprocessing as mp

import torch
from torchaudio.io import StreamReader

logger = logging.getLogger(__file__)


def audio_stream(queue: mp.Queue, args):
    """
    Learn more about how to install and use streaming audio here
    https://pytorch.org/audio/stable/tutorials/streaming_api2_tutorial.html
    """

    streamer = StreamReader(src=args.src, format=args.format)
    streamer.add_basic_audio_stream(frames_per_chunk=args.chunk, sample_rate=args.rate)
    stream_iterator = streamer.stream(-1, 1)

    logger.info("Start audio streaming")
    while True:
        (chunk_,) = next(stream_iterator)
        logger.info("Put chunk to queue")
        queue.put(chunk_)


if __name__ == "__main__":
    args = argparse.ArgumentParser(description="Streaming KWS")
    args.add_argument(
        "-s",
        "--src",
        default="hw:0",
        type=str,
        help="Source for Stream Reader: hw:0 for linux (default), :0 for mac",
    )
    args.add_argument(
        "-f",
        "--format",
        default="alsa",
        type=str,
        help="Format for Stream Reader: alsa for linux (default), avfoundation for mac",
    )
    args.add_argument(
        "-c",
        "--chunk",
        default=4000,
        type=int,
        help="Frames per chunk value for Stream Reader (default 4000)",
    )
    args.add_argument(
        "-r",
        "--rate",
        default=16000,
        type=int,
        help="Sample rate value for Stream Reader (default 16000)",
    )

    args.add_argument(
        "-m",
        "--model",
        default="saved/jit/original/kws.pth",
        type=str,
        help="Path to kws model. Original model is used by default (saved/jit/original/kws.pth)",
    )

    args = args.parse_args()

    model = torch.jit.load(args.model, map_location='cpu').eval()

    ctx = mp.get_context("spawn")
    chunk_queue = ctx.Queue()
    streaming_process = ctx.Process(target=audio_stream, args=(chunk_queue, args))

    streaming_process.start()
    while True:
        try:
            chunk = chunk_queue.get()
            chunk = chunk.sum(dim=-1) # to mono
            chunk = chunk.view(1, -1)
            print(f"{chunk.shape=}")

            with torch.inference_mode():
                result = model(chunk)
            
            print(result)

            if result > 0.7:
                print("DETECTED KEY WORD")

        except KeyboardInterrupt:
            break
        except Exception as exc:
            raise exc

    streaming_process.join()
