from django.http import JsonResponse
from rest_framework.response import Response

def welcomeHome(request):
    return JsonResponse({'detail': 'Welcome to our Megasoft Calculator Api','Developer':'CalcuCo'}, status=401)
