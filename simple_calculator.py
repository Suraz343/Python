#calculator

def addition(n1,n2):
  """helps to add to numbers"""
  return n1+n2
def subtraction(n1,n2):
  """subtract two nunbers"""
  return n1-n2
def multiplication(n1,n2):
  """multilply numbers"""
  return n1*n2
def division(n1,n2):
  """divide two numbers"""
  return n1/n2
operations={"+":addition,"-":subtraction,"*":multiplication, "/":division}
num1=int(input("enter the first number?"))

for i in operations:
  print(i)
operation_symbol=str(input("enter the operation which you want to perform?"))
num2=int(input("enter the second number?"))
calculation_function=operations[operation_symbol]
result=calculation_function(num1,num2)
print(f"{num1} {operation_symbol} {num2} ={result}")