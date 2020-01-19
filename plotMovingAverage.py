import quandl
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [10, 5]
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['xtick.major.width'] = 1.0
plt.rcParams['ytick.major.width'] = 1.0
plt.rcParams['font.size'] = 12
plt.rcParams['axes.linewidth'] = 1.0
plt.rcParams['font.family'] =  'Times New Roman'

code = 7203

quandl.ApiConfig.api_key = 'xxxxxxxxxxxx'
quandl_data = quandl.get("TSE/" + str(code))
quandl_data.to_csv('TSE_' + str(code) + '.csv')

x = []
y = []

data =  pd.read_csv('TSE_' + str(code) + '.csv')
a =list(pd.to_datetime(data.iloc[:,0], format='%Y-%m-%d'))
x += a[::-1]
b = list(data.iloc[:,4])
y += b[::-1]

z = pd.DataFrame(y)
sma75 = pd.DataFrame.rolling(z, window=75,center=False).mean()
sma25 = pd.DataFrame.rolling(z, window=25,center=False).mean()

plt.plot(x, y, color="blue", linewidth=1, linestyle="-")
plt.plot(x, sma25, color="g", linewidth=1, linestyle="-", label="SMA25")
plt.plot(x, sma75, color="r", linewidth=1, linestyle="-", label="SMA75")

plt.title("TOYOA ("+str(code)+")", fontsize=16,  fontname='Times New Roman')
plt.xlabel("Year-Month", fontsize=14, fontname='Times New Roman')
plt.ylabel("Stock price", fontsize=14, fontname='Times New Roman')

plt.legend(loc="best")

plt.show()
