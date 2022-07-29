from distutils.command.upload import upload
from unicodedata import name
from django.urls import  path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',views.index, name='index'),
    path('signup/',views.signup, name='signup'),
    path('signin/',views.signin, name = 'signin'),
    path('signout/',views.signout, name="signout"),
    path('settings/',views.settings,name='settings'),
    path('upload_posts/',views.upload_posts,name='upload_posts'),
    path('posts/',views.posts,name="posts")
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)