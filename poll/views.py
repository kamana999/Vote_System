from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import generic
from django.db.models import Q, Count
from math import ceil
from .forms import *
from django.contrib import messages


def index(r):
    return render(r, 'home.html')


def get_user(r):
    if r.session.has_key('login'):
        return Voter.objects.get(email=r.session['login'])
    else:
        return {"username": "WHOO??"}


def signup(r):
    form = UserForm(r.POST or None)
    if r.method=="POST":
        form.save()
        return redirect(vote)
    return render(r, 'user/index.html', {
        'form': UserForm,

    })


def login(r):
    form = LoginForm(r.POST or None)
    if r.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            cond = Q(email=username) & Q(password=password)
            check = Voter.objects.get(cond)

            if check:
                r.session['login'] = username
                return redirect(vote)
            else:
               return redirect(index)


def logout(r):
    del r.session['login']
    return redirect(index)


def contestant(r):
    form = ContestantForm(r.POST or None, r.FILES or None)
    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(contestant)
    return render(r, 'contestnt/form.html', {
        'form': ContestantForm,
        'city': InsertCity,
    })


def profile(r):
    return render(r, 'contestnt/index.html',{
        'contestants': Contestant.objects.all(),
    })


def profile_view(r, id):
    return render(r, 'contestnt/view.html', {
        'contestants': Contestant.objects.get(pk=id),
    })


def vote(r):
    return render(r, 'user/index.html', {
        'contestants': Contestant.objects.all(),
        'form': UserForm,
        'login_form': LoginForm,
        'user': get_user(r),
    })


def vote_now(r, id):
    contestant_id = get_object_or_404(Contestant, id=id)
    if contestant_id:
        new_vote = Vote(voter=get_user(r), contestaant=contestant_id)
        if new_vote.voter.u_status == 1:
            return redirect(vote)
        else:
            new_vote.voter.u_status += 1
            new_vote.voter.save()
            new_vote.save()
    return render(r, 'user/result.html', {
        'contestants': Contestant.objects.all(),
        'user': get_user(r),

    })


def result(r):
    return render(r, 'user/result.html', {
        'contestants': Contestant.objects.all(),
    })


