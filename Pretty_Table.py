# class PrettyTable

class PrettyTable(list):
    """ Overridden list class which takes a 2-dimensional list of 
        the form [[1,2,3],[4,5,6]], and renders HTML and LaTeX Table in 
        IPython Notebook. For LaTeX export two styles can be chosen."""
    def __init__(self, initlist=[], extra_header=None, print_latex_longtable=True,wide_table=False,label="",caption=""):
        self.print_latex_longtable = print_latex_longtable
        self.wide_table= wide_table
        self.label=label
        self.caption=caption
        if extra_header is not None:
            if len(initlist[0]) != len(extra_header):
                raise ValueError("Header list must have same length as data has columns.")
            initlist = [extra_header]+list(initlist)
        super(PrettyTable, self).__init__(initlist)
    
    def latex_table_tabular(self):
        latex = ["\\begin{tabular}"]
        latex.append("{"+"|".join((["l"]*len(self[0])))+"}\n")
        for row in self:
            latex.append(" & ".join(map(format, row)))
            latex.append("\\\\ \n")
        latex.append("\\end{tabular}")
        return ''.join(latex)
        
    def latex_longtable(self):
        latex=["\\begin{table}[ht] "]
        latex.append("\\rowcolors{2}{white}{gray!25}\n")
        latex.append("\\centering\n")
        if self.wide_table:
            latex.append("\\resizebox{\\textwidth}{!}{%\n")
        latex.append("\\begin{tabular}[l]{")
        latex.append("".join((["l"]*len(self[0]))))
        latex.append("}\n")
        latex.append("\\toprule\n")
        first = True
        for row in self:
            latex.append(" & ".join(map(format, row)))
            latex.append("\\\\ \n")
            if first:
                latex.append("\\midrule\n")
                first = False
        latex.append("\\bottomrule \n \\end{tabular}\n")
        if self.wide_table:
            latex.append("}\n")
        latex.append("\caption{"+self.caption+"}\n")
        latex.append("\label{table:"+self.label+"}\n") 
        latex.append("\end{table}\n")
        return ''.join(latex)
        
    def _repr_html_(self):
        html = ["<table>"]
        for row in self:
            html.append("<tr>")
            for col in row:
                html.append("<td>{0}</td>".format(col))
            html.append("</tr>")
        html.append("</table>")
        return ''.join(html)
    def _repr_latex_(self):
        if self.print_latex_longtable: 
            return self.latex_longtable()
        else: 
            return self.latex_table_tabular()
