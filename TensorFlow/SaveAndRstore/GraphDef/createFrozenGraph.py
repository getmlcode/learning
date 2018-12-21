print('Importing Necessary Files')
import numpy as np
import tensorflow as tf
from tensorflow.python.tools import freeze_graph
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--dir', type=str, 
                    default=os.getcwd()+"\checkpoint", 
                    required=False, 
                    help='Checkpoint Directory')
parser.add_argument('--model', type=str, 
                    default='simpleModel', 
                    required=False, 
                    help='Model Name')

args = parser.parse_args()

#print(tf.test.is_gpu_available())
#tf.device("gpu:1")
print('\nCheckpoint directory : ',args.dir)
print('Model Name : {}'.format(args.model))



b=tf.Variable(tf.zeros((10,)))
W=tf.Variable(tf.random_uniform((4,10),-1,1))
X=tf.placeholder(tf.float32,(1,4))
h=tf.nn.relu(tf.matmul(X,W)+b)

saver = tf.train.Saver()
print('\nInitializing and saving graph checkpoints')
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    result = sess.run([h,X,W],{X:np.array([0.36948335, 0.13245803, 0.10355939, 0.9436994 ]).reshape(1,4)})
    print("Result=\n{}\nX=\n{}\nW=\n{}".format(result[0],result[1],result[2]))
    
    saver.save(sess,args.dir+"\\" + args.model) #create checkpoints

graphDef = tf.get_default_graph().as_graph_def()
#print(graphDef.node)
for node in graphDef.node:
    print(node.name)


# creates test.pb and simpleModel.data that can be used as input to freeze_graph.py
# to create frozenGraph.pb.
# freeze_graph.py is in tensorflow/python/tools

print('\nSaving graph def')  
tf.train.write_graph(graphDef, args.dir, "test.pb", False)
print('\nFreezing Graph')


freeze_graph.freeze_graph(input_graph=args.dir+'\\test.pb',
                          input_saver='',
                          input_checkpoint=args.dir+'\\simpleModel',
                          output_graph=args.dir+'\\frozenGraph.pb',
                          input_binary=True,
                          output_node_names='Relu',
                          initializer_nodes='',
                          filename_tensor_name='',
                          restore_op_name='',
                          clear_devices=True
                          )
print('\nGraph Frozen')

