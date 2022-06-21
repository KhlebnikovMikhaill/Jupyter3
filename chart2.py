import numpy as np
import matplotlib.pyplot as plt

def plot_chart():
	
	# Данные для графика
	mean = 0
	sigma = 1
	x = np.arange(-5,5,0.01)
	f = np.exp(-np.square((x-mean)/sigma)/2)/(np.sqrt(2*np.pi)*sigma)
	
	fig, ax = plt.subplots()
	ax.plot(x, f)
	
	ax.set(xlabel='x', ylabel='y', title='Нормальное распределение')
	ax.grid()
	
	plt.show()

def plot_chart2():
	
	# Данные для графика
	mean = 0
	sigma = 1
	mean2 = 1
	sigma2 = 2
	mean3 = -1
	sigma3 = 0.3	
	
	x = np.arange(-7,7,.01)
	
	f = np.exp(-np.square((x-mean)/sigma)/2)/(np.sqrt(2*np.pi)*sigma)
	f2 = np.exp(-np.square((x-mean2)/sigma2)/2)/(np.sqrt(2*np.pi)*sigma2)
	f3 = np.exp(-np.square((x-mean3)/sigma3)/2)/(np.sqrt(2*np.pi)*sigma3)
	
	fig, ax = plt.subplots()
	ax.plot(x, f)
	ax.plot(x, f2)
	ax.plot(x, f3)
	
	ax.set(xlabel='x', ylabel='y', title='Нормальное распределение')
	ax.grid()
	
	plt.show()
	
	
