# Notebook automated report
convertion of a Jupyter notebook into latex file (and/or pdf) using a nb extentions and template


Here in the notebook:
- **my_notebook.ipynb** 

The output as well as Markdown cells will be converted in with nbconvert:
- **my_notebook.tex**

after compilation with Latex:
- **my_notebook.pdf**


## sources

Litterature ressources used to create this notebook:
- http://blog.juliusschulz.de/blog/ultimate-ipython-notebook
- https://ipypublish.readthedocs.io/en/latest/getting_started.html
- https://www.overleaf.com/learn/latex/Cross_referencing_sections_and_equations#Referencing_equations.2C_figures_and_tables
- https://alvinalexander.com/blog/post/latex/reference-figure-or-table-within-latex-document

## Notebook conversion to Latex:
in a python terminal type:
```python
cd path/of/my_notebook
jupyter nbconvert --to latex --template my_template my_notebook.ipynb 
```

## Create Requirements.txt:
After converting the notebook from .ipynb to .py using the menu File, Download as ...
Type the folowing commands in a terminal:
```Python
pip install pipreqs
pipreqs path/of/my_notebook
```

output file:
 - **requirements.txt**
