from keras.models import load_model


def visualization(model_path):
    '''

    :param model_path: The path where the model is saved
    :return: a summary of model structure using the keras built-in fuction
    '''
    model = load_model(model_path)
    model.summary()


if __name__ == '__main__':
    model_path = "test_model_files/cifar10_model.h5"
    visualization(model_path)
