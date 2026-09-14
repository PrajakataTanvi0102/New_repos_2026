# tuple1=('b','a','n','a','n','a')
# print(tuple1.count('a'))
# print(tuple1.index('n'))

# set4={1,2,3,2,5,6,3,2}
# print(set4)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x=thisdict.get("model")
# print(x)


def greet():
    print("hello baby")
greet()

def greetUser(name):
    print("hello",name)
greetUser("Harry")


def add(a,b):
    sum=a+b
    return sum;

res=add(10,20)
print(res)


add=lambda a,b :a+b
print(add(10,10))
print(add("Hello","World"))

list1=[1,2,3,4,5]
eve=list(filter(lambda x: x % 2 == 0,list1))
print(eve)