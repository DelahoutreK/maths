import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn3_circles

set1 = {2,4,6,8,10,12}
set2 = {3,6,9,12,15}
set3 = {4,8,12,16}

venn3([set1,set2,set3]('mult 2', 'mult 3', 'mult 4'))