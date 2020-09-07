import os
import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import clear_output
from six.moves import urllib

import tensorflow.compat.v2.feature_column as fc

import tensorflow as tf

# Load dataset.
dftrain = pd.read_csv('datasets_13996_18858_WA_Fn-UseC_-Telco-Customer-Churn.csv')
# dfeval = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/eval.csv')
# y_train = dftrain.pop('survived')
# y_eval = dfeval.pop('survived')

print(dftrain.head())

print(dftrain.tenure.value_counts())


# CATEGORICAL_COLUMNS = ['sex', 'n_siblings_spouses', 'parch', 'class', 'deck',
#                        'embark_town', 'alone']
# NUMERIC_COLUMNS = ['age', 'fare']
#
# feature_columns = []
# for feature_name in CATEGORICAL_COLUMNS:
#   vocabulary = dftrain[feature_name].unique()
#   feature_columns.append(tf.feature_column.categorical_column_with_vocabulary_list(feature_name, vocabulary))
#
# for feature_name in NUMERIC_COLUMNS:
#   feature_columns.append(tf.feature_column.numeric_column(feature_name, dtype=tf.float32))
