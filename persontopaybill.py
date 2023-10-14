import random
name_string=input("enter everybody's name,seperated by comma:")
name=name_string.split(",")
a=len(name)
random_name=random.randint(0,a-1)
person_to_pay=name[random_name]
print(person_to_pay + "is going to pay the bill for todays meal")