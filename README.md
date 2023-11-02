# Algebra-of-Boxes-code
This is the GitHub page associated to the manuscript [Algebra of Nonlocal Boxes and Collapse of Communication Complexity] from Pierre Botteron, Anne Broadbent, Réda Chhaibi, Ion Nechita, and Clément Pellegrini.

## Content

The repository is structured as follows. We only describe the most important files for a new user.

```bash
./
|-- nonlocal-boxes/: Core of package. 
|  |-- `__init__.py`: init file.
|  |-- `evaluate.py`: package of the function to evaluate, using PyTorch.
|  |-- `utils.py`: package of the constants, using PyTorch.
|-- ipynb/: Contains Python notebooks which demonstrate how the code works.
|  |-- `Draw-new-collapsing-boxes.ipynb`: Draw the new collapsing found using Algorithm 4, see Figure 10.
|-- `README.md`: This file
```

## Installation

1. Create new virtual environment `.venv_boxes`:

```bash
$ python3 -m venv .venv_boxes
```

2. If needed:

```bash
$ sudo apt install python3-venv
```

3. Activate virtual environment:

```bash
$ source .venv_boxes/bin/activate
```

4. Upgrade pip, wheel and setuptools 

```bash
$ pip install --upgrade pip
$ pip install --upgrade setuptools
$ pip install wheel
```

5. Install the `non_local_boxes` package.

```bash
$ python setup.py develop
```

6. (Optional) In order to use Jupyter with this virtual environment .venv_boxes (see https://janakiev.com/blog/jupyter-virtual-envs/ for details):

```bash
$ pip install ipykernel
$ python -m ipykernel install --user --name=.venv_boxes
```

## Configuration
Nothing to do

## Credits
Later