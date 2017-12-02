from flask import Flask
from flask import request
import base64
import numpy as np
from PIL import Image
import io
import DigitRecognizerKeras as dr


app = Flask(__name__)


@app.route("/")
def main():
    return app.send_static_file('main.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    imgE = request.values['imageData']
    imgD=base64.b64decode(imgE)
    imgN = Image.open(io.BytesIO(imgD)) #Converting the decoded data into an array
    imgN=imgN.resize((28,28),Image.LANCZOS) #Resizeng the image to fit model's expectation
    data = np.asarray(imgN.split()[-1])#As the collors are in the alpha channel, here I split the array taking only the alpha
    ress=dr.recnoizeDigit(data)
    return str(ress)


app.run(host='0.0.0.0', port=8080)
