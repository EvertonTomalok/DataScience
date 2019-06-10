# Variáveis no Tensorflow

# Python code puro
x = 1
y = x + 9
print('Soma em Python:')
print(y)

# O mesmo código anterior com Tensorflow
import tensorflow as tf


# Valor constante
x = tf.constant(1, name = 'x')


# Variáveis no TensorFlow são como variáveis em qualquer outra linguagem
# As variáveis (como você pode adivinhar pelo nome) podem conter valores diferentes ao contrário das constantes. 
y = tf.Variable(x + 9, name = 'y')
print(y)

