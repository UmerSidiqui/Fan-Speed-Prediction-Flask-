README: BLDC Fan Data Analysis Using ANN
This project demonstrates the analysis of BLDC (Brushless Direct Current) fan data using an Artificial Neural Network (ANN) model to predict the speed of the fan based on various environmental factors. The project is deployed on Flask and includes a trained ANN that is used to make predictions on real-time data.

Dataset Overview
The dataset includes the following features:

year: Year of the observation
month: Month of the observation
day: Day of the observation
hour: Hour of the observation
minutes: Minute of the observation
temperature: Temperature reading at the time of observation
humidity: Humidity reading at the time of observation
The target variable is new_speed, representing the speed of the BLDC fan.

Model Summary
A Sequential Artificial Neural Network (ANN) model was built using TensorFlow/Keras. The model consists of:

Three hidden layers with 64, 32, and 8 neurons, respectively, using the ReLU activation function.
A final output layer with 6 neurons and a softmax activation for multi-class classification (predicting fan speeds).
The model was trained for 150 epochs with a batch size of 32 and uses categorical crossentropy as the loss function and Adam optimizer. The dataset was split into training and testing sets using an 80-20 ratio, and the features were scaled using StandardScaler


Install the required dependencies:
pip install -r requirements.txt



Run the Flask app:
python app.py
The web application will be available at http://127.0.0.1:5000/.

Key Features
Predict BLDC fan speed based on environmental factors (temperature, humidity, etc.).
The ANN model achieves high accuracy in predicting fan speed.
Flask-based web deployment for real-time speed prediction based on user input.
