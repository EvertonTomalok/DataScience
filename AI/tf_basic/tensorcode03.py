# Sessão

# A api do TensorFlow é construída em torno da ideia de um grafo computacional, uma forma de visualizar um processo matemático. 

# Uma "TensorFlow Session" é um ambiente para executar um grafo. A sessão é responsável por alocar as operações para GPU (s) e / ou CPU (s), 
# incluindo máquinas remotas. 


import tensorflow as tf


# Cria o objeto TensorFlow chamado hello
hello = tf.constant('Hello World!')


# Sessão
# O código já criou o tensor, hello, das linhas anteriores. O próximo passo é avaliar o tensor em uma sessão.
# O código cria uma instância de sessão, sess, usando tf.Session(). A função sess.run() então avalia o tensor e retorna os resultados.

with tf.Session() as sess:
    # Executa a operação tf.constant na sessão
    output = sess.run(hello)
    print(output)

