from django.test import TestCase, Client
from django.urls import reverse
import json

class TestViews(TestCase):

  # this method will run first before any test methods are tested
  def setUp(self):
    # I set client to mimick the actual user operating the megasoft calculator
    self.client = Client()
    # I set one Web API route to test if my urls are reversed and redirected well 
    # All other functions (subtract,divide,multiple,calculateFaction) can also be intergrated like this
    self.calc_adding_url = reverse('calculator:add')
    self.calc_subtract_url = reverse('calculator:subtract')
    self.calc_multiply_url = reverse('calculator:multiply')
    self.calc_divide_url = reverse('calculator:divide')
    self.calc_factorial_url = reverse('calculator:factorial')

  # Here i define methods to test all urls if are correct
  def test_add_URL(self):
    response = self.client.get(self.calc_adding_url)

  def test_subtract_URL(self):
    response = self.client.get(self.calc_subtract_url)

  def test_multiply_URL(self):
    response = self.client.get(self.calc_multiply_url)

  def test_divide_URL(self):
    response = self.client.get(self.calc_divide_url)

  def test_factorial_URL(self):
    response = self.client.get(self.calc_factorial_url )














    # self.assertEquals(response.status_code,200)