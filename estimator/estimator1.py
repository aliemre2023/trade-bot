import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import yfinance as yf
from datetime import datetime as dt, timedelta

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM



def sequential_model(company):
    # load data
    end = dt.today()
    start = end - timedelta(days=2*365)
    data = yf.download(company, start, end)

    ## PREPARE DATA

    scaler = MinMaxScaler(feature_range=(0,1))
    scaled_data = scaler.fit_transform(data["Close"].values.reshape(-1,1))

    prediction_days = 60

    x_train = []
    y_train = []

    for x in range(prediction_days, len(scaled_data)):
        x_train.append(scaled_data[x-prediction_days:x, 0])
        y_train.append(scaled_data[x, 0])

    x_train = np.array(x_train)
    y_train = np.array(y_train)

    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))


    ## BUILD THE MODEL

    model = Sequential()

    model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50))
    model.add(Dropout(0.2))
    model.add(Dense(units=1)) # prediction of the next point

    model.compile(optimizer="adam", loss="mean_squared_error")
    model.fit(x_train, y_train, epochs=25, batch_size=32)

    ## Predict next day
    last_day_data = scaled_data[-prediction_days:]
    last_day_data = last_day_data.reshape(1, -1, 1)

    prediction = model.predict(last_day_data)
    prediction = scaler.inverse_transform(prediction)

    return prediction >= data["Close"][-1]
