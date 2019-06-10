# Operações Matemáticas com TensorFlow
# https://www.tensorflow.org/api_guides/python/math_ops

# Já sabemos como obter os dados para o TensorFlow, usando os placeholders.
# Mas agora você precisa usar esses dados. Você vai usar operações matemáticas básicas - adição, subtração, multiplicação e divisão - com tensores. 

import tensorflow as tf


x = tf.add(3, 4) 
x = tf.subtract(8, 7) 
y = tf.multiply(3, 6)  


# Pode ser necessário converter os tipos para que certos operadores trabalhem em conjunto

# Falha com ValueError: ensor conversion requested dtype float32 for Tensor with dty
# Isso ocorre porque a constante 1 é um número inteiro, mas a constante 2.0 é um valor de ponto flutuante e tf.subtract() espera que eles correspondam.
#tf.subtract(tf.constant(2.0), tf.constant(1))  


# Agora sim
tf.subtract(tf.cast(tf.constant(2.0), tf.int32), tf.constant(1))   


x = tf.constant(10)
y = tf.constant(2)
z = tf.subtract(tf.div(x,y),tf.constant(1))


with tf.Session() as sess:
    output = sess.run(z)
    print(output)
