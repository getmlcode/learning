import numpy as np
import tensorflow as tf
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--dir', type=str, 
                    default=os.getcwd()+"\checkpoint",
                    required=False, 
                    help='Checkpoint Directory')
parser.add_argument('--model', type=str, 
                    default='frozenGraph', 
                    required=False, 
                    help='Name Of Frozen Graph')

args = parser.parse_args()

FrozenGraphDef = tf.GraphDef()
FrozenGraphDef.ParseFromString(open(args.dir+'\\'+args.model+'.pb','rb').read())
for node in FrozenGraphDef.node:
    print("name :",node.name)
    print("\t -op :",node.op)
    print("\t -input :",node.input)
    print("\t -device :",node.device)
    

dataPoint = np.array([0.36948335, 0.13245803, 0.10355939, 0.9436994 ]).reshape(1,4)
with tf.Session() as sess:
    tf.import_graph_def(FrozenGraphDef,
                        input_map=None,
                        return_elements=None,
                        name=''
                        )
    Y = tf.get_default_graph().get_operation_by_name('ReluOUT')
    X = tf.get_default_graph().get_tensor_by_name('input:0')
    
    result = sess.run(Y,{X:dataPoint})
    print(result)