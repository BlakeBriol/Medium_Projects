# Welcome to Stockinator9000, I hope you enjoy the code!

import yfinance as yf

# create ticker for Apple Stock

# Meat
Greeting = input('Welcome to the Stockinator9000! '
                 'In this program you will be able to'
                 ' enter a stock ticker symbol'
                 ' and receive feedback regarding '
                 'its performance. For more in'
                 'formation please enter 1 or '
                 'to begin asking please enter 2: '
                 )
if Greeting == "1":
    input('This program uses the module yfinance'
          'to request and receive historical stock data.'
          'The data then goes through an algorithm to'
          'determine whether the stock is performing well '
          'or poorly.'
          )

elif Greeting == "2":
    Stock = input("Please Enter Stock Ticker Symbol")
    TDeterminer = input("What timeframe do you want to know?(Day, Week, Month, Year)")
ticker = yf.Ticker(Stock)

# Determinator Meat
todays_data = ticker.history(period='1d')
Week_data = ticker.history(period='5d')
Month_data = ticker.history(period='1mo')
Year_data = ticker.history(period='1y')
TPrice = todays_data['Open'].loc[todays_data.index[0]]
if TDeterminer == "Day":
    past_data = ticker.history(period='1d')
    OPrice = past_data['Open'].loc[todays_data.index[0]]
    Daydetermination = ((TPrice - OPrice) / OPrice)
    GGD = 0.04
    GD = 0.02
    ND = 0.0
    BD = -0.02
    BBD = -0.04
    if Daydetermination > GGD:
        print("Really Good Stock")
    elif GD < Daydetermination < GGD:
        print("Good Stock")
    elif BD < Daydetermination < GD:
        print("Stable Stock")
    elif Daydetermination > BBD and Daydetermination > BD:
        print("Bad Stock")
    elif Daydetermination < BBD:
        print("Really Bad Stock")
elif TDeterminer == "Week":
    WPrice = Week_data['Open'].loc[Week_data.index[0]]
    GGD = 0.04
    GD = 0.02
    ND = 0.0
    BD = -0.02
    BBD = -0.04
    Weekdetermination = (TPrice - WPrice) / WPrice
    if Weekdetermination > GGD:
        print("Really Good Stock")
    elif GD < Weekdetermination < GGD:
        print("Good Stock")
    elif BD < Weekdetermination < GD:
        print("Stable Stock")
    elif BD > Weekdetermination > BBD:
        print("Bad Stock")
    elif Weekdetermination < BBD:
        print("Really Bad Stock")
elif TDeterminer == "Month":
    month_data = ticker.history(period='1mo')
    MPrice = Month_data['Open'].loc[Month_data.index[0]]
    GGD = 0.04
    GD = 0.02
    ND = 0.0
    BD = -0.02
    BBD = -0.04
    Monthdetermination = float((TPrice - MPrice) / MPrice)
    if Monthdetermination:
        print("Really Good Stock")
    elif Monthdetermination:
        print("Good Stock")
    elif Monthdetermination:
        print("Stable Stock")
    elif Monthdetermination:
        print("Bad Stock")
    elif Monthdetermination:
        print("Really Bad Stock")
elif TDeterminer == "Year":
    YPrice = Year_data['Open'].loc[Year_data.index[0]]
    Yeardetermination = float((TPrice - YPrice) / YPrice)
    GGD = 0.04
    GD = 0.02
    ND = 0.0
    BD = -0.02
    BBD = -0.04
    if Yeardetermination > GGD:
        print("Really Good Stock")
    elif GGD > Yeardetermination > GD:
        print("Good Stock")
    elif BD < Yeardetermination < GD:
        print("Stable Stock")
    elif BD > Yeardetermination > BBD:
        print("Bad Stock")
    elif Yeardetermination < BBD:
        print("Really Bad Stock")
