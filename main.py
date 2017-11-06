from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Hello World!"
	
@app.route("/")
def main(method=POST):
    return "Hello World!"
	
def recognizeDigit(image):
	digit=0
	return digit 
	
	
def loadDataToMemory():
	return FALSE

app.start()