import numpy as np
import sys
import tflearn
import tensorflow as tf

# node1 = tf.constant(3.0, dtype=tf.float32)
# node2 = tf.constant(4.0) # also tf.float32 implicitly
# print(node1, node2)
#
# # https://blog.knoldus.com/2017/11/30/getting-started-with-tensorflow-writing-your-first-program/#more-47415
# constantValue1 = tf.constant(9.0, dtype=tf.float32)
# constantValue2 = tf.constant(19.0)
#
# print("constantValue1 = %s" % constantValue1)
# print("constantValue2 = %s" % constantValue2)
#
# sess = tf.Session()
# print(sess.run(constantValue1))
# print(sess.run(constantValue2))
#
# addConstants = constantValue1 + constantValue2
# print("addConstants = ", addConstants)
# sumOfConstants = sess.run(addConstants)
# print("sum = ", sumOfConstants)
#
# myValue1 = tf.placeholder(dtype=tf.float32)
# myValue2 = tf.placeholder(dtype=tf.float32)
# sumOfMyValuesNode = myValue1 + myValue2
# sumOfMyValues = sess.run(sumOfMyValuesNode, {myValue1: 5.0, myValue2: 6.0})
# print("Sum of myValues = ", sumOfMyValues)
#
# myVariable = tf.Variable(2.0, dtype=tf.float32)
# init = tf.global_variables_initializer()
# sess.run(init)
# print("myVariable = ", sess.run(myVariable))
# sess.run(tf.assign(myVariable, 10.0))
# print(sess.run(myVariable))
#
# W = tf.Variable(1, dtype=tf.float32)
# x = tf.placeholder(tf.float32)
# y = tf.placeholder(tf.float32)
#
# myModel = W * x
#
# delta = myModel - y
# squaredDelta = tf.square(delta)
# loss = tf.reduce_sum(squaredDelta)



# Adding one to W
# ~~~
def addOne():
    sess.run(tf.assign(W, sess.run(W) + 1.0))


# ASubtracting one from W
# ~~~
def subtractOne():
    sess.run(tf.assign(W, sess.run(W) - 1.0))


# Defining model parameters
# ~~~
W = tf.Variable(1, dtype=tf.float32)
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

# Defining model and loss function
# ~~~
myModel = W * x
delta = myModel - y
squaredDelta = tf.square(delta)
loss = tf.reduce_sum(squaredDelta)

# Initializing oldLoss to maximum float value
# ~~~
oldLoss = sys.float_info.max

# Initializing global variables
# ~~~
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

# Initializing flags to remember what operation was last executed
# ~~~
adding = 0
subtracting = 0

# Loop to determine the value of W / Model training
# ~~~
while oldLoss > 0:
    currentLoss = sess.run(loss, {x: [1, 2, 3, 4], y: [10, 20, 30, 40]})
    if currentLoss == 0:
        break
    elif adding == 0 and subtracting == 0:
        addOne()
        adding = 1
    elif adding == 1 and currentLoss <= oldLoss:
        addOne()
        adding = 1
        subtracting = 0
    elif adding == 1 and currentLoss >= oldLoss:
        subtractOne()
        adding = 0
        subtracting = 1
    elif subtracting == 1 and currentLoss <= oldLoss:
        subtractOne()
        subtracting = 1
        adding = 0
    elif subtracting == 1 and currentLoss >= oldLoss:
        addOne()
        subtracting = 0
        adding = 1
    oldLoss = currentLoss

# Printing the value of W
# ~~~
print("After training the value of W is -", sess.run(W))

# Printing the output for some inputs to see if the model is giving correct output
# ~~~
print("--------------------------------------------------")
print("Should return 10 times of 27 -", sess.run(myModel, {x: 27.0}))
print("Should return 10 times of 10 -", sess.run(myModel, {x: 10.0}))
print("Should return 10 times of 80 -", sess.run(myModel, {x: 80.0}))

# https://github.com/akshanshjain95/TensorFlow-Sample-Program/blob/master/TensorFlow-Sample-Program/Sample-Program.py






