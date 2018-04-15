from django.conf.urls import url
from homepage import views

# SET THE NAMESPACE!
app_name = 'homepage'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^profile/$',views.profile, name='profile'),
    # url(r'^profile/profile_pics$', views.profile, name='profile'),
    # path('login/',login,views.user_login),
    url(r'^europe/$', views.europe, name='europe'),
    # url(r'^$', views.europe, name='europe'),
    url(r'^sample/$', views.sample, name = 'sample'),
    url(r'^aboutus/$', views.aboutus, name='aboutus'),
    url(r'^blog/index/$', views.index, name='index'),
    url(r'^calculateprice/$', views.calculateprice, name='calculateprice'),
    # url(r'^user_id/$', )
    url(r'^blog/index/first/$', views.first, name='first'),
    url(r'^blog/index/second/$', views.second, name='second'),
    url(r'^blog/index/third/$', views.third, name='third'),
    url(r'^blog/index/fourth/$', views.fourth, name='fourth'),
    url(r'^blog/index/fifth/$', views.fifth, name='fifth'),
    url(r'^blog/index/sixth/$', views.sixth, name='sixth'),
]
