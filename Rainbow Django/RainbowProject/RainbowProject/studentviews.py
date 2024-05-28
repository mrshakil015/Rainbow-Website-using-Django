from django.shortcuts import redirect,render
from RainbowApp.models import *
from django.contrib import messages

def addStudentPage(request):
    if request.method == 'POST':
        fullname=request.POST.get('fullname')
        fathername=request.POST.get('fathername')
        mothername=request.POST.get('mothername')
        gender=request.POST.get('gender')
        dateofbirth=request.POST.get('dateofbirth')
        religion=request.POST.get('religion')
        mobile=request.POST.get('mobile')
        emergencymobile=request.POST.get('emergencymobile')
        email=request.POST.get('email')
        studentImage=request.FILES.get('studentImage')
        presentaddress=request.POST.get('presentaddress')
        permanentaddress=request.POST.get('permanentaddress')
        
        rollno=request.POST.get('rollno')
        coursename=request.POST.get('coursename')
        batch=request.POST.get('batch')
        section=request.POST.get('section')
        coursefee=request.POST.get('coursefee')
        payment=request.POST.get('payment')
        
        due = int(coursefee) - int(payment)
        
        if CustomUserModel.objects.filter(username=rollno).exists():
            messages.warning(request,'User already exist.')
           
        else:            
            studentuser = CustomUserModel.objects.create_user(
                username = rollno,
                email = email,
                password = mobile,
                UserType = 'Student',
            )
            studentuser.save()
            
            studentData = StudentInfoModel(
                user=studentuser,
                StudentName=fullname,
                FatherName=fathername,
                MotherName=mothername,
                Gender=gender,
                DOB=dateofbirth,
                Religion=religion,
                Mobile=mobile,
                EmergencyMobile=emergencymobile,
                StudentPhoto=studentImage,
                PresentAddress=presentaddress,
                PermanentAddress=permanentaddress,
                
                RollNo=rollno,
                CourseName=coursename,
                Batch=batch,
                Section=section,
                CourseFee=coursefee,
                Payment=payment,
                Due=due,
            )
            studentData.save()
            messages.success(request,'Successfully Created.')
            return redirect('studentList') 
    
    return render(request,'students/addstudent.html')
    
def studentList(request):
    studentinfo = StudentInfoModel.objects.all()
    
    context = {
        'studentinfo':studentinfo,
    }
    return render(request,'students/studentlist.html',context)