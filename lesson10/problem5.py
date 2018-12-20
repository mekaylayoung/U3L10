print('-'*65)
print('Booze Bot')
print()
print("I'm a vending machine that dispenses different kinds of alcohol. Please answer the following question:")
print()

age = input('How old are you? ')

age = int(age)

if age >= 21: 
	order = input('What would you like to order? ')
	print( 'Please pay by inserting your card. Pick up your ' + order + ' from the slot below.')

else: 
	years = 21 - age
	years = str(years)
	print("I think you're a bit too young to have alcohol. Come back in " + years + " years to order.")
print('-'*65)