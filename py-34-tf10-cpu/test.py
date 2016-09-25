import tensorflow as tf
print(tf)
a = tf.constant(3)
sess = tf.Session()
d = sess.run(a)
print(d)
print("Tensorflow is up and running ")
