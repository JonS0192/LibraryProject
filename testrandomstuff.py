import inspect

class apples():
    size = 'a'
    shape = 'b'
    def apples(self):
        size = 0
        shape = ""
returnvalue = []
returnvalue2 = []
apple_dict=apples.__dict__
thislist = (a for a in apple_dict if not (a[0].startswith('_')))
for x in thislist:
    returnvalue.append(x)
    returnvalue2.append(apple_dict[x])
print(apple_dict)
print(returnvalue)
print(returnvalue2)
d={}
d['mynewkey'] = 'mynewvalue'
print(d)