#Density Plots
# Dsnsity plots look like an abstracted histogram with a smooth curve drawn through the top of each bin much like how your eye tried to do with the histograms
from matplotlib import pyplot
from pandas import read_csv
filename = 'pima-indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename,names = names)
data.plot(kind = 'density',subplots = True, layout = (3,3),sharex = False)
pyplot.show()
