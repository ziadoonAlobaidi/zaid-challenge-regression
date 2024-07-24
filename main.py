
import seaborn as sns
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import mean_absolute_error

X = df[['livingarea', 'bedroomcount', 'kitchen', 'bathroomcount']]
y = df['price']




X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=25)


model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_pred


mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
mean_absolute_error(y_test, y_pred)
