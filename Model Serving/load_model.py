# import libraries
import tensorflow as tf
import string
import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')


@tf.keras.utils.register_keras_serializable()
def custom_standardization(input_data):
    '''
    Function to perform string standardization.

    Parameters:
        text (string): Raw string.

    Return:
        text (string): Standardized string, i.e., lowercased, punctuation removed, and stopwords removed.
    '''
    lowercase = tf.strings.lower(input_data)
    remove_punctuation = tf.strings.regex_replace(lowercase, '[%s]' % re.escape(string.punctuation), '')
    remove_stopwords = tf.strings.regex_replace(remove_punctuation, r'\b(' + r'|'.join(stopwords.words('english')) + r')\b\s*', '')
    return remove_stopwords


def load():
    '''
    Function to load saved model and label list for prediction.

    Parameters:
        NONE

    Return:
        model (tf model): Tensorflow model.
        label_list (list): List of output labels.
    '''
    # load saved tf model
    path = 'Models/model2_intencoding' # path to saved model
    model = tf.keras.models.load_model(path)

    # label list as per label encoding
    label_list = ['AddToPlaylist', 'BookRestaurant', 'GetWeather', 'PlayMusic', 'RateBook', 
            'SearchCreativeWork', 'SearchScreeningEvent']
    
    return model, label_list

