import tensorflow as tf
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--dir', type=str, default=os.getcwd()+"\checkpoint", required=False, help='Checkpoint Directory')
parser.add_argument('--model', type=str, default='simpleModel', required=False, help='Model Name')
args = parser.parse_args()

with tf.Session() as sess:
    print('\nModel Directory : {}'.format(args.dir))
    print('Model Name : {}'.format(args.model))
    
    saver = tf.train.import_meta_graph(os.path.join(args.dir,args.model+'.meta'))
    #sess.run(tf.global_variables_initializer())
    saver.restore(sess,os.path.join(args.dir,args.model))
    trainables = tf.trainable_variables()
    for trainVars in trainables:
        print(sess.run(trainVars))
        print(trainVars)