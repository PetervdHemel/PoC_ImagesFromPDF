# Quick PoC pikepdf extracting images

> Takes an input file path towards a `.pdf` file, and extracts all available images. Proof of concept for using in FastAPI, used for refactoring.

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Installation

Make sure you have [Python 3.10](https://www.python.org/downloads/) installed.

> **Python 3.11 as of now is not yet supported by pikepdf.**

Clone the repository to your directory of choice. If you use [git](https://git-scm.com/downloads) you can follow these commands in order:

```sh
cd [path/to/directory]
```

```sh
git clone https://github.com/PetervdHemel/PoC_ImagesFromPDF.git
```

---
Next up, create and activate a [virtual environment](https://docs.python.org/3/library/venv.html) (venv):

```sh
py -3.10 -m venv venv
```

**OS X and Linux**

```sh
./venv/bin/activate
```

```sh
pip3 install -r requirements.txt
```

**Windows**

```sh
.\venv\Scripts\activate
```

```sh
python -m pip install -r requirements.txt
```

## Run the Application

> Make sure you have a valid pdf file path linked in main.py source code.

**OS X and Linux**

```sh
python ./main.py
```

**Windows**

```sh
python .\main.py
```

> Standard output is `.\imgs\` directory.
