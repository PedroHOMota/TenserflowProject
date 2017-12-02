# Digit Recognitizion with neural network
This is my project for the module [Emerging Technologies](https://emerging-technologies.github.io/problems/project.html)
<br />
The project overview goes as follows:
<br />
```In this project you will create a web application in Python to recognise digits in images. Users will be able to visit the web application through their browser, submit (or draw) an image containing a single digit, and the web application will respond with the digit contained in the image```

## Requirements
1. [Python 3](https://docs.scipy.org/doc/numpy-1.13.0/user/install.html)
2. [Keras](https://www.pyimagesearch.com/2016/11/14/installing-keras-with-tensorflow-backend/)
3. [Numpy](https://docs.scipy.org/doc/numpy-1.13.0/user/install.html)
4. [h5py](http://docs.h5py.org/en/latest/build.html) 
5. Jquery, HTML5, [Bootstrap 4](https://getbootstrap.com/)
## How to clone
1. Get the github clone url
2. Use the following command to clone
```bash
$ git clone "url"
```

## How to Run
1. Execute the following command*
```bash
$ python main.py 
```
2. The ip and port used by the webapp will be shown on command prompt window
3. Access the ip on a browser

*The file keras-mnist.h5 has o be present on the same folder as the others scripts, otherwise  it won't run. The file can be clonned with this repo or generated running the NeuralNetworkTraining.py script.

## Architecture

### Back-end

The backend(server) uses flask to create an API with the following routes:
* "/"(root): Returns webapp's page
* "/upload": Receives a POST with canvas's image enconded in base64. Upon call, it decodes and resizes the image, then calls model to predict the image and returns the prediction to the front-end  


Python files in repository are structured as following:
<br />
**main.py**: Server file.
<br />
**NeuralNetworkTraining.py**: Python file used to create the model and train it, after its execution, the file "keras-mnist.h5" with the trained neural network is generated. 
<br />
**keras-mnist.h5**: As previously stated, this file contains the trained neural network.
<br />
<br />
**static**: Folder containing front-end.
<br />
    &nbsp;**main.html**: Application's HTML page


### Front-end

The front-end is an HTML page where the user can draw a number on a canvas and send it to the server to predict which number it was.


## Built using
* [Pingendo](https://pingendo.com/)
* [Visual Studio](https://www.visualstudio.com/)
