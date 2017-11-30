import numpy as np

from keras.models import load_model

model = load_model('keras-mnist.h5')

def recnoizeDigit(data): #The image has to be an array 28x28
    data = np.ndarray.flatten(data) #Transforms the 2d array into a 1d array row major
    data=data.reshape(1,784) 
    prediction = np.around(model.predict_classes(data)).astype(np.int)[0]
    print(prediction)
    return prediction
