from django.shortcuts import render


def index(request):
          x={
                    "name":"ahmed"
          }
          return render(request,'pages/index.html',x)

          