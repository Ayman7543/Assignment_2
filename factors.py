def main():
	#welcome message 
	print('Hello,this program generates all the factors of a positive integer  ')
	print()
	num = get_int()
	print()
	print(f'the factors of the number {num} are {fctrs(num)}')
	

def fctrs(num):
	i=1
	#initializing an empty list of factors of the number
	fctrs = []
	while True:
	# avoide duplicating the values
		if i > num / i:
			break
	# finding the numbers that the chosen number is divisable by and adding them to the list
		if num % i ==0:
			fctrs.append(i) 
			fctrs.append(int(num/i))
		i += 1 
	#sorting the list
	return sorted(fctrs)		 


def get_int():
	num = input("Please enter a positive integer: ")
	try:
		num = int(num)
	except:
		print('Not a valid number ')
		return get_int()

	return num

main()		