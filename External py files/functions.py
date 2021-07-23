import os
import time
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import datetime as dt
import numpy as np

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import Dense, Dropout, LSTM
from tensorflow.keras.models import Sequential

def get_time():
    m_time = int(round(time.time() * 1000))
    return m_time
        
        
#####################################################################################

def get_data(currency1, currency2, start, end):
    data = web.DataReader(f'{currency1}-{currency2}', 'yahoo', start, end)
    return data

def train_data_sets(data, days):
    scaler = MinMaxScaler(feature_range=(0,1))
    scaled_data = scaler.fit_transform(data.values.reshape(-1,1))
    
    prediction_days = days
    
    X_train, y_train = [], [] 

    for x in range(prediction_days, len(scaled_data)):
        X_train.append(scaled_data[x-prediction_days:x, 0])
        y_train.append(scaled_data[x, 0])
    
    X_train, y_train = np.array(X_train), np.array(y_train)
    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
    
    return X_train, y_train


def model_build(X_train, y_train, batch, epoch):
    model = Sequential()

    model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50))
    model.add(Dropout(0.2))
    model.add(Dense(units=1))
    
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(X_train, y_train, epochs=epoch, batch_size=batch)
    
    
def test_data_inputs(data, start, end):
    scaler = MinMaxScaler()
    
    test_data = get_data(crypto_currency, base_currency, start, end)
    actual_prices = test_data['Close'].values

    total_dataset = pd.concat(data['Close'], test_data['Close'], axis=0)