#zip is used to connect two lists in key value pair
alias=('Superman','Batman','Flash')#in this case tuple
names=('Clark Kent','Bruce Wayne','Barry Allen')

identities=dict(zip(alias,names))#can be list,tuple,set etc
print(identities)
print(identities['Batman'])
