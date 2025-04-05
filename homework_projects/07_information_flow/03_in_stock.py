# Sophia has a fruit store. She has written a function num_in_stock 
# which takes a string fruit as a parameter and returns how many of that fruit are in her inventory.
def main():
	fruit : str = input("\n\033[1;3mEnter a fruit: \033[0m")
	stock = num_in_stock(fruit)
	if stock == 0:
		print("\nThis fruit is not in stock.")
	else:
		print("\nThis fruit is in stock! Here is how many:")
		print(stock)

# There is no need to edit code beyond this point

def num_in_stock(fruit):
	"""
	This function returns the number of fruit Sophia has in stock.
	"""
	if fruit == 'apple':
		return 2
	if fruit == 'mango':
		return 4
	if fruit == 'pear':
		return 1000
	else:
		# this fruit is not in stock.
		return 0


if __name__ == '__main__':
    main()