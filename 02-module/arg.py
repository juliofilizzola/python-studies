def some(x, y):
	return x + y


print(some(1, 2))


def some_func(x):
	return x * 2


print(some_func(x=334))


def some_func2(x, y=None):
	if y is None:
		return x * 3
	else:
		return x + y * 8
	

print(some_func2(x=3))
print(some_func2(x=6, y=4))
