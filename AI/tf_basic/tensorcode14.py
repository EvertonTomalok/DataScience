# Convertendo imagens

# Preparando os dados
import matplotlib.image as mp_image
filename = "image.jpg"
input_image = mp_image.imread(filename)


# Dimensão
print ('input dim = {}'.format(input_image.ndim))


# Shape
print ('input shape = {}'.format(input_image.shape))


# Visualizando a imagem original
import matplotlib.pyplot as plt
plt.imshow(input_image)
plt.show()


# Convertendo com TensorFlow
import tensorflow as tf


# Slice
my_image = tf.placeholder("uint8",[None,None,3])
slice = tf.slice(my_image,[10,0,0],[16,-1,-1])


# Sessão
with tf.Session() as session:
    result = session.run(slice, feed_dict = {my_image: input_image})
    print(result.shape)

plt.imshow(result)
plt.show()

