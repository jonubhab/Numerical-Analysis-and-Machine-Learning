# Numerical-Analysis

Files to be used: 

1) 01_Lagrange Interpolation.py fits curve to data using Lagrange Interpolation method.
   It has 3 modes: (Taking m as an object of class Model)
   1) m.run(): Inputs parameter, predicts output and gets updated with true data.
   2) m.feed(file): Inputs a csv file containing data and updates itself.
   3) m.plot(): Shows the current curve fitted to the data points.

2) 02_Roots.py contains the solve(f,a,b) method which returns a set containing roots of f(x)=0 for a<=x<=b.

Example Usage for 01_Lagrange Interpolation.py:
1) sinrad.csv: Data to be fed
2) curve.csv : Available data
