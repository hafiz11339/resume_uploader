from django.shortcuts import redirect, render
from . forms import ResumeForm
from .models import Resume
from django.views import View
# Create your views here.
class HomeView(View):
    def get(self,request):
        form = ResumeForm()
        candidates = Resume.objects.all()
        return render(request,'resumeapp/home.html',context={"form":form,"candidates":candidates}) 
    def post(self,request):
        form = ResumeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")

class DetailView(View):
    def get(self,request,pk):
        data = Resume.objects.get(pk=pk)
        return render(request,"resumeapp/detail.html",context={"data":data})