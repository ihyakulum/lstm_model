import os
import pandas as pd
import numpy as np
from tensorflow import keras
from pandas_datareader import data
import matplotlib.pyplot as plt
import datetime
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import math
