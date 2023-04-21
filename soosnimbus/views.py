from django.core.mail import EmailMessage
import random
import string
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import User, Music, Comment, Playlist
from django.utils import timezone
from django.urls import reverse
import datetime

def index(request):
    template = loader.get_template('main.html')
    log_ses = request.session.get('User_')
    
    if log_ses is not None:
        user= User.objects.get(uemail=log_ses)
        login_butt = "Logout"
        login_link = "logout"
        signup_butt = "Profile"
        signup_link = "profile/{{user.uemail}}"
    else:
        login_butt = "Login"
        login_link = "login"
        signup_butt = "Sign up"
        signup_link = "email_test"
        
    musics = Music.objects.all().order_by('-id').values()[:10] ## 최근 10개의 업로드 목록을 출력
    nowDatetime = timezone.now()
    all_musics1 = Music.objects.all().order_by('-mview', '-id').values()
    all_musics2 = Music.objects.all().order_by('-mview', '-id').values()
    
    rank1_list = []
    rank1_no = 1
    for x in all_musics1:
        if nowDatetime-x['mrdate'] <= datetime.timedelta(days=7):
            dict1 = {}
            dict1['rank'] = rank1_no
            dict1['mtitle'] = x['mtitle']
            dict1['msinger'] = x['msinger']
            dict1['mp3'] = x['mp3']
            dict1['mphoto'] = x['mphoto']
            dict1['id'] = x['id']
            rank1_list.append(dict1)
            rank1_no = rank1_no + 1
    rank1_list = rank1_list[:5]
            
    rank2_list = []
    rank2_no = 1
    for x in all_musics2:
        if nowDatetime-x['mrdate'] <= datetime.timedelta(days=7):
            dict2 = {}
            dict2['rank'] = rank2_no
            dict2['mtitle'] = x['mtitle']
            dict2['msinger'] = x['msinger']
            dict2['mp3'] = x['mp3']
            dict2['mphoto'] = x['mphoto']
            dict2['id'] = x['id']
            rank2_list.append(dict2)
            rank2_no = rank2_no + 1
    rank2_list = rank2_list[5:10]

    ballad_musics = Music.objects.filter(mgenre='ballade').order_by('-id').values()
    rock_musics = Music.objects.filter(mgenre='rock').order_by('-id').values()
    hiphop_musics = Music.objects.filter(mgenre='hiphop').order_by('-id').values()
    pop_musics = Music.objects.filter(mgenre='pop').order_by('-id').values()
    ccm_musics = Music.objects.filter(mgenre='ccm').order_by('-id').values()
        
    music_list = []
    delay = 0
    count = 0
    for x in musics:
        count = count + 1
        dict = {}
        dict['delay'] = delay
        dict['mtitle'] = x['mtitle']
        dict['msinger'] = x['msinger']
        dict['mp3'] = x['mp3']
        dict['mphoto'] = x['mphoto']
        dict['id'] = x['id']
        music_list.append(dict)
        delay = delay + 60
        if count >= 6:
            delay = 0
        
    ballad_music_list = []
    delay = 0
    count = 0
    for x in ballad_musics:
        count = count + 1
        dict = {}
        dict['delay'] = delay
        dict['mtitle'] = x['mtitle']
        dict['msinger'] = x['msinger']
        dict['mp3'] = x['mp3']
        dict['mphoto'] = x['mphoto']
        dict['id'] = x['id']
        ballad_music_list.append(dict)
        delay = delay + 60
        if count >= 6:
            delay = 0
        
    rock_music_list = []
    delay = 0
    count = 0
    for x in rock_musics:
        count = count + 1
        dict = {}
        dict['delay'] = delay
        dict['mtitle'] = x['mtitle']
        dict['msinger'] = x['msinger']
        dict['mp3'] = x['mp3']
        dict['mphoto'] = x['mphoto']
        dict['id'] = x['id']
        rock_music_list.append(dict)
        delay = delay + 60
        if count >= 6:
            delay = 0
        
    hiphop_music_list = []
    delay = 0
    count = 0
    for x in hiphop_musics:
        count = count + 1
        dict = {}
        dict['delay'] = delay
        dict['mtitle'] = x['mtitle']
        dict['msinger'] = x['msinger']
        dict['mp3'] = x['mp3']
        dict['mphoto'] = x['mphoto']
        dict['id'] = x['id']
        hiphop_music_list.append(dict)
        delay = delay + 60
        if count >= 6:
            delay = 0
        
    pop_music_list = []
    delay = 0
    count = 0
    for x in pop_musics:
        count = count + 1
        dict = {}
        dict['delay'] = delay
        dict['mtitle'] = x['mtitle']
        dict['msinger'] = x['msinger']
        dict['mp3'] = x['mp3']
        dict['mphoto'] = x['mphoto']
        dict['id'] = x['id']
        pop_music_list.append(dict)
        delay = delay + 60
        if count >= 6:
            delay = 0
        
    ccm_music_list = []
    delay = 0
    count = 0
    for x in ccm_musics:
        count = count + 1
        dict = {}
        dict['delay'] = delay
        dict['mtitle'] = x['mtitle']
        dict['msinger'] = x['msinger']
        dict['mp3'] = x['mp3']
        dict['mphoto'] = x['mphoto']
        dict['id'] = x['id']
        ccm_music_list.append(dict)
        delay = delay + 60
        if count >= 6:
            delay = 0

    try:
        user= User.objects.get(uemail=log_ses)
        message = "님 환영합니다"
        context = {
            'music_list':music_list,
            'ballad_music_list':ballad_music_list,
            'rock_music_list':rock_music_list,
            'hiphop_music_list':hiphop_music_list,
            'pop_music_list':pop_music_list,
            'ccm_music_list':ccm_music_list,
            'log_nick':user.unick+message,
            'login_butt':login_butt,
            'login_link':login_link,
            'signup_butt':signup_butt,
            'signup_link':signup_link,
            'user': user,
            'rank1_list':rank1_list,
            'rank2_list':rank2_list
        }        
    except:
        message = "로그인 해주세요"
        context = {
            'music_list':music_list,
            'ballad_music_list':ballad_music_list,
            'rock_music_list':rock_music_list,
            'hiphop_music_list':hiphop_music_list,
            'pop_music_list':pop_music_list,
            'ccm_music_list':ccm_music_list,
            'log_nick':message,
            'login_butt':login_butt,
            'login_link':login_link,
            'signup_butt':signup_butt,
            'signup_link':signup_link,
            'rank1_list':rank1_list,
            'rank2_list':rank2_list
        }
    return HttpResponse(template.render(context, request))

