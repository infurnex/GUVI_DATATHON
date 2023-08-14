import pandas as pd
import numpy as np
import json
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder
from statsmodels.stats.outliers_influence import variance_inflation_factor
import seaborn as sns
import matplotlib. pyplot as plt

df= pd.read_excel("/content/House_Rent_Train.xlsx")
df= df.dropna()
df.describe()

categorical= [ 'type', 'lease_type', 'facing', 'water_supply', 'building_type', 'furnishing', 'parking']

# Initialize the OneHotEncoder
encoder = LabelEncoder()

df['lease_type']= encoder.fit_transform(df['lease_type'])
