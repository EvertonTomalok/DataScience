# Inicializando as variáveis

import tensorflow as tf


# Valor constante
x = tf.constant(1, name = 'x')


# Variável
y = tf.Variable(x + 9, name = 'y')

# As variáveis precisam ser inicializadas separadamente. 
# Entretanto, o TensorFlow fornece um mecanismo para inicializar todas as variáveis de uma só vez. 
init_op = tf.global_variables_initializer()


# Sessão
with tf.Session() as session:
    session.run(init_op)
    print(session.run(y))
