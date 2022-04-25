from django.shortcuts import render
from . forms import ResumeForm
from .models import Resume
from django.views import View
# Create your views here.
class HomeView(View):
    def get(self,request):
        form = ResumeForm()
        return render(request,'resumeapp/home.html',context={"form":form}) 
