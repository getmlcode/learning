'''
@funtionality
This is just a simple code which restores graph architecture
and weight values. Aim is to learn restoration of checkpoint
weights in tensorflow.

It does the following : 
1. Restores a simple model from given checkpoint directory
   and reproduces the result of buildAndSaveModel.py by using
   same hard coded values for placeholder X.
   
2. Appends a new operation to existing graph by adding a
   non-zero bias and prints the result.

@Arguments
dir   : Directroty where checkpoint files are kept
model : Name of the model to be used
'''

import numpy as np
import tensorflow as tf
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--dir', type=str, default=os.getcwd()+"\checkpoint", required=False, help='Checkpoint Directory')
parser.add_argument('--model', type=str, default='simpleModel', required=False, help='Model Name (file name with .meta extension)')
args = parser.parse_args()

with tf.Session() as sess:
    print('\nModel Directory : {}'.format(args.dir))
    print('Model Name : {}'.format(args.model))
    
    saver = tf.train.import_meta_graph(os.path.join(args.dir,args.model+'.meta'))
    nonZeroBias = tf.Variable(tf.ones((10,))) #Add new variable

    x = tf.get_collection('v')[0]
    w = tf.get_collection('v')[1]
    Output = tf.get_collection('v')[2]
    ModifiedOutput = Output + nonZeroBias #Append new node to the restored graph
    
    #Intialize nonZeroBias before restoring saved graph values otherwise weights are reinitalized
    sess.run(tf.global_variables_initializer()) 
    saver.restore(sess,os.path.join(args.dir,args.model)) #2nd argument should be everything before .data
    
    #sess.run(tf.global_variables_initializer()) # If intialized here restored values of W will change
    #print(x)
    #print(w)
    #print(Output)

    result = sess.run([Output,x,w],{x:np.array([0.36948335, 0.13245803, 0.10355939, 0.9436994 ]).reshape(1,4)})
    print("Result=\n{}\nX=\n{}\nW=\n{}".format(result[0],result[1],result[2]))
    
    NewResult = sess.run(ModifiedOutput,\
                         {x:np.array([0.36948335, 0.13245803, 0.10355939, 0.9436994 ]).reshape(1,4)})
    print('\nNewResult=\n',NewResult)    