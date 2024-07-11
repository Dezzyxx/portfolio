import matplotlib.pyplot as plt
import seaborn as sns

# Data
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
apples = [0.89, 0.72, 0.82, 0.49, 0.3, 0.79, 1.08]

sns.set(style="whitegrid")  
plt.figure(figsize=(10, 6))  # Set the figure size
sns.lineplot(x=years, y=apples, marker='o')

plt.xlabel('Years')
plt.ylabel('Apples')
plt.title('Apples Production Over Years')

plt.show()