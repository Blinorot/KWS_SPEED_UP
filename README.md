# KWS SPEED UP

This is a repository for KWS homework of HSE DLA Course. The task is to speed up the original model by a factor of 10 and implement streaming framework.

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

### Weights

To download weights run the following command:

```bash
python3 scripts/get_weights.py
```

## Authors

-   Petr Grinberg

## License

This project is licensed under the [MIT](LICENSE) License - see the [LICENSE](LICENSE) file for details.

## Credits

Base KWS model and weights were taken from [DLA Seminar 6](https://github.com/markovka17/dla/blob/2022/week06/seminar.ipynb) and [DLA HW2](https://github.com/markovka17/dla/blob/2022/hw2_kws/kws.pth).
