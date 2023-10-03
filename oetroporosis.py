# -*- coding: utf-8 -*-
"""oetroporosis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GCmUWrFwKVQQvxp34QhTnXYLxu1x5rZa
"""

import pandas as pd
import numpy as np

data = pd.read_csv('/content/drive/MyDrive/5th sem/MLDL/project/bmd.csv')

data.head()

data.info()

data.isnull().sum()

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
disease =['sex','fracture','medication']
data[disease]=data[disease].apply(le.fit_transform)
data

x=data.drop('fracture',axis=1)
x

y = data['fracture']
y

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25)

from sklearn.svm import SVC
classifier = SVC(kernel = 'linear')
classifier.fit(x_train,y_train)

y_preds = classifier.predict(x_test)

classifier.predict([[ 469,  57,  0,  64, 155.5, 0, 18, 0.8793  ]])

import joblib

# Train your model
classifier.fit(x_train,y_train)

# Save the model to a file
joblib.dump(classifier, 'model.pkl')

pip install gradio

import gradio as gr
import joblib
import pandas as pd


# Load the SVM model
model = joblib.load('model.pkl')  # Replace 'your_svm_model.pkl' with your model file path


def predict_chronic_kidney_disease(id, age, sex, weight_kg, height_cm, medication, waiting_time, bmd):
    # Create a feature vector with the input values
    input_features = pd.DataFrame({
        'id': [id],
        'age': [age],
        'sex': [sex],
        'weight_kg': [weight_kg],
        'height_cm': [height_cm],
        'medication': [medication],
        'waiting_time': [waiting_time],
        'bmd': [bmd]

    })


    # Make a prediction using the model
    prediction = model.predict(input_features)

    # Return the prediction
    if prediction == 1:
        result = "Oestroporosis Disease"
    else:
        result = "Not Oestroporosis Disease"

    return result


# Create a Gradio interface
iface = gr.Interface(fn=predict_chronic_kidney_disease,
                     inputs=["number", "number", "number", "number", "number", "number", "number", "number"],
                     outputs="text", live=True, title="Oestroporosis Disease Prediction")


# Launch the Gradio interface
iface.launch()
