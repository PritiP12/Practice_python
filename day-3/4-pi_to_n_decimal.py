#Given a number n, write a function that returns PI to n decimal places.
from math import pi
def my_pi(n):
  return round(pi, n)
print(my_pi(15))