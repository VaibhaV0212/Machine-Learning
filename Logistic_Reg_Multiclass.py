import pandas as pd
from sklearn import linear_model
from sklearn.datasets import load_digits

digits = load_digits()
print(dir(digits))