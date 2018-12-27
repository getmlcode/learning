from keras.myModels import Sequential
from keras.layers import Dense, Activation
from keras.layers import Dropout


# =======================================================
# Different predefined myModels are stacked together in
# a linear pipeline of layers
# =======================================================

myModel = Sequential()
myModel.add(Dense(2, input_shape=(784,)))
myModel.add(Activation('relu'))
myModel.add(Dropout(0.5))
myModel.add(Dense(2))
myModel.add(Activation('sigmoid'))
myModel.add(Dropout(.5))
myModel.add(Dense(5))
myModel.add(Activation('softmax'))
myModel.summary()