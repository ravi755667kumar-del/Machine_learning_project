import os
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model =joblib.load(os.path.join(BASE_DIR, 'model.pkl'))
vectorizer=joblib.load(os.path.join(BASE_DIR, "vectorizer.pkl"))