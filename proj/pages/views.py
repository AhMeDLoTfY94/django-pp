from django.shortcuts import render


def index(request):
          x={
                    "name":"mohamed"
          }
          return render(request,'pages/index.html',x)

          