import csv 
import numpy as np
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("sensors.csv")
# a = np.genfromtxt("sensors.csv", usecols=(2,3), skip_header=1, dtype=None, encoding=None)


x = df['x']
y = df['y']

print(x,y)