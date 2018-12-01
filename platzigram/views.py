from django.http import HttpResponse
from django.http import JsonResponse
import json

from datetime import datetime

def hello_world(request):
    #now = datetime.now()
    #return HttpResponse('<h1><b>Hello World</b><h1/><p>Our current server time is {}'.format(str(now)))
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('<h1><b>Hello World</b><h1/><p>Our current server time is {}'.format(now))


def hi(request):
    import pdb
    pdb.set_trace() # pone un debugger en la consola
    return HttpResponse('Hi!')


def sort_integers(request):
    # http://localhost:8000/hi2/?numbers=10,4,50,32
    # devolver una lista ordenada de los numeros del argumento de numbers

    #import pdb
    #pdb.set_trace()
    #'10,4,50,32' son los argumentos de numbers en el objeto request 
    #X=list(map(int, request.GET['numbers'].split(',')))
    #X--> [10, 4, 50, 32]
    #return JsonResponse({'Numeros':json.dumps(sorted(X))})
    numbers=[int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints= sorted(numbers)
    #return HttpResponse(str(sorted_ints), content_type='application/json)')
    
    #diccionario
    data = {
        'status':'ok',
        'numbers':sorted_ints,
        'message':'Integer sorted successfully'
    }

    return HttpResponse(json.dumps(data), content_type='application/json')

def say_hi(request,name,age):
    #en el browser http://localhost:8000/hi2/John/17/
    if age<12:
        message='Sorry {}, You are not allowed here'.format(name)
    else:
        message='Hi {}, Welcome to the site'.format(name)    
    return HttpResponse(message)