from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse

"""
  An addition function. 
  Figures to be computed are passed as URL params and should be 
  converted to Int

  example call: **your_host_address**/add/?a=1&b=1
  should return a json looks like:
  {'function': 'add','result': 2}
""" 
def add(request):  
  try:
      first_number = int(request.GET.get('a'))
      second_number = int(request.GET.get('b'))
      result = first_number + second_number
      return JsonResponse({'function': 'add','result': result})
  except Exception as e:
      return JsonResponse({'function': 'add','result': 'there was an error ' + str(e)})



"""
    An Subtraction function.     
    Figures to be computed are passed as URL params and should be 
    converted to Int

    example call: **your_host**/add/?a=1&b=1
    should return a json looks like:
    {'function': 'add','result': 2}
"""
def subtract(request):    
    try:
        first_number = int(request.GET.get('a'))
        second_number = int(request.GET.get('b'))
        return JsonResponse({'function': 'subtract','result': first_number - second_number})
    except Exception as e:
        return JsonResponse({'function': 'subtract','result': 'there was an error ' + str(e)})



"""
    A multiplication function. 
    Figures to be computed are passed as URL params and should be 
    converted to Int
    
    example call: **your_host**/multiply/?a=1&b=2
    should return a json looks like:
    {'function': 'multiply','result': 2}
""" 
def multiply(request):   
  try:
      first_number = int(request.GET.get('a'))
      second_number = int(request.GET.get('b'))
      return JsonResponse({'function': 'multiply','result': first_number * second_number})
  except Exception as e:
      return JsonResponse({'function': 'multiply','result': 'there was an error ' + str(e)})

"""
    A division function. 
    Figures to be computed are passed as URL params and should be 
    converted to Int
""" 
def divide(request):   
    try:
        first_number = int(request.GET.get('a'))
        second_number = int(request.GET.get('b'))
        return JsonResponse({'function': 'divide','result': first_number / second_number})
    except Exception as e:
        return JsonResponse({'function': 'divide','result': 'there was an error ' + str(e)})

"""This is a recursive function that calls
   itself to find the factorial of given number
"""
def factorial(num):
    
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)

"""
Function to handle factorial calculation of a number received
"""
def calculateFactorial(request):
  try:
    number = int(request.GET.get('a'))
    if number < 0:
        return JsonResponse({'details': "Factorial cannot be found for negative numbers"})
    elif number == 0:
      return JsonResponse({'details': "Factorial of 0 is 1"})
    else:
      return JsonResponse({'Factorial of': number, 'result': factorial(number) })

  except Exception as e:
    return JsonResponse({'function': 'calculateFactorial','result': 'there was an error ' + str(e)})


  
