#!/usr/bin/env python
# coding: utf-8

# # Initialisation

# ## import packages

# In[1]:


#import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
get_ipython().run_line_magic('matplotlib', 'inline')
from prettytable import PrettyTable
from ipypublish import nb_setup
from IPython.display import set_matplotlib_formats, Image
import Pretty_Table as pt
#define the chart overall settings
set_matplotlib_formats('pdf', 'png')
plt.rcParams['savefig.dpi'] = 75
plt.rcParams['figure.autolayout'] = False
plt.rcParams['figure.figsize'] = 12, 6
plt.rcParams['axes.labelsize'] = 18
plt.rcParams['axes.titlesize'] = 20
plt.rcParams['font.size'] = 16
plt.rcParams['lines.linewidth'] = 2.0
plt.rcParams['lines.markersize'] = 8
plt.rcParams['legend.fontsize'] = 14


# ## definition of functions

# ### function tp display beatiful tables

# In[2]:


#function for beatiful tables 
pd = nb_setup.setup_pandas(escape_latex=True)
def format_for_print(df,n=0,wide=False):
    #latex = df.round(n).to_latex(index=True)
    #html = df.to_html(index=True)   
    #return display({'text/latex': latex,'text/html': html}, raw=True)
    #return df.round(n)
    df2=df.round(n).reset_index()
    col=[w.replace("_", " ") for w in list(df2.columns)]
    return pt.PrettyTable(df2.values,col,wide_table=wide)


# # import data

# In[3]:


# generation of Dataframe 

#file name
file_name='data_weather_berlin_monthly.xlsx'

#import
df=pd.read_excel(file_name, 'berlin_tempelhof', header = [0])

df.rename(columns={'Unnamed: 0': 'month'}, inplace=True)

# print units
df_unit=df[:1]
df_unit

# remove units and month from df
df_data=df[1:].drop('month',axis=1)
#convert to numeric format
df_data=df_data.astype(float)


# The data for this example are generated with the demo version of meteonorm 7
# 
# the data will be dealing with the weather data of the berlin tempelhof weatherstation on monthly basis. 

# In[4]:


data=[]
data_header=['Symbol','Unit','Description']
data.append(['G Gh', 'kWh/m²','Global solar irradiance monthly averages'])
data.append(['G Dh', 'kWh/m²','Diffuse solar irradiance monthly averages'])
data.append(['Ta', '°C','Air temperature'])
data.append(['Td', '°C','Dew point'])
data.append(['FF', 'm/s','wind speed'])
pt.PrettyTable(data,data_header)


# # Text and Images 

# ## markdown image and text

# In[5]:


meta_data={"label": "Pandas Logo"}
Image('pics/pandas_logo.png',metadata=meta_data)


# here above image is a markdown image and the present text is a markdown text

# ## Code images and text

# In[6]:


nb_setup.images_hconcat(['pics/python3_logo.jpg', 'pics/python_logo_alt.png'], gap=10)


# In[7]:


print(' The here above images are generated from the concatenation of 2 images',
        'using  nb_setup.images_hconcat','and this text was written using the print statement')


# # Example of a table

# ## table small

# In[8]:


print('Monthly weather data from Berlin')


# In[9]:


print('units')
format_for_print(df_unit,n=0,wide=False)


# In[10]:


print('data')
format_for_print(df_data,n=0,wide=False)


# ## Table wide

# This is an example of wide table with random float rounded to 3 position after comma

# In[11]:


#wide_table
list_cols=[]
for i in range(1,16):
    list_cols.append('col_'+'{}'.format(i))
wide_table=pd.DataFrame(np.random.rand(20, 15) * 254, columns=list_cols)
format_for_print(wide_table,n=3,wide=True)


# # Example of chart

# ## chart bar

# In[12]:


if True: #True to show chart
    ax=df_data[['G_Gh']].plot(kind='bar',stacked=False,color='red', width=0.8)
    df_data[['G_Dh']].plot(kind='bar',stacked=False,color='yellow', width=0.6,ax=ax)
    plt.xlabel(' Month')
    plt.ylabel(' Solar irradiance [kWh/m²]')
    plt.grid()
    title = '\nSolar irradiance in Berlin\n'
    plt.title(title)
    #legend
    legend_elements  = [Line2D([0], [0], color='red', lw=4,label='Global'),
                        Line2D([0], [0], color='yellow', lw=4,label='Diffuse')] 
    plt.legend(handles=legend_elements)
    plt.show()