def profile(request, uemail):
    template = loader.get_template('profile.html')
    log_ses = request.session.get('User_')
    user= User.objects.get(uemail=log_ses)
    my_musics = Music.objects.filter(uemail_id=log_ses).order_by('-id').values()
    playlists = Playlist.objects.filter(uemail_id=log_ses).order_by('-id').values()
    
    pnames = set()
    for x in playlists:
        pnames.add(x['pname'])
        
    my_musics_list = []
    delay = 0
    count = 0
    for x in my_musics:
        count = count + 1
        dict = {}
        dict['delay'] = delay
        dict['mtitle'] = x['mtitle']
        dict['msinger'] = x['msinger']
        dict['mp3'] = x['mp3']
        dict['mphoto'] = x['mphoto']
        dict['id'] = x['id']
        my_musics_list.append(dict)
        delay = delay + 60
        if count >= 6:
            delay = 0
    
    list1 = []
    for x in pnames:
        dict1 = {}
        dict1['pname'] = x
        list1.append(dict1)
        list2 = []
        for y in playlists.filter(pname=x):
            dict2 = {}
            mid = y['mid_id']
            dict2['mtitle'] = Music.objects.get(id=mid).mtitle
            dict2['msinger'] = Music.objects.get(id=mid).msinger
            dict2['mp3'] = Music.objects.get(id=mid).mp3
            dict2['mphoto'] = Music.objects.get(id=mid).mphoto
            dict2['id'] = mid
            dict2['pid'] = y['id']
            list2.append(dict2)
        dict1['music'] = list2
        
    if log_ses is not None:
        login_butt = "Logout"
        login_link = "logout"
        signup_butt = "Profile"
        signup_link = "profile/{{user.uemail}}"
    else:
        login_butt = "Login"
        login_link = "login"
        signup_butt = "Sign up"
        signup_link = "email_test"
    message = "님 환영합니다"
    context = {
        'my_musics_list':my_musics_list,
        'log_nick':user.unick+message,
        'login_butt':login_butt,
        'login_link':login_link,
        'signup_butt':signup_butt,
        'signup_link':signup_link,
        'playlists':playlists,
        'pnames':pnames,
        'user': user,
        'list1':list1
    }
    return HttpResponse(template.render(context, request))

