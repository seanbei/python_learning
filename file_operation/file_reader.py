with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

#write: original data will be erased
with open('pi_digits.txt', 'w') as file_object:
    file_object.write('I try to write')
    
#Append: original data will be kept, write new after them  
with open('pi_digits.txt', 'a') as file_object:
    file_object.write('I try to append')    
