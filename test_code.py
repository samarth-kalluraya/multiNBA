# -*- coding: utf-8 -*-

from task import Task
from buchi_parse import Buchi
from workspace import Workspace

import datetime
from collections import OrderedDict
import numpy as np
from draw_picture import path_plot, path_print
from text_editor import export_to_txt, export_cov_to_txt, export_disc_to_txt
import matplotlib.pyplot as plt
import pyvisgraph as vg
from termcolor import colored
import networkx as nx



if __name__ == "__main__":
    # task
    
    start = datetime.datetime.now()
    task = Task()
    buchi = Buchi(task)
    buchi.construct_buchi_graph()
    buchi.get_minimal_length()
    buchi.get_feasible_accepting_state()
    buchi_graph = buchi.buchi_graph
    NBA_time = (datetime.datetime.now() - start).total_seconds()
    print('Time for constructing the NBA: {0:.4f} s'.format(NBA_time))
