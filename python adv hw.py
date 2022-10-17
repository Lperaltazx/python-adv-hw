#In-Class Exercise #3
#Print each persons name and twitter handle, using groups, should look like:

#==============
#Full Name / Twitter
#==============
#Derek Hawkins / @derekhawkins
#Erik Sven-Osterberg / @sverik

#Ryan Butz / @ryanbutz

#Example Exampleson / @example

#Ripal Pael / @ripalp

#Darth Vader / @darthvader

file = open("names.txt")
data = file.read()

print(data)

file.close()


with open("names.txt") as file:
    data = file.read()
    print(data) 

answer = input("What would you like to search for? ")
found = re.findall(answer, data)
if found:
    print(f'I found your data: {found}')
else:
    print('no data found')

includes_handle = re.findall('.*\W\@[a-z]*', data)
name = '[A-Z][a-z]*\,\s[A-Z][a-z]*[-]*[A-Z]*[a-z]*'
handle = '\W\@[a-z]*'
# type(includes_handle)
# print(includes_handle)

print("====================\nFull Name / Twitter\n====================")

for item in includes_handle:
    this_name = re.findall(name,item)
    x = this_name[0].split(', ')
    x.reverse()
    new_name = ' '.join(x)
    
    this_handle = re.findall(handle, item)
    new_handle = re.findall('\@[a-z]*',str(this_handle))
    
    print(new_name + ' / ' + new_handle[0])


    #Regex project
#Use python to read the file regex_test.txt and print the last name on each line using regular expressions and groups (return None for names with no first and last name, or names that aren't properly capitalized)

import re

with open("regex-test.txt") as file:
    data = file.read()
    
for item in data.split('\n'):
    if re.match('[A-Z][a-z]*\s*[A-Z]*[a-z]*\s[A-Z][a-z]*', item):
        print(' '.join(re.findall('[A-Z][a-z]*', item)))
    else:
        print('None')