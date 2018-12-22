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
    
    loader = tf.train.import_meta_graph(os.path.join(args.dir,args.model+'.meta'))
    loader.restore(sess,os.path.join(args.dir,args.model))
    
    #Get list of trainable variables , (W,b here)
    trainables = tf.trainable_variables()
    print('\nTrainables')
    for trainVars in trainables:
        print(sess.run(trainVars))
        print('\t-',trainVars)
        
    graph = tf.get_default_graph()
    
    operations = graph.get_operations()
    print("\nOperations")
    for op in operations:
        print('\n\t-',op.name)
        print('\t--Depends On :',op.control_inputs)
    
    collect = graph.collections
    print('\nCollections : ',collect)
    for cname in collect:
        c = tf.get_collection(cname)
        print('Collection : ',cname)
        print(c)
    
    print("\nGraph Def Object")
    graphDef = tf.get_default_graph().as_graph_def()
    print(graphDef.node)
    
    print('No. Of Collection : ',len(collect))
    print("No. Of Operations : ",len(operations))
    print("No. Of Trainable Variables : ",len(trainables))