# Usando o Método de Montecarlo

# O Método de Montecarlo é um método probabilístico numérico amplamente utilizado na aplicação de computação científica de alto desempenho.

import tensorflow as tf
import matplotlib.pyplot as plt

trials = 100
hits = 0
x = tf.random_uniform([1], minval = -1, maxval = 1, dtype = tf.float32)
y = tf.random_uniform([1], minval = -1, maxval = 1, dtype = tf.float32)
pi = []

# Dentro da sessão, calculamos o valor de π (pi)
# A relação entre os números dentro do círculo e o total de pontos gerados deve convergir (muito lentamente) para π, e 
# Contamos quantos pontos caem dentro da equação do círculo x2 + y2 = 1.
sess = tf.Session()
with sess.as_default():
    for i in range(1,trials):
        for j in range(1,trials):
            if x.eval()**2 + y.eval()**2 < 1 :
                hits = hits + 1
                pi.append((4 * float(hits) / i)/trials)  

plt.plot(pi)
plt.show()
