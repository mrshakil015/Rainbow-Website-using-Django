## Add Options Name from Model
```python
    courseData = CourseInfoModel.objects.all()
    
    context = {
        'courseData':courseData,
    }
```

```html
<div class="form-group">
<label>Course Name</label>
<select name="coursename" class="form-control">
    <option>Select Course</option>                              
    {% for i in courseData %}
    <option value="{{i.CourseName}}">{{i.CourseName}}</option>
    {% endfor %}
</select>
</div>
```

## To Limit No of Options:
```html
<select name="coursename" class="form-control">
    <option>Select Course</option>                              
    {% for i in courseData|slice:":10" %}
    <option value="{{i.CourseName}}">{{i.CourseName}}</option>
    {% endfor %}
</select>
```


## Based on one field, automatically change the another field

```html
<div class="col-12 col-sm-6">
<div class="form-group">
    <label>Batch No</label>
    <select name="batchno" id="batchno" class="form-control">
        <option>Select BatchNo</option>                              
        {% for i in batchData|slice:":10" %}
        
        {% if i.Status == 'Running' %}
        <option value="{{i.BatchNo}}" data-schedule="{{ i.Batchschedule }}">{{i.BatchNo}}</option>
        {% endif %}
            
        
        {% endfor %}
    </select>
</div>
</div>
<div class="col-12 col-sm-6">
<div class="form-group">
    <label>Batch Schedule</label>
    <select name="batchschedule" id="batchschedule" class="form-control">
        <option>Select Batch Schedule</option>
        <!-- Options will be populated dynamically -->
    </select>
</div>
</div>

<script>
document.getElementById('batchno').addEventListener('change', function() {
    var selectedOption = this.options[this.selectedIndex];
    var schedule = selectedOption.getAttribute('data-schedule');
    
    var batchScheduleSelect = document.getElementById('batchschedule');
    batchScheduleSelect.innerHTML = ''; // Clear existing options

    if (schedule) {
        var option = document.createElement('option');
        option.value = schedule;
        option.textContent = schedule;
        batchScheduleSelect.appendChild(option);
    } else {
        var defaultOption = document.createElement('option');
        defaultOption.textContent = 'Select Batch Schedule';
        batchScheduleSelect.appendChild(defaultOption);
    }
});


</script>
```


## Update another model: 
One Model modification automatically updates other models previous field. If model within a relation:

```python
from django.db import transaction
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
```

Can i do it without `from django.db import transaction`. Without transactions, this increases the risk of race conditions and data corruption. Using transaction.atomic() ensures that all updates succeed or fail together, maintaining data integrity and consistency.

### Without transaction:

```python
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
```