from django.shortcuts import render
from .models import *
import random

# Create your views here.

def index(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'Chairmen':
            cid = Chairmen.objects.get(urser_id=uid)
            context ={
                'uid' : uid,
                'cid' : cid,
            }
            return render(request, "myapp/index.html",context)
    else:
        return render(request, "myapp/login.html")

def login(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'Chairmen':
            cid = Chairmen.objects.get(urser_id=uid)
            context ={
                'uid' : uid,
                'cid' : cid,
            }
            return render(request, "myapp/index.html",context)
        else:
            return render(request, "myapp/login.html",context)
    else:
        if request.POST:
            email = request.POST['email']
            password = request.POST['password']

            uid = User.objects.get(email=email)
            if uid.password == password:
                if uid.role == 'Chairmen':
                    cid = Chairmen.objects.get(urser_id=uid)
                    request.session['email'] = uid.email
                    context ={

                        'uid' : uid,
                        'cid' : cid,
                    }
                    return render(request, "myapp/index.html",context)
            else:
                s_msg = "INVALID PASSWORD...."
                context = {
                    's_msg' : s_msg,
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
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'Chairmen':
            cid = Chairmen.objects.get(urser_id=uid)
            context ={
                'uid' : uid,
                'cid' : cid,
            }
            return render(request, "myapp/profile.html",context)
    else:
        return render(request, "myapp/index.html")

def change_password(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'Chairmen':
            cid = Chairmen.objects.get(urser_id=uid)
            
            if request.POST:
                current_password = request.POST['current_password']
                new_password = request.POST['new_password']
                
                uid.password =  current_password
                uid.password = new_password
                uid.save()

            context ={
                'uid' : uid,
                'cid' : cid,
            }
            return render(request, "myapp/profile.html",context)
    else:
        return render(request, "myapp/index.html")

def change_username(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'Chairmen':
            cid = Chairmen.objects.get(urser_id=uid)
            
            if request.POST:
                username = request.POST['username']
                if  "picture" in request.FILES:
                    cid.pic = request.FILES['picture']
                    cid.save()

                cid.username = username
                cid.save()
                
            context ={
                'uid' : uid,
                'cid' : cid,
            }
            return render(request, "myapp/profile.html",context)
    else:
        return render(request, "myapp/index.html")

def add_member(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'Chairmen':
            cid = Chairmen.objects.get(urser_id=uid)
            if request.POST:
                email         = request.POST['email']
                firstname     = request.POST['firstname']
                lastname      = request.POST['lastname']
                contact_no    = request.POST['contact_no']
                family_member = request.POST['family_member']
                occupation    = request.POST['occupation']
                block_no      = request.POST['block_no']
                house_no      = request.POST['house_no']              
                
                l1 = ['#12ad','#454as','askj#12','#klj12', 'lkj#145']
                password = random.choice(l1) + email[3:6] + str(contact_no[3:8])

                uid = User.objects.create(email=email,password=password,role='member')
                mid = Member.objects.create(urser_id=uid,
                                            firstname=firstname,
                                            lastname=lastname,
                                            contact_no=contact_no,
                                            family_member=family_member,
                                            occupation=occupation,
                                            block_no=block_no,
                                            house_no=house_no,     
                )
                context ={

                    'uid' : uid,
                    'cid' : cid,
                    's_msg' : "successfully add_member......."
                }
                return render(request, "myapp/add_member.html",context)
 
            else:
                context ={

                    'uid' : uid,
                    'cid' : cid,
                }
                return render(request, "myapp/add_member.html",context)
    else:
        return render(request, "myapp/index.html")

def All_member(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'Chairmen':
            cid = Chairmen.objects.get(urser_id=uid)
            
            mall = Member.objects.all()
            context ={

                    'uid' : uid,
                    'cid' : cid,
                    'mall' : mall,
            }
            return render(request, "myapp/All_member.html",context)



def add_notice(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'Chairmen':
            cid = Chairmen.objects.get(urser_id=uid)
            if request.POST:
                titel = request.POST['titel']
                descrition = request.POST['descrition']
             

                nid = Notice.objects.create(titel=titel,descrition=descrition)
                context ={

                    'uid' : uid,
                    'cid' : cid,
                    'nid' : nid,
                    'n_msg' : "successfully add_notice......."
                }
                return render(request, "myapp/add_notice.html",context)
 
            else:
                context ={

                    'uid' : uid,
                    'cid' : cid,
                }
                return render(request, "myapp/add_notice.html",context)
    else:
        return render(request, "myapp/index.html")


    


def all_notice(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'Chairmen':
            cid = Chairmen.objects.get(urser_id=uid)
            
            nall = Notice.objects.all()
            context ={

                    'uid' : uid,
                    'cid' : cid,
                    'nall' : nall,
            }
            return render(request, "myapp/all_notice.html",context)


    



  


          
    

