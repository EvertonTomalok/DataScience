# Random Numbers

import tensorflow as tf
import matplotlib.pyplot as plt

# Cria um tensor de shape [100] constituído por valores normais aleatórios, com média 0 e desvio padrão 2.
norm = tf.random_normal([100], mean = 0, stddev = 2)
with tf.Session() as session:
    plt.hist(norm.eval(), normed = True)
    plt.show()  


uniform = tf.random_uniform([100], minval = 0, maxval = 1, dtype = tf.float32)
with tf.Session() as session:
    print (uniform.eval())
    plt.hist(uniform.eval(), normed = True)
    plt.show() 


uniform_with_seed = tf.random_uniform([1], seed = 1)
uniform_without_seed = tf.random_uniform([1])

# Repetidamente executando este bloco com o mesmo grafo irá gerar a mesma
# sequência de valores para 'a', mas diferentes sequências de valores para 'b'.
print("First Run")
with tf.Session() as first_session:
  print("uniform with (seed = 1) = {}"\
        .format(first_session.run(uniform_with_seed)))  
  print("uniform with (seed = 1) = {}"\
        .format(first_session.run(uniform_with_seed)))
  print("uniform without seed = {}"\
        .format(first_session.run(uniform_without_seed)))  
  print("uniform without seed = {}"\
        .format(first_session.run(uniform_without_seed)))  

print("Second Run")
with tf.Session() as second_session:
  print("uniform with (seed = 1) = {}"\
        .format(second_session.run(uniform_with_seed)))  
  print("uniform with (seed = 1) = {}"\
        .format(second_session.run(uniform_with_seed)))  
  print("uniform without seed = {}"\
        .format(second_session.run(uniform_without_seed)))  
  print("uniform without seed = {}"\
        .format(second_session.run(uniform_without_seed)))


