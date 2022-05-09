import pandas as pd
import numpy as np
import datetime
import warnings
warnings.filterwarnings("ignore")
from sklearn.model_selection import train_test_split
data = pd.read_csv('./invoice.csv', nrows=50000)
def getdate(n,y):
    return data[data['name_customer']==n].loc[data['total_open_amount']==y][['clear_date','AgingBucket']].to_dict()