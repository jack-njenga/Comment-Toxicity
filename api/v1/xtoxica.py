#!/usr/bin/env python3
"""
main
"""
import os
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import TextVectorization # this is for vectorizing the input text


df = pd.read_csv(os.path.join('input_data', 'train.csv'))
X = df['comment_text']

model = tf.keras.models.load_model('toxicity-v5.h5')

MAX_FEATURES = 400000
vectorizer = TextVectorization(max_tokens=MAX_FEATURES,
                               output_sequence_length=1800,
                               output_mode='int')
vectorizer.adapt(X.values)


class Toxicity_model():
    """
    toxicity model
    """

    def __init__(self, *args, **kwargs):
        """
        init
        """
        self.toxicities = ["toxic", "severe_toxic", "obscene", "threat", "insult", "identity_hate"]

    def vectorize_text(self, input_str):
        """
        text vectorizer part
        """
        vstr = vectorizer(input_str)
        return vstr

    def predict(self, vct_str):
        """
        makes the predictions given a vectorized text
        """
        vct_str = np.expand_dims(vct_str, axis=0)
        res = model.predict(vct_str)

        if len(res[0]) != len(self.toxicities):
            print(f"--E--(ERR): Length of prediction is not ok: ({len(res)})length of pred != ({len(self.toxicities)})length of toxicities")
        else:
            pred_dict = {}
            for label, pred in zip(self.toxicities, res[0]):
                pred_value = float(pred)
                pred_dict[label] = round(pred_value, 2)
            return pred_dict
        return False

    def xtoxica(self, input_str):
        """
        XToxica
        """

        vct_text = self.vectorize_text(input_str)
        prediction = self.predict(vct_text)

        if prediction:
            return prediction
        else:
            return False
