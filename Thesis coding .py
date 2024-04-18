# -*- coding: utf-8 -*-
"""Thesis Coding.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1exk0PnnBiMEXfBGlcu4y4VJxnhEqe_hW
"""

import pandas as pd

df = pd.read_csv('/content/drive/MyDrive/creditcard.csv')
df.head()

df.shape

# Check for missing values and drop rows with any missing values
data = df.dropna()

df.shape

"""Performing Exploratory Data Analyses (EDA)"""

import matplotlib.pyplot as plt
import seaborn as sns

# Set the style of seaborn for better visualization
sns.set(style="whitegrid")

# Plot the distribution of the target variable (Class)
plt.figure(figsize=(8, 6))
sns.countplot(x="Class", data=df)
plt.title("Distribution of Classes (0: Non-Fraudulent, 1: Fraudulent)")
plt.show()

# Plot the distribution of transaction amounts
plt.figure(figsize=(10, 6))
sns.histplot(df["Amount"], bins=50, kde=True)
plt.title("Distribution of Transaction Amounts")
plt.xlabel("Amount")
plt.show()

# Plot the distribution of time
plt.figure(figsize=(10, 6))
sns.histplot(df["Time"], bins=50, kde=True)
plt.title("Distribution of Transaction Times")
plt.xlabel("Time (in seconds)")
plt.show()

# Plot correlation matrix heatmap for features V1-V28
plt.figure(figsize=(14, 10))
corr_matrix = df.iloc[:, 1:29].corr()
sns.heatmap(corr_matrix, cmap="coolwarm", annot=True, fmt=".2f")
plt.title("Correlation Matrix Heatmap")
plt.show()

