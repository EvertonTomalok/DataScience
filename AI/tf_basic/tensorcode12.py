# Tensores com 3 dimensões

import numpy as np 
import tensorflow as tf


# Cria o tensor tridimensional
tensor_3d = np.array([[[1,2],[3,4]],[[5,6],[7,8]]]) 


# Print
print(tensor_3d)


# Shape
tensor_3d.shape


# Elementos do array
tensor_3d[0,0,0] 
tensor_3d[0,0,1]  
tensor_3d[0,1,0]  
tensor_3d[0,1,1]


# Convertendo o array numpy para tensorflow
tf_tensor = tf.convert_to_tensor(tensor_3d, dtype = tf.float64)


# Sessão
with tf.Session() as sess:
    print (sess.run(tf_tensor))

