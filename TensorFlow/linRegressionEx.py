'''
    This doesn't take overfitting and underfitting into account,
    just bare bones stuff to understand how Tensorflow works.
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
                        NumOfSteps=200
                        ):
    '''
    create the appropriate placeholders for our input
    and output data and Variables for our weights and
    intercept
    '''
    
    x = tf.placeholder(tf.float32,shape=[None,noOfFeatures],name='inputData')
    y_true = tf.placeholder(tf.float32,shape=[1,noOfDataPoints],name='trueTarget')
    w = tf.Variable(W_0,dtype=tf.float32,name='weights')
    b = tf.Variable(0,dtype=tf.float32,name='bias')
    
    init = tf.global_variables_initializer()
    
    '''define prediction and loss'''
    y_pred = tf.matmul(w,tf.transpose(x)) + b
    loss = tf.reduce_mean(tf.square(Target-y_pred))
    
    '''define optimizer'''
    optimizer = tf.train.GradientDescentOptimizer(stepSize)
    train = optimizer.minimize(loss)
    
    '''use dataset api for creating data batches'''
    
    

    with tf.Session() as sess:
        sess.run(init)
        start_point = sess.run([w,b])
        print('Start point\nw={}\nb={}'.format(start_point[0],start_point[1]))
        for step in range(NumOfSteps):
            result=sess.run([train,w,b,loss],feed_dict={x:Data,y_true:Target})
            print('step = {} , Loss = {}'. format(step+1,result[3]))
    
    print('\n\nTotal No. Of Steps : ',NumOfSteps)
    print('Step Size : ',stepSize)
    return (result[1],result[2],result[3])

if __name__ == "__main__":
    
    Data,Target,WeightTrue,BiasTrue = getArtificialData(500,50)
    
    print('\nNumber Of Data Points : {}'. format(Data.shape[0]))
    print('Number Of Features : {}'. format(Data.shape[1]))
    
    W0 = np.random.randn(1,Data.shape[1])
    
    W_hat,b_hat,loss = fitParametersToData(Data,Target,W0,Data.shape[0],Data.shape[1])
    print('\n\t\t\t=======Summary=======\nTrue Weight : \n{}\nTrue Bias : \n{}'.\
          format( WeightTrue,BiasTrue))
    print('\nW_hat = \n{}\nb_hat = \n{}\nLoss = \n{}'. format(W_hat,b_hat,loss))
    