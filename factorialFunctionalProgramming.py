def factorial(num):
	return reduce(lambda i, j : i*j, range(1,num+1))

if __name__ == '__main__':
	print factorial(5)
