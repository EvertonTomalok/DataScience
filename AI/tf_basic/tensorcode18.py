# Regressão Linear com TensorFlow

import tensorflow as tf
import numpy as np


# Gerando conjunto de dados
trainX = np.linspace(-1, 1, 101)
trainY = 3 * trainX + np.random.randn(*trainX.shape) * 0.33


# Placeholders
X = tf.placeholder("float")
Y = tf.placeholder("float")


# O modelo de regressão linear é y_model = w * x e temos de calcular o valor de w através do nosso modelo. 
# Vamos inicializar w com 0 e criar um modelo para resolver este problema. 
# Definimos o custo como o quadrado de (Y-y_model). TensorFlow possui muitos otimizadores que calculam e atualizam os gradientes após cada iteração 
# enquanto tentam minimizar o custo especificado. Vamos definir a operação de treinamento como a mudança dos valores 
# usando GradientDescentOptimizer para minimizar o custo com uma taxa de aprendizado de 0,01. Mais tarde, vamos executar esta operação de treinamento em um loop.

# Define a variável w
w = tf.Variable(0.0, name = "weights")
init = tf.initialize_all_variables()


# Até este ponto, apenas definimos o grafo. Nenhum cálculo aconteceu.
# Nenhuma das variáveis TensorFlow tem qualquer valor. 
# Para executar este grafo, precisamos criar uma sessão e executá-la. Antes disso, precisamos criar o init para inicializar todas as variáveis:

# Inicializa a variável
init = tf.global_variables_initializer()

# Multiplic ao conjunto de dados X pelos pesos w
y_model = tf.multiply(X, w)

# Calcula função de custo
cost = (tf.pow(Y-y_model, 2))

# Treinamento do modelo com Gradient Descent para otimizar a função de custo
train_op = tf.train.GradientDescentOptimizer(0.01).minimize(cost)

# Sessão
with tf.Session() as sess:
    sess.run(init)
    for i in range(100):
        for (x, y) in zip(trainX, trainY):
            sess.run(train_op, feed_dict = {X: x, Y: y})
    print(sess.run(w))


# Tensorboard

# Sessão
with tf.Session() as session:
    merged = tf.summary.merge_all()
    writer = tf.summary.FileWriter("/tmp/my_graph", session.graph)
    session.run(init)
    print(session.run(w))


# Para inicializar o TensorBoard: tensorboard --logdir=/tmp/my_graph








    



