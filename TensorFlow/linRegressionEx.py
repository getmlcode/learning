'''
This doesn't take overfitting and underfitting into account
this is just bare bones stuff to understand some workings of
Tensorflow.
'''

import tensorflow as tf
import numpy as np
# === Create data ===
x_data = np.random.randn(2000,3)
w_true = [3.0,5.0,0.1]
b_true = -0.2

noise = np.random.randn(1,2000)*0.1
y_data = np.matmul(w_true,x_data.T) + b_true + noise

'''
create the appropriate placeholders for our input
and output data and Variables for our weights and
intercept
'''

x = tf.placeholder(tf.float32,shape=[None,3])
y_true = tf.placeholder(tf.float32,shape=None)
w = tf.Variable([[0,0,0]],dtype=tf.float32,name='weights')
b = tf.Variable(0,dtype=tf.float32,name='bias')
init = tf.global_variables_initializer()

'''define prediction and loss'''
y_pred = tf.matmul(w,tf.transpose(x)) + b
loss = tf.reduce_mean(tf.square(y_true-y_pred))

NumOfSteps = 10
optimizer = tf.train.GradientDescentOptimizer(0.2)
train = optimizer.minimize(loss)

with tf.Session() as sess:
    sess.run(init)
    start_point = sess.run([w,b])
    print('Start point\nw={}\nb={}'.format(start_point[0],start_point[1]))
    for step in range(NumOfSteps):
        result=sess.run([train,w,b,loss],feed_dict={x:x_data,y_true:y_data})
        print('step : {} \nw = {}\nb = {}\nLoss = {}'.\
        format(step+1,result[1],result[2],result[3]))
