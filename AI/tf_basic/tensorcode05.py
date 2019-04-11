# TensorFlow Programming Model - Feed_dict

import tensorflow as tf

# Use o parâmetro feed_dict em tf.session.run() para definir o valor para o tensor placeholder. 
# Abaixo temos o tensor x sendo definido para a sequência de caracteres "Hello, world". 
x = tf.placeholder(tf.string)


# Sessão
with tf.Session() as sess:
    output1 = sess.run(x, feed_dict = {x: 'Hello World'})
    print(output1)


# Também é possível definir mais de um tensor usando feed_dict.
x = tf.placeholder(tf.string)
y = tf.placeholder(tf.int32)
z = tf.placeholder(tf.float32)

with tf.Session() as sess:
    output2 = sess.run(x, feed_dict = {x:'Teste String', y:123, z:45.67})
    print(output2)


# Nota: Se os dados passados para o feed_dict não coincidem com o tipo tensor e não podem ser convertidos para o tipo tensor, 
# você obterá o erro "ValueError: invalid literal for...".