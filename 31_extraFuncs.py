#split
sent="hello i am under the water, here too much raining"
word1=sent.split()[3]#3rd word
word2=sent.split()[-2]#2nd from the last 

print(sent)
print(word1)
print(word2)

#formatting
fname="anakin"
lname="skywalker"
print(f'{fname} is the not the first {lname}') 
fullSent=f'''
    By using triple quotes we can write in many lines
    fname:{fname}
    lname:{lname}
'''
print(fullSent)

#replace
sen="hello there general kenobi"
new_sen=sen.replace('e','a')
print(new_sen)

#in and not in
if 'hello' in sen: #or not in
    print('hello is in sen')

#with statement
'''
with statement in Python is used in exception handling to make the code cleaner and much more readable.
# file handling
  
#without using with statement:
    file = open('file_path', 'w')
    file.write('hello world !')
    file.close()
  
#using with statement:
    with open('file_path', 'w') as file:
        file.write('hello world !')
'''
with open('./files/sw.txt','r') as file:
    content=file.read()
    print(content)

#Enemurator, get both index no and value
wordd='hello there'
for index,char in enumerate(wordd):
    print(f'{char} is at index {index}')