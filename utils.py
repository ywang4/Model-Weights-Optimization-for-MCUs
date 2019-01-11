from keras.models import load_model


def print_model_structure(model):
    '''

    :param model: a keras model
    :return: a summary of model structure using the keras built-in fuction
    '''
    model.summary()

def load_model_weights(model):
    # Create two variables to store the layer information and weight matrixes.
    layers_name = []
    weights = []
    
    # Loop through the model layer by layer
    for layer in model.layers:
        # extract the layer information by using layer.get_config()
        layers_name.append(layer.get_config())
        
        # extract the weight matrix for this layer using layer.get_weights()
        weights.append(layer.get_weights())
    return weights, layers_name

def save_model_weights(model, new_weights):
    # Loop through the list containing each layer's new weight
    for i in range(len(new_weights)):
        # set the weight for each layer using set_weight()
        model.layers[i].set_weights(new_weights[i])
    return model

if __name__ == '__main__':
    model_path = "test_model_files/cifar10_model.h5"
    model = load_model(model_path)
    # print_model_structure(model)
    print_model_weights(model)
