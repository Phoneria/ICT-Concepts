"""
Strateji 1:
Bir önceki mumun yükseliş mumu olması durumunda şu anki mum önceki mumun high değerinden daha büyük bir high değerine sahipse
bu mumun kapandığı anda bu kapanış değerinden girip önceki mumun lowunu hedefliyoruz. Stop bu mumun high değeri olucak

Vice Versa

Strateji 2:
Mumdan önceki 2 mum da düşüş mumu olup önceki mum bu mumdan iki önceki mumun low'undan daha düşük bir low'a sahip ve şu anki mum
önceki mumun low'undan daha düşük bir değere sahip ise bu mumun kapanış değerinden girilip high değerine stop atılı 1:1r hedeflenir

Vice Versa

"""

import pandas as pd

NDX = pd.read_csv("15_minute_NDX.csv")


def trade_result(enter_price, stop_price, trade_type):
    """
    Returns change rate according to enter and exit prices
    """
    global balance

    try:
        if trade_type == "Short":
            change_rate = (enter_price - stop_price) / enter_price
        else:
            change_rate = (stop_price - enter_price) / enter_price

        change_rate += 1
        balance *= change_rate 
        print(balance, change_rate)
        return change_rate

    except:
        pass

def candle_type(index):
    """
    Returns 1 if it is bullish
    Returns 0 if it is bearish
    """
    if NDX.iloc[index]["Close"] > NDX.iloc[index]["Open"]:
        return 1
    return 0 

def strategy_1():
    """
    Koşullar: 
        Bir önceki mum yükseliş mumu mu 
        Şu anki mum düşüş mumu mu 
        Şu anki mumun en yüksek seviyesi bir önceki mumun en yüksek seviyesinden daha mı yüksek

    İşleme Giriş:
        Bu mum kapanış değeri

    Hedef:  
        Önceki mumun low değeri
        
    Stop:
        Bu mumun high değeri olucak

    Ek :
        Tam tersi de geçerli
    """

def strategy_2():
    """
    Mumdan önceki 2 mum da düşüş mumu olup önceki mum bu mumdan iki önceki mumun low'undan daha düşük bir low'a sahip ve şu anki mum
    önceki mumun low'undan daha düşük bir değere sahip ise bu mumun kapanış değerinden girilip high değerine stop atılı 1:1r hedeflenir

    Koşullar: 
        Önceki iki mum düşüş mumu mu
        Her mum bir önceki mumun low değerinden daha düşük bir low değerine sahip mi
    
    İşleme Giriş:
        Bu mum kapanış değeri

    Hedef:  
        1:1 RR
    Stop:
        Bu mumun high değeri
        
    Ek :
        Tam tersi de geçerli
    
    """

number_of_trades = 0
balance = 100
