import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\Saurabh\OneDrive\Documents\Programming Language\Python Prep\population.csv")
print(data.head())

data.describe

#List of contries for the graph.
countries_to_plot = ['United States', 'Canada', 'Brazil', 'Japan', 'Germany', 'France']

#Filtering the data frame
filtered_data = data[data['Country Name'].isin(countries_to_plot)]

#Creating the bar chart
plt.bar (filtered_data['Country Name'], filtered_data['2022'])
plt.xlabel ('Country Name')
plt.ylabel ('Population in 2022')
plt.title('Population of selected countries in 2022')
plt.xticks(rotation=45, ha='right') #Rotating the x-axis labels for readability
plt.show()