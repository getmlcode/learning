'''
    This doesn't take overfitting and underfitting into account,
    just bare bones stuff to understand how Tensorflow works.
    
    It demonstrates the use of Tensoflow Dataset API for creating
    data batches and cycle through dataset.
    
'''

import tensorflow as tf
import numpy as np

# === Create Artificial Data ===
def getArtificialData(noOfDataPoints,noOfFeatures):
    x_data = np.random.randn(noOfDataPoints,noOfFeatures)
    w_true = np.random.randn(1,noOfFeatures)
    b_true = np.random.randn()
    
    noise = np.random.randn(1,noOfDataPoints)*0.1
    y_data = np.matmul(w_true,x_data.T) + b_true + noise
    
    return (x_data,y_data,w_true,b_true)

# === Learn Parameters W,b ===
def fitParametersToData(Data,
                        Target,
                        W_0,
                        noOfDataPoints,
                        noOfFeatures,
                        stepSize=.02,
                        numOfEpochs=500,
                        batchSize=10
                        ):
    '''
    create the appropriate placeholders for our input
    and output data and Variables for our weights and
    intercept
    '''
    
    x = tf.placeholder(tf.float32,shape=[batchSize,noOfFeatures],name='inputData')
    y_true = tf.placeholder(tf.float32,shape=[1,batchSize],name='trueTarget')
    w = tf.Variable(W_0,dtype=tf.float32,name='weights')
    b = tf.Variable(0,dtype=tf.float32,name='bias')
    
    init = tf.global_variables_initializer()
    
    '''define prediction and loss'''
    y_pred = tf.matmul(w,tf.transpose(x)) + b
    loss = tf.reduce_mean(tf.square(y_true-y_pred))
    
    '''define optimizer'''
    optimizer = tf.train.GradientDescentOptimizer(stepSize)
    train = optimizer.minimize(loss)
    
    '''create dataset using TF Dataset API'''
    dataset = tf.data.Dataset.from_tensor_slices((Data, Target.T))
    dataset = dataset.batch(batchSize)
    dataset = dataset.shuffle(buffer_size = noOfDataPoints) #Algo gets different sets of databatch
    cycleIterator = dataset.make_initializable_iterator()
    nextBatch = cycleIterator.get_next()
    
    with tf.Session() as sess:
        sess.run(init)
        start_point = sess.run([w,b])
        descentStep = 1
        #Epoch means whole data set is seen once
        for Epoch in range(numOfEpochs): 
            sess.run(cycleIterator.initializer)
            print('\nEpoch {} in progress'. format(Epoch+1))
            while True:
                try:
                    batch = sess.run(nextBatch)
                    result=sess.run([train,w,b,loss],feed_dict={x:batch[0],y_true:batch[1].T})
                    print('step = {} , Loss = {}'. format(descentStep,result[3]))
                    descentStep=descentStep+1
                except tf.errors.OutOfRangeError:
                    print("\nEpoch {} Completed :) ". format(Epoch+1))
                    Epoch=Epoch+1
                    break
        print('\nStart Point : \nb_0=\n{}'.format(start_point[1]))
        #print("\nW_0=\n{}". format(start_point[0]))
    print('\n\nTotal No. Of Steps : ',descentStep-1)
    print('Step Size : ',stepSize)
    
    return (result[1],result[2],result[3])

if __name__ == "__main__":
    
    Data,Target,WeightTrue,BiasTrue = getArtificialData(1000,200)
    
    print('\nNumber Of Data Points : {}'. format(Data.shape[0]))
    print('Number Of Features : {}'. format(Data.shape[1]))
    
    W0 = np.random.randn(1,Data.shape[1])
    
    W_hat,b_hat,loss = \
    fitParametersToData(Data,Target,W0,Data.shape[0],Data.shape[1],batchSize=500)
    
    #print("\nW_hat = ",WeightTrue)
    print('\n\t\t\t=======Summary=======\nTrue Bias : \n{}'. format(BiasTrue))
    #print("\nW_hat = ",W_hat)
    print('\nb_hat = \n{}\nLoss = \n{}'. format(b_hat,loss))
    
