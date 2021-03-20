print("Hello Python world!")

name = "Eric"
print("Hello " + name.title() + ", would you like to learn some Python today?")

print(name.lower())
print(name.upper())
print("hello \"world\"")

bicyles = ['trek', 'cannondale', 'redline']
print(bicyles)
print(bicyles[0])
print(bicyles[0].title())
#append
bicyles.append('honda')
print(bicyles)
#insert
bicyles.insert(1, 'yamaha')
print(bicyles)
#del
del bicyles[1]
print(bicyles)
#pop or pop by index - pop(index)
bicyle = bicyles.pop()
print(bicyles)
print(bicyle)
#remove by value, just the first one in the list, not all
bicyles.remove('trek')
print(bicyles)
#sort
bicyles = ['trek', 'cannondale', 'redline']
print("Before sort: " + str(bicyles))
bicyles.sort()
print("After sort: " + str(bicyles))
bicyles.sort(reverse=True)
print("Reverse sort: " + str(bicyles))
#sorted - not change the original list
bicyles = ['trek', 'cannondale', 'redline']
print(sorted(bicyles))
print("original: " + str(bicyles))
#reverse
bicyles = ['trek', 'cannondale', 'redline']
bicyles.reverse()
print("Reversed list: " + str(bicyles))
print("length: " + str(len(bicyles)))


magicians = ['alice', 'david', 'carolina']
for magician in magicians:	# do not forget the colon
	print(magician)  
	print("Stand up")	# note that indented line means in the loop
print("All stand up")	# note the difference with above print

#range()
for value in range(1,5): #include 1,2,3,4, not 5
	print(value)

numbers = list(range(2,11,2))
print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

squares = [value**2 for value in range(1,11)]
print(squares)
print(squares[1:4]) # slicing a list
print(squares[-3:]) # last 3 value

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] #copy list value
print(friend_foods)
my_foods.append('cannoli')
print(friend_foods)


friend_foods = my_foods #copy list address
print(friend_foods)
my_foods.append('ice cream')  #the value in friend_foods is also changed
print(friend_foods)
	

#tuples
dimensions = (200, 50) # the value in tuple can't be changed
#this is not allowed: dimensions[0] = 250
dimensions = (250, 50) #this is allowed

#styling your Code
#1.Indentation - 4 spaces
#2.Line Length - 72 characters per line
#3.Blank Lines - add it in a right way 

#-----------Dictionary--------------------------
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
new_points = alien_0['points']
print(new_points)
#add new pairs to dictionary
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)




# n=int(input("Give me the number of lines :"))
# alphabets="abc"
# for i in range(n+1):
    # for j in range(i):
        # print(alphabets[j%3], end ="")
    # print("")
    
del alien_0['y_position']
print(alien_0)

user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}
#loop dictionary, key, value is self-defined, you can also use k,v
for key, value in user_0.items():
	print("\nKey: " + key)
	print("Value: " + value)

for key in user_0.keys():
	print(key)
for key in user_0:
	print(key)
for key in sorted(user_0.keys()):
	print(key)
for value in user_0.values():
	print(value)

#Nesting
# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)
# Show the first 5 aliens:
for alien in aliens[:5]:
	print(alien)
print("...")
# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))


#input
# !Python 2.7, use raw_input() instead of input()
#message = input("Tell me something, and I will repeat it back to you: ")
#print(message)  
# be aware of that if you enter a number, you should use int(message) to 
# get a number, otherwise it's a string.

#FUNCTION
#
def greet_user():
	"""Display a simple greeting."""
	print("Hello!")
greet_user()

def describe_pet(animal_type, pet_name):
	"""Display information about a pet."""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#Keyword arguments, to avoid wrong order
describe_pet(animal_type='hamster', pet_name='harry')

#Preveting a funtion from modifying a list -- using [:]
def print_models(unprinted_designs, completed_models):
	"""
	Simulate printing each design, until none are left.
	Move each design to completed_models after printing.
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		# Simulate creating a 3D print from the design.
		print("Printing model: " + current_design)
		completed_models.append(current_design)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models)
print(unprinted_designs)
print(completed_models)
print_models(unprinted_designs, completed_models)
print(unprinted_designs)
print(completed_models)

#Passing an arbitrary number of arguments
def make_pizza(*toppings):
	"""Print the list of toppings that have been requested."""
	print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

#Using Arbitrary Keyword Arguments
def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
user_profile = build_profile('albert', 'einstein',
location='princeton',
field='physics')
print(user_profile)

#MODULE
#
#import <module_name>
#	<module_name>.function()
#
#import <module_name> as <alias_name>
#	<alias_name>.function()	
#
#from <module_name> import <function_name>
#	<function_name>()   -- no module name needed
#
#from <module_name> import <function_name> as <alias_name>
#	<alias_name>()   -- no module name needed
#
#from <module_name> import *  -- import all functions, not recommand
#	<function_name>()   -- no module name needed
#

#styling functions
#def function_name(
#		parameter_0, parameter_1, parameter_2,   -- two tabs here
#		parameter_3, parameter_4, parameter_5):  -- two tabs here
#	function body...
