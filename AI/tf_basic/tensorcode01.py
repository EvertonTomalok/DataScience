# Hello World Tensorflow

import tensorflow as tf

# Cria o objeto TensorFlow chamado hello
# Constantes são objetos cujo valor não pode ser alterado.
hello = tf.constant('Hello World!')

with tf.Session() as sess:
    # Executa a operação tf.constant na sessão
    output = sess.run(hello)
    print(output)