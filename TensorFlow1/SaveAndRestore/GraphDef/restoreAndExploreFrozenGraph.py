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