# ## chart scatter

# In[13]:


if True: #True to show chart
    x=df_data.index.tolist()
    y=df_data.FF.tolist()
    plt.scatter(x,y,color='green',label='Wind_speed')
    plt.xlabel(' Month')
    plt.ylabel(' Wind_speed [m/s]')
    plt.grid()
    title = '\nWind speed in Berlin\n'
    plt.title(title)
    plt.legend()
    plt.show()


# ## chart line

# In[14]:


if True: #True to show chart
    x=df_data.index.tolist()
    y1=df_data.Ta.tolist()
    y2=df_data.Td.tolist()
    plt.plot(x,y1,color='blue',label='Ambiant')
    plt.plot(x,y2,color='orange',label='dew')
    plt.xlabel(' Month')
    plt.ylabel(' Temperature [°C]')
    plt.grid()
    title = '\nAmbiant and Dew temperature in Berlin\n'
    plt.title(title)
    plt.legend()
    plt.show()


# # Example of matematic formulas

# example 1:
# 
# $$ y = a x + b $$
# 
# with:
# 
# - y : Ordonate
# - x : Abscissa
# - a : Slope
# - b : Initial value
# 
# 

# example 2:
# 
# $$\sum_{i=1}^{\infty} i = \frac{n(n+1)}{2}$$

# example 3:
#     
# $$ \int\limits_0^\infty {\sqrt{x} e^{ - x} dx} = \frac{1}{2}\sqrt{\pi}$$

# # Generation of the template

# In[15]:


