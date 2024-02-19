from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.core.mail import send_mail   
from M_Project_1 import settings
from .forms import *

# Create your views here.
def index(request):
    msg = ''
    # Login & sinup
    if request.method == "POST":
        if request.POST.get('signup') == 'signup':
            newdata = signupForm(request.POST)
            if newdata.is_valid():
                # unique username
                username = newdata.cleaned_data.get('username') 
                try:
                    signupModel.objects.get(username=username)
                    msg = 'usename already exists...!!!'
                    print('usename already exists.')
                except signupModel.DoesNotExist:
                    newdata.save()
                    msg = 'Signup Successfully...!!!'
                    print('Signup Successfully.')
            else:
                msg = 'Somethig went wrong, Please try again...!!!'
                print(newdata.errors)
        elif request.POST.get('login') == 'login':
            unm = request.POST['username']
            pas = request.POST['password']

            user = signupModel.objects.filter(username=unm, password=pas)
            uid = signupModel.objects.get(username=unm) # update
            if user: # True
                msg = 'Login Successfully...!!!'
                print('Login Successfully.')
                request.session['user'] = unm
                request.session['userid'] = uid.id  # update
            if user: # True
                return redirect('notes')
            else:
                print('Something went wrong.')
                msg = 'Something went wrong...!!'

    return render(request, 'index.html', {'msg':msg})

def notes(request):
    user = request.session.get('user')
    if request.method == 'POST':
        notesdata = notesForm(request.POST, request.FILES)
        if notesdata.is_valid():
            notesdata.save()
            print('Your notes has neeb submited')
        else:
            print(notesdata.errors)
            
    return render(request, 'notes.html', {'user':user})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        feedbackdata = feedbackForm(request.POST)
        if feedbackdata.is_valid():
            feedbackdata.save()
            print('Your feedback is successfully send.')

            # Email Sent
            sub = request.POST['subject']
            msg = f"Hello Dear, {request.POST['name']}\n\nThanks for your feedback.\nWe received this message from you {request.POST['msg']}\nWe are contact shortly...!\n\nThanks & Regards.\nNotes Team,\n+91 932855315+ | notesapp@gmail.com | www.notesapp.com"
            from_id = settings.EMAIL_HOST_USER
            to_id = [request.POST['email']]
            send_mail(subject=sub, message=msg, from_email=from_id, recipient_list=to_id)

        else:
            print(feedbackdata.errors)

    return render(request, 'contact.html')

def profile_update(request):
    user = request.session.get('user')
    userid = request.session.get('userid')
    uid = signupModel.objects.get(id=userid)
    if request.method == "POST":
        updata = updateForm(request.POST, instance=uid)
        if updata.is_valid():
            updata.save()
            print('Your profile has been updated!.')
            return redirect('notes')

    return render(request,'profile.html', {'user':user,'uid':uid})

def userlogout(request):
    logout(request)
    return redirect('/')