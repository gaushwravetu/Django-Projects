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
        djtext=result
        parameters = {'purpose':'Removed punctuations','analysed_text':djtext}
        return render(request,"analyze.html",parameters)
    
    if capital=='on':
        result = ''
        result = djtext.upper()
        djtext=result
        parameters = {'purpose':'Capitalized text','analysed_text':djtext}
        return render(request,"analyze.html",parameters)
    
    if newline=='on':
        result = ''
        for char in djtext:
            if char!= '\n':
                result+=char
        djtext=result
        parameters = {'purpose':'New line remover','analysed_text':djtext}
        return render(request,"analyze.html",parameters)

    else:
        return HttpResponse('Error')

# def capitalizefirst(request):
#     return render(request,"capitalizefirst.html")

# def newlineremover(request):
#     return render(request,"newlineremover.html")

# def spaceremover(request):
#     return render(request,"spaceremover.html")

# def charcount(request):
#     return render(request,"charcount.html")