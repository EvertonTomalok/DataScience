# Usando o TensorBoard
import tensorflow as tf


# Definindo os tensores
a = tf.constant(10, name = "a")
b = tf.constant(90, name = "b")
y = tf.Variable(a + b * 2, name = 'y')


# Inicializando a variável
model = tf.initialize_all_variables()


# Sessão
with tf.Session() as session:
    merged = tf.summary.merge_all()
    writer = tf.summary.FileWriter("/tmp/my_graph", session.graph)
    session.run(model)
    print(session.run(y))



# Para inicializar o TensorBoard: tensorboard --logdir=/tmp/my_graph

