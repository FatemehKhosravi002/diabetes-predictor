from django import forms
from .models import PredictModel

class PredictForm(forms.ModelForm):
    class Meta:
        model = PredictModel
        fields = '__all__'
        labels = {
            'Pregnancies': 'تعداد بارداری‌ها',
            'Glucose': 'سطح گلوکز',
            'BloodPressure': 'فشار خون',
            'SkinThickness': 'ضخامت پوست',
            'Insulin': 'انسولین',
            'BMI': 'شاخص توده بدنی',
            'DiabetesPedigreeFunction': 'سابقه خانوادگی دیابت',
            'age': 'سن',
        }
        widgets = {
            'Pregnancies': forms.NumberInput(attrs={'placeholder': 'تعداد بارداری‌ها را وارد کنید'}),
            'Glucose': forms.NumberInput(attrs={'placeholder': 'سطح گلوکز را وارد کنید'}),
            'BloodPressure': forms.NumberInput(attrs={'placeholder': 'فشار خون را وارد کنید'}),
            'SkinThickness': forms.NumberInput(attrs={'placeholder': 'ضخامت پوست را وارد کنید'}),
            'Insulin': forms.NumberInput(attrs={'placeholder': 'میزان انسولین را وارد کنید'}),
            'BMI': forms.NumberInput(attrs={'placeholder': 'شاخص توده بدنی را وارد کنید'}),
            'DiabetesPedigreeFunction': forms.NumberInput(attrs={'placeholder': 'سابقه خانوادگی دیابت را وارد کنید'}),
            'age': forms.NumberInput(attrs={'placeholder': 'سن را وارد کنید'}),
        }
