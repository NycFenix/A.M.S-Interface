
import keras
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

ds = pd.read_csv('data.csv')

model = keras.Sequential([
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(5)
])


# Para teste, ver o desempenho de uma rede com apenas uma camada escondida
# model = keras.Sequential([
#     keras.layers.Dense(128, activation='relu'),
#     keras.layers.Dense(5)
# ])

# TODO: testar funções de perda diferentes
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])