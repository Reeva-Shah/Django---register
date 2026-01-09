from django.shortcuts import render
from .models import *

def Home(req):
    return render(req, 'home.html')
def Reg(req):
    if req.method == 'POST':
        nm=req.POST['n']
        em=req.POST['e']
        pw=req.POST['p']
        pw1=req.POST['p1']
        if pw!=pw1:
            Error="your password doesnt match"
            return render(req, 'register.html',context={'Err':Error})
        ema=form.objects.filter(Email=em).count()
        if ema==1:
            Error="Email already registered"
            return render(req, 'register.html', context={'Err': Error})
        obj=form(Name=nm,Email=em,Password=pw)
        obj.save()
    return render(req, 'register.html')
