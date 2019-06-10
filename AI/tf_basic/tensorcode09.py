# Imprimindo os grafos

import tensorflow as tf


# Constante a
a = tf.constant(1.0)
print(a)


# Sessão para a constante a
with tf.Session() as sess:
    print(sess.run(a))


# Variável b
b = tf.Variable(2.0, name = "test_var")


# Inicializa a variável
init_op = tf.global_variables_initializer()


# Sessão para a variável b
with tf.Session() as sess:
    sess.run(init_op)
    print(sess.run(b))


# Imprime os grafos gerados
graph = tf.get_default_graph()
for op in graph.get_operations(): 
    print(op.name)


# Como você pode ver, nós declaramos 'a' como constante então isso foi adicionado ao grafo. Da mesma forma, 
# para a variável b, muitos estados "test_var" foram adicionados ao grafo TensorFlow como test_var/initial_value, test_var/read, etc. 
# Você pode visualizar a rede completa usando TensorBoard, que é uma ferramenta para visualizar um gráfico TensorFlow e um processo de treinamento.