def profile2(request,uemail):
    template = loader.get_template('profile2.html')
    log_ses = request.session.get('User_')
    user_me =User.objects.get(uemail=log_ses)
    user= User.objects.get(uemail=uemail)
    my_musics = Music.objects.filter(uemail_id=uemail).order_by('-id').values()
    my_musics_list = []
    delay = 0
    count = 0
    for x in my_musics:
        count = count + 1
        dict = {}
        dict['delay'] = delay
        dict['mtitle'] = x['mtitle']
        dict['msinger'] = x['msinger']
        dict['mp3'] = x['mp3']
        dict['mphoto'] = x['mphoto']
        dict['id'] = x['id']
        my_musics_list.append(dict)
        delay = delay + 60
        if count >= 6:
            delay = 0
            
    playlists = Playlist.objects.filter(uemail_id=uemail).order_by('-id').values()
    pnames = set()
    for x in playlists:
        pnames.add(x['pname'])
            
    list1 = []
    for x in pnames:
        dict1 = {}
        dict1['pname'] = x
        list1.append(dict1)
        list2 = []
        for y in playlists.filter(pname=x):
            dict2 = {}
            mid = y['mid_id']
            dict2['mtitle'] = Music.objects.get(id=mid).mtitle
            dict2['msinger'] = Music.objects.get(id=mid).msinger
            dict2['mp3'] = Music.objects.get(id=mid).mp3
            dict2['mphoto'] = Music.objects.get(id=mid).mphoto
            dict2['id'] = mid
            dict2['pid'] = y['id']
            list2.append(dict2)
        dict1['music'] = list2
        
    if log_ses is not None:
        login_butt = "Logout"
        login_link = "logout"
        signup_butt = "Profile"
        signup_link = "profile/{{user.uemail}}"
    else:
        login_butt = "Login"
        login_link = "login"
        signup_butt = "Sign up"
        signup_link = "email_test"
    message = "님 환영합니다"
    context = {
        'my_musics_list':my_musics_list,
        'log_nick':user_me.unick+message,
        'login_butt':login_butt,
        'login_link':login_link,
        'signup_butt':signup_butt,
        'signup_link':signup_link,
        'user': user,
        'list1':list1
    }
    return HttpResponse(template.render(context, request))

def upload(request):
    template = loader.get_template('upload.html')
    log_ses = request.session.get('User_')
    user= User.objects.get(uemail=log_ses)
    if log_ses is not None:
        login_butt = "Logout"
        login_link = "logout"
        signup_butt = "Profile"
        signup_link = "profile/{{user.uemail}}"
    else:
        login_butt = "Login"
        login_link = "login"
        signup_butt = "Sign up"
        signup_link = "email_test"
    user= User.objects.get(uemail=log_ses)
    # request.session['user']=user.email
    # upl_ses = request.session.get('user')
    message = "님 환영합니다"
    context = {
        'user':user,
        'log_nick':user.unick+message,
        'login_butt':login_butt,
        'login_link':login_link,
        'signup_butt':signup_butt,
        'signup_link':signup_link,
    }
    return HttpResponse(template.render(context, request))

def upload_ok(request):
    nowDatetime = timezone.now().strftime('%Y-%m-%d %H')
    music = Music()
    try:
        music.mphoto = request.FILES['photo']
    except:
        music.mphoto = 'images/music_profile.png'
    music.mp3 = request.FILES['music']
    music.mtitle = request.POST['title']
    music.msinger = request.POST['singer']
    music.mdesc = request.POST['explanation']
    music.mgenre = request.POST['genre']
    music.mrdate = nowDatetime
    music.mudate = nowDatetime
    music.mview = 0
    music.uemail_id=request.POST['email']
    music.save()
    return redirect('../profile/{{user.uemail}}')

def login(request):
    template = loader.get_template('login_test.html')
    log_ses = request.session.get('User_')
    if log_ses is not None:
        login_butt = "Logout"
        login_link = "logout"
        signup_butt = "Profile"
        signup_link = "profile/{{user.uemail}}"
    else:
        login_butt = "Login"
        login_link = "login"
        signup_butt = "Sign up"
        signup_link = "email_test"
        
    musics = Music.objects.all().order_by('-id').values()
    try:
        user= User.objects.get(uemail=log_ses)
        message = "님 환영합니다"
        context = {
            'musics':musics,
            'log_nick':user.unick+message,
            'login_butt':login_butt,
            'login_link':login_link,
            'signup_butt':signup_butt,
            'signup_link':signup_link
        }        
    except:
        message = "로그인 해주세요"
        context = {
            'musics':musics,
            'log_nick':message,
            'login_butt':login_butt,
            'login_link':login_link,
            'signup_butt':signup_butt,
            'signup_link':signup_link
        }
    return HttpResponse(template.render(context, request))

