from django.shortcuts import render
from .models import *
import random
# Create your views here.


def index(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        if uid.role == "chairmen":
            cid = chairmen.objects.get(user_id=uid)
            context = {

                'uid' : uid,
                'cid' : cid
            }
            return render(request, "myapp/index.html",context)
    else:
        return render(request, "myapp/login.html")
   

def login(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        if uid.role == "chairmen":
            cid = chairmen.objects.get(user_id=uid)
            context = {
                'uid' : uid,
                'cid' : cid
            }
            return render(request, "myapp/index.html",context)

    else:
        if request.POST:
            email = request.POST['emailname']
            password = request.POST['passwordname']

            uid = User.objects.get(email = email)
            if uid.password == password:
                if uid.role == 'chairmen':
                    cid = chairmen.objects.get(user_id = uid)
                    request.session['email'] = uid.email
                    context = {
                        'uid' : uid,
                        'cid' : cid
                    }
                    return render(request, "myapp/index.html",context)
                    
                else:
                    return render(request, "myapp/login.html") 
            else:
                e_msg = 'invalid password'
                context = {
                    'e_msg' : e_msg
                }
                return render(request, "myapp/login.html",context)
                
    
        else:
            return render(request, "myapp/login.html")

def logout(request):
    if 'email' in request.session:
        del request.session['email']
        return render(request, "myapp/login.html")
    else:
        return render(request, "myapp/login.html")

def profile(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        if uid.role == "chairmen":
            cid = chairmen.objects.get(user_id=uid)
            context = {
                'uid' : uid,
                'cid' : cid
            }
            return render(request, "myapp/profile.html",context)

def add_member(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        if uid.role == "chairmen":
            cid = chairmen.objects.get(user_id=uid)
            if request.POST:
                email = request.POST['email']
                firstname = request.POST['firstname']
                lastname = request.POST['lastname']
                contact_no =request.POST['contact_no']
                family_member = request.POST['family_member']
                job_location =request.POST['job_location']
                block_no  = request.POST['block_no']
                house_no = request.POST['house_no']
                
                l1 = ['ad785','jkash3','klj#45','k544#','dkj#54','djk221#']
                password = random.choice(l1) + email[3:6] + str(contact_no[3:8])

                uid = User.objects.create(email=email,password=password,role='member')
                mid = Member.objects.create(user_id=uid,firstname=firstname,
                                            lastname=lastname,
                                            contact_no=contact_no,
                                            family_member=family_member,
                                            job_location=job_location,
                                            block_no=block_no,
                                            house_no=house_no,
                                            
                                            )                
                print("---------->email",email)

                context = {
                'uid' : uid,
                'cid' : cid,
                'mid' : mid,
                's_msg' : "successfuly member create"
                }
                return render(request, "myapp/add_member.html",context)

            else:
                context = {
                'uid' : uid,
                'cid' : cid
            }
            return render(request, "myapp/add_member.html",context)

def change_password(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        if uid.role == "chairmen":
            cid = chairmen.objects.get(user_id=uid)
            
            if request.POST:
                current_password = request.POST['current_password']
                new_password = request.POST['new_password']
                if uid.password == current_password:
                    uid.password = new_password
                    uid.save()#update

                context = {
                    'uid' : uid,
                    'cid' : cid
                }
                return render(request, "myapp/profile.html",context)
        else:
            context = {
                'uid' : uid,
                'cid' : cid
            }
            return render(request, "myapp/profile.html",context)

def update_profile_chairmen(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        if uid.role == "chairmen":
            cid = chairmen.objects.get(user_id=uid)
            
            
            if request.POST:
               username = request.POST['username']
               if 'picture' in request.FILES:
                   cid.pic = request.FILES['picture']
                   cid.save()
               cid.username = username
               cid.save()

               context = {
                    'uid' : uid,
                    'cid' : cid
               }
               return render(request, "myapp/profile.html",context)
        else:
            context = {
                'uid' : uid,
                'cid' : cid
            }
            return render(request, "myapp/profile.html",context)

def view_member(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        if uid.role == "chairmen":
            cid = chairmen.objects.get(user_id=uid)
            mall = Member.objects.all()
            context = {
                'uid' : uid,
                'cid' : cid,
                'mall': mall, 
            }
            return render(request, "myapp/view_member.html",context)
        else:
            pass

def add_notice(request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session["email"])
        if uid.role == 'chairmen':
            cid = chairmen.objects.get(user_id=uid)
            if request.POST:
                title = request.POST['title']
                descriptions = request.POST['descriptions']
                
                nid =Notice.objects.create(title=title,descriptions=descriptions)
                context ={
                    'uid' : uid,
                    'cid' : cid,
                    'nid':nid,
                    'n_msg' : "successfully add_notice",
                }
                return render(request, "myapp/add_notice.html",context)
            else:
                context ={
                    'uid' : uid,
                    'cid' : cid
                }
                return render(request, "myapp/add_notice.html",context)

def view_notice(request):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        if uid.role == "chairmen":
            cid = chairmen.objects.get(user_id=uid)

            nall = Notice.objects.all()
            context = {
                'uid' : uid,
                'cid' : cid,
                'nall': nall, 
            }
            return render(request, "myapp/view_notice.html",context)
        else:
            pass



  




    
        

