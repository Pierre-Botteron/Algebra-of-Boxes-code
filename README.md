# Algebra-of-Boxes-code

## Associated Manuscript
This GitHub page is associated to the following manuscript 
- <b>Manuscript:</b> [&#128195; Algebra of Nonlocal Boxes and the Collapse of Communication Complexity](https://arxiv.org/abs/2312.00725)
- <b>Authors:</b> 
[&#128100; Pierre Botteron](https://pierre-botteron.github.io/), 
[&#128100; Anne Broadbent](https://mysite.science.uottawa.ca/abroadbe/), 
[&#128100; Reda Chhaibi](https://www.math.univ-toulouse.fr/~rchhaibi/), 
[&#128100; Ion Nechita](https://ion.nechita.net/about/), and 
[&#128100; Clément Pellegrini](https://www.math.univ-toulouse.fr/~pellegri/).

## Content


```
./
|__ nonlocal-boxes/: Core of package. 
|  |-- `__init__.py`: Init file.
|  |-- `evaluate.py`: Package of the function to evaluate, using PyTorch.
|  |-- `utils.py`: Package of the constants, using PyTorch.
|  |-- `Vectorization-of-the-code.pdf`: Explanations of the vectorization.
|__ ipynb/: Contains Python notebooks which demonstrate how the code works.
|-- `README.md`: This file.
```
#### Details of the Python notebooks (folder `ipynb/`):

| File name | Description | Link with the manuscript |
| :------------ |:---------------| :-----|
| `Coordinates_extremal_NS_boxes.ipynb` | Drawing the 24 extremal boxes of $\mathcal{NS}$ in terms of $2$ games. ![24 extremal points of NS](tree/main/Images/24-extremal-points-of-NS.png) | Figures&nbsp;11 and&nbsp;8 |
| `Draw-new-collapsing-boxes.ipynb` | Drawing new collapsing boxes using Algorithm&nbsp;4. ![Collapsing area from Algo 4](https://github.com/Pierre-Botteron/Algebra-of-Boxes-code/tree/main/Images/Collapsing-area-from-Algo-4.png) | Figure&nbsp;10 |
| `Draw-Orbit.ipynb` | Drawing the Orbit of a box $\mathtt{P}$ in some slices. ![Orbit BS09](https://github.com/Pierre-Botteron/Algebra-of-Boxes-code/tree/main/Images/Orbit-BS09.png) | Figures&nbsp;7 and&nbsp;8, Appendix&nbsp;A |
| `Histograms.ipynb` | Drawing the histograms of the ouputs of Algorithms&nbsp;2 and&nbsp;3. ![Histogram](https://github.com/Pierre-Botteron/Algebra-of-Boxes-code/tree/main/Images/Histogram.png) | Figure&nbsp;9 |
| `Multiplication-Table.ipynb` | Computing the multiplication table given some boxes and a wiring. ![Multiplication table](https://github.com/Pierre-Botteron/Algebra-of-Boxes-code/tree/main/Images/Multiplication-table.png) | Figure&nbsp;4, Eq.&nbsp;(18), Appendix&nbsp;C |
| `Test_if_W_is_collapsing.ipynb` | Given a wiring $\mathsf{W}$ and a triangle of boxes, test if the wiring collapses the triangle. ![Test if a wiring is collapsing](https://github.com/Pierre-Botteron/Algebra-of-Boxes-code/tree/main/Images/Test-if-a-wiring-is-collapsing.png) | Proof of Thm.&nbsp;41 |

![24 extremal points of NS](https://github.com/Pierre-Botteron/Algebra-of-Boxes-code/tree/main/Images/24-extremal-points-of-NS.png)

## Installation of the Package

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
The bigger that number is, the more precise is the optimisation but the longer is the run time.

## Reference

```bibtex
@misc{botteron2024algebra,
      title={Algebra of Nonlocal Boxes and the Collapse of Communication Complexity}, 
      author={Pierre Botteron and Anne Broadbent and Reda Chhaibi and Ion Nechita and Clément Pellegrini},
      year={2024},
      eprint={2312.00725},
      archivePrefix={arXiv},
      primaryClass={quant-ph}
}
```
