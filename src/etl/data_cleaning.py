import pandas as pd

def clean_data(data):
    data = data.dropna()
    data['date'] = pd.to_datetime(data['date'])
    return data