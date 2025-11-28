# train_strong_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

# Load dataset
df = pd.read_csv('strong_food_data.csv')

X = df[['Type','Storage','Packaging','Temperature','Humidity','Age']]
y = df['Expired']

# Preprocessing for categorical columns
categorical_features = ['Type','Storage','Packaging']
numeric_features = ['Temperature','Humidity','Age']

preprocessor = ColumnTransformer(transformers=[
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
], remainder='passthrough')

# Random Forest Pipeline
clf = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=200, random_state=42))
])

# Split and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf.fit(X_train, y_train)

print("Model trained. Accuracy:", clf.score(X_test, y_test))

# Save the pipeline (preprocessing + model)
joblib.dump(clf, 'strong_food_model.pkl')
print("Model saved as strong_food_model.pkl")
