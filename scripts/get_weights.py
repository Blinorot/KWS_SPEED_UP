import gzip
import os
import shutil
from pathlib import Path

import gdown
from speechbrain.utils.data_utils import download_file

URL_LINKS = {
    "saved_data": "https://drive.google.com/u/0/uc?id=1PPSwMPzajbcoeBoRagVADQ04eE_bGLr8&export=download",
}

def main():
    data_dir = Path(__file__).absolute().resolve().parent.parent
    data_dir = data_dir / "saved"

    for name, url in URL_LINKS.items():
        print(f"Loading {name}")
        arc_path = data_dir / f'{name}.zip'
        if not arc_path.exists():
            gdown.download(URL_LINKS[name], str(arc_path))
            shutil.unpack_archive(str(arc_path), str(data_dir))
            os.remove(arc_path)
    

if __name__ == "__main__":
    main()
