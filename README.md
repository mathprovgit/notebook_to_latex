# Notebook automated report

convertion of the notebook to latex file(and/or pdf) using a nb extentions and template

## sources

most tricks where borrowed from:
    - http://blog.juliusschulz.de/blog/ultimate-ipython-notebook
    - https://ipypublish.readthedocs.io/en/latest/getting_started.html
    - [https://ipypublish.readthedocs.io/en/latest/getting_started.html](https://ipypublish.readthedocs.io/en/latest/getting_started.html) 

## commands
convert to Latex:

open a conda terminal
    - cd to path of my_notebook
    - jupyter nbconvert --to latex --template my_template my_notebook.ipynb
