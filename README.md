# KWS SPEED UP

This is a repository for KWS homework of HSE DLA Course. The task is to speed up and compress the original model (CRNN) by a factor of 10 and implement streaming framework.

## Getting Started

These instructions will help you to run a project on your machine.

### Installation

Clone the repository into your local folder:

```bash
cd path/to/local/folder
git clone https://github.com/Blinorot/KWS_SPEED_UP.git
```

Install `python 3.9.7.` for `pyenv` and create virtual environment:

```bash
pyenv install 3.9.7
cd path/to/cloned/KWS_SPEED_UP/project
~/.pyenv/versions/3.9.7/bin/python -m venv kws_env
```

Install required python packages to python environment:

```bash
source kws_env/bin/activate
pip install -r requirements.txt
```

It's also recommended to install Jupyter-extensions or open notebook in Colab in order to have table of contents.

Install ffmpeg package (system, not python) to run the streaming script and test the model.

### Weights

To download weights run the following command:

```bash
python3 scripts/get_weights.py
```

The weights will be downloaded to `saved` folder, which structure is the following:

-   `torch` subfolder contains different model checkpoints for basic non-streaming model

-   `jit` subfolder contains streaming versions

Each subfoled is divided into two parts: `original` and `speed_up`. The first one contains original models, and the second one -- after compression\speed_up methods.

## Compression\Speed Up Methods

The notebook `KWS_SPEED_UP.ipynb` contains implementation of the following speed_up or
compression methods:

-   Unstructured Pruning
-   Structured Pruning of Conv2d, Attention, Single-layer GRU (hidden pruning), GRU (input pruning)
-   Basic Distillation
-   Layer-wise Distillation with Constant\Learnable Projections (projection from student's to teacher's domain)
-   Layer-wise Distillation with Constant\Learnable\Pre-trained([TED](https://arxiv.org/abs/2210.01351)-like) Projections (projection from teacher's to student's domain)
-   QAT for Conv2d
-   Dynamic Quantization for GRU\Linear
-   DepthWise Separable Convolution instead of Conv2d

The final model has `speed_up_rate=9.315`, `compression_rate=8.3044`. It's PyTorch version is located in `saved/torch/speed_up/pruned_conv_distil_ft.pth` (PyTorch version needs extra Dynamic Quantization after loading, see sections 9 and 10 of the notebook). It's streaming JIT version is located in `saved/jit/speed_up/distil_kws_buffer_{1,2,3}.pth` with different buffer sizes (1 is recommended).

## Streaming

`stream.py` allows users to test the model on their own laptops with their microphones. To run the script run the following command:

```bash
python3 stream.py -s STREAM_READER_SOURCE_DEVICE\
     -f STREAM_READER_FORMAT\
     -m PATH_TO_MODEL_CHECKPOINT\
     -c CHUNK_SIZE\
     -r SAMPLE_RATE
```

The source and format depends on your system settings. See `python3 stream.py -h` and ffmpeg website for details.

The keyword is `sheila`.

**Note:** the command may sometimes lag for first 1-5 seconds at the start.

## Authors

-   Petr Grinberg

## License

This project is licensed under the [MIT](LICENSE) License - see the [LICENSE](LICENSE) file for details.

## Credits

Base KWS model and weights were taken from [DLA Seminar 6](https://github.com/markovka17/dla/blob/2022/week06/seminar.ipynb) and [DLA HW2](https://github.com/markovka17/dla/blob/2022/hw2_kws/kws.pth).
