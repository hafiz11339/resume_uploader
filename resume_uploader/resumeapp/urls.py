from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",views.HomeView.as_view(),name="home"),
    path("detail/<int:pk>",views.DetailView.as_view(),name='detail'),
    path('register',views.Register.as_view(),name='register'),
    path("login/",views.LoginUser.as_view(),name='login_user'),
    path("logout",views.LogoutUser.as_view(),name='logout'),
    path("list",views.ListView.as_view(),name="list")

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)