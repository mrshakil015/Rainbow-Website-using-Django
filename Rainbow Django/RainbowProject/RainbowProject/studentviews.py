import os
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from RainbowApp.models import *
from django.contrib import messages

@login_required
def addStudentPage(request):
    courseData = CourseInfoModel.objects.all()
    batchData = BatchInfoModel.objects.all()
    
    context = {
        'courseData':courseData,
        'batchData':batchData,
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
        
        print("First name of image: ",studentImage)
        
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
            batchinfo = BatchInfoModel.objects.get(BatchNo=batchno)
            
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
                BatchNo=batchinfo,
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

@login_required
def editStudent(request,myid):
    courseData = CourseInfoModel.objects.all()   
    batchData = BatchInfoModel.objects.all()
    studentdata = StudentInfoModel.objects.get(id=myid)
    date_of_birth = studentdata.DOB.isoformat() if studentdata.DOB else ''
    context = {
        'studentdata':studentdata,
        'courseData':courseData,
        'date_of_birth': date_of_birth,
        'batchData': batchData,
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
        courseinfo = CourseInfoModel.objects.get(CourseName=coursename)
        batchinfo = BatchInfoModel.objects.get(BatchNo=batchno)
        
        
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
        studentdata.BatchNo=batchinfo
        if batchschedule != 'Select Batch Schedule':
            studentdata.Batchschedule=batchschedule
        if section != 'Select Section':
            studentdata.Section=section
        studentdata.CourseFee=coursefee
        studentdata.Payment=payment
        studentdata.Due=due
        
        CustomUserModel.objects.filter(username = rollno).update(
            email=email
        )
        studentdata.save()
        messages.success(request,'Successfully Updated.')
        return redirect('studentList')
    
    return render(request,'students/editstudent.html',context)

@login_required
def deleteStudent(request,user):
   studentdata = CustomUserModel.objects.get(username=user)
   img= studentdata.studentuser.StudentPhoto
   os.remove(img.path)
   studentdata.delete()
   messages.success(request,'Student Deleted Done.')
   return redirect('studentList')

@login_required
def admitedcourseInfo(request):
    current_batch = request.user
    studentData=StudentInfoModel.objects.get(user=current_batch)
    batchData = BatchInfoModel.objects.get(BatchNo=studentData.BatchNo)
    print("Current batch, ",batchData.Status)
    context ={
        'batchData':batchData,
    }
    
    return render(request,'students/admitedcourseinfo.html',context)

@login_required
def admitedcoursePaymentInfo(request):
    
    return render(request,'students/admitedcoursepaymentinfo.html')

@login_required    
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
        messages.success(request,'Thanks for Registraion.')
        return redirect('admissionformPage')
        
    return render(request,'students/admissionform.html',context)

@login_required
def pendingStudentList(request):
    pendingstudentdata = AdmissionFormModel.objects.all()

    context = {
        'pendingstudentdata':pendingstudentdata,
    }
    
    return render(request,'students/pendingstudentlist.html',context)

@login_required
def editPendingStudent(request,myid):
    pendingstudentdata = AdmissionFormModel.objects.get(id=myid)
    batchData = BatchInfoModel.objects.all()
    courseData = CourseInfoModel.objects.all()   
    date_of_birth = pendingstudentdata.DOB.isoformat() if pendingstudentdata.DOB else ''
    for batch in batchData:
        print("Batch data is: ",batch.Batchschedule)
    context = {
        'pendingstudentdata':pendingstudentdata,
        'courseData':courseData,
        'batchData':batchData,
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
        preimg=request.POST.get('preimg')
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
            batchinfo = BatchInfoModel.objects.get(BatchNo=batchno)
            
            if studentImage:
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
                    BatchNo=batchinfo,
                    Batchschedule=batchschedule,
                    Section=section,
                    CourseFee=coursefee,
                    Payment=payment,
                    Due=due,
                )
            else:
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
                    StudentPhoto=preimg,
                    PresentAddress=presentaddress,
                    PermanentAddress=permanentaddress,
                    
                    RollNo=rollno,
                    CourseName=courseinfo,
                    BatchNo=batchinfo,
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

@login_required
def deletePendingStudent(request,myid):
   pendingstudentdata = AdmissionFormModel.objects.get(id=myid)
   img= pendingstudentdata.StudentPhoto
   os.remove(img.path)
   
   pendingstudentdata.delete()
   messages.success(request,'Student Deleted Done.')
   return redirect('pendingStudentList')

#-----------------Successfull Students-----------------
@login_required
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

@login_required
def successStudentList(request):
    studentData = SuccessfulStudentInfoModel.objects.all()
    
    context = {
        'studentData':studentData
    }
    
    return render(request,'students/success_student_list.html',context)

@login_required
def deleteSuccessStudent(request,myid):
    studentData = SuccessfulStudentInfoModel.objects.get(id=myid)
    img = studentData.StudentImage
    os.remove(img.path)
    studentData.delete()
    messages.success(request,'Delete Successfully.') 
    return redirect('successStudentList')

@login_required
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

@login_required
def printAdmissionform(request,myid):
    courseData = CourseInfoModel.objects.all()   
    batchData = BatchInfoModel.objects.all()
    studentdata = StudentInfoModel.objects.get(id=myid)
    date_of_birth = studentdata.DOB.isoformat() if studentdata.DOB else ''
    context = {
        'studentdata':studentdata,
        'courseData':courseData,
        'date_of_birth': date_of_birth,
        'batchData': batchData,
    }
    
    return render(request,'students/print_admissionform.html',context)

@login_required
def downloadAdmissionform(request,myid):
    courseData = CourseInfoModel.objects.all()   
    batchData = BatchInfoModel.objects.all()
    studentdata = StudentInfoModel.objects.get(id=myid)
    date_of_birth = studentdata.DOB.isoformat() if studentdata.DOB else ''
    context = {
        'studentdata':studentdata,
        'courseData':courseData,
        'date_of_birth': date_of_birth,
        'batchData': batchData,
    }
    
    return render(request,'students/print_admissionform.html',context)


#-------------------Exam Result-----------------------
def examList(request):
    current_user = request.user
    current_userType = request.user.UserType
    if current_userType == 'Admin':
        examdata = ExamResultModel.objects.all()
    else:
        examdata = ExamResultModel.objects.filter(Candidate=current_user)
    
    context = {
        'examdata': examdata
    }
    
    
    return render(request,'examresult/examlist.html',context)

def addExamResult(request):
    if request.method == 'POST':
        studentroll= request.POST.get('studentroll')
        examtitle= request.POST.get('examtitle')
        
        obtainedmcq= request.POST.get('obtainedmcq')
        totalmcq= request.POST.get('totalmcq')
        obtainedwritten= request.POST.get('obtainedwritten')
        totalwritten= request.POST.get('totalwritten')
        obtainedpractical= request.POST.get('obtainedpractical')
        totalpractical= request.POST.get('totalpractical')
        examdate= request.POST.get('examdate')
        
        obtaintotalmarks= int(obtainedmcq) + int(obtainedwritten) + int(obtainedpractical)
        totalexamark= int(totalmcq) + int(totalwritten) + int(totalpractical)
        student = CustomUserModel.objects.get(username=studentroll)
        
        examdata = ExamResultModel.objects.create(
            Candidate=student,
            ExamTitle = examtitle,
            
            ObtainMCQ = obtainedmcq,
            ObtainWritten = obtainedwritten,
            ObtainPracticle = obtainedpractical,
            ObtainTotalMark = obtaintotalmarks,
            TotalMCQ = totalmcq,
            TotalWritten = totalwritten,
            TotalPracticle = totalpractical,
            TotalExamMark = totalexamark,
            ExamDate = examdate,
        )
        examdata.save()
        messages.success(request,'Exam Result Added')
        return redirect('examList')
    
    return render(request,'examresult/addexamresult.html')