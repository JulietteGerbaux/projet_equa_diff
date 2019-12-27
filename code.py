import numpy as np
import matplotlib.pyplot as plt

def solve_euler_explicit(f, x0, dt, n = 100):
  t = np.linspace(0, dt*(n-1), n)
  x = np.zeros(n)
  x[0] = x0
  for j in range(1, n):
    x[j] = x[j-1] + dt*f(x[j-1])
  return t, x

def show_solver(solver, f, x0, dt, n =100):
  t, x = solver(f, x0, dt, n)
  plt.close()
  plt.plot(t, x)
  plt.show()

def exp_solver(solver, dt, xf = 5, x0 = 1):
  t, x = solver(lambda x : x, x0, dt, int(xf//dt))
  plt.close()
  plt.plot(t, x)
  plt.plot(t, [np.exp(i) for i in t])
  plt.show()



