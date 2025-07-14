import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Simulate dataset with WHOIS columns (real project: extract from URLs)
df = pd.read_csv('phishing.csv')  # Your dataset must include WHOIS features

X = df.drop('Result', axis=1)
y = df['Result']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, 'model/phishing_model.pkl')
