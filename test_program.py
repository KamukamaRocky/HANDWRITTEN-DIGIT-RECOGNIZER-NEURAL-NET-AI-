import mnist_loader
import neural_net_1
training_data,validation_data,test_data=mnist_loader.load_data_wrapper()
net=neural_net_1.Network([784,30,10])
net.SGD(training_data,30,10,3.0,test_data)
