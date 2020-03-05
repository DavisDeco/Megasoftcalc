from django.urls import path
from .views import *

urlpatterns = [
  # add function
  path('add', add,name='add'),
  # subtract function
  path('subtract', subtract,name='subtract'),
  # multiply function   factorial
  path('multiply', multiply,name='multiply'),
  # divide function
  path('divide', divide,name='divide'),
  # factorial function
  path('factorial', calculateFactorial,name='factorial'),




]