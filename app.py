# app.py

from flask import Flask, render_template, redirect, url_for
from forms import DataEntryForm
import pickle  
import numpy as np
from tensorflow.keras.models import model_from_json

# Load the model data from the .pkl file
with open('model.pkl', 'rb') as file:
    model_data = pickle.load(file)

# Reconstruct the model from the saved config and weights
model = model_from_json(model_data['config'])
model.set_weights(model_data['weights'])




app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

@app.route('/', methods=['GET', 'POST'])
def home():
    form = DataEntryForm()
    prediction = None
    if form.validate_on_submit():
        # Process form data
        inputs = [
            form.year.data,
            form.month.data,
            form.day.data,
            form.hour.data,
            form.minute.data,
            form.temperature.data,
            form.humidity.data
        ]
        inputs = np.array([inputs])
        
        # Assuming the model expects a 2D array input
        prediction = model.predict(inputs)
        prediction=np.argmax(prediction)
        
        # Handle the data as needed (e.g., store in database, perform calculations, etc.)
        
    
    return render_template('home.html', form=form, prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)
