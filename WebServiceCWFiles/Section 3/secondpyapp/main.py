from flask import Flask, render_template

#URLs for images accessed directly from the storage bucket
url1 = 'https://storage.googleapis.com/secondpybucket/dog_1.jpg'
url2 = 'https://storage.googleapis.com/secondpybucket/dog_2.jpg'
url3 = 'https://storage.googleapis.com/secondpybucket/dog_3.jpg'

#App engine will automatically look for 'app' within main.py unless specified in the config file
app = Flask(__name__)

@app.route("/chris")
def get_dogs():
    message = 'Here are some dogs for you'
    return render_template('index.html', message = message, user_image1 = url1, user_image2 = url2, user_image3 = url3)  

@app.route("/chris/1")
def get_dog1():
    message = 'Here is one dog'
    return render_template('collection.html', message = message, user_image1 = url1)

@app.route("/chris/2")
def get_dog2():
    message = 'Here is the second dog'
    return render_template('collection.html', message = message, user_image1 = url2)

@app.route("/chris/3")
def get_dog3():
    message = 'Here is the final dog'
    return render_template('collection.html', message = message, user_image1 = url3)