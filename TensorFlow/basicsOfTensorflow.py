import tensorflow as tf

h = tf.constant("hello")
w = tf.constant(" World")

hw = h+w #this doesnt compute but adds sum operation to the graph

#session object acts as interface to external computation mechanism
with tf.Session() as sess:
    concatString = sess.run(hw)

print(concatString)

'''simple graph'''
a = tf.constant(5)
b = tf.constant(2)
c = tf.constant(3)
d = tf.multiply(a,b)
e = tf.add(c,b)
f = d+e

sess = tf.Session()
outs = sess.run([f,d,e])
out = sess.run(c)
sess.close()
print("outs = {}".format(outs))
print("out = {}".format(out))
print(f)

'''Interactive session : we don't need to use session oject
all the time'''
sess=tf.InteractiveSession()
c=tf.linspace(1.0,5.0,10)
print('c:{}'.format(c.eval()))

'''Variable creation'''
var = tf.Variable(tf.random_normal((1,5),4,1),name='var')
print('pre run var = {}'.format(var))


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    post_var = sess.run(var)
print("\npost run: \n{}".format(post_var))
