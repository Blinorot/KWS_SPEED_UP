import gzip
import os
import shutil
from pathlib import Path

import gdown
from speechbrain.utils.data_utils import download_file

URL_LINKS = {
    "kws": "https://github.com/markovka17/dla/raw/2022/hw2_kws/kws.pth",
}

def main():
    data_dir = Path(__file__).absolute().resolve().parent.parent
    data_dir = data_dir / "saved"
    original_data_dir = data_dir / "original"
    speed_up_data_dir = data_dir / "speed_up"
    original_data_dir.mkdir(exist_ok=True, parents=True)
    speed_up_data_dir.mkdir(exist_ok=True, parents=True)

    for name, url in URL_LINKS.items():
        if name == "kws":
            dir_type = "original"
            dir = original_data_dir
        else:
            dir_type = "speed_up"
            dir = speed_up_data_dir

        final_path = dir / (name + ".pth")

        if not final_path.exists():
            print(f"Loading {name}")
            if dir_type == "speed_up":
                gdown.download(URL_LINKS[name], str(final_path))
            else:
                download_file(URL_LINKS[name], str(final_path))
    

if __name__ == "__main__":
    main()
