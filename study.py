from keras.layers import Input,Dense,Activation,Conv2D,MaxPooling2D,Flatten
from functools import reduce
from keras.models import Sequential
from keras.layers.advanced_activations import LeakyReLU
def compose(*funcs):
  """Compose arbitrarily many functions, evaluated left to right.

  Reference: https://mathieularose.com/function-composition-in-python/
  """
  # return lambda x: reduce(lambda v, f: f(v), funcs, x)
  if funcs:
    return reduce(lambda f, g: lambda *a, **kw: g(f(*a, **kw)), funcs)
  else:
    raise ValueError('Composition of empty sequence not supported.')

def add(x,y):
  return x+y

def multi(x):
  return x*2

def minus(x):
  return x-3

#
# a=Conv2D(filters=6, kernel_size=(5, 5), padding="valid", activation="tanh")
# b=MaxPooling2D(pool_size=(2, 2))
# c=Conv2D(filters=16, kernel_size=(5, 5), padding="valid", activation="tanh")
#
# print(compose(a, b, LeakyReLU(alpha=0.1))(Input(shape=(28, 28, 1))))
# print(compose(a, b, c)(Input(shape=(28, 28, 1))))
#
# model = Sequential()
# model.add(Conv2D(filters=6, kernel_size=(5, 5), padding="valid", activation="tanh", input_shape=[28, 28, 1]))
# model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(Conv2D(filters=16, kernel_size=(5, 5), padding="valid", activation="tanh"))
# print(model)



from keras.layers import UpSampling2D
import numpy as np
import tensorflow as tf
x=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
x=x.reshape(4,2,2)
print('x2:')
print(x)
x=tf.convert_to_tensor(x)
y=UpSampling2D(2)(x)
print('y1:')
print(y)
