print("Welcome to python..")

#Sum of two nums

# def sum(a,b):
#     return a + b
# print("Enter two numbers: ")
# num1 = int(input("Enter 1st num : "))
# num2 = int(input("Enter 2nd num : "))
# res=sum(num1,num2)

# print(res)

#Learn about loops in Python

listA = {1,3,5} 
for i in listA:
    print(i * 10)

#global var
global x
x = "Im a global var"
def example():
    print(x)

example()

#python datatypes

x = "40"
y = int(x)
floatVal = float(x)
complexVal = complex(x)
print(y)
print(floatVal)
print(complexVal)

#Dictionary : used to store key : value pairs

dictA = {
    "name" : "Soumik Bose",
    "age" : 40,
    "status" : "Trillonaire",
    "worth" : "4000 billion dollars"
}

print(dictA)
print(dictA["name"])

#Python read file
x = open("C:\\Users\Infiflex214\Desktop\Completed ftlh\\assign rest call.txt","r")
print(x.read())




