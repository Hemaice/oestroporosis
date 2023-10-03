from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the input values from the form
        input_features = [float(x) for x in request.form.values()]
        # Make a prediction using the loaded model
        prediction = model.predict([input_features])[0]
        # Convert the prediction to a meaningful result
        result = "Fracture" if prediction == 1 else "No Fracture"
        return render_template('index.html', prediction_text='Predicted Result: {}'.format(result))

if __name__ == '__main__':
    app.run(debug=True)
