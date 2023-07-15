import numpy as np

from Network import Network
from FCLayer import FCLayer
from ActivationLayer import ActivationLayer
from activations import tanh, tanh_prime
# from activations import poly, poly_prime

from losses import mse, mse_prime

x_train = np.array([[[0,0]],[[0,1]],[[1,0]],[[1,1]]])
y_train = np.array([[[0]],[[1]],[[1]],[[0]]])

net = Network()
net.add(FCLayer(2,3))
net.add(ActivationLayer(tanh, tanh_prime))
# net.add(ActivationLayer(poly, poly_prime))
net.add(FCLayer(3,1))
net.add(ActivationLayer(tanh, tanh_prime))
# net.add(ActivationLayer(poly, poly_prime))


net.use(mse, mse_prime)
net.fit(x_train, y_train, epochs=1000, learning_rate=0.1)

out = net.predict(x_train)
print(out)