get_ipython().run_cell_magic('writefile', 'my_template.tplx', '\n\n((*- extends \'article.tplx\' -*))\n\n%-------- remove inputs ---------\n((* block input_group *))\n    ((*- if cell.metadata.get(\'nbconvert\', {}).get(\'show_code\', False) -*))\n        ((( super() )))\n    ((*- endif -*))\n((* endblock input_group *))\n\n%-------- output without prompt ---------\n((* block execute_result scoped *))\n    ((* block display_data scoped *))\n        ((( super() )))\n    ((* endblock display_data *))\n((* endblock execute_result *))\n\n\n%-------- docclass section ---------\n((* block docclass *))\n\n\\documentclass[reprint, floatfix, groupaddress, prb]{article}\n\n%set main font\n\\usepackage[T1]{fontenc}\n\\usepackage{lmodern}\n\n%depth of toc\n\\setcounter{tocdepth}{3}\n\n\\AtBeginDocument{\n\\heavyrulewidth=.08em\n\\lightrulewidth=.05em\n\\cmidrulewidth=.03em\n\\belowbottomsep=0pt\n\\aboverulesep=.4ex\n\\abovetopsep=0pt\n\\cmidrulesep=\\doublerulesep\n\\cmidrulekern=.5em\n\\defaultaddspace=.5em\n}\n\n\\usepackage{array}\n\\usepackage{placeins}\n\\usepackage{graphicx}\n\\usepackage{multirow}\n\\usepackage[table]{xcolor}\n\n% new page before each chapter\n\\usepackage{sectsty}\n\\sectionfont{\\clearpage}\n\n((* endblock docclass *))\n\n%-------- Title  ---------\n\n((* block title *))\n\n\\title{\\huge{\\textbf{My Latex automated Report}}\\\\[2ex]  \\LARGE{Generated from my notebook.ipynb}}\n\\author{Mathieu Provost}\n\\date{\\today}\n   \n\\makeatletter         \n\\def\\@maketitle{\n\\raggedright\n\n\\begin{center}\n\\includegraphics[width=30mm]{pics/jupyter_logo.png}\\\\[4ex]\n{\\@title }\\\\[6ex] \n{\\Large  \\@author}\\\\[4ex] \n\\@date\\\\[8ex]\n\\includegraphics{pics/jupyter_picture.jpg}\n\\end{center}}\n\n% newline after paragraph\n\\makeatletter\n\\renewcommand\\paragraph{%\n    \\@startsection{paragraph}{4}{0mm}%\n       {-\\baselineskip}%\n       {.5\\baselineskip}%\n       {\\normalfont\\normalsize\\bfseries}}\n\\setcounter{secnumdepth}{4}\n\\makeatother\n\n((* endblock title *))\n\n((* block maketitle *))\n    \n\\maketitle\n\n\\newpage\n\n\\tableofcontents\n\n\\newpage\n\n\\listoffigures\n\n\\newpage\n\n\\listoftables\n\n\\newpage\n((* endblock maketitle *))\n\n\n% New mechanism for rendering figures with captions\n((*- block data_png -*))\n((*- if cell.metadata.widefigure: -*))\n    ((( draw_widefigure_with_caption(output.metadata.filenames[\'image/png\'], cell.metadata.caption, cell.metadata.label) )))\n((*- else -*))\n    ((*- if cell.metadata.caption: -*))\n        ((*- if cell.metadata.label: -*))\n            ((( draw_figure_with_caption(output.metadata.filenames[\'image/png\'], cell.metadata.caption, cell.metadata.label) )))\n        ((*- else -*))\n            ((( draw_figure_with_caption(output.metadata.filenames[\'image/png\'], cell.metadata.caption, "") )))\n        ((*- endif *))\n    ((*- else -*))\n        ((( draw_figure_with_caption(output.metadata.filenames[\'image/png\'], "") )))\n    ((*- endif *))\n((*- endif *))\n((*- endblock -*))\n((*- block data_jpg -*))\n((*- if cell.metadata.caption: -*))\n    ((*- if cell.metadata.label: -*))\n        ((( draw_figure_with_caption(output.metadata.filenames[\'image/jpeg\'], cell.metadata.caption, cell.metadata.label) )))\n    ((*- else -*))\n        ((( draw_figure_with_caption(output.metadata.filenames[\'image/jpeg\'], cell.metadata.caption, "") )))\n    ((*- endif *))\n((*- else -*))\n    ((( draw_figure_with_caption(output.metadata.filenames[\'image/jpeg\'], "") )))\n((*- endif *))\n((*- endblock -*))\n((*- block data_svg -*))\n((*- if cell.metadata.caption: -*))\n    ((*- if cell.metadata.label: -*))\n        ((( draw_figure_with_caption(output.metadata.filenames[\'image/svg+xml\'], cell.metadata.caption, cell.metadata.label) )))\n    ((*- else -*))\n        ((( draw_figure_with_caption(output.metadata.filenames[\'image/svg+xml\'], cell.metadata.caption, "") )))\n    ((*- endif *))\n((*- else -*))\n    ((( draw_figure_with_caption(output.metadata.filenames[\'image/svg+xml\'], "") )))\n((*- endif *))\n((*- endblock -*))\n((*- block data_pdf -*))\n((*- if cell.metadata.widefigure: -*))\n    ((( draw_widefigure_with_caption(output.metadata.filenames[\'application/pdf\'], cell.metadata.caption, cell.metadata.label) )))\n((*- else -*))\n    ((*- if cell.metadata.caption: -*))\n        ((*- if cell.metadata.label: -*))\n            ((( draw_figure_with_caption(output.metadata.filenames[\'application/pdf\'], cell.metadata.caption, cell.metadata.label) )))\n        ((*- else -*))\n            ((( draw_figure_with_caption(output.metadata.filenames[\'application/pdf\'], cell.metadata.caption, "") )))\n        ((*- endif *))\n    ((*- else -*))\n        ((( draw_figure_with_caption(output.metadata.filenames[\'application/pdf\'], "") )))\n    ((*- endif *))\n((*- endif *))\n((*- endblock -*))\n\n% Draw a figure using the graphicx package.\n((* macro draw_figure_with_caption(filename, caption, label) -*))\n((* set filename = filename | posix_path *))\n((*- block figure scoped -*))\n    \\begin{figure}\n        \\begin{center}\\adjustimage{max size={0.9\\linewidth}{0.4\\paperheight}}{((( filename )))}\\end{center}\n        \\caption{((( caption )))}\n        \\label{((( label )))}\n    \\end{figure}\n((*- endblock figure -*))\n((*- endmacro *))\n\n% Draw a figure using the graphicx package.\n((* macro draw_widefigure_with_caption(filename, caption, label) -*))\n((* set filename = filename | posix_path *))\n((*- block figure_wide scoped -*))\n    \\begin{figure*}\n        \\begin{center}\\adjustimage{max size={0.9\\linewidth}{0.4\\paperheight}}{((( filename )))}\\end{center}\n        \\caption{((( caption )))}\n        \\label{((( label )))}\n    \\end{figure*}\n((*- endblock figure_wide -*))\n((*- endmacro *))')


# In[ ]:




