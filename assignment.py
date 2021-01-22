import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('datasets\life-expectancy-vs-gdp-per-capita.csv')
df.tail(20)

countries = df['Entity']
countries = set(countries)
countries

gdp2012 = df[df['Year'] == 2012]
gdp2012 = pd.DataFrame(gdp2012, columns=['Entity', 'Year', 'Real GDP per capita in 2011US$, multiple benchmarks (Maddison Project Database (2018))', 'Life expectancy'])
gdp2012.dropna(subset=['Real GDP per capita in 2011US$, multiple benchmarks (Maddison Project Database (2018))'], inplace=True)
gdp2012.dropna(subset=['Life expectancy'], inplace=True)
gdp2012

x = gdp2012['Real GDP per capita in 2011US$, multiple benchmarks (Maddison Project Database (2018))']
y = gdp2012['Life expectancy']

plt.scatter(x, y)
plt.xlim(0, 50000)
plt.ylim(45, 85)

m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b, color='red')