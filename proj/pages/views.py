from django.shortcuts import render
from .models import Login
from .forms import LoginForm


def index(request):
          if request.method =="POST":
                    data=LoginForm(request.POST)
                    if data.is_valid:
                              data.save()
                    
                    
          
          context={
                    'lf':LoginForm
          }


          

          return render(request,'pages/index.html',context)

          