def login_ok(request):
    x = request.POST['email']
    y = request.POST['pwd']
    #res_data = {}
    try:
        mach_email = User.objects.get(uemail = x)
        if mach_email.upwd == y:           
            request.session['User_'] = mach_email.uemail                   
            return redirect('/')
        else:  
            #res_data['error'] = "Incorrect password :( "
            #return render(request,'login_test.html',res_data)             
            return HttpResponse("<script>alert('"+ 'Incorrect password :(' +"');location.href=history.back();</script>")
    except:
        #res_data['error'] ="Incorrect email :( "
        #return render(request, 'login_test.html',res_data) 
        return HttpResponse("<script>alert('"+ 'Incorrect email :(' +"');location.href=history.back();</script>")

def forgot_email(request):  
    template = loader.get_template('forgot_email.html')  

    login_butt = "Login"
    login_link = "login"
    signup_butt = "Sign up"
    signup_link = "email_test"

    message = "로그인 해주세요"
    context = {
        'log_nick':message,
        'login_butt':login_butt,
        'login_link':login_link,
        'signup_butt':signup_butt,
        'signup_link':signup_link
    }
    return HttpResponse(template.render(context, request))


def forgot_email_ok(request):      
    x = request.POST['name']
    y = request.POST['phonenumber']    
    res_data = {}
    
    try:
        f_phoneNumber = User.objects.get(utel = y)           
        if f_phoneNumber.uname == x:                                                                 
            res_data['error'] = "Your email has been verified : " 
            res_data['email'] = f_phoneNumber.uemail                           
            return render(request,'forgot_email.html',res_data) 
        else : 
            res_data['error'] = "No matching name found :("
            res_data['email'] = ""         
            return render(request,'forgot_email.html',res_data)
    except: 
        res_data['error'] = "No matching number :("
        res_data['email'] = ""        
        return render(request,'forgot_email.html',res_data)


def register(request):
    template = loader.get_template('register_test.html')
    log_ses = request.session.get('email')
    log_ses2 = request.session.get('User_')
    if log_ses2 is not None:
        login_butt = "Logout"
        login_link = "logout"
        signup_butt = "Profile"
        signup_link = "profile/{{user.uemail}}"
    else:
        login_butt = "Login"
        login_link = "login"
        signup_butt = "Sign up"
        signup_link = "email_test"
    try:
        user= User.objects.get(uemail=log_ses2)
        message = "님 환영합니다"
        context = {
            'log_nick':user.unick+message,
            'login_butt':login_butt,
            'login_link':login_link,
            'signup_butt':signup_butt,
            'signup_link':signup_link,
            'email':log_ses
        }        
    except:
        message = "로그인 해주세요"
        context = {
            'log_nick':message,
            'login_butt':login_butt,
            'login_link':login_link,
            'signup_butt':signup_butt,
            'signup_link':signup_link,
            'email':log_ses
        }
    return HttpResponse(template.render(context, request))

def email_test(request):
    template = loader.get_template('email_test.html')
    log_ses = request.session.get('User_')
    
    if log_ses is not None:
        login_butt = "Logout"
        login_link = "logout"
        signup_butt = "Profile"
        signup_link = "profile/{{user.uemail}}"
    else:
        login_butt = "Login"
        login_link = "login"
        signup_butt = "Sign up"
        signup_link = "email_test"
    try:
        user= User.objects.get(uemail=log_ses)
        message = "님 환영합니다"
        context = {
            'log_nick':user.unick+message,
            'login_butt':login_butt,
            'login_link':login_link,
            'signup_butt':signup_butt,
            'signup_link':signup_link
        }        
    except:
        message = "로그인 해주세요"
        context = {
            'log_nick':message,
            'login_butt':login_butt,
            'login_link':login_link,
            'signup_butt':signup_butt,
            'signup_link':signup_link
        }
    return HttpResponse(template.render(context, request))

def email_ok(request):
    x= request.POST['email']
    _LENGTH = 6
    number = string.digits
    result = ""
    for i in range(_LENGTH):
        result += random.choice(number)
    email = EmailMessage(
    'Nimbus 인증코드를 확인해주세요', #이메일 제목
    result, #내용
    to=[x], #받는 이메일
    )
    #res_data = {}  
    if User.objects.filter(uemail=x).exists():
        #res_data['error'] = '<!> This email address is already registered.'        
        #return render(request,'email_test.html',res_data) 
        return HttpResponse("<script>alert('"+ '<!> This email address is already registered.' +"');location.href=history.back();</script>")
    
    email.send()
    request.session['email']= x
    request.session['code']= result

    return redirect(reverse('code_check'))

