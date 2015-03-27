# Create your views here.

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import messages

from .forms import SignUpForm


def home(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        new_sign_up = form.save(commit=False)
        new_sign_up.save()
        messages.success(request, 'Thank you for joining.')
        
    return render_to_response('form.html', locals(), context_instance=RequestContext(request))
    