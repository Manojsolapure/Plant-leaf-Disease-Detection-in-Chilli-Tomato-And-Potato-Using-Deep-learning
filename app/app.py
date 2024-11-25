from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import numpy as np
from flask import Flask, render_template, request
import os
import cv2
# import requests
from joblib import load
from tensorflow.keras.models import load_model
from datetime import datetime
# from keras.models import load_model

app = Flask(__name__, static_folder='static')

app.secret_key = '5766ghghgg7654dfd7h9hffh'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        re_password = request.form['re_password']
        security_question_1 = request.form['security_question_1']
        answer_1 = request.form['answer_1']
        security_question_2 = request.form['security_question_2']
        answer_2 = request.form['answer_2']

        # Check if email already exists in the database
        conn = sqlite3.connect('database/Farmer.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user_details WHERE email = ?", (email,))
        user = cursor.fetchone()

        if user is not None:
            # If the user already exists, add a flash message and redirect back to the signup page
            conn.close()
            session['message'] = 'Email already exists. Please go to the login page.'
            return redirect(url_for('signup', error='Email already exists.'))

        elif password != re_password:
            conn.close()
            session['message'] = 'Passwords do not match.'
            return redirect(url_for('signup', error='Passwords do not match.'))

        else:
            # Insert the new user into the database, including security questions and answers
            cursor.execute("""
                INSERT INTO user_details (
                    username, email, password, 
                    security_question_1, answer_1, 
                    security_question_2, answer_2
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (username, email, password, 
                  security_question_1, answer_1, 
                  security_question_2, answer_2))
            conn.commit()
            conn.close()

            return redirect(url_for('login'))
        
    elif request.args.get('error') is None:
        return render_template('signup.html')

    else:
        error = request.args.get('error')
        return render_template('signup.html', error=error)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect('database/Farmer.db')
        c = conn.cursor()

        c.execute(
            "SELECT * FROM user_details WHERE email = ? AND password = ?", (email, password))
        user = c.fetchone()
        conn.close()

        if user is not None:
            print(user)
            print(user[2])
            session['email'] = user[2]
            
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid email or password')
    else:
        return render_template('login.html')
    

@app.route('/dashboard')
def dashboard():

    email = session.get('email')
    print(email)
    conn = sqlite3.connect('database/Farmer.db')
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM user_details WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()


    if 'email' in session:
        return render_template('dashboard.html', current_user=session['email'], user=user[0])
    return redirect(url_for('login'))

@app.route('/reset', methods=['GET', 'POST'])
def reset():
    if request.method == 'POST':
        email = request.form['email']
        security_question_1 = request.form['security_question_1']
        answer_1 = request.form['answer_1']
        security_question_2 = request.form['security_question_2']
        answer_2 = request.form['answer_2']
        new_password = request.form['new_password']

        conn = sqlite3.connect('database/Farmer.db')
        cursor = conn.cursor()

        # Check if the email and security questions/answers match the records in the database
        cursor.execute("""
            SELECT * FROM user_details 
            WHERE email = ? 
            AND security_question_1 = ? 
            AND answer_1 = ? 
            AND security_question_2 = ? 
            AND answer_2 = ?
        """, (email, security_question_1, answer_1, security_question_2, answer_2))

        user = cursor.fetchone()

        if user:
            # If the answers match, update the password
            cursor.execute("""
                UPDATE user_details 
                SET password = ? 
                WHERE email = ?
            """, (new_password, email))
            conn.commit()
            conn.close()

            return redirect(url_for('login', message="Password successfully updated. Please log in with your new password."))
        else:
            # If answers do not match, display an error message
            conn.close()
            message = "Security answers do not match our records. Please try again."
            return render_template('reset.html', message=message)

    return render_template('reset.html')


@app.route('/new_plants')
def new_plants():

    email = session.get('email')
    print(email)
    conn = sqlite3.connect('database/Farmer.db')
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM user_details WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()


    if 'email' in session:
        return render_template('new_plants.html', current_user=session['email'], user=user[0])
    return redirect(url_for('login'))

@app.route('/disease_details1')
def disease_details1():
    return render_template('disease_details1.html')

@app.route('/disease_details2')
def disease_details2():
    return render_template('disease_details2.html')

@app.route('/disease_details3')
def disease_details3():
    return render_template('disease_details3.html')

@app.route('/disease_details4')
def disease_details4():
    return render_template('disease_details4.html')

@app.route('/disease_details5')
def disease_details5():
    return render_template('disease_details5.html')

@app.route('/disease_details6')
def disease_details6():
    return render_template('disease_details6.html')

@app.route('/disease_details7')
def disease_details7():
    return render_template('disease_details7.html')

@app.route('/disease_details8')
def disease_details8():
    return render_template('disease_details8.html')

@app.route('/disease_details9')
def disease_details9():
    return render_template('disease_details9.html')

@app.route('/disease_details10')
def disease_details10():
    return render_template('disease_details10.html')

@app.route('/disease_details11')
def disease_details11():
    return render_template('disease_details11.html')

@app.route('/disease_details12')
def disease_details12():
    return render_template('disease_details12.html')

@app.route('/disease_details13')
def disease_details13():
    return render_template('disease_details13.html')

@app.route('/disease_details14')
def disease_details14():
    return render_template('disease_details14.html')

@app.route('/disease_details15')
def disease_details15():
    return render_template('disease_details15.html')


## Page Redirect Steps

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# Function to preprocess the image for model prediction
def preprocess_image(file_path):
    gray = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    if gray is None:
        raise ValueError(f"Image at path {file_path} could not be loaded.")
    
    resized = cv2.resize(gray, (224, 224))
    resized_rgb = np.stack((resized,)*3, axis=-1)
    resized_rgb = resized_rgb / 255.0
    return np.expand_dims(resized_rgb, axis=0)

# Function to make predictions using an ensemble of models
def ensemble_prediction(file_path, models):
    # Preprocess the image
    processed_image = preprocess_image(file_path)

    # Collect predictions from each model
    predictions = []
    for model in models:
        prediction = model.predict(processed_image)
        predictions.append(prediction)

    # Convert list of predictions to a numpy array for easier manipulation
    predictions = np.array(predictions)

    # Average the predictions across models
    average_prediction = np.mean(predictions, axis=0)

    # Get the predicted class index from the averaged predictions
    predicted_class_index = np.argmax(average_prediction, axis=1)
    return predicted_class_index

UPLOAD_FOLDER = 'static/uploaded_images'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/check', methods=['GET', 'POST'])
def check():

    email = session.get('email')

    conn = sqlite3.connect('database/Farmer.db')
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM user_details WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()

    if request.method == 'POST':

        plant_name = request.form['plant']    
        file = request.files['plant-image']

        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        if plant_name == 'tomato':

            class_mapping = ['Tomato_Bacterial_spot', 'Tomato_Early_blight', 'Tomato_healthy', 'Tomato_Late_blight', 'Tomato_Leaf_Mold', 'Tomato_Septoria_leaf_spot', 'Tomato__Tomato_mosaic_virus']

            # Load your trained models
            model_paths = ['../models/vgg/tomato.h5', 
                        '../models/resnet/tomato.h5', 
                        '../models/mixednet/tomato.h5',
                        '../models/efficient/tomato.h5']

            models = [load_model(model_path) for model_path in model_paths]

            predicted_class_index = ensemble_prediction(file_path, models)

            predicted_class = class_mapping[predicted_class_index[0]]
    
        elif plant_name == 'potato':

            class_mapping = ['Nematode', 'Phytopthora', 'Potato___Early_blight', 'Potato___healthy', 'Potato___Late_blight', 'Virus']
            
            model_paths = ['../models/vgg/potato.h5', 
                        '../models/resnet/potato.h5', 
                        '../models/mixednet/potato.h5',
                        '../models/efficient/potato.h5']

            models = [load_model(model_path) for model_path in model_paths]

            predicted_class_index = ensemble_prediction(file_path, models)

            predicted_class = class_mapping[predicted_class_index[0]]

        elif plant_name == 'chilli':

            class_mapping =  ['healthy', 'leaf curl', 'leaf spot', 'whitefly', 'yellowish']

            model_paths = ['../models/vgg/chilli.h5', 
                        '../models/resnet/chilli.h5', 
                        '../models/mixednet/chilli.h5',
                        '../models/efficient/chilli.h5']

            models = [load_model(model_path) for model_path in model_paths]

            predicted_class_index = ensemble_prediction(file_path, models)

            predicted_class = class_mapping[predicted_class_index[0]]

         # Insert the data into the SQLite database
        conn = sqlite3.connect('database/Farmer.db')
        cursor = conn.cursor()
        
        cursor.execute(
            """
            INSERT INTO predictions (username, image_name, plant_name, predicted_class, timestamp)
            VALUES (?, ?, ?, ?, ?)
            """,
            (user[0], file.filename, plant_name, predicted_class, datetime.now())
        )
        
        conn.commit()
        conn.close()
        
        return render_template('check.html', image=file_path, predicted_label=predicted_class, user=user[0])
    
    return render_template('check.html')


if __name__ == "__main__":
    app.run(debug=True)
