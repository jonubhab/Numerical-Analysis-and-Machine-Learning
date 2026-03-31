# Numerical-Analysis

Files to be used: 01_Lagrange Interpolation.py

01_Lagrange Interpolation.py fits curve to data using Lagrange Interpolation method.
It has 3 modes: (Taking m as an object of class Model)
1) m.run(): Inputs parameter, predicts output and gets updated with true data.
2) m.feed(file): Inputs a csv file containing data and updates itself.
3) m.plot(): Shows the current curve fitted to the data points.

Example Usage:
1) sinrad.csv: Data to be fed
2) curve.csv : Available data