def register_ok(request):
    email = request.POST['email']
    name = request.POST['name']
    nick = request.POST['nick']
    tel = request.POST['tel']
    pwd = request.POST['pwd']
    nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
    image = 'upload/profile/기본프로필.jpg'
    user = User(uemail=email, upwd=pwd, uname=name, unick=nick, utel=tel, urdate=nowDatetime, uimage=image)
    #res_data = {}    
    if User.objects.filter(utel=tel).exists():
        #res_data['error'] = '<!> This phone number is already registered.'        
        #return render(request,'register_test.html',res_data)   
        return HttpResponse("<script>alert('"+ '<!> This telephone number is already registered.' +"');location.href=history.back();</script>")  
    else:
        user.save()
        #return redirect('/login')   
        return HttpResponse("<script>alert('"+ 'Sign up is complete.' +"');location.href='/login';</script>")  

def stream(request,id):
    template = loader.get_template('stream.html')
    log_ses = request.session.get('User_')
    try:
        user= User.objects.get(uemail=log_ses)
    except:
        return HttpResponse("<script>alert('"+ 'Please log in first' +"');location.href=history.back();</script>")
    if log_ses is not None:
        login_butt = "Logout"
        login_link = "logout"
        signup_butt = "Profile"
        signup_link = "profile/{{user.uemail}}"
    else:
        login_butt = "Login"
        login_link = "login"
        signup_butt = "Sign up"
        signup_link = "email_test"
    user = User.objects.get(uemail=log_ses)
    music = Music.objects.get(id=id)
    music.mview += 1
    music.save()
    request.session['id']= id
    musics = Music.objects.filter(mgenre=music.mgenre).order_by('-mrdate').values()
    comments = Comment.objects.filter(mid_id=music.id).order_by('-id')
    #prof= User.objects.get(uemail=comments.uemail)
    # request.session['user']=user.email
    # upl_ses = request.session.get('user')
    
    comment_list = []
    for x in comments:
        dict = {}
        dict['unick'] = User.objects.get(uemail=x.uemail).unick
        dict['uemail'] =User.objects.get(uemail=x.uemail).uemail
        dict['cdesc'] = x.cdesc
        dict['crdate'] = x.crdate
        dict['uimage'] = User.objects.get(uemail=x.uemail).uimage
        comment_list.append(dict)
    
    message = "님 환영합니다"
    context = {
        'user' : user,
        'music' : music,
        'musics': musics,
        'log_nick':user.unick+message,
        'login_butt':login_butt,
        'login_link':login_link,
        'signup_butt':signup_butt,
        'signup_link':signup_link,
        'id':id,
        'comment_list':comment_list
        #'prof':prof,
    }
    return HttpResponse(template.render(context, request))

def comment_ok(request,id):
    comment=request.POST['message']
    #nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
    log_ses = request.session.get('User_')
    user= User.objects.get(uemail=log_ses)
    id = request.session.get('id')
    music = Music.objects.get(id=id)
    nowDatetime = timezone.now().strftime('%Y-%m-%d %H')
    comm=Comment(cdesc=comment, crdate=nowDatetime, mid_id=music.id, uemail=user)
    comm.save()
    return redirect('/stream/'+str(id))

