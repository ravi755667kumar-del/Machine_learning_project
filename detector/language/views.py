import json
from django.http import JsonResponse
from django.shortcuts import render
from .ml_model.model_loader import model, vectorizer


# Create your views here.
def index(request):
    return render(request, 'index.html')
def predict(request):
    if request.method == 'POST':
            data = json.loads(request.body)
            text = data.get("text")
            vector = vectorizer.transform([text])
            prediction = model.predict(vector)[0]
          
            return JsonResponse({'prediction': prediction})
    
    return JsonResponse({"error": "only POST requests are allowed."}
                                ,status=405)