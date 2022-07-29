from django.shortcuts import render , redirect
from django.contrib.auth.models import User , auth
from django.contrib.auth import authenticate , login
from django.contrib import messages
from .models import Profile , Post
from django.contrib.auth.decorators import login_required
 
# Create your views here.
@login_required(login_url='signin')
def index(request):
    
    user_object=User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    return render(request,'index.html',{'user_profile':user_profile})
    

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_re = request.POST['password-re']
        if password == password_re:
            if User.objects.filter(email = email).exists():
                messages.info(request,'Email already Taken...')
                return redirect('signup')
            elif User.objects.filter(username = username).exists():
                messages.info(request,'Username already Taken...')
                return render('signup')
            else:
                user = User.objects.create_user(username = username , email = email , password = password)
                user.save()

                #log user in and redirect to the settings page
                user_login=authenticate(username = username , password = password)
                login(request,user_login)
                #create profile object for new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model,id_user = user_model.id)
                new_profile.save()
                return redirect('settings')
        else:
            messages.info(request,'Password Not matching...')
            return redirect('signup')
    else:
        return render(request,'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate( username = username , password = password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request , 'Credentials Invalid....')
            return redirect('signin')
    else:
        return render(request,'signin.html')

@login_required(login_url="signin")
def signout(request):
    auth.logout(request)
    return redirect('signin')

@login_required(login_url="signin")
def settings(request):
    regions = ['Sagaing','Kayin','Magway','Chin','Mandalay','Kayah','Rakhine',
                'Yangon','Mon','Bago','Kachin','Shan','Ayyearwady','Tanintharyi']
    languages = ['Burmese','English','Chin','Karen','Arakan','Kayan','Mon','Jinpho','Shan']
    user_profile = Profile.objects.get(user = request.user)
    if request.method == 'POST' :
        if request.FILES.get('image') == None:
            image = user_profile.profile_img
            fst_name = request.POST['fst-name']
            lst_name = request.POST['lst-name']
            region = request.POST['region']
            language = request.POST['language']
            if region not in regions:
                messages.info(request,"Please fill correct regions of Myanmar..\n Available regions = 'Sagaing','Kayin','Magway','Chin','Mandalay','Kayah','Rakhine','Yangon','Mon','Bago','Kachin','Shan','Ayyearwady','Tanintharyi'")
                return redirect('settings')
            elif language not in languages:
                messages.info(request,"Please fill correct languages..\n Available languaes = 'Burmese','English','Chin','Karen','Arakan','Kayan','Mon','Jinpho','Shan'")
                return redirect('settings')
            else:
                user_profile.profile_img = image
                user_profile.fst_name = fst_name
                user_profile.lst_name = lst_name
                user_profile.region = region
                user_profile.language = language
                user_profile.save()
        if request.FILES.get('image') != None :
            image = request.FILES.get('image')
            fst_name = request.POST['fst-name']
            lst_name = request.POST['lst-name']
            region = request.POST['region']
            language = request.POST['language']
            if region not in regions:
                messages.info(request,"Please fill correct regions of Myanmar..\n Available regions = 'Sagaing','Kayin','Magway','Chin','Mandalay','Kayah','Rakhine','Yangon','Mon','Bago','Kachin','Shan','Ayyearwady','Tanintharyi'")
                return redirect('settings')
            elif language not in languages:
                messages.info(request,"Please fill correct languages..\n Available languaes = 'Burmese','English','Chin','Karen','Arakan','Kayan','Mon','Jinpho','Shan'")
                return redirect('settings')
            else:
                user_profile.profile_img = image
                user_profile.fst_name = fst_name
                user_profile.lst_name = lst_name
                user_profile.region = region
                user_profile.language = language
                user_profile.save()
        return redirect('settings')
    return render(request,'settings.html' , { 'user_profile' : user_profile})

@login_required(login_url="signin")
def upload_posts(request):
    
    if request.method == 'POST' :
        user= request.user.username
        image = request.FILES.get('upload_img')
        caption = request.POST['caption']
        txt = request.POST['txt']
        new_post = Post.objects.create(user = user ,image = image , caption = caption , txt = txt)
        new_post.save()
        return redirect('/')
    else:
        return redirect('/')
        
def posts(request):
    user_object=User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    posts = Post.objects.all()
    return render(request,'posts.html',{'posts':posts,'user_profile':user_profile})   
    