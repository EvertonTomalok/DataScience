# TensorFlow Programming Model - Placeholder

# Já criamos um tensor em uma sessão e retornamos o resultado. 
# E se você quiser usar um não-constante? 
# Usamos o tf.placeholder () e feed_dict para isso. 
# Vejamos como ocorre a alimentação de dados no TensorFlow.


# tf.placeholder()

# Infelizmente, você não pode simplesmente definir x para o seu conjunto de dados e colocá-lo no TensorFlow, 
# porque com o tempo você vai querer que o seu modelo TensorFlow receba diferentes conjuntos de dados com parâmetros diferentes. 
# Você precisa do tf.placeholder()

# tf.placeholder() retorna um tensor que obtém seu valor a partir de dados passados para a função tf.session.run(), 
# permitindo que você defina a entrada antes da execução da sessão.

import tensorflow as tf

a = tf.placeholder("int32")
b = tf.placeholder("int32")


# A função multiply() retorna o resultado da multiplicação
y = tf.multiply(a, b)

# Sessão
sess = tf.Session()
print (sess.run(y, feed_dict = {a:3, b:4}))


# a e b são tensores que estão esperando para serem inicializados / alimentados. 
# Os placeholders são usados para dados de treinamento que só são alimentados quando o código é realmente executado dentro de uma sessão. 
# O que é alimentado no placeholder é chamado feed_dict. Feed_dict são pares de valores-chave para a retenção de dados.