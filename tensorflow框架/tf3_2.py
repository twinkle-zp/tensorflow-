import tensorflow as tf
x=tf.constant([[1.0,2.0]])   #一行两列的张量
w=tf.constant([[3.0],[4.0]])  #两行一列的张量
y=tf.matmul(x,w)       #矩阵乘法
print y
with tf.Session() as sess:    #计算
	print sess.run(y)
