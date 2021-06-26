from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/meta")
def get_meta():
    meta1 = requests.get('https://www.googleapis.com/storage/v1/b/secondpybucket/o/dog_1.jpg')
    meta2 = requests.get('https://www.googleapis.com/storage/v1/b/secondpybucket/o/dog_2.jpg')
    meta3 = requests.get('https://www.googleapis.com/storage/v1/b/secondpybucket/o/dog_3.jpg')
    
    return render_template('index.html', meta_data1 = meta1.text, meta_data2 = meta2.text, meta_data3 = meta3.text)