def stream2(request,pid):
    template = loader.get_template('stream2.html')
    log_ses = request.session.get('User_')
    user= User.objects.get(uemail=log_ses)
    id = Playlist.objects.get(id=pid).mid_id
    uemail_id = Playlist.objects.get(id=pid).uemail_id
    pname = Playlist.objects.get(id=pid).pname
    playlists = Playlist.objects.filter(pname=pname, uemail_id=uemail_id).order_by('-id')
    
    playlist_list = []
    for x in playlists:
        dict = {}
        dict['mp3'] = Music.objects.get(id=x.mid_id).mp3
        dict['mphoto'] = Music.objects.get(id=x.mid_id).mphoto
        dict['mtitle'] = Music.objects.get(id=x.mid_id).mtitle
        dict['msinger'] = Music.objects.get(id=x.mid_id).msinger
        dict['id'] = x.mid_id
        dict['pid'] = x.id
        playlist_list.append(dict)
    
    if log_ses is not None:
        login_butt = "Logout"
        login_link = "logout"
        signup_butt = "Profile"
        signup_link = "profile/{{user.uemail}}"
    else:
        login_butt = "Login"
        login_link = "login"
        signup_butt = "Sign up"
        signup_link = "email_test"
    user= User.objects.get(uemail=log_ses)
    music = Music.objects.get(id=id)
    music.mview += 1
    music.save()
    request.session['id']= id
    musics=Music.objects.filter(mgenre=music.mgenre).order_by('-mrdate').values()
    comments = Comment.objects.filter(mid_id=music.id).order_by('-id')
    comment_list = []
    for x in comments:
        dict = {}
        dict['unick'] = User.objects.get(uemail=x.uemail).unick
        dict['uemail'] =User.objects.get(uemail=x.uemail).uemail
        dict['cdesc'] = x.cdesc
        dict['crdate'] = x.crdate
        dict['uimage'] = User.objects.get(uemail=x.uemail).uimage
        comment_list.append(dict)
    #prof= User.objects.get(uemail=comments.uemail)
    # request.session['user']=user.email
    # upl_ses = request.session.get('user')
    message = "님 환영합니다"
    context = {
        'user' : user,
        'music' : music,
        'musics': musics,
        'log_nick':user.unick+message,
        'login_butt':login_butt,
        'login_link':login_link,
        'signup_butt':signup_butt,
        'signup_link':signup_link,
        'playlist_list':playlist_list,
        'comment_list':comment_list,
        'pid':pid,
        'id':id
        #'prof':prof,
    }
    return HttpResponse(template.render(context, request))

def comment_ok2(request,pid):
    comment=request.POST['message']
    #nowDatetime = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
    log_ses = request.session.get('User_')
    user= User.objects.get(uemail=log_ses)
    
    id = request.session.get('id')
    music = Music.objects.get(id=id)
    nowDatetime = timezone.now().strftime('%Y-%m-%d %H')
    comm=Comment(cdesc=comment, crdate=nowDatetime, mid_id=music.id, uemail=user)
    comm.save()
    return redirect('/stream2/'+str(pid))

def code_check(request):
    request.session.get('code')
    template = loader.get_template('code_check.html')
    log_ses = request.session.get('User_')
    if log_ses is not None:
        login_butt = "Logout"
        login_link = "logout"
        signup_butt = "Profile"
        signup_link = "profile/{{user.uemail}}"
    else:
        login_butt = "Login"
        login_link = "login"
        signup_butt = "Sign up"
        signup_link = "email_test"
    try:
        context = {
            'login_butt':login_butt,
            'login_link':login_link,
            'signup_butt':signup_butt,
            'signup_link':signup_link
        }        
    except:
        message = "로그인 해주세요"
        context = {
            'log_nick':message,
            'login_butt':login_butt,
            'login_link':login_link,
            'signup_butt':signup_butt,
            'signup_link':signup_link
        }
    return HttpResponse(template.render(context, request))

def code_check_ok(request):
    code = request.POST['number']
    code_ses = request.session.get('code')
    if code_ses == code:
        del(request.session['code'])
        return redirect(reverse('register'))
        
    else:
        #return redirect(reverse('email_test'))
        return HttpResponse("<script>alert('"+ 'Incorrect code :(' +"');location.href=history.back();</script>")

    
def logout(request):
    if request.session.get('User_'):
        del (request.session['User_'])
        return redirect('/')

def Int(request):
    template = loader.get_template('Int.html')
    log_ses = request.session.get('User_')
    user = User.objects.get(uemail=log_ses)
    context = {
        'user':user,
    }
    return HttpResponse(template.render(context, request))

def Int_ok(request):
    log_ses = request.session.get('User_')
    user = User.objects.get(uemail=log_ses)
    user.udesc = request.POST['text']
    user.save()
    return redirect('/profile/user.uemail')

def profilephoto(request):
    template = loader.get_template('profilephoto.html')
    log_ses = request.session.get('User_')
    user = User.objects.get(uemail=log_ses)
    context = {
        'user':user,
    }
    return HttpResponse(template.render(context, request))

def profilephoto_ok(request):
    log_ses = request.session.get('User_')
    user = User.objects.get(uemail=log_ses)
    # user.uimage = request.FILES["profile_image"]
    try:
        user.uimage = request.FILES["profile_image"]
    except:
        return HttpResponse("<script>alert('"+ 'Please enter a picture' +"');location.href='/profilephoto';</script>")
    user.save()
    return redirect('/profile/user.uemail')

