#Adapted from tensorflow tutorials
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf


mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

x = tf.placeholder(tf.float32, [None, 784]) #None significa que a dimensão do array pode ser de qualquer tamanho, no caso, 1# pq vou mandar só uma img
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

y = tf.nn.softmax(tf.matmul(x, W) + b)
y_ = tf.placeholder(tf.float32, [None, 10])
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

sess = tf.InteractiveSession()
tf.global_variables_initializer().run()

for _ in range(1000):
  batch_nums, batch_lbls = mnist.train.next_batch(100)
  sess.run(train_step, feed_dict={x: batch_nums, y_: batch_lbls})

def evaluateIMG(img):
    result = sess.run(tf.argmax(y,1), feed_dict={x: [img]})
    return result
