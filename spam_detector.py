# spam_detector.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Load and preprocess dataset
df = pd.read_csv('spam.csv')
df.Category =  df.Category.map({'ham': 0, 'spam':1})

X = df.Message
y = df.Category

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build model pipeline
model = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')),
    ('clf', LogisticRegression(solver='liblinear'))
])

# Train the model
model.fit(X_train, y_train)

# Prediction function
def predict_spam(message):
    prediction = model.predict([message])[0]
    return 'Spam' if prediction == 1 else 'Ham'