def newPlaylist(request,id):
    template = loader.get_template('newPlaylist.html')
    log_ses = request.session.get('User_')
    
    user= User.objects.get(uemail=log_ses)
    login_butt = "Logout"
    login_link = "logout"
    signup_butt = "Profile"
    signup_link = "profile/{{user.uemail}}"
    
    message = "님 환영합니다"
    context = {
        'log_nick':user.unick+message,
        'login_butt':login_butt,
        'login_link':login_link,
        'signup_butt':signup_butt,
        'signup_link':signup_link,
        'id':id
    }
    return HttpResponse(template.render(context,request))

def newPlaylist_ok(request,id):
    log_ses = request.session.get('User_')
    pname = request.POST['pname']
    playlist=Playlist(pname=pname, mid_id=id, uemail_id=log_ses)
    playlist.save()
    return redirect('../../stream/'+str(id))

def addPlaylist(request,id):
    template = loader.get_template('addPlaylist.html')
    log_ses = request.session.get('User_')
    playlists = Playlist.objects.filter(uemail_id=log_ses).order_by('-id').values()
    count = 0
    pnames = set()
    for x in playlists:
        pnames.add(x['pname'])
        count = count + 1
    if count == 0:
        return redirect('/newPlaylist/'+str(id))
        
    user= User.objects.get(uemail=log_ses)
    login_butt = "Logout"
    login_link = "logout"
    signup_butt = "Profile"
    signup_link = "profile/{{user.uemail}}"
    
    message = "님 환영합니다"
    context = {
        'pnames' : pnames,
        'log_nick':user.unick+message,
        'login_butt':login_butt,
        'login_link':login_link,
        'signup_butt':signup_butt,
        'signup_link':signup_link,
        'id':id
    }
    return HttpResponse(template.render(context,request))

def addPlaylist_ok(request,id):
    log_ses = request.session.get('User_')
    pname = request.POST['playlist']
    playlist=Playlist(pname=pname, mid_id=id, uemail_id=log_ses)
    playlist.save()
    return redirect('../../stream/'+str(id))

def account(request):  
    template = loader.get_template('account.html')
    log_ses = request.session.get('User_')
    
    if log_ses is not None:
        user= User.objects.get(uemail=log_ses)
        login_butt = "Logout"
        login_link = "logout"
        signup_butt = "Profile"
        signup_link = "profile/{{user.uemail}}"
    else:
        login_butt = "Login"
        login_link = "login"
        signup_butt = "Sign up"
        signup_link = "email_test"
        
    user= User.objects.get(uemail=log_ses) 
    name = user.uname #user 세션을 끌어서 사용
    nick = user.unick
    tel = user.utel
    pwd = user.upwd 
    message = "님 환영합니다"
    context = {        
        'email': user.uemail,      
        'name': name,
        'nick': nick,  
        'tel': tel,
        'pwd': pwd,
        'log_nick':user.unick+message,
        'login_butt':login_butt,
        'login_link':login_link,
        'signup_butt':signup_butt,
        'signup_link':signup_link,                    
        }
    return HttpResponse(template.render(context, request))

def account_ok(request):    
    x = request.POST['name']
    y = request.POST['nick']
    z = request.POST['tel']
    p = request.POST['pwd']
    
    log_ses = request.session.get('User_')
    user = User.objects.get(uemail=log_ses) 
    user.uname = x
    user.unick = y
    user.utel = z 
    # res_data = {}

    if user.upwd == p:  
        user.save()
        # return redirect('../profile/{{user.uemail}}')
        return HttpResponse("<script>alert('"+ 'Member information has been modified' +"');location.href='../profile/{{user.uemail}}';</script>")
    else:
        # res_data['error_'] = '<!> Incorrect password'        
        # return render(request,'account.html',res_data) 
        # return redirect('/account')
        return HttpResponse("<script>alert('"+ 'Incorrect password :(' +"');location.href='/account';</script>")
    
def forgot_pwd(request):
    template = loader.get_template('forgot_pwd.html')
    log_ses = request.session.get('User_')
    if log_ses is not None:
        login_butt = "Logout"
        login_link = "logout"
        signup_butt = "Profile"
        signup_link = "profile/{{user.uemail}}"
    else:
        login_butt = "Login"
        login_link = "login"
        signup_butt = "Sign up"
        signup_link = "email_test"
    try:
        user= User.objects.get(uemail=log_ses)
        context = {
            'log_nick':user.unick,
            'login_butt':login_butt,
            'login_link':login_link,
            'signup_butt':signup_butt,
            'signup_link':signup_link
        }        
    except:
        message = "로그인 해주세요"
        context = {
            'log_nick':message,
            'login_butt':login_butt,
            'login_link':login_link,
            'signup_butt':signup_butt,
            'signup_link':signup_link
        }
    return HttpResponse(template.render(context, request))

