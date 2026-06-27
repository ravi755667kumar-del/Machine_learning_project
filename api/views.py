from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import joblib
import os

# 1. Locate and load your trained model and vectorizer
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'ml_model', 'model.pkl')
VEC_PATH = os.path.join(os.path.dirname(__file__), 'ml_model', 'vectorizer.pkl')

model = joblib.load(MODEL_PATH)
cv = joblib.load(VEC_PATH)

@csrf_exempt # Disables CSRF tokens for easier API testing
def predict(request):
    if request.method == 'POST':
        try:
            # 2. Receive the JSON data sent from your frontend UI
            data = json.loads(request.body)
            text_from_ui = data.get('text', '') # Assumes frontend sends {"text": "Bonjour"}

            if not text_from_ui:
                return JsonResponse({'error': 'No text provided'}, status=400)
            
            # 3. Translate the text into numbers using the vectorizer
            vectorized_text = cv.transform([text_from_ui]).toarray()
            
            # 4. Predict the language using the model
            prediction = model.predict(vectorized_text)[0]
            
            # 5. Send the result back to the frontend
            return JsonResponse({'prediction': prediction}, status=200)
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
            
    return JsonResponse({'error': 'Only POST requests allowed'}, status=405)