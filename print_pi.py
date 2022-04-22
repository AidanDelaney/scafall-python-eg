#!env -- {{.PythonVersion}}
from math import pi

print("%.{{.NumDigits}}f" % pi)