def forgot_pwd_ok(request):
    x= request.POST['email']
    if not User.objects.filter(uemail=x).exists():
        return HttpResponse("<script>alert('"+ 'The email does not exist :(' +"');location.href=history.back();</script>")
    
    _LENGTH = 6
    number = string.digits
    result = ""
    for i in range(_LENGTH):
        result += random.choice(number)
    email = EmailMessage(
    'Nimbus 인증코드를 확인해주세요', #이메일 제목
    result, #내용
    to=[x], #받는 이메일
    )
    email.send()
    request.session['forgot_email']=x
    request.session['forgot_code']= result
    return redirect(reverse('forgot_code_check'))

def forgot_code_check(request):
    request.session.get('forgot_code')
    template = loader.get_template('forgot_code_check.html')
    log_ses = request.session.get('User_')
    if log_ses is not None:
        login_butt = "Logout"
        login_link = "logout"
        signup_butt = "Profile"
        signup_link = "profile/{{user.uemail}}"
    else:
        login_butt = "Login"
        login_link = "login"
        signup_butt = "Sign up"
        signup_link = "email_test"
    #try:
    #    context = {
    #        'login_butt':login_butt,
    #        'login_link':login_link,
    #        'signup_butt':signup_butt,
    #        'signup_link':signup_link
    #    }        
    #except:
    message = "로그인 해주세요"
    context = {
        'log_nick':message,
        'login_butt':login_butt,
        'login_link':login_link,
        'signup_butt':signup_butt,
        'signup_link':signup_link
    }
    return HttpResponse(template.render(context, request))

def forgot_code_check_ok(request):
    code = request.POST['number']
    code_ses = request.session.get('forgot_code')
    if code_ses == code:
        del(request.session['forgot_code'])
        return redirect(reverse('password_Edit'))
        
    else:
        #return redirect(reverse('forgot_pwd'))
        return HttpResponse("<script>alert('"+ 'Incorrect code :(' +"');location.href=history.back();</script>")
    
def password_Edit(request):
    template = loader.get_template('password_Edit.html')
    login_butt = "Login"
    login_link = "login"
    signup_butt = "Sign up"
    signup_link = "email_test"

    message = "로그인 해주세요"
    context = {
        'log_nick':message,
        'login_butt':login_butt,
        'login_link':login_link,
        'signup_butt':signup_butt,
        'signup_link':signup_link
    }
    return HttpResponse(template.render(context, request))
    
def password_Edit_ok(request):
    email_ses = request.session.get('forgot_email')
    user = User.objects.get(uemail=email_ses)
    user.upwd = request.POST['pwdcheck']
    user.save()
    return redirect('/login')

def delete(request, id):
    music = Music.objects.get(id=id)
    music.delete()
    return redirect('/profile/user.uemail')

def delete2(request, pid):
    playlist = Playlist.objects.get(id=pid)
    playlist.delete()
    return redirect('/profile/user.uemail')

def withdrawal(request):
    template = loader.get_template('withdrawal.html')
    log_ses = request.session.get('User_')
    user = User.objects.get(uemail=log_ses)
    login_butt = "Logout"
    login_link = "logout"
    signup_butt = "Profile"
    signup_link = "profile/{{user.uemail}}"
    message = "님 환영합니다"
    context = {
        'user':user,
        'log_nick':user.unick+message,
        'login_butt':login_butt,
        'login_link':login_link,
        'signup_butt':signup_butt,
        'signup_link':signup_link,
    }
    return HttpResponse(template.render(context, request))

def withdrawal_ok(request):
    log_ses = request.session.get('User_')
    user = User.objects.get(uemail=log_ses)
    print(user.upwd)
    pwd_check = request.POST['pwd']
    if user.upwd == pwd_check:
        user.delete()
        del (request.session['User_'])
        # return redirect('/')
        return HttpResponse("<script>alert('"+ "Membership has been withdrawn" +"');location.href='"+"/"+"';</script>")
    else:
        return HttpResponse("<script>alert('"+ "Incorrect password" +"');location.href='"+"/withdrawal"+"';</script>")
        