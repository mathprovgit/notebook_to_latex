# Notebook automated report

convertion of the notebook to latex file(and/or pdf) using a nb extentions and template

## sources

most tricks where borrowed from:
- http://blog.juliusschulz.de/blog/ultimate-ipython-notebook
- https://ipypublish.readthedocs.io/en/latest/getting_started.html


## commands to perform the conversuion to Latex:

1. open Terminal
2. ```$ cd path/of/my_notebook ```
3. ```$ jupyter nbconvert --to latex --template my_template my_notebook.ipynb ```

## Create Requirements.txt:
0. Convert the notebook from .ipynb to .py using the menu File, Download as ...
1. open Terminal
2. Type following commands
```Python
pip install pipreqs
pipreqs path/of/my_notebook
```


2.  ```$ pip install pipreqs ```
3. ```$ pipreqs path/of/my_notebook ```


@mathprovgit



