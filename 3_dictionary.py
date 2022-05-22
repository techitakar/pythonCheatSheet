#Dictionaries, They are like javascript object literals
'''
Dictionary:
- Key:value pair
- Key should be unique
- 
'''

dict1={1:"Anakin",2:"Padme",3:"Obi Wan",4:"Luke"}
dict2={"name":"Mando","age":35,"isCool":True,"series":"The mandalorian"}
print(dict1)
print(dict2)
print(dict2["series"])
dict1.clear()
print(dict1)
print("age is ",dict2.get("age"))

gameKeys=['Bethesda','Activision','EA','Ubisoft','From Software']
gameValues=['TESV','Call of duty','Apex Legends','shit','Sekiro']
gameData=dict(zip(gameKeys,gameValues)) #use dict function to map key and values
print(gameData)
print("Game by from software is:",gameData["From Software"])
gameData['Arkane']='Dishonored' #add another key value pairs
del gameData['EA'] #delete data associated with key 'EA'
print(gameData)
print(gameData.keys())
print(gameData.values())

#Nested Dictionaries
prog={
    'JS':'Atom',
    'c':'VSCode',
    'python':['pycharm','sublime'],
    'java':{
        'jse':'Net Beans',
        'JEE':'Eclipse'
    }
}
print(prog['python'][1])
print(prog['java']['jse'])
