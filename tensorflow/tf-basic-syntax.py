import tensorflow as tf
import tensorflow.compat.v1 as tfc

hello = tfc.constant("Hello")
world = tfc.constant("World")
print(hello)
sess = tfc.InteractiveSession()
my_tensor = tfc.random_uniform((4, 4), 0, 1)
my_var = tfc.Variable(initial_value=my_tensor)
result = tfc.global_variables_initializer()
print(sess.run(result))