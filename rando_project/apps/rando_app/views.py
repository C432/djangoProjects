from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    request.session['counter'] += 1
    request.session['random_word'] = get_random_string(length = 14)

    return render(request, 'rando_app/index.html')

def reset(request):
    print 'this route works!'
    request.session['counter'] = -1
    # return redirect(request, '/random_word/reset') doesn't work!!
    return redirect('/')