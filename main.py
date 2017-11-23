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


@app.route("/analyse", methods=["POST"])
def recognizeDigit():
    return "Hello World!"


def loadDataToMemory():
    return ""


@app.route('/upload', methods=['POST'])
def upload_file():
    print('chegou aqui')
    #imgE=request.get_json(True)
    imgE = request.values['imageData']
    print(imgE)
    imgD=base64.b64decode(imgE)
    #print(imgD)
    imgN = Image.open(io.BytesIO(imgD))
    imgN=imgN.resize((28,28),Image.LANCZOS)
    data = np.asarray(imgN.split()[-1])#As the collers are in the alpha channel, here I split the array taking only the alpha
    #data = (lambda x: 255 - x)(np.asarray(imgN.split()[-1]))
    #data.setflags(write=1)
    data = np.ndarray.flatten(data)
    ress=dr.recnoizeDigit(data)
    print(ress)
    return str(ress)


app.run(host='0.0.0.0', port=8080)
