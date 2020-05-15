def sum(numbers):
	total = 0
	for i in numbers:
		total += i
	return total
numbers = eval(input("Insert numbers here:"))
print(sum(numbers))