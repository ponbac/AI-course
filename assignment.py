import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('datasets\life-expectancy-vs-gdp-per-capita.csv')
df.tail(20)

countries = df['Entity']
countries = set(countries)
countries

gdp2000 = df[df['Year'] == 2012]
gdp2000 = pd.DataFrame(gdp2000, columns=['Entity', 'Year', 'Real GDP per capita in 2011US$, multiple benchmarks (Maddison Project Database (2018))', 'Life expectancy'])
gdp2000.dropna(subset=['Real GDP per capita in 2011US$, multiple benchmarks (Maddison Project Database (2018))'], inplace=True)
gdp2000.dropna(subset=['Life expectancy'], inplace=True)
gdp2000

x = gdp2000['Real GDP per capita in 2011US$, multiple benchmarks (Maddison Project Database (2018))']
y = gdp2000['Life expectancy']

plt.scatter(x, y)
plt.xlim(0, 50000)
plt.ylim(45, 85)

m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b, color='red')