import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# ۱) بارگذاری داده
df = pd.read_csv("/home/bahar/last-try/diabetes.csv")

# ۲) انتخاب ۸ ویژگی اصلی
feature_cols = [
    'Pregnancies', 
    'Glucose', 
    'BloodPressure', 
    'SkinThickness', 
    'Insulin', 
    'BMI', 
    'DiabetesPedigreeFunction', 
    'Age'
]

# ۳) جایگزینی مقادیر گمشده با میانه ستون
for col in feature_cols:
    df[col].fillna(df[col].median(), inplace=True)

X = df[feature_cols]
y = df['Outcome']

# ۴) تقسیم داده به آموزش و تست
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ۵) ساخت و آموزش مدل جنگل تصادفی
rf_model = RandomForestClassifier(random_state=42, n_estimators=100)
rf_model.fit(X_train, y_train)

# ۶) پیش‌بینی روی داده تست
y_pred = rf_model.predict(X_test)

# ۷) گزارش دقت و معیارها
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# ۸) ذخیره مدل برای استفاده بعدی
joblib.dump(rf_model, "/home/bahar/last-try/rf_model.joblib")
print("مدل Random Forest ذخیره شد.")

# ۹) نمونه پیش‌بینی روی داده مشخص (مثلاً یک نمونه مثبت احتمالی)
sample_data = [[10, 180, 90, 35, 200, 40, 1.2, 50]]
prediction = rf_model.predict(sample_data)
print("Prediction for sample data:", "Positive" if prediction[0] == 1 else "Negative")
