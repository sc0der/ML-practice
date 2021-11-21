import tensorflow as tf
import tensorflow.compat.v1 as tfc

sess = tfc.InteractiveSession()
my_tensor = tfc.random_uniform((4, 4), 0, 1)
my_var = tfc.Variable(initial_value=my_tensor)
print(my_var)
result = tfc.global_variables_initializer()
sess.run(result)
sess.run(my_var)
#