from django.shortcuts import render
import joblib
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Create your views here.
def index(request):

    model = joblib.load('model_svc.pkl')

    if request.method == 'POST':
        message = request.POST['title']

        prediction = model.predict([message])

        def predict(item):
            if item == 1:
                return "Positive Review"
            else:
                return "Negative Review"

        predict_result = predict(prediction)
        return render(request, 'index.html', {'predicts':predict_result})

    return render(request, 'index.html')
