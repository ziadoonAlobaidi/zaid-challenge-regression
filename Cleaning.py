import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor
import pickle
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import GradientBoostingRegressor


filename  ='final_dataset.json'
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
df = pd.read_json(filename)

df.columns = df.columns.str.lower()


df.drop('url', axis = 1, inplace = True)
df.drop('monthlycharges', axis = 1, inplace = True)
df.drop('kitchen', axis = 1, inplace = True)

print(df.isnull().sum())

df['constructionyear'].fillna(df['constructionyear'].mean(),inplace=True)
df['bathroomcount'].fillna(df['bathroomcount'].median(), inplace = True)
df['garden'].fillna(0, inplace = True)
df['showercount'].fillna(0, inplace = True)
df['gardenarea'].fillna(0, inplace = True)
df['roomcount'].fillna(0, inplace = True)
df['surfaceofplot'].fillna(0, inplace = True)
df['fireplace'].fillna(0 , inplace = True)
df['floodingzone'].fillna('NON_FLOOD_ZONE', inplace = True)
df['furnished'].fillna(0, inplace = True)
df['peb'].fillna(df.peb.mode()[0], inplace = True)
df['swimmingpool'].fillna(0, inplace = True)
df['numberoffacades'].fillna(df['numberoffacades'].median(),inplace=True)
df['livingarea'].fillna(df['livingarea'].median(),inplace=True)
df['terrace'].fillna(0, inplace = True)
df['toiletcount'].fillna(df['toiletcount'].median(), inplace = True)

q1 = df.constructionyear.quantile(0.18)
q3 = df.constructionyear.quantile(0.9)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

df = df[(df.constructionyear > lower_bound) & (df.constructionyear < upper_bound)]

df = df.dropna(subset=['stateofbuilding'])
df = df.dropna(subset=['district'])
df = df.dropna(subset=['province'])
df = df.dropna(subset=['region'])
df = df.dropna(subset=['locality'])
df = df.dropna(subset=['furnished'])

print(df.isnull().sum())

ordinal_encoder = OrdinalEncoder()
df['peb_encoded'] = ordinal_encoder.fit_transform(df[['peb']])

df= df.drop(['locality'],axis=1)

encoder = OneHotEncoder(sparse_output=False)
categorical_columns = df.select_dtypes(include=['object']).columns.tolist()

one_hot_encoded = encoder.fit_transform(df[categorical_columns])

one_hot_df = pd.DataFrame(one_hot_encoded, columns=encoder.get_feature_names_out(categorical_columns))

df_encoded = pd.concat([df, one_hot_df], axis=1)

df_encoded = df_encoded.select_dtypes(exclude=object)

df_encoded = df_encoded.dropna()

target_column = 'price'

# Features (X) and target (y)
X = df_encoded.drop(columns=[target_column])
y = df_encoded[target_column]


X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3,shuffle=True)



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the GradientBoostingRegressor
model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=13, random_state=22)

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean absolute Error: {mae}')
print(f'R^2 Score: {r2}')

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)