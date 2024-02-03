import tensorflow as tf
import numpy as np

x_Data=np.random.randn(5,10)
w_Data=np.random.randn(10,1)

ph = tf.placeholder(tf.float32,shape=(None,None))
'''
If a shape is not fed or is passed as None, then the
placeholder can be fed with data of any size

Whenever we define a placeholder, we must feed it with some
input values or else an exception will be thrown. The input
data is passed to the session.run() method as a dictionary,
where each key corresponds to a placeholder variable name,
and the matching values are the data values given in the
form of a list or a NumPy array:
'''

print('ph={}, \ndata type = {}'.format(ph,ph.dtype))

x=tf.placeholder(tf.float32,shape=(None,10))
w=tf.placeholder(tf.float32,shape=(10,None))
b=tf.fill((x_Data.shape[0],1),-1.0)
xw_b=tf.matmul(x,w)+b

xwb_max = tf.reduce_max(xw_b)

with tf.Session() as sess:
    result = sess.run([xwb_max,xw_b,x,w,b],feed_dict={x: x_Data,w: w_Data})

print('\n\nmax = {} \nx = {} \n w = {} \nb = {} \nxwb = {}'.\
      format(result[0],result[2],result[3],result[4],result[1]))




