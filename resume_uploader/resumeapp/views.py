from django.shortcuts import redirect, render, HttpResponse
from .forms import ResumeForm, CustomUserForm, LoginForm
from .models import Resume
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class HomeView(View):
    # login_url = '/login'
    @method_decorator(login_required(login_url='login/'))
    def get(self,request):
        form = ResumeForm()
        context = {"form": form}
        return  render(request,'resumeapp/home.html',context)

    @method_decorator(login_required(login_url='login/'))
    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "CV Added")
            form = ResumeForm()
            return render(request, 'resumeapp/home.html', context={"form": form, "message": messages})


class ListView(View):
    @method_decorator(login_required(login_url='login/'))
    def get(self, request):
        candidates = Resume.objects.all()
        return render(request, 'resumeapp/list.html', context={ "candidates": candidates})
class DetailView(View):
    def get(self, request, pk):
        data = Resume.objects.get(pk=pk)
        return render(request, "resumeapp/detail.html", context={"data": data})


class Register(View):
    def get(self, request):
        form = CustomUserForm()
        context = {'form': form}
        return render(request, "resumeapp/register.html", context)

    def post(self, request):
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')


class LoginUser(View):
    def get(self, request):
        form = LoginForm()
        context = {'form': form}
        return render(request, "resumeapp/login.html", context)

    def post(self, request):
        user = authenticate(email=request.POST['email'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login_user')


class LogoutUser(View):
    def get(self, request):
        logout(request)
        return redirect('login_user')
