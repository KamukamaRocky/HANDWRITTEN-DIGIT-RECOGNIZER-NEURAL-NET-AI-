How It Works:
Under the Hood  The model follows a classic Feedforward Neural Network architecture, 
specifically a Multi-Layer Perceptron (MLP). 
Here is the step-by-step logic of the training process implemented in neural_net_1.py:
1. Data Input & Flattening
 Each 28x28 pixel image from the MNIST dataset is "unrolled" into a 1D vector of 784 values. Each value represents the grayscale intensity of a pixel (0 for white, 1 for black). These serve as the activations for our Input Layer.
2. Forward Propagation
The data flows from the input layer through a Hidden Layer of 30 neurons.Each neuron calculates a weighted sum of its inputs, adds a bias, and passes the result through a Sigmoid activation function. This process repeats for the Output Layer, where 10 neurons represent the probability of the image being a specific digit (0–9).
3. Stochastic Gradient Descent (SGD)
Instead of calculating the gradient for the entire dataset at once (which is computationally expensive), this model uses Mini-batch SGD.The training data is shuffled and split into small "batches" of 10 images.The model calculates the error for that specific batch and updates the weights and biases immediately. This allows for faster convergence and helps the model avoid getting stuck in local minima.
4. Backpropagation & Learning
For every training example, the model uses the Backpropagation algorithm to compute the gradient of the cost function.It calculates how much each weight and bias contributed to the error in the prediction.Using a Learning Rate  of 3.0, the model adjusts these weights in the opposite direction of the gradient to "step" toward a more accurate prediction.
5. Evaluation
After each epoch (one full pass through the training data), the model is tested against the test_data. This provides a real-time accuracy percentage, showing how well the network is generalizing to images it has never seen before.
