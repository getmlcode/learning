import numpy as np
import tensorflow as tf
import os
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument('--dt', type=str, default='txt', required=False)
parser.add_argument('--dir', type=str, default=os.getcwd()+"\data", required=False, help='Data Directory')
parser.add_argument('--fname', type=str, default='test', required=False)
args = parser.parse_args()

def iterateOverText():
    dataset = tf.data.TextLineDataset(args.dir + '\\' + args.fname + '.'+ args.dt)
    iterator = dataset.make_one_shot_iterator()
    nextElement = iterator.get_next()
    
    #Iterate once with no batch and shuffle
    print("\n---Iterate once with no batch or shuffle")
    with tf.Session() as sess:
        while True:
            try:
                print(sess.run(nextElement))
            except tf.errors.OutOfRangeError:
                print("End Of Dataset")
                break
    
    
    #Iterate once with batch and shuffle
    print("\n---Iterate once with batch and shuffle")
    dataset = dataset.shuffle(buffer_size=5)
    dataset = dataset.batch(2)
    batchIterator = dataset.make_one_shot_iterator()
    nextBatch = batchIterator.get_next()
    with tf.Session() as sess:
        while True:
            try:
                print(sess.run(nextBatch))
            except tf.errors.OutOfRangeError:
                print("End Of Dataset")
                break
    
    #Iterate for fixed duration with batch and shuffle
    print("\n---Iterate for fixed duration with batch and shuffle")
    cycleIterator = dataset.make_initializable_iterator()
    nextCycleElement = cycleIterator.get_next()
    t_end = time.time() + 60 * 2 #loop for 2 minutes
    with tf.Session() as sess:
        sess.run(cycleIterator.initializer)
        while time.time() < t_end:
            try:
                print(sess.run(nextCycleElement))
            except tf.errors.OutOfRangeError:
                print("\nReached End Of Dataset")
                print("Restarting")
                sess.run(cycleIterator.initializer)
    
    
def processNumpyArray():
    print(np.__version__)

if __name__=="__main__":
    
    if args.dt == 'txt':
        iterateOverText()    