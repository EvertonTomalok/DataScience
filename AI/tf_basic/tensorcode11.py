# Definindo Tensors

# Tensores são as estruturas de dados básicas no TensorFlow. Como já dissemos, eles representam as arestas de conexão em um Gráfico de Fluxo de Dados. 
# Um tensor simplesmente identifica uma matriz ou lista multidimensional.

# Pode ser identificado por três parâmetros, rank, shape e type: 
# rank: Cada tensor é descrito por uma unidade de dimensionalidade chamada rank. Identifica o número de dimensões do tensor. Por esta razão, uma classificação é conhecida como ordem ou n-dimensões de um tensor (por exemplo, um tensor de grau 2 é uma matriz e um tensor de grau 1 é um vetor). 
# Shape: A forma de um tensor é o número de linhas e colunas que ele tem. 
# Type: É o tipo de dados atribuído aos elementos do tensor.



# Criando um array Numpy
import numpy as np


# Criando array numpy unidimensional
tensor_1d = np.array([1.3,1,4.0,23.99])


# Print
print (tensor_1d)
print (tensor_1d[0])
print (tensor_1d[2])


# Criando tensores com TensorFlow
import tensorflow as tf


# Convertendo o array numpy para tensorflow
tf_tensor = tf.convert_to_tensor(tensor_1d, dtype = tf.float64)


# Sessão
with tf.Session() as sess:
    print (sess.run(tf_tensor))
    print (sess.run(tf_tensor[0]))
    print (sess.run(tf_tensor[2]))


# Criando array numpy bidimensional
tensor_2d = np.array([(1,2,3,4),(4,5,6,7),(8,9,10,11),(12,13,14,15)])


# Print
print (tensor_2d)
print (tensor_2d[3][3])
print (tensor_2d[0:2,0:2])


# Convertendo o array numpy para tensorflow
tf_tensor = tf.convert_to_tensor(tensor_2d, dtype = tf.float64)


# Sessão
with tf.Session() as sess:
    print (sess.run(tf_tensor))




