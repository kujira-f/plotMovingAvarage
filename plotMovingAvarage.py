import quandl
import pandas as pd
import  matplotlib.pyplot as plt

plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

quandl.ApiConfig.api_key = 'xxxxxxxxxxxxxx'
quandl_data = quandl.get("TSE/4689")
quandl_data.to_csv('TSE_4689.csv')

stock = pd.read_csv('TSE_4689.csv')

stock['25MA'] = stock['Close'].rolling(window = 25, min_periods=0).mean()
stock['75MA'] = stock['Close'].rolling(window = 75, min_periods=0).mean()

fig = plt.figure()

axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes.plot(stock['Close'][-365:], 'black', lw = 1, label="close")
axes.plot(stock['25MA'][-365:], label="25MA")
axes.plot(stock['75MA'][-365:], label="75MA")
axes.set_xlabel('Time')
axes.set_ylabel('Price')
axes.set_title('TSE4689_1_Year_Moving_Avarage')
axes.legend(loc="best")

plt.show()
