import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

# Load the Titanic dataset
df = pd.read_csv('titanic.csv')

# Prepare the data for training
X = df[['Pclass', 'Age', 'Sex', 'SibSp', 'Cabin','Parch', 'Embarked']]
y = df['Survived']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

# Train the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model performance
accuracy = np.mean(y_pred == y_test)
print('Accuracy:', accuracy)

# Passenger information
passenger = {
    'Pclass': 1,
    'Age': 25,
    'Sex': 'female',
    'SibSp': 4,
    'Parch' : 2
    'CabinClass': 1,
    'Embarked': 'S'
}

# Make a prediction
prediction = model.predict([passenger])

# Print the prediction
print('Prediction:', prediction)
