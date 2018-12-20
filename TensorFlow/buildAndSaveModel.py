import numpy as np
import tensorflow as tf
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--dir', type=str, default=os.getcwd()+"\checkpoint", required=False, help='Checkpoint Directory')
parser.add_argument('--model', type=str, default='simpleModel', required=False, help='Model Name')
args = parser.parse_args()

#print(tf.test.is_gpu_available())
#tf.device("gpu:1")
print('\nCheckpoint directory : ',args.dir)
print('Model Name : {}'.format(args.model))

b=tf.Variable(tf.zeros((10,)))
W=tf.Variable(tf.random_uniform((4,10),-1,1))
X=tf.placeholder(tf.float32,(1,4))
h=tf.nn.relu(tf.matmul(X,W)+b)

#make collection of ops and vars so as to access them when graph is restored
V=[X,W,h]
tf.add_to_collection('v',V[0])
tf.add_to_collection('v',V[1])
tf.add_to_collection('v',V[2])

saver = tf.train.Saver()
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    result = sess.run([h,X,W],{X:np.array([0.36948335, 0.13245803, 0.10355939, 0.9436994 ]).reshape(1,4)})
    print("Result=\n{}\nX=\n{}\nW=\n{}".format(result[0],result[1],result[2]))
    '''save graph and weights'''
    saver.save(sess,args.dir+"\\" + args.model)