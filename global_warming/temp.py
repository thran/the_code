import pandas as pd
import seaborn as sns
import pylab as plt

df = pd.read_csv('data/TG_SOUID106031.txt')

df['TG'] *= .1
df = df[df['Q_TG'] == 0]
df['year'] = df['DATE'] // 10000
temps = df.groupby('year')['TG'].mean()

d = pd.DataFrame(index=temps.index, data=temps)
d['year'] = d.index
print(d)

sns.lmplot(x="year", y="TG", data=d, order=3)

d = d[d['year'] > 1900]

sns.lmplot(x="year", y="TG", data=d, order=3)


plt.show()
