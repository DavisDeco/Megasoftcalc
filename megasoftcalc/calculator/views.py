from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse


 
def add(request):
  """
  An addition function. 
  Figures to be computed are passed as URL params
  add(
      a: int,
      b: int,
      ret: int
  )
  example call: **your_host_address**/add/?a=1&b=1
  should return a json looks like:
  {'function': 'add','result': 2}
  """
  try:
      first_number = int(request.GET.get('a'))
      second_number = int(request.GET.get('b'))
      result = first_number + second_number
      return JsonResponse({'function': 'add','result': result})
  except Exception as e:
      return JsonResponse({'function': 'add','result': 'there was an error ' + str(e)})

def subtract(request):
    """
    An addition function.     
    add(
        a: int,
        b: int,
        ret: int
    )
    example call: **your_host**/add/?a=1&b=1
    should return a json looks like:
    {'function': 'add','result': 2}
    """
    try:
        first_number = int(request.GET.get('a'))
        second_number = int(request.GET.get('b'))
        return JsonResponse({'function': 'add','result': first_number - second_number})
    except Exception as e:
        return JsonResponse({'function': 'add','result': 'there was an error ' + str(e)})



 
def multiply(request):
    """
    A multiplication function. 
    multiply(
        a: int,
        b: int,
        ret: int
    )
    example call: **your_host**/multiply/?a=1&b=2
    should return a json looks like:
    {'function': 'multiply','result': 2}
    """
    try:
        first_number = int(request.GET.get('a'))
        second_number = int(request.GET.get('b'))
        return JsonResponse({'function': 'multiply','result': first_number * second_number})
    except Exception as e:
        return JsonResponse({'function': 'multiply','result': 'there was an error ' + str(e)})


 
def divide(request):
    """
    A division function. 
    divide(
        a: int,
        b: int,
        ret: int
    )
    """
    try:
        first_number = int(request.GET.get('a'))
        second_number = int(request.GET.get('b'))
        return JsonResponse({'function': 'divide','result': first_number / second_number})
    except Exception as e:
        return JsonResponse({'function': 'divide','result': 'there was an error ' + str(e)})

def factorial(num):
    """This is a recursive function that calls
   itself to find the factorial of given number"""
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)

def calculateFactorial(request):
  number = int(request.GET.get('a'))

  # We will find the factorial of this number
  # num = int(input("Enter a Number: "))

  # if input number is negative then return an error message
  # elif the input number is 0 then display 1 as output
  # else calculate the factorial by calling the user defined function
  if number < 0:
      return JsonResponse({'details': "Factorial cannot be found for negative numbers"})
      # print("Factorial cannot be found for negative numbers")
  elif number == 0:
    return JsonResponse({'details': "Factorial of 0 is 1"})
    # print("Factorial of 0 is 1")
  else:
    return JsonResponse({'result': factorial(number) })
    # print("Factorial of", number, "is: ", )

