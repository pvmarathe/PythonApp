# Rescale Data

# Scale generally means to change the range of the values. The shape of the distribution doesn’t change. Think about how a scale model of a building has the same proportions as the original, just smaller. That’s why we say it is drawn to scale. The range is often set at 0 to 1.

# When your data is comprised of attributes with varying scales, many machine learning algorithms
# can benefit from rescaling the attributes to all have the same scale. Often this is referred to
# as normalization and attributes are often rescaled into the range between 0 and 1. This is
# useful for optimization algorithms used in the core of machine learning algorithms like gradient
# descent. It is also useful for algorithms that weight inputs like regression and neural networks
# and algorithms that use distance measures like k-Nearest Neighbors. You can rescale your data
# using scikit-learn using the MinMaxScaler class2.

# Rescale data (between 0 and 1)
from pandas import read_csv
from numpy import set_printoptions
from sklearn.preprocessing import MinMaxScaler
filename = 'pima-indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names=names)
array = dataframe.values
# separate array into input and output components
X = array[:,0:8]
Y = array[:,8]
scaler = MinMaxScaler(feature_range=(0, 1))
rescaledX = scaler.fit_transform(X)
# summarize transformed data
set_printoptions(precision=3)
print(rescaledX[0:5,:])

# After rescaling you can see that all of the values are in the range between 0 and 1.
