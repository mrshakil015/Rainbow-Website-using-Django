from django.shortcuts import render, redirect
from RainbowApp.models import *
from django.contrib import messages
from django.db import transaction

def addBatch(request):
    if request.method=='POST':
        batchno=request.POST.get('batchno')
        schedule=request.POST.get('schedule')
        section=request.POST.get('section')
        status=request.POST.get('status')
        batchstart=request.POST.get('batchstart')
        
        batchData = BatchInfoModel(
            BatchNo=batchno,
            Batchschedule=schedule,
            Section=section,
            Status=status,
            BatchStart=batchstart,
        )
        batchData.save()
        messages.success(request,'Batch Create Successfully')
        return redirect('batchList')
    
    return render(request,'mybatch/addbatch.html')


def batchList(request):
    batchData = BatchInfoModel.objects.all()
    batch_data_with_counts = []
    for batch in batchData:
        student_count = StudentInfoModel.objects.filter(BatchNo=batch).count()
        batch_data_with_counts.append((batch, student_count))
        
    context = {
        'batch_data_with_counts': batch_data_with_counts
    }

    return render(request, 'mybatch/batchlist.html', context)


    
def deleteBatch(request,myid):
    batchData = BatchInfoModel.objects.get(id=myid)
    batchData.delete()
    messages.success(request,'Batch Delete Successfully')
    return redirect('batchList')


def editBatch(request, myid):
    batchData = BatchInfoModel.objects.get(id=myid)
    batch_Date = batchData.BatchStart.isoformat() if batchData.BatchStart else ''
    context = {
       'batchData': batchData,
       'batch_Date': batch_Date,
    } 
    if request.method == 'POST':
        batchno = request.POST.get('batchno')
        schedule = request.POST.get('schedule')
        section = request.POST.get('section')
        status = request.POST.get('status')
        batchstart = request.POST.get('batchstart')
        
        with transaction.atomic():
            # Update BatchInfoModel instance
            batchData.BatchNo = batchno
            batchData.Batchschedule = schedule
            batchData.Section = section
            batchData.Status = status
            batchData.BatchStart = batchstart
            batchData.save()

            # Update related StudentInfoModel instances
            related_students = StudentInfoModel.objects.filter(BatchNo=batchData)
            related_students.update(Batchschedule=schedule, Section=section)

        messages.success(request, 'Batch Updated Successfully')
        return redirect('batchList')
    
    return render(request, 'mybatch/editbatch.html', context)

def viewSingleBatch(request,batchno):
    studentData = StudentInfoModel.objects.filter(BatchNo__BatchNo=batchno)
    batchData = BatchInfoModel.objects.get(BatchNo=batchno)
    context = {
        'studentData':studentData,
        'batchData':batchData,
    }
    print("BatchData : ",studentData)
    
    return render(request,'mybatch/viewbatch.html',context)

def batchPrint(request, batchno):
    studentData = StudentInfoModel.objects.filter(BatchNo__BatchNo=batchno)
    batchData = BatchInfoModel.objects.get(BatchNo=batchno)
    context = {
        'studentData':studentData,
        'batchData':batchData,
    }
    print("BatchData : ",studentData)
    
    return render(request,'mybatch/batchPrint.html',context)

def attendenceSheetPrint(request, batchno):
    studentData = StudentInfoModel.objects.filter(BatchNo__BatchNo=batchno)
    batchData = BatchInfoModel.objects.get(BatchNo=batchno)
    context = {
        'studentData':studentData,
        'batchData':batchData,
    }
    print("BatchData : ",studentData)
    
    return render(request,'mybatch/attendance_sheet_print.html',context)