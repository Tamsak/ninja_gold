# -*- coding: utf-8 -*
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse,redirect
import random
from time import gmtime, strftime

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    if 'activity' not in request.session:
        request.session['activity'] = []
    return render(request, 'ninja_gold/index.html')

def gold(request):
    time = strftime("%Y-%m-%d %H:%M %p", gmtime()),
    if request.POST['location'] == "farm":
        farm_gold = random.randint(10,21)
        request.session['counter'] += int(farm_gold)
        activity = "You went to the {} and earn {} gold {}". format(request.POST['location'], farm_gold,time)
    if request.POST['location'] == "cave":
        cave_gold = random.randint(5,10)
        request.session['counter'] += cave_gold
        activity = "You went to the {} and earn {} gold {}". format(request.POST['location'],cave_gold,time)
    if request.POST['location'] == "house":
        house_gold = random.randint(2,5)
        request.session['counter'] += house_gold
        activity = "You went to the {} and earn {} gold {}". format(request.POST['location'], house_gold,time)
    elif request.POST['location'] == "casino":
        casino_gold = random.randint(0,50)
        chance = random.randint(0,2)
        if chance == 1:
            request.session['counter'] += casino_gold
            activity = "You went to the {} and earn {} gold {}". format(request.POST['location'], casino_gold,time)
        elif chance == 0:
            request.session['counter'] -= casino_gold
            activity = "You went to the {} and lost {} gold {}". format(request.POST['location'], casino_gold,time)
    
    request.session['activity'].append(activity)
    
    return redirect('/')

def reset(request):
    del request.session['counter']
    del request.session['activity']
    return redirect('/')




