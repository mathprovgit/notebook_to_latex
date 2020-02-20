# Notebook automated report

convertion of the notebook to latex file(and/or pdf) using a nb extentions and template

## sources

most tricks where borrowed from:
- http://blog.juliusschulz.de/blog/ultimate-ipython-notebook
- https://ipypublish.readthedocs.io/en/latest/getting_started.html


## commands to perform the conversuion to Latex:
in a python terminal type:
```python
$ cd path/of/my_notebook
$ jupyter nbconvert --to latex --template my_template my_notebook.ipynb 
```

## Create Requirements.txt:
After converting the notebook from .ipynb to .py using the menu File, Download as ...
Type the folowing commands in a terminal:
```Python
pip install pipreqs
pipreqs path/of/my_notebook
```
