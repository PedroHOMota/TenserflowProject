from flask import Flask
from flask import render_template
from flask import request
import re
import base64
import json
from PIL import Image
import io
import tensorflow


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

    imgE = request.values['imageData']
    imgD=base64.b64decode(bytes(imgE,"ascii"))
    print(imgD)
    imgN = Image.open(io.BytesIO(imgD))
    imgN=imgN.resize((28,28))
    imgN.save("foo.png")
    # file = request.files['file']
    # file = request.get_json()["imageData"]
    # file = str.encode(file)
    # image = bytes(file)
    # print(image)
    # image = base64.standard_b64decode(image)
    # pyplot.plot(image)
    # pyplot.show()
    # print(image)
    # f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

    # add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)
    # file.save(f)

    # return render_template('index.html')
    return "teste"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
