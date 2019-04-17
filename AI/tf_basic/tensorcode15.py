# Trabalhando com Tensores usando a função transpose()

# Preparando os dados
import matplotlib.image as mp_image
filename = "image.jpg"
input_image = mp_image.imread(filename)


# Dimensão
print ('input dim = {}'.format(input_image.ndim))

# Shape
print ('input shape = {}'.format(input_image.shape))

# Coleta as dimensões
height, width, depth = input_image.shape

# Imprime a imagem
import matplotlib.pyplot as plt
plt.imshow(input_image)
plt.show()


import tensorflow as tf

x = tf.Variable(input_image, name = 'x')
model = tf.initialize_all_variables()

with tf.Session() as session:
    x = tf.transpose(x, perm = [1,0,2])
    session.run(model)
    result=session.run(x)

plt.imshow(result)
plt.show()




