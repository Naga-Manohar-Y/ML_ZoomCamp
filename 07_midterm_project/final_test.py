import pickle

input_file = 'XGBoost_model.bin'

with open(input_file, 'rb') as f_in: 
    dv, model = pickle.load(f_in)


dv, model


test_record1 = {'amount': 66.98,
 'card_present': 0,
 'card_type': 'Platinum Credit',
 'channel': 'POS',
 'city': 'Chicago',
 'city_size': 'medium',
 'country': 'USA',
 'device': 'Chrome',
 'distance_from_home': 100.51,
 'high_risk_merchant': 1,
 'hour': 3,
 'max_single_amount_in_last_hour': 90.48,
 'merchant': 'Netflix',
 'merchant_category': 'Entertainment',
 'merchant_type': 'online',
 'num_transactions_in_last_hour': 4,
 'total_amount_in_last_hour': 965.14,
 'transaction_hour': 9,
 'unique_countries_in_last_hour': 1,
 'unique_merchants_in_last_hour': 2,
 'weekend_transaction': 0,
 'year': 2021,
 'month': 6,
 'day': 13}

test_record2 = {'amount': 66.98,
 'card_present': 1,
 'card_type': 'Platinum Credit',
 'channel': 'POS',
 'city': 'Chicago',
 'city_size': 'medium',
 'country': 'USA',
 'device': 'Chip Reader',
 'distance_from_home': 10.51,
 'high_risk_merchant': 0,
 'hour': 3,
 'max_single_amount_in_last_hour': 66.98,
 'merchant': 'Home Depot',
 'merchant_category': 'Retail',
 'merchant_type': 'physical',
 'num_transactions_in_last_hour': 4,
 'total_amount_in_last_hour': 160.14,
 'transaction_hour': 9,
 'unique_countries_in_last_hour': 1,
 'unique_merchants_in_last_hour': 2,
 'weekend_transaction': 0,
 'year': 2021,
 'month': 6,
 'day': 13}

import pandas as pd
import xgboost as xgb

# Assuming `model` and `dv` are already loaded/defined in your environment






import requests


url = 'http://localhost:9696/predict'

response = requests.post(url, json=test_record1).json()

if response['transaction_status'] == 'Fraud':
    print('Send the notification to Customer')
else:
    print("Successful")


response = requests.post(url, json=test_record2).json()

if response['transaction_status'] == 'Fraud':
    print('Send the notification to Customer')
else:
    print("Successful")




