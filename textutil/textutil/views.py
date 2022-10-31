from os import remove
from symbol import parameters
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,"index.html")

def analyze(request):
    #get the text
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    capital = request.GET.get('capital','off')
    newline = request.GET.get('newline','off')
    punclist = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    if removepunc=='on':
        result = ''
        for char in djtext:
            if char not in punclist:
                result+=char
        parameters = {'purpose':'Removed punctuations','analysed_text': result}
        djtext=result
    
    if capital=='on':
        result = ''
        result = djtext.upper()
        parameters = {'purpose':'Capitalized text','analysed_text': result}
        djtext=result
    
    if newline=='on':
        result = ''
        for char in djtext:
            if char!= '\n' and char!='\r':
                result+=char
        parameters = {'purpose':'New line remover','analysed_text': result}

    if(removepunc!='on' and capital!='on' and newline!='on'):
        return HttpResponse('Error')
    
    return render(request,"analyze.html",parameters)

# def capitalizefirst(request):
#     return render(request,"capitalizefirst.html")

# def newlineremover(request):
#     return render(request,"newlineremover.html")

# def spaceremover(request):
#     return render(request,"spaceremover.html")

# def charcount(request):
#     return render(request,"charcount.html")