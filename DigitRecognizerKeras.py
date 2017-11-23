import numpy as np

from keras.models import load_model

model = load_model('keras-mnist.h5')
print("chegou aqui")
def recnoizeDigit(data):
    data = np.ndarray.flatten(data)
    data=data.reshape(1,784)
    print(data)
    prediction = np.around(model.predict_classes(data)).astype(np.int)[0]
    print(prediction)
    return prediction
