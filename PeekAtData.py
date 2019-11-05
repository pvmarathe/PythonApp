# Peek at data
# View First 20 rows of the data

from pandas import read_csv
filename = 'pima-indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename,names = names)
peek = data.head(20)
print(peek)
