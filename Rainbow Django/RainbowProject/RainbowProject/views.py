import os
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from RainbowApp.models import *
from django.contrib import messages

def adminlogout_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(request, "You are already logged in.")
            return redirect('adminDashboard')
        return view_func(request, *args, **kwargs)
    return wrapper

def studentlogout_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(request, "You are already logged in.")
            return redirect('studentDashboard')
        return view_func(request, *args, **kwargs)
    return wrapper

def homePage(request):
    courseData = CourseInfoModel.objects.all()
    serviceData = ServiceInfoModel.objects.all()
    successStudentData = SuccessfulStudentInfoModel.objects.all()
    galleryData = GalleryImageModel.objects.all()
    contactData = ContactUsModel.objects.all()
    
    context = {
        'courseData': courseData,
        'serviceData': serviceData,
        'successStudentData': successStudentData,
        'galleryData': galleryData,
        'contactData': contactData,
    }
    
    return render(request,'commons/index.html',context)

def aboutUs(request):
    contactData = ContactUsModel.objects.all()
    courseData = CourseInfoModel.objects.all()
    
    context = {
       'contactData' :contactData,
       'courseData': courseData,
    }
    
    return render(request,'commons/aboutus.html',context)

@adminlogout_required
def adminSignUP(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')

        if password == confirmpassword:
            user = CustomUserModel.objects.create_user(username=username,password=password)
            user.email = email
            user.UserType = 'Admin'
            
            user.save()
            return redirect('adminSignin')
        else:
            return redirect('adminSignUP')
    
    return render(request,'myadmin/adminregister.html')

@adminlogout_required
def adminSignin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        if user:
            if user.UserType == 'Admin':
                login(request,user)
                return redirect('adminDashboard')
        else:
            messages.warning(request,'Username and Password not matched.')
            return redirect('adminSignin')
    
    return render(request,'myadmin/adminlogin.html')


def logoutPage(request):
    logout(request)
    return redirect('homePage')

@login_required
def adminDashboard(request):
    studentinfo = StudentInfoModel.objects.all()
    courseinfo = CourseInfoModel.objects.all()
    pendingstudent = AdmissionFormModel.objects.all().count()
    totalbatch = BatchInfoModel.objects.all().count()
    
    courseList = []
    totalStudents = 0
    
    for i in courseinfo:
        studentcount = StudentInfoModel.objects.filter(CourseName=i).count()
        totalStudents+=studentcount
        
        courseList.append(
            {
            'id':i.id,
            'CourseName':i.CourseName,
            'studentcount':studentcount,
            'CourseDuration':i.CourseDuration,
            'CourseFee':i.CourseFee,
            }
        )
    totalCourse = len(courseList)
    context = {
        'studentinfo':studentinfo,
        'courseList':courseList,
        'totalStudents':totalStudents,
        'totalCourse':totalCourse,
        'pendingstudent':pendingstudent,
        'totalbatch':totalbatch,
    }

    return render(request,'myadmin/admindashboard.html',context)

@studentlogout_required
def studentSignin(request):
    if request.method == 'POST':
        studentroll = request.POST.get('studentroll')
        studentpassword = request.POST.get('studentpassword')
        
        user = authenticate(username=studentroll,password=studentpassword)
        if user:
            if user.UserType == 'Student':
                login(request,user)
                return redirect('studentDashboard')
            else:
                return redirect('studentSignin')
        else:
            messages.warning(request,'Username and Password not matched.')
            return redirect('studentSignin')
        
    return render(request,'students/studentlogin.html')

@login_required
def studentDashboard(request):

    return render(request,'students/studentdashboard.html')

#----------------Service-----------------
def servicePage(request):
    serviceData = ServiceInfoModel.objects.all()
    
    context = {
        'serviceData': serviceData,
    }
    
    return render(request,'ourservice/servicepage.html',context)

@login_required
def serviceList(request):
    servicedata = ServiceInfoModel.objects.all()
    context = {
        'servicedata':servicedata,
    }
    return render(request,'ourservice/servicelist.html',context)

@login_required
def addService(request):
    if request.method=='POST':
        servicename = request.POST.get('servicename')
        aboutservice = request.POST.get('aboutservice')
        
        servicedata = ServiceInfoModel(
            ServiceName= servicename,
            AboutService = aboutservice,
        )
        servicedata.save()
        messages.success(request,'Service Successfully Added.')
        return redirect('serviceList')
        
    return render(request,'ourservice/addservice.html')

@login_required
def editService(request,myid):
    servicedata = ServiceInfoModel.objects.get(id=myid)
    
    context = {
        'servicedata':servicedata,
    }
    if request.method=='POST':
        servicename = request.POST.get('servicename')
        aboutservice = request.POST.get('aboutservice')


        servicedata.ServiceName= servicename
        servicedata.AboutService = aboutservice
        servicedata.save()
        messages.success(request,'Service Successfully Updated.')
        return redirect('serviceList')
    
    return render(request,'ourservice/editservice.html',context)    

@login_required
def deleteService(request,myid):
    servicedata = ServiceInfoModel.objects.get(id=myid)
    servicedata.delete()
    messages.success(request,'Service Successfully Deleted.')
    return redirect('serviceList')

#----------------Payment-----------------
@login_required
def paymentList(request):
    studentinfo = StudentInfoModel.objects.all().order_by('-RollNo')
    context = {
        'studentinfo':studentinfo,
    }
    return render(request,'payment/paymentlist.html',context)

@login_required
def updatePayment(request,myid):
    studentpayment = StudentInfoModel.objects.get(id=myid)
    context = {
        'studentpayment':studentpayment,
    }
    if request.method == 'POST':
        newpayment = request.POST.get('newpayment')
        
        prepayment = studentpayment.Payment
        predue = studentpayment.Due
        pay = int(prepayment) + int(newpayment)
        due = int(predue) - int(newpayment)
        
        studentpayment.Payment = pay
        studentpayment.Due = due
        studentpayment.save()
        messages.success(request,'Payment Updated Successfully.')
        return redirect('paymentList')

    return render(request,'payment/updatepayment.html',context)

#------------Gallery-----------------
def galleryPage(request):
    galleryData = GalleryImageModel.objects.all()
    
    context = {
        'galleryData': galleryData,
    }
    
    return render(request,'gallery/gallerypage.html',context)

@login_required
def addGallery(request):
    if request.method == 'POST':
        imagetitle = request.POST.get('imagetitle')
        galleryimage = request.FILES.get('galleryimage')
        
        galleryData = GalleryImageModel(
            ImageTitle=imagetitle,
            GalleryImage=galleryimage
        )
        galleryData.save()
        messages.success(request,'Image Successfully Added.')
        return redirect('galleryList')      
        
    return render(request,'gallery/addgallery.html')

@login_required
def galleryList(request):
    galleryData = GalleryImageModel.objects.all()
    context = {
        'galleryData':galleryData
    }
    return render(request,'gallery/gallerylist.html',context)

@login_required
def editImage(request,myid):
    galleryData = GalleryImageModel.objects.get(id=myid)
    context = {
        'galleryData':galleryData
    }
    if request.method == 'POST':
        imagetitle = request.POST.get('imagetitle')
        galleryimage = request.FILES.get('galleryimage')
        
        galleryData.ImageTitle=imagetitle
        if galleryimage:
            galleryData.GalleryImage=galleryimage
        galleryData.save()
        messages.success(request,'Image Successfully Updated.')
        return redirect('galleryList')
    return render(request,'gallery/editgallery.html',context)

@login_required
def deleteImage(request,myid):
    galleryData = GalleryImageModel.objects.get(id=myid)
    img= galleryData.GalleryImage
    os.remove(img.path)
    galleryData.delete()
    messages.success(request,'Image Successfully Deleted.')
    return redirect('galleryList')
    
#------------Contact------------
def contactUsPage(request):
    contactData = ContactUsModel.objects.all()
    context = {
        'contactData':contactData,
    }
    
    return render(request,'contact/contactus.html',context)

@login_required
def contactList(request):
    contactData = ContactUsModel.objects.all()
    
    context = {
        'contactData':contactData,
    }
    return render(request,'contact/contactlist.html',context)

@login_required
def addContact(request):
    if request.method=='POST':
        address=request.POST.get('address')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        facebooklink=request.POST.get('facebooklink')
        googlemap=request.POST.get('googlemap')
        
        contactData = ContactUsModel(
            Address = address,
            Email = email,
            Mobile = mobile,
            Facebook = facebooklink,
            MapLink = googlemap,
        )
        contactData.save()
        messages.success(request,'Contact Successfully Added.')
        return redirect('contactList')
    return render(request,'contact/addcontact.html')

@login_required
def deleteContact(request,myid):
    contactData = ContactUsModel.objects.get(id=myid)
    contactData.delete()
    return redirect('contactList')

@login_required
def editContact(request,myid):
    contactData = ContactUsModel.objects.get(id=myid)
    context = {
        'contactData':contactData,
    }
    
    if request.method=='POST':
        address=request.POST.get('address')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        facebooklink=request.POST.get('facebooklink')
        googlemap=request.POST.get('googlemap')
        
        contactData.Address = address
        contactData.Email = email
        contactData.Mobile = mobile
        contactData.Facebook = facebooklink
        contactData.MapLink = googlemap
        
        contactData.save()
        messages.success(request,'Contact Successfully Updated.')
        return redirect('contactList')
    
    return render(request,'contact/editcontact.html',context)