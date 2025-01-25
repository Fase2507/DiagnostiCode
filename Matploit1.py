import pandas as pd

import numpy as np
import glob


import matplotlib.pyplot as plt
import seaborn as sns


# Example visualizations using seaborn
df=pd.read_csv("titanic.csv")

# 1. Histogram
plt.figure(figsize=(8, 6))
sns.histplot(df['Age'], kde=True)
plt.title('Distribution of Passenger Ages')
plt.show()

# 2. Box plot
plt.figure(figsize=(8, 6))
sns.boxplot(x='Pclass', y='Age', data=df)
plt.title('Age Distribution by Passenger Class')
plt.show()

# 3. Count plot
plt.figure(figsize=(8, 6))
sns.countplot(x='Survived', hue='Sex', data=df)
plt.title('Survival Count by Gender')
plt.show()

# 4. Scatter plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Age', y='Fare', hue='Survived', data=df)
plt.title('Age vs. Fare with Survival')
plt.show()

# 5. Heatmap of correlation
plt.figure(figsize=(10, 8))
sns.heatmap(df.select_dtypes(include=[np.number]).corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of Numerical Features')
plt.show()

# 6. Pairplot
sns.pairplot(df, hue='Survived')  #This can be computationally expensive for large datasets
plt.title("Kapsamlı Görüntüleme")
plt.show()

# 7. Violin plot
plt.figure(figsize=(8, 6))
sns.violinplot(x='Embarked', y='Fare', hue='Survived', data=df, split=True)
plt.title('Fare Distribution by Embarkation Point')
plt.show()


# ... (rest of your existing code) ...

# df=pd.read_csv("titanic.csv")
print(df.groupby('Sex')['Age'].mean())
print(df[(df["Age"]>30) & (df["Sex"]=="male")].tail(2))
print(df.iloc[0:8,0:4])