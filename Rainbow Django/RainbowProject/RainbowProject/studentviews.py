from django.shortcuts import redirect,render
from RainbowApp.models import *
from django.contrib import messages

def addStudentPage(request):
    
    courseData = CourseInfoModel.objects.all()
    
    context = {
        'courseData':courseData
    }
    
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
        batchno=request.POST.get('batchno')
        batchschedule=request.POST.get('batchschedule')
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
            
            courseinfo = CourseInfoModel.objects.get(CourseName=coursename)
            
            studentData = StudentInfoModel.objects.create(
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
                CourseName=courseinfo,
                BatchNo=batchno,
                Batchschedule=batchschedule,
                Section=section,
                CourseFee=coursefee,
                Payment=payment,
                Due=due,
            )
            studentData.save()
            
            messages.success(request,'Successfully Created.')
            return redirect('studentList') 
    
    return render(request,'students/addstudent.html',context)

def editStudent(request,myid):
    courseData = CourseInfoModel.objects.all()   
    studentdata = StudentInfoModel.objects.get(id=myid)
    date_of_birth = studentdata.DOB.isoformat() if studentdata.DOB else ''
    context = {
        'studentdata':studentdata,
        'courseData':courseData,
        'date_of_birth': date_of_birth,
    }
    
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
        print("Image path: ",studentImage)
        presentaddress=request.POST.get('presentaddress')
        permanentaddress=request.POST.get('permanentaddress')
        
        rollno=request.POST.get('rollno')
        coursename=request.POST.get('coursename')
        batchno=request.POST.get('batchno')
        batchschedule=request.POST.get('batchschedule')
        section=request.POST.get('section')
        coursefee=request.POST.get('coursefee')
        payment=request.POST.get('payment')
        
        due = int(coursefee) - int(payment)
        courseinfo = CourseInfoModel.objects.get(CourseName=coursename)

        studentdata.StudentName=fullname
        studentdata.FatherName=fathername
        studentdata.MotherName=mothername
        studentdata.Gender=gender
        studentdata.DOB=dateofbirth
        studentdata.Religion=religion
        studentdata.Mobile=mobile
        studentdata.EmergencyMobile=emergencymobile
        if studentImage:
            studentdata.StudentPhoto=studentImage
        studentdata.PresentAddress=presentaddress
        studentdata.PermanentAddress=permanentaddress
        
        studentdata.RollNo=rollno
        studentdata.CourseName=courseinfo
        studentdata.BatchNo=batchno
        studentdata.Batchschedule=batchschedule
        studentdata.Section=section
        studentdata.CourseFee=coursefee
        studentdata.Payment=payment
        studentdata.Due=due
        
        studentdata.save()
        messages.success(request,'Successfully Updated.')
        return redirect('studentList')
    
    return render(request,'students/editstudent.html',context)

def deleteStudent(request,user):
   studentdata = CustomUserModel.objects.get(username=user)
   studentdata.delete()
   messages.success(request,'Student Deleted Done.')
   return redirect('studentList')

def admitedcourseInfo(request):
    
    return render(request,'students/admitedcourseinfo.html')

def admitedcoursePaymentInfo(request):
    
    return render(request,'students/admitedcoursepaymentinfo.html')
    
def studentList(request):
    studentinfo = StudentInfoModel.objects.all()


    context = {
        'studentinfo':studentinfo,
    }
    return render(request,'students/studentlist.html',context)


def admissionformPage(request):
    
    courseData = CourseInfoModel.objects.all()


    context = {
        'courseData':courseData,
    }
    
    if request.method == 'POST':
        coursename = request.POST.get('coursename')
        studentname = request.POST.get('studentname')
        fathername = request.POST.get('fathername')
        mothername = request.POST.get('mothername')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        studentphoto = request.FILES.get('studentphoto')
        
        courseinfo = CourseInfoModel.objects.get(CourseName=coursename)
        
        admissiondata = AdmissionFormModel(
            CourseName=courseinfo,
            StudentName=studentname,
            FatherName=fathername,
            MotherName=mothername,
            DOB=dob,
            Gender=gender,
            email=email,
            Mobile=mobile,
            Address=address,
            StudentPhoto=studentphoto,
        )
        admissiondata.save()
        return redirect('homePage')
        
    return render(request,'students/admissionform.html',context)

def pendingStudentList(request):
    pendingstudentdata = AdmissionFormModel.objects.all()
    
    
    context = {
        'pendingstudentdata':pendingstudentdata,
    }
    
    return render(request,'students/pendingstudentlist.html',context)

def editPendingStudent(request,myid):
    pendingstudentdata = AdmissionFormModel.objects.get(id=myid)
    courseData = CourseInfoModel.objects.all()   
    date_of_birth = pendingstudentdata.DOB.isoformat() if pendingstudentdata.DOB else ''
    
    context = {
        'pendingstudentdata':pendingstudentdata,
        'courseData':courseData,
        'date_of_birth':date_of_birth,
    }
    
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
        batchno=request.POST.get('batchno')
        batchschedule=request.POST.get('batchschedule')
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
            courseinfo = CourseInfoModel.objects.get(CourseName=coursename)
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
                CourseName=courseinfo,
                BatchNo=batchno,
                Batchschedule=batchschedule,
                Section=section,
                CourseFee=coursefee,
                Payment=payment,
                Due=due,
            )
            studentData.save()
            
            pendingstudentdata.delete()
            messages.success(request,'Successfully Created.')
            return redirect('studentList') 
    
    return render(request,'students/editpendingstudent.html',context)


def admissionPage(request):
    student_info=StudentInfoModel.objects.get(RollNo=21)
    context = {
        'student_info':student_info,
    }
    return render(request,'commons/test.html',context)



#-----------------Successfull Students-----------------
def addSuccessfulStudent(request):
    if request.method == 'POST':
        studentname=request.POST.get('studentname')
        jobplace=request.POST.get('jobplace')
        designation=request.POST.get('designation')
        studentImage=request.FILES.get('studentImage')
        
        studentData = SuccessfulStudentInfoModel(
            StudentName=studentname,
            StudentDesignation=jobplace,
            StudentInstitute=designation,
            StudentImage=studentImage,
        )
        studentData.save()
        messages.success(request,'Successfully Created.') 
        return redirect('successStudentList')
    return render(request,'students/addsuccessstudent.html')

def successStudentList(request):
    studentData = SuccessfulStudentInfoModel.objects.all()
    
    context = {
        'studentData':studentData
    }
    
    return render(request,'students/success_student_list.html',context)

def deleteSuccessStudent(request,myid):
    studentData = SuccessfulStudentInfoModel.objects.get(id=myid)
    studentData.delete()
    messages.success(request,'Delete Successfully.') 
    return redirect('successStudentList')

def editSuccessStudent(request,myid):
    studentData = SuccessfulStudentInfoModel.objects.get(id=myid)
    context = {
        'studentData':studentData
    }
    
    if request.method=='POST':
        studentname=request.POST.get('studentname')
        jobplace=request.POST.get('jobplace')
        designation=request.POST.get('designation')
        studentImage=request.FILES.get('studentImage')
        
        studentData.StudentName = studentname
        studentData.StudentInstitute = jobplace
        studentData.StudentDesignation = designation
        if studentImage:
            studentData.StudentImage = studentImage
        
        studentData.save()
        messages.success(request,'Updated Successfully.')
        return redirect('successStudentList')
    
    return render(request,'students/success_student_edit.html',context)