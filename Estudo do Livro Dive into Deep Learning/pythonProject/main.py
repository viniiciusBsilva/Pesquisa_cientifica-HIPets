import cv2
import keras
import numpy as np
from keras import layers

img_size=32
img = cv2.imread("dog.jpg")
cv2.imshow("img", img)
cv2.waitKey(0)
'''img = cv2.resize(img, (img_size,img_size))

#Model
model = keras.Sequential()
model.add(layers.Conv2D(input_shape=(img_size,img_size), filters=64, kernel_size=(3,3)))
model.add(layers.MaxPooling2D(pool_size=(2,2), strides=(1,1)))

result = model.predict(np.array([img]))
print(result)'''