"""Naive Bayes"""

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Separate features (X) and target variable (y)
X = df.drop("Class", axis=1)
y = df["Class"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Naive Bayes classifier
nb_classifier = GaussianNB()

# Train the classifier
nb_classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = nb_classifier.predict(X_test)

# Evaluate the classifier
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print("Accuracy:", accuracy)
print("\nConfusion Matrix:\n", conf_matrix)
print("\nClassification Report:\n", classification_rep)

"""Testing the model"""

# New transaction data for prediction
new_data = pd.DataFrame({
    "Time": [1],
    "V1": [1.19185711131486],
    "V2": [0.26615071205963],
    "V3": [0.16648011335321],
    "V4": [0.448154078460911],
    "V5": [0.0600176492822243],
    "V6": [-0.0823608088155687],
    "V7": [-0.0788029833323113],
    "V8": [0.0851016549148104],
    "V9": [-0.255425128109186],
    "V10": [-0.166974414004614],
    "V11": [1.61272666105479],
    "V12": [1.06523531137287],
    "V13": [0.48909501589608],
    "V14": [-0.143772296441519],
    "V15": [0.635558093258208],
    "V16": [0.463917041022171],
    "V17": [-0.114804663102346],
    "V18": [-0.183361270123994],
    "V19": [-0.145783041325259],
    "V20": [-0.0690831352230203],
    "V21": [-0.225775248033138],
    "V22": [-0.638671952771851],
    "V23": [0.101288021253234],
    "V24": [-0.339846475529127],
    "V25": [0.167170404418143],
    "V26": [0.125894532368176],
    "V27": [-0.00898309914322813],
    "V28": [0.0147241691924927],
    "Amount": [2.69]
})

# Use the trained Naive Bayes classifier to make predictions
prediction = nb_classifier.predict(new_data)

# Print the prediction result
if prediction[0] == 1:
    print("The transaction is predicted as FRAUDULENT.")
else:
    print("The transaction is predicted as NON-FRAUDULENT.")

"""Logistic regression"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load the CSV file into a DataFrame
data = pd.read_csv("/content/drive/MyDrive/creditcard.csv")

# Check for missing values and drop rows with any missing values
data = data.dropna()

# Separate features (X) and target variable (y)
X = data.drop("Class", axis=1)
y = data["Class"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Logistic Regression classifier
lr_classifier = LogisticRegression(random_state=42)

# Train the classifier
lr_classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = lr_classifier.predict(X_test)

# Evaluate the classifier
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print("Accuracy:", accuracy)
print("\nConfusion Matrix:\n", conf_matrix)
print("\nClassification Report:\n", classification_rep)

# New transaction data for prediction
new_data = pd.DataFrame({
    "Time": [1],
    "V1": [1.19185711131486],
    "V2": [0.26615071205963],
    "V3": [0.16648011335321],
    "V4": [0.448154078460911],
    "V5": [0.0600176492822243],
    "V6": [-0.0823608088155687],
    "V7": [-0.0788029833323113],
    "V8": [0.0851016549148104],
    "V9": [-0.255425128109186],
    "V10": [-0.166974414004614],
    "V11": [1.61272666105479],
    "V12": [1.06523531137287],
    "V13": [0.48909501589608],
    "V14": [-0.143772296441519],
    "V15": [0.635558093258208],
    "V16": [0.463917041022171],
    "V17": [-0.114804663102346],
    "V18": [-0.183361270123994],
    "V19": [-0.145783041325259],
    "V20": [-0.0690831352230203],
    "V21": [-0.225775248033138],
    "V22": [-0.638671952771851],
    "V23": [0.101288021253234],
    "V24": [-0.339846475529127],
    "V25": [0.167170404418143],
    "V26": [0.125894532368176],
    "V27": [-0.00898309914322813],
    "V28": [0.0147241691924927],
    "Amount": [2.69]
})

# Use the trained Naive Bayes classifier to make predictions
prediction = lr_classifier.predict(new_data)

# Print the prediction result
if prediction[0] == 1:
    print("The transaction is predicted as FRAUDULENT.")
else:
    print("The transaction is predicted as NON-FRAUDULENT.")

"""Random Forest Classifier"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load the CSV file into a DataFrame
data = pd.read_csv("/content/drive/MyDrive/creditcard.csv")

# Check for missing values and drop rows with any missing values
data = data.dropna()

# Separate features (X) and target variable (y)
X = data.drop("Class", axis=1)
y = data["Class"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest Classifier
rf_classifier = RandomForestClassifier(random_state=42)

# Train the classifier
rf_classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf_classifier.predict(X_test)

# Evaluate the classifier
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print("Accuracy:", accuracy)
print("\nConfusion Matrix:\n", conf_matrix)
print("\nClassification Report:\n", classification_rep)

# New transaction data for prediction
new_data = pd.DataFrame({
    "Time": [1],
    "V1": [1.19185711131486],
    "V2": [0.26615071205963],
    "V3": [0.16648011335321],
    "V4": [0.448154078460911],
    "V5": [0.0600176492822243],
    "V6": [-0.0823608088155687],
    "V7": [-0.0788029833323113],
    "V8": [0.0851016549148104],
    "V9": [-0.255425128109186],
    "V10": [-0.166974414004614],
    "V11": [1.61272666105479],
    "V12": [1.06523531137287],
    "V13": [0.48909501589608],
    "V14": [-0.143772296441519],
    "V15": [0.635558093258208],
    "V16": [0.463917041022171],
    "V17": [-0.114804663102346],
    "V18": [-0.183361270123994],
    "V19": [-0.145783041325259],
    "V20": [-0.0690831352230203],
    "V21": [-0.225775248033138],
    "V22": [-0.638671952771851],
    "V23": [0.101288021253234],
    "V24": [-0.339846475529127],
    "V25": [0.167170404418143],
    "V26": [0.125894532368176],
    "V27": [-0.00898309914322813],
    "V28": [0.0147241691924927],
    "Amount": [2.69]
})

# Use the trained Naive Bayes classifier to make predictions
prediction = rf_classifier.predict(new_data)

# Print the prediction result
if prediction[0] == 1:
    print("The transaction is predicted as FRAUDULENT.")
else:
    print("The transaction is predicted as NON-FRAUDULENT.")

"""Stacking Classifier"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import StackingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load the CSV file into a DataFrame
data = pd.read_csv("/content/drive/MyDrive/creditcard.csv")

# Check for missing values and drop rows with any missing values
data = data.dropna()

# Separate features (X) and target variable (y)
X = data.drop("Class", axis=1)
y = data["Class"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the base classifiers
rf_classifier = RandomForestClassifier(random_state=42)
nb_classifier = GaussianNB()

from google.colab import drive
drive.mount('/content/drive')

# Initialize the Stacking Classifier with Logistic Regression as the meta-classifier
stacking_classifier = StackingClassifier(
    estimators=[('rf', rf_classifier), ('nb', nb_classifier)],
    final_estimator=LogisticRegression(),
    stack_method='auto',
    n_jobs=-1
)

# Train the Stacking Classifier
stacking_classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = stacking_classifier.predict(X_test)

# Evaluate the classifier
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print("Accuracy:", accuracy)
print("\nConfusion Matrix:\n", conf_matrix)
print("\nClassification Report:\n", classification_rep)

# New transaction data for prediction
new_data = pd.DataFrame({
    "Time": [1],
    "V1": [1.19185711131486],
    "V2": [0.26615071205963],
    "V3": [0.16648011335321],
    "V4": [0.448154078460911],
    "V5": [0.0600176492822243],
    "V6": [-0.0823608088155687],
    "V7": [-0.0788029833323113],
    "V8": [0.0851016549148104],
    "V9": [-0.255425128109186],
    "V10": [-0.166974414004614],
    "V11": [1.61272666105479],
    "V12": [1.06523531137287],
    "V13": [0.48909501589608],
    "V14": [-0.143772296441519],
    "V15": [0.635558093258208],
    "V16": [0.463917041022171],
    "V17": [-0.114804663102346],
    "V18": [-0.183361270123994],
    "V19": [-0.145783041325259],
    "V20": [-0.0690831352230203],
    "V21": [-0.225775248033138],
    "V22": [-0.638671952771851],
    "V23": [0.101288021253234],
    "V24": [-0.339846475529127],
    "V25": [0.167170404418143],
    "V26": [0.125894532368176],
    "V27": [-0.00898309914322813],
    "V28": [0.0147241691924927],
    "Amount": [2.69]
})

# Use the trained Naive Bayes classifier to make predictions
prediction = stacking_classifier.predict(new_data)

# Print the prediction result
if prediction[0] == 1:
    print("The transaction is predicted as FRAUDULENT.")
else:
    print("The transaction is predicted as NON-FRAUDULENT.")

"""Xgboost Classifier"""

import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load the CSV file into a DataFrame
data = pd.read_csv("/content/drive/MyDrive/creditcard.csv")

# Check for missing values and drop rows with any missing values
data = data.dropna()

# Separate features (X) and target variable (y)
X = data.drop("Class", axis=1)
y = data["Class"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the XGBoost Classifier
xgb_classifier = XGBClassifier(random_state=42)

# Train the classifier
xgb_classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = xgb_classifier.predict(X_test)

# Evaluate the classifier
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print("Accuracy:", accuracy)
print("\nConfusion Matrix:\n", conf_matrix)
print("\nClassification Report:\n", classification_rep)

# New transaction data for prediction
new_data = pd.DataFrame({
    "Time": [1],
    "V1": [1.19185711131486],
    "V2": [0.26615071205963],
    "V3": [0.16648011335321],
    "V4": [0.448154078460911],
    "V5": [0.0600176492822243],
    "V6": [-0.0823608088155687],
    "V7": [-0.0788029833323113],
    "V8": [0.0851016549148104],
    "V9": [-0.255425128109186],
    "V10": [-0.166974414004614],
    "V11": [1.61272666105479],
    "V12": [1.06523531137287],
    "V13": [0.48909501589608],
    "V14": [-0.143772296441519],
    "V15": [0.635558093258208],
    "V16": [0.463917041022171],
    "V17": [-0.114804663102346],
    "V18": [-0.183361270123994],
    "V19": [-0.145783041325259],
    "V20": [-0.0690831352230203],
    "V21": [-0.225775248033138],
    "V22": [-0.638671952771851],
    "V23": [0.101288021253234],
    "V24": [-0.339846475529127],
    "V25": [0.167170404418143],
    "V26": [0.125894532368176],
    "V27": [-0.00898309914322813],
    "V28": [0.0147241691924927],
    "Amount": [2.69]
})

# Use the trained Naive Bayes classifier to make predictions
prediction = xgb_classifier.predict(new_data)

# Print the prediction result
if prediction[0] == 1:
    print("The transaction is predicted as FRAUDULENT.")
else:
    print("The transaction is predicted as NON-FRAUDULENT.")

"""Comparison between all classifiers"""

import matplotlib.pyplot as plt
import seaborn as sns

# Classifier names
classifiers = ['Naive Bayes', 'Logistic Regression', 'Random Forest', 'Stacking Classifier', 'XGBoost']

# Accuracy comparison
accuracy_values = [0.993, 0.999, 0.999, 0.999, 0.999]
plt.figure(figsize=(10, 6))
sns.barplot(x=classifiers, y=accuracy_values, palette='viridis')
plt.title('Accuracy Comparison')
plt.ylim(0.98, 1.0)
plt.show()

# Precision, Recall, F1-score comparison
precision_values = [1.00, 1.00, 1.00, 1.00, 1.00]
recall_values = [0.63, 0.56, 0.77, 0.72, 0.78]
f1_score_values = [0.24, 0.59, 0.86, 0.84, 0.86]

plt.figure(figsize=(15, 6))
plt.subplot(1, 3, 1)
sns.barplot(x=classifiers, y=precision_values, palette='viridis')
plt.title('Precision Comparison')
plt.xticks(rotation=45)

plt.subplot(1, 3, 2)
sns.barplot(x=classifiers, y=recall_values, palette='viridis')
plt.title('Recall Comparison')
plt.xticks(rotation=45)

plt.subplot(1, 3, 3)
sns.barplot(x=classifiers, y=f1_score_values, palette='viridis')
plt.title('F1-Score Comparison')
plt.xticks(rotation=45)

plt.show()