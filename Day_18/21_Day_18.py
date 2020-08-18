import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

fruit = pd.read_csv(r'Day_18\apples_and_oranges.csv')
g = sns.pairplot(fruit,hue="Class") 
plt.title("Fruit Classification")
plt.show()