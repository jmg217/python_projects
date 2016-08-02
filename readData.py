#!/usr/bin/env python                                                                                                

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
 
film_data = pd.read_csv('films.txt', sep="\t", header = None, encoding="utf-8")
book_data = pd.read_csv('books.txt', sep="\t", header = None, encoding="utf-8")
#book_data.head(10)
book_data.columns=['title','rating']
film_data.columns=['title','rating']
#print(film_data.head(10))

df = pd.merge(film_data, book_data, on=['title'])
filmX=df['rating.x'].values
bookY=(df['rating.y'].values)*2

filmX=filmX.reshape(-1, 1)
bookY=bookY.reshape(-1, 1)

regr = linear_model.LinearRegression()

regr.fit(filmX, bookY)
print('Coefficients: \n', regr.coef_)
# The mean square error
print("Residual sum of squares: %.2f"
      % np.mean((regr.predict(diabetes_X_test) - diabetes_y_test) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(diabetes_X_test, diabetes_y_test))
#print(df.head(500))
