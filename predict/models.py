from django.db import models

# Create your models here.
class PredictModel(models.Model):

    Pregnancies=models.IntegerField()
    Glucose=models.FloatField()
    BloodPressure=models.FloatField()
    SkinThickness=models.DecimalField(max_digits=5, decimal_places=2)
    Insulin=models.DecimalField(max_digits=8, decimal_places=2)
    BMI=models.FloatField()
    DiabetesPedigreeFunction=models.FloatField()
    age=models.IntegerField()




