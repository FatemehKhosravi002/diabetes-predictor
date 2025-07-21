from django.shortcuts import render
from .forms import PredictForm
import joblib
import numpy as np

# مسیر مدل
import os
from django.conf import settings
model_path = os.path.join(settings.BASE_DIR, 'rf_model.joblib')
model = joblib.load(model_path)


def PredictView(request):
    result = None  # فقط عدد 0 یا 1

    if request.method == 'POST':
        form = PredictForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            features = np.array([[ 
                data['Pregnancies'], 
                data['Glucose'], 
                data['BloodPressure'],
                data['SkinThickness'], 
                data['Insulin'], 
                data['BMI'],
                data['DiabetesPedigreeFunction'], 
                data['age'] 
            ]])
            prediction = model.predict(features)[0]
            result = int(prediction)  # حتما عدد 0 یا 1

    else:
        form = PredictForm()

    return render(request, 'predict/predict_form.html', {
        'form': form,
        'prediction': result
    })
