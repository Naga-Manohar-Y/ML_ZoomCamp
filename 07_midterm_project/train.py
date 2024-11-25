import pandas as pd
import xgboost as xgb
import ast
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer

from sklearn.metrics import roc_auc_score

print('Loading the data ...')

file_path = "sampled_fraud_data.csv"
data = pd.read_csv(file_path)
df = pd.DataFrame(data)

print('Data preprocessing...')

conversion_rates = {
    'USD': 1.0,
    'EUR': 1.1,
    'GBP': 1.3,
    'JPY': 0.0075,
    'RUB': 0.013,
    'AUD': 0.65,
    'BRL': 0.2,
    'MXN': 0.05,
    'SGD': 0.73,
    'CAD': 0.74,
    'NGN': 0.002
}

# Convert amounts to USD
df['amount'] = df.apply(
    lambda x: x['amount'] * conversion_rates[x['currency']], axis=1
)

df.drop(['transaction_id', 'customer_id', 'card_number', 'ip_address', 'device_fingerprint', 'currency'], axis = 1, inplace = True)

boolean_columns = df.select_dtypes('boolean').columns

for boolean_col in boolean_columns:
  df[boolean_col] = df[boolean_col].astype(int)

if isinstance(df['velocity_last_hour'].iloc[0], str):
    df['velocity_last_hour'] = df['velocity_last_hour'].apply(ast.literal_eval)

# Step 2: Extract each metric from the dictionary
df['num_transactions_in_last_hour'] = df['velocity_last_hour'].apply(lambda x: x.get('num_transactions', 0))
df['total_amount_in_last_hour'] = df['velocity_last_hour'].apply(lambda x: x.get('total_amount', 0.0))
df['unique_merchants_in_last_hour'] = df['velocity_last_hour'].apply(lambda x: x.get('unique_merchants', 0))
df['unique_countries_in_last_hour'] = df['velocity_last_hour'].apply(lambda x: x.get('unique_countries', 0))
df['max_single_amount_in_last_hour'] = df['velocity_last_hour'].apply(lambda x: x.get('max_single_amount', 0.0))

df = df.drop(columns=['velocity_last_hour'])

df['timestamp'] = pd.to_datetime(df['timestamp'], format='ISO8601')

df['year'] = df['timestamp'].dt.year
df['month'] = df['timestamp'].dt.month
df['day'] = df['timestamp'].dt.day
df['hour'] = df['timestamp'].dt.hour
df.drop('timestamp', axis = 1, inplace = True)

print('Splitting the data ...')

df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)


df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=1)

df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_train = df_train.is_fraud.values
y_val = df_val.is_fraud.values
y_test = df_test.is_fraud.values

del df_train['is_fraud']
del df_val['is_fraud']
del df_test['is_fraud']

numerical = ['amount',
             'distance_from_home',
             'high_risk_merchant',
             'transaction_hour',
             'weekend_transaction',
             'num_transactions_in_last_hour',
             'total_amount_in_last_hour',
             'unique_merchants_in_last_hour',
             'unique_countries_in_last_hour',
             'max_single_amount_in_last_hour']

categorical = ['merchant_category',
               'merchant_type',
               'merchant',
               'country',
               'city',
               'city_size',
               'card_type',
               'card_present',
               'device',
               'channel',
               'year',
               'month',
               'day',
               'hour']

# train and validation
print('model training...')

dv = DictVectorizer(sparse=False)

train_dict = df_train[categorical + numerical].to_dict(orient='records')
X_train = dv.fit_transform(train_dict)

test_dict = df_test[categorical + numerical].to_dict(orient='records')

x_test = dv.fit_transform(test_dict)

dtrain = xgb.DMatrix(X_train, label=y_train,
                         feature_names=dv.get_feature_names_out().tolist())

dtest = xgb.DMatrix(x_test, feature_names=dv.get_feature_names_out().tolist())

xgb_params = {
    'eta': 0.5, 
    'max_depth': 6,
    'min_child_weight': 1,

    'objective': 'binary:logistic',
    'eval_metric': 'auc',

    'nthread': 8,
    'seed': 1,
    'verbosity': 1,
}

model = xgb.train(xgb_params, dtrain, num_boost_round=175)

print('predicting...\n')

y_pred = model.predict(dtest)

print("XGboost Results")
print('ROC AUC Score', roc_auc_score(y_test, y_pred))

print("Saving the XGboost model...")

output_file = f'XGBoost_model.bin'


with open(output_file, 'wb') as f_out: 
    pickle.dump((dv, model), f_out)

print("XGboost model saved")
