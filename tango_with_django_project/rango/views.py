from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #construct a dictionary to pass to the tempalge engine as its context
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}

    #return a redered response to send to the client.
    # We Make use of the shortcut fucntion to make our lived easier.
    #Note that the first parameter is the tempale we wish to use

    #return HttpResponse("Rango says hey there partner!")
    return render(request, 'rango/index.html', context = context_dict)