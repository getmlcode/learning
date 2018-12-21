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


def_G = tf.get_default_graph() #get the default graph
graphDef = def_G.as_graph_def() #returns serialized GraphDef representation of graph

print(graphDef.node)
for node in graphDef.node:
    print(node.name)

tf.train.write_graph(graphDef, args.dir, "test.pb", False)






