# https://www.kaggle.com/alexisbcook/titanic-tutorial

# Titanic Machine Learning Challenge
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import numpy as np # linear algebra
from pandas import read_csv

filename = 'train.csv'
filename2 = 'test.csv'

train_data = read_csv(filename)
print(train_data.head)

test_data = read_csv(filename2)
print(test_data.head)

women = train_data.loc[train_data.Sex == 'female']["Survived"]
rate_women = sum(women)/len(women)


print("% of women who survived:", rate_women)

men = train_data.loc[train_data.Sex == 'male']["Survived"]
rate_men = sum(men)/len(men)

print("% of men who survived:", rate_men)

from sklearn.ensemble import RandomForestClassifier

y = train_data["Survived"]
features = ["Pclass","Sex","SibSp","Parch"]
X = pd.get_dummies(train_data[features])
X_test = pd.get_dummies(test_data[features])

model = RandomForestClassifier(n_estimators = 100, max_depth = 5, random_state = 1)
model.fit(X,y)
predictions = model.predict(X_test)

output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': predictions})
output.to_csv('my_submission.csv', index = False)
print("Your submission was successfully saved!")
