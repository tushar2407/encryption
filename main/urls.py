from django.urls import path
from main import views
from django.contrib.auth.decorators import login_required

urlpatterns=[
    path('page1/', views.page1, name='page1'),
    path('', views.Index.as_view(),name='login'),
    path('account/',views.Account.as_view(), name='account'),
    path('/',views.Logout.as_view(),name='logout'),
    path('encrypt',views.Encrypt.as_view(), name='encrypt'),
    path('decrypt',views.Decrypt.as_view(), name='decrypt'),
   # path('encrypt_file',views.Encrypt_file.as_view(), name='encrypt_file'),
    path('signup', views.SignUp.as_view(), name='signup')
   # path('account/logout/', views.Index.as_view())
   #path('encrypt',views.encrypt)

]