# Tensor

import tensorflow as tf


# Cria o objeto TensorFlow chamado hello
hello = tf.constant('Hello World!')


with tf.Session() as sess:
    # Executa a operação tf.constant na sessão
    output = sess.run(hello)
    print(output)


# Tensor
# O TensorFlow armazena dados em Tensores que são semelhantes a arrays multidimensionais do numPy 
# Em TensorFlow, os dados não são armazenados como inteiros, floats ou strings de caracteres. 
# Esses valores são encapsulados em um objeto chamado de tensor. No caso de hello = tf.constant('Hello World!'), 
# hello é um tensor de string 0-dimensional, mas tensores podem assumir uma variedade de tamanhos como mostrado abaixo:

# A é um tensor 0-dimensional int32 
A = tf.constant(1234) 
print(A)


# B é um tensor 1-dimensional int32 
B = tf.constant([123,456,789]) 
print(B)


# C é um tensor 2-dimensional int32
C = tf.constant([ [123,456,789], [222,333,444] ])    
print(C)


# tf.constant () é uma das muitas operações TensorFlow disponíveis. 
# O tensor retornado por tf.constant() é chamado de tensor constante, porque o valor do tensor nunca muda.