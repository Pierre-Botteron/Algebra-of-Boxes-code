# Algebra-of-Boxes-code
This is the GitHub page associated to the manuscript "Algebra of Nonlocal Boxes and Collapse of Communication Complexity" from Pierre Botteron, Anne Broadbent, Réda Chhaibi, Ion Nechita, and Clément Pellegrini.

## Content

The repository is structured as follows. We only describe the most important files for a new user.

```bash
./

|-- nonlocal-boxes/: Core of package. 
|  |-- `__init__.py`: Init file.
|  |-- `evaluate.py`: Package of the function to evaluate, using PyTorch.
|  |-- `utils.py`: Package of the constants, using PyTorch.

|-- ipynb/: Contains Python notebooks which demonstrate how the code works.
|  |-- `Draw-new-collapsing-boxes.ipynb`: Drawing the new collapsing found using Algorithm 4, see Figure 10.
|  |-- `Draw-Orbit.ipynb`: Drawing the Orbit of a box P in different slices.

|-- `README.md`: This file.

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
There is a variable `nb_columns` in `non_local_boxes/evaluate.py` that can be set depending on the algo that is running: 
- for optimisation codes, set it to a large number, e.g. 1000; 
- for evaluation codes, set it to 1.

## Credits
Later.