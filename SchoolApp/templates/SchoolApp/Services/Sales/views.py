import uuid
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.timezone import now
from .filters import *
from .forms import *
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile,TemporaryUploadedFile
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.db.models import Sum

# Create your views here.
def home(request):
    return render(request, 'home.html')    

@login_required    
def index(request):
    return render(request, 'SchoolApp/index.html')  

#Programme view //////////////////////////////////////////////////////////////////////////
@login_required    
def ProgrammeView(request):
    ProgrammesList = Programme.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(ProgrammesList, 50)
    try:
        Programmes = paginator.page(page)
    except PageNotAnInteger:
        Programmes = paginator.page(1)
    except EmptyPage:
        Programmes = paginator.page(paginator.num_pages)
    return render(request, 'SchoolApp/accademics/Programmes/list.html', {'Programmes': Programmes})  

@login_required    
def createProgramme(request):
    form = ProgrammeForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/createProgramme')
    return render(request, 'SchoolApp/accademics/Programmes/create.html', {'form': form})

@login_required    
def editProgramme(request, pk):
    pickProgramme = Programme.objects.get(pk=pk)
    editForm = ProgrammeForm(request.POST or None, instance=pickProgramme)

    if editForm.is_valid():
        editForm.save()
        return redirect('/Programme')
    return render(request, 'SchoolApp/accademics/Programmes/update.html', {'form': editForm})


@login_required    
def deleteProgramme(request, pk):
    pickProgramme = Programme.objects.get(pk=pk)
    if request.method == 'POST':
        pickProgramme.delete()
        return redirect('/Programme')
    context = {'item': pickProgramme} 
    return render(request, 'SchoolApp/accademics/Programmes/delete.html', context)

#school type viewn //////////////////////////////////////////////////////////////////////
@login_required    
def SchoolTypeView(request):
    SchoolTypeList = SchoolType.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(SchoolTypeList, 50)
    try:
        SchoolTypes = paginator.page(page)
    except PageNotAnInteger:
        SchoolTypes = paginator.page(1)
    except EmptyPage:
        SchoolTypes = paginator.page(paginator.num_pages)
    return render(request, 'SchoolApp/accademics/schoolTypes/list.html', {'SchoolTypes': SchoolTypes}) 

@login_required    
def createSchoolType(request):
    form = SchoolTypeForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/createSchoolType')
    return render(request, 'SchoolApp/accademics/schoolTypes/create.html', {'form': form})

@login_required    
def editSchoolType(request, pk):
    pickSchoolType = SchoolType.objects.get(pk=pk)
    editForm = SchoolTypeForm(request.POST or None, instance=pickSchoolType)
    if editForm.is_valid():
        editForm.save()
        return redirect('/SchoolType')
    return render(request, 'SchoolApp/accademics/schoolTypes/update.html', {'form': editForm})

@login_required    
def deleteSchoolType(request, pk):

    pickSchoolType = SchoolType.objects.get(id=pk)
    if request.method == 'POST':
        pickSchoolType.delete()
        return redirect('/SchoolType')
    context = {'item': pickSchoolType}
 
    return render(request, 'SchoolApp/accademics/schoolTypes/delete.html', context)



#course view //////////////////////////////////////////////////////////////////////////
@login_required    
def courseView(request):
    coursesList = Course.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(coursesList, 50)
    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        courses = paginator.page(1)
    except EmptyPage:
        courses = paginator.page(paginator.num_pages)
    return render(request, 'SchoolApp/accademics/Courses/list.html', {'courses': courses})  

@login_required    
def createCourse(request):
    form = courseForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/create')

    return render(request, 'SchoolApp/accademics/Courses/create.html', {'form': form})

@login_required    
def editcourse(request, pk):
    pickCourse = Course.objects.get(pk=pk)
    editForm = courseForm(request.POST or None, instance=pickCourse)

    if editForm.is_valid():
        editForm.save()
        return redirect('/course')
    return render(request, 'SchoolApp/accademics/Courses/update.html', {'form': editForm})

@login_required    
def deletecourse(request, pk):
    pickCourse = Course.objects.get(pk=pk)
    if request.method == 'POST':
        pickCourse.delete()
        return redirect('/course')
    context = {'item': pickCourse} 
    return render(request, 'SchoolApp/accademics/Courses/delete.html', context)

#Section view //////////////////////////////////////////////////////////////////////////
@login_required    
def SectionView(request):
    SectionsList = Section.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(SectionsList, 50)
    try:
        Sections = paginator.page(page)
    except PageNotAnInteger:
        Sections = paginator.page(1)
    except EmptyPage:
        Sections = paginator.page(paginator.num_pages)
    return render(request, 'SchoolApp/accademics/Sections/list.html', {'Sections': Sections})  

@login_required    
def createSection(request):
    form = SectionForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            
            messages.success(request, "Section created succesful" )
            return redirect('/createSection')
    return render(request, 'SchoolApp/accademics/Sections/create.html', {'form': form})

@login_required    
def editSection(request, pk):
    pickSection = Section.objects.get(pk=pk)
    editForm = SectionForm(request.POST or None, instance=pickSection)

    if editForm.is_valid():
        editForm.save()
        return redirect('/Section')
    return render(request, 'SchoolApp/accademics/Sections/update.html', {'form': editForm})


@login_required    
def deleteSection(request, pk):
    pickSection = Section.objects.get(pk=pk)
    if request.method == 'POST':
        pickSection.delete()
        return redirect('/Section')
    context = {'item': pickSection} 
    return render(request, 'SchoolApp/accademics/Sections/delete.html', context)

#Subject view //////////////////////////////////////////////////////////////////////////
@login_required    
def SubjectView(request):
    SubjectsList = Subject.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(SubjectsList, 50)
    try:
        Subjects = paginator.page(page)
    except PageNotAnInteger:
        Subjects = paginator.page(1)
    except EmptyPage:
        Subjects = paginator.page(paginator.num_pages)
    return render(request, 'SchoolApp/accademics/Subjects/list.html', {'Subjects': Subjects})  

@login_required    
def createSubject(request):
    form = SubjectForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/createSubject')
    return render(request, 'SchoolApp/accademics/Subjects/create.html', {'form': form})

@login_required    
def editSubject(request, pk):
    pickSubject = Subject.objects.get(pk=pk)
    editForm = SubjectForm(request.POST or None, instance=pickSubject)

    if editForm.is_valid():
        editForm.save()
        return redirect('/Subject')
    return render(request, 'SchoolApp/accademics/Subjects/update.html', {'form': editForm})

@login_required    
def deleteSubject(request, pk):
    pickSubject = Subject.objects.get(pk=pk)
    if request.method == 'POST':
        pickSubject.delete()
        return redirect('/Subject')
    context = {'item': pickSubject} 
    return render(request, 'SchoolApp/accademics/Subjects/delete.html', context)



# Registered students viewn //////////////////////////////////////////////////////////////////////
@login_required    
def StudentView(request):
    StudentList = RegisteredStudent.objects.all()
    page = request.GET.get('page', 1)
    myFilter = StudentAdmissionFilter(request.GET, queryset=StudentList)
    StudentList = myFilter.qs 

    paginator = Paginator(StudentList, 50)
    try:
        Students = paginator.page(page)
    except PageNotAnInteger:
        Students = paginator.page(1)
    except EmptyPage:
        Students = paginator.page(paginator.num_pages)
    return render(request, 'SchoolApp/Students/list.html', {'Students': Students, 'myFilter':myFilter}) 

@login_required    
def createStudent(request):
    form = StudentForm(request.POST or None,request.FILES or None)
    if request.method == 'POST' and 'Photo' in request.FILES:

        if form.is_valid():
            newform = form.save(commit=False)
            newform.PhotoURL = handle_uploaded_file(request.FILES['Photo'])           
            newform.save()
            return redirect('/createStudent')   
    return render(request, 'SchoolApp/Students/create.html', {'form': form})

@login_required    
def editStudent(request, pk):
    pickStudent = RegisteredStudent.objects.get(pk=pk)
    editForm = StudentForm(request.POST or None, request.FILES or None , instance=pickStudent )

    if editForm.is_valid():
        newform = editForm.save(commit=False)
        newform.save()
        return redirect('/Student')
    return render(request, 'SchoolApp/Students/update.html', {'form': editForm, 'Id':pk})

@login_required    
def deleteStudent(request, pk):
    pickStudent = RegisteredStudent.objects.get(id=pk)
    if request.method == 'POST':
        pickStudent.delete()
        return redirect('/Student')
    context = {'item': pickStudent}
    return render(request, 'SchoolApp/Students/delete.html', context)


def handle_uploaded_file(request):
    Now = date.today()
    fileToUpload = request
    fileDirectory = fileToUpload.temporary_file_path()
    extension = fileToUpload.name.split(".")[-1].lower()
    uniquePictureId = uuid.uuid4().hex
    mediaLocation = "Photos/" +f"{Now.year}{Now.month}{Now.day}" + "/" + uniquePictureId + "." + extension
    mediaUrl = "https://omyseazonbucket.s3.amazonaws.com/" + mediaLocation
   # Let's use Amazon S3
    #s3 = boto3.client("s3")
    client = boto3.client(
        "s3",
        aws_access_key_id="AKIAYN3ZGH3C4XS66IKS",
        aws_secret_access_key='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',
        # aws_session_token="wg3rf398r2887fes",
        region_name="us-east-1"
    )
    try:
        client.upload_file(
                Filename=fileDirectory,
                Bucket="omyseazonbucket",
                Key= mediaLocation,
            )
        return mediaUrl    
    except Exception as e:
        return e  
    
   
#StudentAdmission view //////////////////////////////////////////////////////////////////////////
@login_required    
def StudentAdmissionView(request):
    StudentAdmissionsList = StudentAdmission.objects.all()
    page = request.GET.get('page', 1)

    myFilter = StudentAdmissionFilter(request.GET, queryset=StudentAdmissionsList)
    StudentAdmissionsList = myFilter.qs 

    
    paginator = Paginator(StudentAdmissionsList, 50)
    try:
        StudentAdmissions = paginator.page(page)
    except PageNotAnInteger:
        StudentAdmissions = paginator.page(1)
    except EmptyPage:
        StudentAdmissions = paginator.page(paginator.num_pages)
    return render(request, 'SchoolApp/StudentAdmissions/list.html', {'StudentAdmissions': StudentAdmissions, 'myFilter':myFilter})  

@login_required    
def createStudentAdmission(request):
    form = StudentAdmissionForm(request.POST  or None,request.FILES or None)
    Now = date.today()
    if request.method == 'POST':


        if form.is_valid():
            newform = form.save(commit=False)
            newform.AdmissionNumber = f'ADM-{Now.year}{Now.day}{Now.month}/{Now.year}'
            newform.AdmissionDate = Now
            newform.PhotoURL = f"http://127.0.0.1:8000/{newform.Photo.url}"  
            newform.BirthCertificateUrl = f"http://127.0.0.1:8000/{newform.BirthCertificate.url}"  
            newform.ResultCertificateUrl = f"http://127.0.0.1:8000/{newform.ResultCertificate.url}"  
           
            # if newform.AdmissionStatus == 'Approved':


            newform.save()
            messages.success(request, "Form Submitted succesful" )
            return redirect('/createStudentAdmission')
        else:
            messages.error(request, "Form Error")
    return render(request, 'SchoolApp/StudentAdmissions/create.html', {'form': form})

@login_required    
def editStudentAdmission(request, pk):
    pickStudentAdmission = StudentAdmission.objects.get(pk=pk)
    editForm = StudentAdmissionForm(request.POST or None, instance=pickStudentAdmission)

    if editForm.is_valid():
        newForm = editForm.save(commit=False)

        if newForm.AdmissionStatus == 'Approved' and newForm.RegistrationStatus == 'Unregistered':
            Now = date.today()
            newForm.RegistrationStatus = 'Registered'
            RegisterStudent = RegisteredStudent(
                AdmissionNumber = newForm.AdmissionNumber,RegistrationNumber = f'Reg-0{newForm.id}/{Now.year}',
                FirstName =  newForm.FirstName,MiddleName =  newForm.MiddleName,LastName =  newForm.LastName,
                DateOfBirth = newForm.DateOfBirth,Photo  = newForm.Photo,PhotoURL = newForm.PhotoURL,Gender = newForm.Gender,
                BirthPlace = newForm.BirthPlace,Health =  newForm.Health,ClassName = newForm.ClassName,Programme = newForm.Programme,
                SchoolType  = newForm.SchoolType,Nationality =  newForm.Nationality,Region =  newForm.Region,
                Street =  newForm.Street,HomeAddress =  newForm.HomeAddress,Mobile =  newForm.Mobile,Religion =  newForm.Religion,
                BirthCertificate = newForm.BirthCertificate,BirthCertificateUrl = newForm.BirthCertificateUrl,
                ResultCertificate = newForm.ResultCertificate,ResultCertificateUrl = newForm.ResultCertificateUrl,
            )

            RegisterRelative = Relative(
                Student = RegisterStudent,
                RelativeFirstName =  newForm.RelativeFirstName,
                RelativeMiddleName =  newForm.RelativeMiddleName,
                RelativeLastName =  newForm.RelativeLastName,
                RelativeGender = newForm.RelativeGender,
                RelativeRelation =  newForm.RelativeRelation,
                RelativeMobile =  newForm.RelativeMobile,
                RelativeEmail =  newForm.RelativeEmail,
                RelativeHomeAddress =  newForm.RelativeHomeAddress,
                RelativeOccupation =  newForm.RelativeHomeAddress,
                RelativeWorkAddress =  newForm.RelativeWorkAddress,
            )

            RegisterParent = Parent(
                Student = RegisterStudent,
                FatherFirstName =  newForm.FatherFirstName,
                FatherMiddleName = newForm.FatherMiddleName,
                FatherLastName =  newForm.FatherLastName,
                FatherPhoneNumber =  newForm.FatherPhoneNumber,
                FatherOccupation =  newForm.FatherOccupation,
                FatherHomeAddress =  newForm.FatherHomeAddress,
                MotherFirstName =  newForm.MotherFirstName,
                MotherMiddleName = newForm.MotherMiddleName,
                MotherLastName =  newForm.MotherLastName,
                MotherOccupation =  newForm.MotherOccupation,
                MotherPhoneNumber =  newForm.MotherPhoneNumber,
                MotherHomeAddress=  newForm.MotherHomeAddress,
            )
            RegisterStudent.save()
            RegisterParent.save()
            RegisterRelative.save()
        newForm.save()

        return redirect('/StudentAdmission')
    return render(request, 'SchoolApp/StudentAdmissions/update.html', {'form': editForm, 'StudentId':pk})


@login_required    
def deleteStudentAdmission(request, pk):
    pickStudentAdmission = StudentAdmission.objects.get(pk=pk)
    if request.method == 'POST':
        pickStudentAdmission.delete()
        return redirect('/StudentAdmission')
    context = {'item': pickStudentAdmission} 
    return render(request, 'SchoolApp/StudentAdmissions/delete.html', context)



#Hostel view //////////////////////////////////////////////////////////////////////////
@login_required    
def HostelView(request):
    HostelsList = Hostel.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(HostelsList, 50)
    try:
        Hostels = paginator.page(page)
    except PageNotAnInteger:
        Hostels = paginator.page(1)
    except EmptyPage:
        Hostels = paginator.page(paginator.num_pages)
    return render(request, 'SchoolApp/Hostels/Hostel/list.html', {'Hostels': Hostels})  

@login_required    
def createHostel(request):
    form = HostelForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/createHostel')
    return render(request, 'SchoolApp/Hostels/Hostel/create.html', {'form': form})

@login_required    
def editHostel(request, pk):
    pickHostel = Hostel.objects.get(pk=pk)
    editForm = HostelForm(request.POST or None, instance=pickHostel)

    if editForm.is_valid():
        editForm.save()
        return redirect('/Hostel')
    return render(request, 'SchoolApp/Hostels/Hostel/update.html', {'form': editForm})

@login_required    
def deleteHostel(request, pk):
    pickHostel = Hostel.objects.get(pk=pk)
    if request.method == 'POST':
        pickHostel.delete()
        return redirect('/Hostel')
    context = {'item': pickHostel} 
    return render(request, 'SchoolApp/Hostels/Hostel/delete.html', context)


#RoomType view //////////////////////////////////////////////////////////////////////////
@login_required    
def RoomTypeView(request):
    RoomTypesList = RoomType.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(RoomTypesList, 50)
    try:
        RoomTypes = paginator.page(page)
    except PageNotAnInteger:
        RoomTypes = paginator.page(1)
    except EmptyPage:
        RoomTypes = paginator.page(paginator.num_pages)
    return render(request, 'SchoolApp/Hostels/RoomTypes/list.html', {'RoomTypes': RoomTypes})  

@login_required    
def createRoomType(request):
    form = RoomTypeForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/createRoomType')
    return render(request, 'SchoolApp/Hostels/RoomTypes/create.html', {'form': form})

@login_required    
def editRoomType(request, pk):
    pickRoomType = RoomType.objects.get(pk=pk)
    editForm = RoomTypeForm(request.POST or None, instance=pickRoomType)

    if editForm.is_valid():
        editForm.save()
        return redirect('/RoomType')
    return render(request, 'SchoolApp/Hostels/RoomTypes/update.html', {'form': editForm})

@login_required    
def deleteRoomType(request, pk):
    pickRoomType = RoomType.objects.get(pk=pk)
    if request.method == 'POST':
        pickRoomType.delete()
        return redirect('/RoomType')
    context = {'item': pickRoomType} 
    return render(request, 'SchoolApp/Hostels/RoomTypes/delete.html', context)



#HostelRoom view //////////////////////////////////////////////////////////////////////////
@login_required    
def HostelRoomView(request):
    HostelRoomsList = HostelRoom.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(HostelRoomsList, 50)
    try:
        HostelRooms = paginator.page(page)
    except PageNotAnInteger:
        HostelRooms = paginator.page(1)
    except EmptyPage:
        HostelRooms = paginator.page(paginator.num_pages)
    return render(request, 'SchoolApp/Hostels/HostelRooms/list.html', {'HostelRooms': HostelRooms})  

@login_required    
def createHostelRoom(request):
    form = HostelRoomForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            newform = form.save(commit=False)
            newform.CurrentCapacity = 0
            newform.AvailableCapacity = newform.Capacity
            newform.save()
            messages.success(request, "Form Submitted succesful" )
            return redirect('/createHostelRoom')
        else:
            messages.error(request, "Form Error")    
    return render(request, 'SchoolApp/Hostels/HostelRooms/create.html', {'form': form})

@login_required    
def editHostelRoom(request, pk):
    pickHostelRoom = HostelRoom.objects.get(pk=pk)
    editForm = HostelRoomFormTwo(request.POST or None, instance=pickHostelRoom)

    if editForm.is_valid():
        editForm.save()
        return redirect('/HostelRoom')
    return render(request, 'SchoolApp/Hostels/HostelRooms/update.html', {'form': editForm})

@login_required    
def deleteHostelRoom(request, pk):
    pickHostelRoom = HostelRoom.objects.get(pk=pk)
    if request.method == 'POST':
        pickHostelRoom.delete()
        return redirect('/HostelRoom')
    context = {'item': pickHostelRoom} 
    return render(request, 'SchoolApp/Hostels/HostelRooms/delete.html', context)    


#Route view //////////////////////////////////////////////////////////////////////////
@login_required    
def RouteView(request):
    RoutesList = Route.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(RoutesList, 50)
    try:
        Routes = paginator.page(page)
    except PageNotAnInteger:
        Routes = paginator.page(1)
    except EmptyPage:
        Routes = paginator.page(paginator.num_pages)
    return render(request, 'SchoolApp/Transports/Routes/list.html', {'Routes': Routes})  

@login_required    
def createRoute(request):
    form = RouteForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/createRoute')
    return render(request, 'SchoolApp/Transports/Routes/create.html', {'form': form})

@login_required    
def editRoute(request, pk):
    pickRoute = Route.objects.get(pk=pk)
    editForm = RouteForm(request.POST or None, instance=pickRoute)

    if editForm.is_valid():
        editForm.save()
        return redirect('/Route')
    return render(request, 'SchoolApp/Transports/Routes/update.html', {'form': editForm})

@login_required    
def deleteRoute(request, pk):
    pickRoute = Route.objects.get(pk=pk)
    if request.method == 'POST':
        pickRoute.delete()
        return redirect('/Route')
    context = {'item': pickRoute} 
    return render(request, 'SchoolApp/Transports/Routes/delete.html', context)    



#Driver view //////////////////////////////////////////////////////////////////////////
@login_required    
def DriverView(request):
    DriversList = Driver.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(DriversList, 50)
    try:
        Drivers = paginator.page(page)
    except PageNotAnInteger:
        Drivers = paginator.page(1)
    except EmptyPage:
        Drivers = paginator.page(paginator.num_pages)
    return render(request, 'SchoolApp/Transports/Drivers/list.html', {'Drivers': Drivers})  

@login_required    
def createDriver(request):
    form = DriverForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Form Submitted succesful" )
            return redirect('/createDriver')
        else:
            messages.error(request, "Form Error")    
    return render(request, 'SchoolApp/Transports/Drivers/create.html', {'form': form})

@login_required    
def editDriver(request, pk):
    pickDriver = Driver.objects.get(pk=pk)
    editForm = VehicleUpdateForm(request.POST or None, instance=pickDriver)

    if editForm.is_valid():
        editForm.save()
        return redirect('/Driver')
    return render(request, 'SchoolApp/Transports/Drivers/update.html', {'form': editForm})

@login_required    
def deleteDriver(request, pk):
    pickDriver = Driver.objects.get(pk=pk)
    if request.method == 'POST':
        pickDriver.delete()
        return redirect('/Driver')
    context = {'item': pickDriver} 
    return render(request, 'SchoolApp/Transports/Drivers/delete.html', context)        


#Vehicle view //////////////////////////////////////////////////////////////////////////
@login_required    
def VehicleView(request):
    VehiclesList = Vehicle.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(VehiclesList, 50)
    try:
        Vehicles = paginator.page(page)
    except PageNotAnInteger:
        Vehicles = paginator.page(1)
    except EmptyPage:
        Vehicles = paginator.page(paginator.num_pages)
    return render(request, 'SchoolApp/Transports/Vehicles/list.html', {'Vehicles': Vehicles})  

@login_required    
def createVehicle(request):
    form = VehicleForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            newform = form.save(commit=False)
            newform.CurrentCapacity = 0
            newform.AvailableCapacity = newform.Capacity
            newform.save()
            messages.success(request, "Form Submitted succesful" )
            return redirect('/createVehicle')
        else:
            messages.error(request, "Form Error")  
            return redirect('/createVehicle')
    return render(request, 'SchoolApp/Transports/Vehicles/create.html', {'form': form})

@login_required    
def editVehicle(request, pk):
    pickVehicle = Vehicle.objects.get(pk=pk)
    editForm = VehicleUpdateForm(request.POST or None, instance=pickVehicle)

    if editForm.is_valid():
        newform = editForm.save(commit=False)
        newform.CurrentCapacity = 0
        newform.AvailableCapacity = newform.Capacity
        newform.save()
        return redirect('/Vehicle')
    return render(request, 'SchoolApp/Transports/Vehicles/update.html', {'form': editForm})

@login_required    
def deleteVehicle(request, pk):
    pickVehicle = Vehicle.objects.get(pk=pk)
    if request.method == 'POST':
        pickVehicle.delete()
        return redirect('/Vehicle')
    context = {'item': pickVehicle} 
    return render(request, 'SchoolApp/Transports/Vehicles/delete.html', context) 


#AssignVehicle view //////////////////////////////////////////////////////////////////////////
@login_required    
def AssignVehicleView(request):
    AssignVehiclesList = AssignVehicle.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(AssignVehiclesList, 50)
    try:
        AssignVehicles = paginator.page(page)
    except PageNotAnInteger:
        AssignVehicles = paginator.page(1)
    except EmptyPage:
        AssignVehicles = paginator.page(paginator.num_pages)
    return render(request, 'SchoolApp/Transports/AssignVehicles/list.html', {'AssignVehicles': AssignVehicles})  

@login_required    
def createAssignVehicle(request):
    form = AssignVehicleForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/createAssignVehicle')
    return render(request, 'SchoolApp/Transports/AssignVehicles/create.html', {'form': form})

@login_required    
def editAssignVehicle(request, pk):
    pickAssignVehicle = AssignVehicle.objects.get(pk=pk)
    editForm = AssignVehicleForm(request.POST or None, instance=pickAssignVehicle)

    if editForm.is_valid():
        editForm.save()
        return redirect('/AssignVehicle')
    return render(request, 'SchoolApp/Transports/AssignVehicles/update.html', {'form': editForm})

@login_required    
def deleteAssignVehicle(request, pk):
    pickAssignVehicle = AssignVehicle.objects.get(pk=pk)
    if request.method == 'POST':
        pickAssignVehicle.delete()
        return redirect('/AssignVehicle')
    context = {'item': pickAssignVehicle} 
    return render(request, 'SchoolApp/Transports/AssignVehicles/delete.html', context)    

#StudentEnrollment view //////////////////////////////////////////////////////////////////////////
@login_required    
def StudentEnrollmentView(request):
    StudentEnrollmentsList = StudentEnrollment.objects.all()
    page = request.GET.get('page', 1)
    Now = date.today()

    myFilter = StudentEnrollFilter(request.GET, queryset=StudentEnrollmentsList)
    myFilter.form.AcademicYear = int(Now.year)
    StudentEnrollmentsList = myFilter.qs

    paginator = Paginator(StudentEnrollmentsList, 50)
    try:
        StudentEnrollments = paginator.page(page)
    except PageNotAnInteger:
        StudentEnrollments = paginator.page(1)
    except EmptyPage:
        StudentEnrollments = paginator.page(paginator.num_pages)
    return render(request, 'SchoolApp/StudentEnrollments/list.html', {'StudentEnrollments': StudentEnrollments, 'myFilter': myFilter})  

@login_required    
def createStudentEnrollment(request):
    
    form = StudentEnrollmentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
           
            # newform = form.save(commit=False)
            # newform.SchoolType = newform.RegisteredStudent.SchoolType
            form.save()
            messages.success(request, "StudentEnrollment created succesful" )
            return redirect('/createStudentEnrollment')
    return render(request, 'SchoolApp/StudentEnrollments/create.html', {'form': form})

@login_required    
def editStudentEnrollment(request, pk):
    pickStudentEnrollment = StudentEnrollment.objects.get(pk=pk)
    editForm = StudentEnrollmentForm(request.POST or None, instance=pickStudentEnrollment)

    if editForm.is_valid():
        editForm.save()
        return redirect('/StudentEnrollment')
    return render(request, 'SchoolApp/StudentEnrollments/update.html', {'form': editForm})


@login_required    
def deleteStudentEnrollment(request, pk):
    pickStudentEnrollment = StudentEnrollment.objects.get(pk=pk)
    if request.method == 'POST':
        pickStudentEnrollment.delete()
        return redirect('/StudentEnrollment')
    context = {'item': pickStudentEnrollment} 
    return render(request, 'SchoolApp/StudentEnrollments/delete.html', context)

#Designation view //////////////////////////////////////////////////////////////////////////
@login_required    
def DesignationView(request):
    DesignationsList = Designation.objects.all()
    page = request.GET.get('page', 1)
    Now = date.today()

    myFilter = DesignationFilter(request.GET, queryset=DesignationsList)
    DesignationsList = myFilter.qs

    paginator = Paginator(DesignationsList, 50)
    try:
        Designations = paginator.page(page)
    except PageNotAnInteger:
        Designations = paginator.page(1)
    except EmptyPage:
        Designations = paginator.page(paginator.num_pages)
    return render(request, 'SchoolApp/HumanResources/Designations/list.html', {'Designations': Designations, 'myFilter': myFilter})  

@login_required    
def createDesignation(request):
    
    form = DesignationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
           
            # newform = form.save(commit=False)
            # newform.SchoolType = newform.RegisteredStudent.SchoolType
            form.save()
            messages.success(request, "Designation created succesful" )
            return redirect('/createDesignation')
    return render(request, 'SchoolApp/HumanResources/Designations/create.html', {'form': form})

@login_required    
def editDesignation(request, pk):
    pickDesignation = Designation.objects.get(pk=pk)
    editForm = DesignationForm(request.POST or None, instance=pickDesignation)

    if editForm.is_valid():
        editForm.save()
        return redirect('/Designation')
    return render(request, 'SchoolApp/HumanResources/Designations/update.html', {'form': editForm})


@login_required    
def deleteDesignation(request, pk):
    pickDesignation = Designation.objects.get(pk=pk)
    if request.method == 'POST':
        pickDesignation.delete()
        return redirect('/Designation')
    context = {'item': pickDesignation} 
    return render(request, 'SchoolApp/HumanResources/Designations/delete.html', context)

#Department view //////////////////////////////////////////////////////////////////////////
@login_required    
def DepartmentView(request):
    DepartmentsList = Department.objects.all()
    page = request.GET.get('page', 1)
    Now = date.today()

    myFilter = DepartmentFilter(request.GET, queryset=DepartmentsList)
    DepartmentsList = myFilter.qs

    paginator = Paginator(DepartmentsList, 50)
    try:
        Departments = paginator.page(page)
    except PageNotAnInteger:
        Departments = paginator.page(1)
    except EmptyPage:
        Departments = paginator.page(paginator.num_pages)
    return render(request, 'SchoolApp/HumanResources/Departments/list.html', {'Departments': Departments, 'myFilter': myFilter})  

@login_required    
def createDepartment(request):
    
    form = DepartmentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
           
            # newform = form.save(commit=False)
            # newform.SchoolType = newform.RegisteredStudent.SchoolType
            form.save()
            messages.success(request, "Department created succesful" )
            return redirect('/createDepartment')
    return render(request, 'SchoolApp/HumanResources/Departments/create.html', {'form': form})

@login_required    
def editDepartment(request, pk):
    pickDepartment = Department.objects.get(pk=pk)
    editForm = DepartmentForm(request.POST or None, instance=pickDepartment)

    if editForm.is_valid():
        editForm.save()
        return redirect('/Department')
    return render(request, 'SchoolApp/HumanResources/Departments/update.html', {'form': editForm})

@login_required    
def deleteDepartment(request, pk):
    pickDepartment = Department.objects.get(pk=pk)
    if request.method == 'POST':
        pickDepartment.delete()
        return redirect('/Department')
    context = {'item': pickDepartment} 
    return render(request, 'SchoolApp/HumanResources/Departments/delete.html', context)

#Role view //////////////////////////////////////////////////////////////////////////
@login_required    
def RoleView(request):
    RolesList = Role.objects.all()
    page = request.GET.get('page', 1)
    Now = date.today()

    myFilter = RoleFilter(request.GET, queryset=RolesList)
    RolesList = myFilter.qs

    paginator = Paginator(RolesList, 50)
    try:
        Roles = paginator.page(page)
    except PageNotAnInteger:
        Roles = paginator.page(1)
    except EmptyPage:
        Roles = paginator.page(paginator.num_pages)
    return render(request, 'SchoolApp/HumanResources/Roles/list.html', {'Roles': Roles, 'myFilter': myFilter})  

@login_required    
def createRole(request):
    
    form = RoleForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
           
            # newform = form.save(commit=False)
            # newform.SchoolType = newform.RegisteredStudent.SchoolType
            form.save()
            messages.success(request, "Role created succesful" )
            return redirect('/createRole')
    return render(request, 'SchoolApp/HumanResources/Roles/create.html', {'form': form})

@login_required    
def editRole(request, pk):
    pickRole = Role.objects.get(pk=pk)
    editForm = RoleForm(request.POST or None, instance=pickRole)

    if editForm.is_valid():
        editForm.save()
        return redirect('/Role')
    return render(request, 'SchoolApp/HumanResources/Roles/update.html', {'form': editForm})


@login_required    
def deleteRole(request, pk):
    pickRole = Role.objects.get(pk=pk)
    if request.method == 'POST':
        pickRole.delete()
        return redirect('/Role')
    context = {'item': pickRole} 
    return render(request, 'SchoolApp/HumanResources/Roles/delete.html', context)

#Staff view //////////////////////////////////////////////////////////////////////////
@login_required    
def StaffView(request):
    StaffsList = Staff.objects.all()
    page = request.GET.get('page', 1)
    Now = date.today()

    myFilter = StaffFilter(request.GET, queryset=StaffsList)
    StaffsList = myFilter.qs

    paginator = Paginator(StaffsList, 50)
    try:
        Staffs = paginator.page(page)
    except PageNotAnInteger:
        Staffs = paginator.page(1)
    except EmptyPage:
        Staffs = paginator.page(paginator.num_pages)
    return render(request, 'SchoolApp/HumanResources/Staffs/list.html', {'Staffs': Staffs, 'myFilter': myFilter})  

@login_required    
def createStaff(request):
    
    form = StaffForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
           
            # newform = form.save(commit=False)
            # newform.SchoolType = newform.RegisteredStudent.SchoolType
            form.save()
            messages.success(request, "Staff created succesful" )
            return redirect('/createStaff')
    return render(request, 'SchoolApp/HumanResources/Staffs/create.html', {'form': form})

@login_required    
def editStaff(request, pk):
    pickStaff = Staff.objects.get(pk=pk)
    editForm = StaffForm(request.POST or None,request.FILES or None, instance=pickStaff)

    if editForm.is_valid():
        editForm.save()
        return redirect('/Staff')
    return render(request, 'SchoolApp/HumanResources/Staffs/update.html', {'form': editForm})

@login_required    
def deleteStaff(request, pk):
    pickStaff = Staff.objects.get(pk=pk)
    if request.method == 'POST':
        pickStaff.delete()
        return redirect('/Staff')
    context = {'item': pickStaff} 
    return render(request, 'SchoolApp/HumanResources/Staffs/delete.html', context)

#AttendanceConfiguration view //////////////////////////////////////////////////////////////////////////
@login_required    
def AttendanceConfigurationView(request):
    AttendanceConfigurationsList = AttendanceConfiguration.objects.all()
    page = request.GET.get('page', 1)
    Now = date.today()

    paginator = Paginator(AttendanceConfigurationsList, 50)
    try:
        AttendanceConfigurations = paginator.page(page)
    except PageNotAnInteger:
        AttendanceConfigurations = paginator.page(1)
    except EmptyPage:
        AttendanceConfigurations = paginator.page(paginator.num_pages)
    return render(request, 'SchoolApp/HumanResources/AttendanceConfigurations/list.html', {'AttendanceConfigurations': AttendanceConfigurations,})  

@login_required    
def createAttendanceConfiguration(request):
    
    form = AttendanceConfigurationForm(request.POST or None)
    data = AttendanceConfiguration.objects.first()
    editForm = AttendanceConfigurationForm(request.POST or None, instance=data)
    if request.method == 'POST':
        if form.is_valid():
           
            newform = form.save(commit=False)
            if(newform.OutTime.hour >= newform.InTime.hour):
                Minutes = newform.OutTime.minute - newform.InTime.minute
                Hours = newform.OutTime.hour - newform.InTime.hour
                newform.TotalHour = Hours + Minutes/60
                newform.save()
                messages.success(request, "Attendance Time created succesful" )
                return redirect('/createAttendanceConfiguration')
            else:
                messages.error(request, "Enter valid Time" )
                return redirect('/createAttendanceConfiguration')

        else:
            messages.error(request, "form error" )
            return redirect('/createAttendanceConfiguration')    
    return render(request, 'SchoolApp/HumanResources/AttendanceConfigurations/create.html', {'form': form, 'data': editForm,})

@login_required    
def editAttendanceConfiguration(request, pk):
    pickAttendanceConfiguration = AttendanceConfiguration.objects.get(pk=pk)
    editForm = AttendanceConfigurationForm(request.POST or None, instance=pickAttendanceConfiguration)

    if editForm.is_valid():
        editForm.save()
        return redirect('/AttendanceConfiguration')
    return render(request, 'SchoolApp/HumanResources/AttendanceConfigurations/update.html', {'form': editForm})

@login_required    
def deleteAttendanceConfiguration(request, pk):
    pickAttendanceConfiguration = AttendanceConfiguration.objects.get(pk=pk)
    if request.method == 'POST':
        pickAttendanceConfiguration.delete()
        return redirect('/AttendanceConfiguration')
    context = {'item': pickAttendanceConfiguration} 
    return render(request, 'SchoolApp/HumanResources/AttendanceConfigurations/delete.html', context)

#StaffAttendance view //////////////////////////////////////////////////////////////////////////
@login_required    
def StaffAttendanceView(request):
    StaffAttendancesList = StaffAttendance.objects.all()
    page = request.GET.get('page', 1)
    Now = date.today()

    myFilter = StaffAttendanceFilter(request.GET, queryset=StaffAttendancesList)
    StaffAttendancesList = myFilter.qs

    paginator = Paginator(StaffAttendancesList, 50)
    try:
        StaffAttendances = paginator.page(page)
    except PageNotAnInteger:
        StaffAttendances = paginator.page(1)
    except EmptyPage:
        StaffAttendances = paginator.page(paginator.num_pages)
    return render(request, 'SchoolApp/HumanResources/StaffAttendances/list.html', {'StaffAttendances': StaffAttendances, 'myFilter': myFilter})  

@login_required    
def createStaffAttendance(request):
    
    form = StaffAttendanceForm(request.POST or None)
    Attendance = AttendanceConfiguration.objects.first()
    if request.method == 'POST':
        if form.is_valid():
            newform = form.save(commit=False)
            if(newform.PermissionOut.hour < newform.PermissionIn.hour):
                messages.error(request, "Enter valid Permission Time" )
                return redirect('/createStaffAttendance')
            if(newform.OutTime.hour < newform.InTime.hour):
                messages.error(request, "Enter valid working Time" )
                return redirect('/createStaffAttendance')

            if Attendance:
                Hours = newform.PermissionOut.hour - newform.PermissionIn.hour
                Minutes = newform.PermissionOut.minute - newform.PermissionIn.minute
                TotalHour = Hours + Minutes/60
                if TotalHour >= 0:
                    hour1 = newform.PermissionIn.hour - newform.InTime.hour   
                    Minute1 = newform.PermissionIn.minute - newform.InTime.minute
                    TotalHour1 = hour1 + Minute1/60

                    hour2 = newform.OutTime.hour - newform.PermissionOut.hour   
                    Minute2 = newform.OutTime.minute - newform.PermissionOut.minute
                    TotalHour2 = hour2 + Minute2/60
                    TotalWorkingHours = TotalHour1 + TotalHour2 + TotalHour
                    newform.TotalHour = TotalWorkingHours
                    if(newform.TotalHour > float(Attendance.TotalHour)):
                        newform.OverTime = newform.TotalHour - float(Attendance.TotalHour)
                else:
                    Minutes = newform.OutTime.minute - newform.InTime.minute
                    Hours = newform.OutTime.hour - newform.InTime.hour
                    newform.TotalHour = Hours + Minutes/60
                    if(newform.TotalHour > float(Attendance.TotalHour)):
                        newform.OverTime = newform.TotalHour - float(Attendance.TotalHour)
                        
                LateHour = newform.InTime.hour - Attendance.InTime.hour   
                LateMinute = newform.InTime.minute - Attendance.InTime.minute
                LateSignIn = LateHour + LateMinute/60
                if LateSignIn > 0:
                    newform.LateSignIn = LateSignIn
                
                EarlyHour = Attendance.OutTime.hour - newform.OutTime.hour   
                EarlyMinute = Attendance.OutTime.minute - newform.OutTime.minute
                EarlySignOut = EarlyHour + EarlyMinute/60
                if EarlySignOut > 0:
                    newform.EarlySignOut = EarlySignOut

                newform.save()
                messages.success(request, "Attendance created succesful" )
                return redirect('/createStaffAttendance')
           
        else:
            messages.error(request, "Form Error" )
            return redirect('/createStaffAttendance')    
    return render(request, 'SchoolApp/HumanResources/StaffAttendances/create.html', {'form': form})

@login_required    
def editStaffAttendance(request, pk):
    pickStaffAttendance = StaffAttendance.objects.get(pk=pk)
    editForm = StaffAttendanceForm(request.POST or None, instance=pickStaffAttendance)

    if editForm.is_valid():
        editForm.save()
        return redirect('/StaffAttendance')
    return render(request, 'SchoolApp/HumanResources/StaffAttendances/update.html', {'form': editForm})

@login_required    
def deleteStaffAttendance(request, pk):
    pickStaffAttendance = StaffAttendance.objects.get(pk=pk)
    if request.method == 'POST':
        pickStaffAttendance.delete()
        return redirect('/StaffAttendance')
    context = {'item': pickStaffAttendance} 
    return render(request, 'SchoolApp/HumanResources/StaffAttendances/delete.html', context)


#ProductCategory view //////////////////////////////////////////////////////////////////////////
@login_required    
def ProductCategoryView(request):
    ProductCategorysList = ProductCategory.objects.all()
    page = request.GET.get('page', 1)
    Now = date.today()

    myFilter = ProductCategoryFilter(request.GET, queryset=ProductCategorysList)
    ProductCategorysList = myFilter.qs

    paginator = Paginator(ProductCategorysList, 50)
    try:
        ProductCategorys = paginator.page(page)
    except PageNotAnInteger:
        ProductCategorys = paginator.page(1)
    except EmptyPage:
        ProductCategorys = paginator.page(paginator.num_pages)
    return render(request, 'SchoolApp/Services/ProductCategorys/list.html', {'ProductCategorys': ProductCategorys, 'myFilter': myFilter})  

@login_required    
def createProductCategory(request):
    
    form = ProductCategoryForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
           
            # newform = form.save(commit=False)
            # newform.SchoolType = newform.RegisteredStudent.SchoolType
            form.save()
            messages.success(request, "ProductCategory created succesful" )
            return redirect('/createProductCategory')
    return render(request, 'SchoolApp/Services/ProductCategorys/create.html', {'form': form})

@login_required    
def editProductCategory(request, pk):
    pickProductCategory = ProductCategory.objects.get(pk=pk)
    editForm = ProductCategoryForm(request.POST or None, instance=pickProductCategory)

    if editForm.is_valid():
        editForm.save()
        return redirect('/ProductCategory')
    return render(request, 'SchoolApp/Services/ProductCategorys/update.html', {'form': editForm})

@login_required    
def deleteProductCategory(request, pk):
    pickProductCategory = ProductCategory.objects.get(pk=pk)
    if request.method == 'POST':
        pickProductCategory.delete()
        return redirect('/ProductCategory')
    context = {'item': pickProductCategory} 
    return render(request, 'SchoolApp/Services/ProductCategorys/delete.html', context)


#Unit view //////////////////////////////////////////////////////////////////////////
@login_required    
def UnitView(request):
    UnitsList = Unit.objects.all()
    page = request.GET.get('page', 1)
    Now = date.today()

    myFilter = UnitFilter(request.GET, queryset=UnitsList)
    UnitsList = myFilter.qs

    paginator = Paginator(UnitsList, 50)
    try:
        Units = paginator.page(page)
    except PageNotAnInteger:
        Units = paginator.page(1)
    except EmptyPage:
        Units = paginator.page(paginator.num_pages)
    return render(request, 'SchoolApp/Services/Units/list.html', {'Units': Units, 'myFilter': myFilter})  

@login_required    
def createUnit(request):
    
    form = UnitForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
           
            # newform = form.save(commit=False)
            # newform.SchoolType = newform.RegisteredStudent.SchoolType
            form.save()
            messages.success(request, "Unit created succesful" )
            return redirect('/createUnit')
    return render(request, 'SchoolApp/Services/Units/create.html', {'form': form})

@login_required    
def editUnit(request, pk):
    pickUnit = Unit.objects.get(pk=pk)
    editForm = UnitForm(request.POST or None, instance=pickUnit)

    if editForm.is_valid():
        editForm.save()
        return redirect('/Unit')
    return render(request, 'SchoolApp/Services/Units/update.html', {'form': editForm})

@login_required    
def deleteUnit(request, pk):
    pickUnit = Unit.objects.get(pk=pk)
    if request.method == 'POST':
        pickUnit.delete()
        return redirect('/Unit')
    context = {'item': pickUnit} 
    return render(request, 'SchoolApp/Services/Units/delete.html', context)


#Supplier view //////////////////////////////////////////////////////////////////////////
@login_required    
def SupplierView(request):
    SuppliersList = Supplier.objects.all()
    page = request.GET.get('page', 1)
    Now = date.today()

    myFilter = SupplierFilter(request.GET, queryset=SuppliersList)
    SuppliersList = myFilter.qs

    paginator = Paginator(SuppliersList, 50)
    try:
        Suppliers = paginator.page(page)
    except PageNotAnInteger:
        Suppliers = paginator.page(1)
    except EmptyPage:
        Suppliers = paginator.page(paginator.num_pages)
    return render(request, 'SchoolApp/Services/Suppliers/list.html', {'Suppliers': Suppliers, 'myFilter': myFilter})  

@login_required    
def createSupplier(request):
    
    form = SupplierForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
           
            # newform = form.save(commit=False)
            # newform.SchoolType = newform.RegisteredStudent.SchoolType
            form.save()
            messages.success(request, "Supplier created succesful" )
            return redirect('/createSupplier')
    return render(request, 'SchoolApp/Services/Suppliers/create.html', {'form': form})

@login_required    
def editSupplier(request, pk):
    pickSupplier = Supplier.objects.get(pk=pk)
    editForm = SupplierForm(request.POST or None, instance=pickSupplier)

    if editForm.is_valid():
        editForm.save()
        return redirect('/Supplier')
    return render(request, 'SchoolApp/Services/Suppliers/update.html', {'form': editForm})

@login_required    
def deleteSupplier(request, pk):
    pickSupplier = Supplier.objects.get(pk=pk)
    if request.method == 'POST':
        pickSupplier.delete()
        return redirect('/Supplier')
    context = {'item': pickSupplier} 
    return render(request, 'SchoolApp/Services/Suppliers/delete.html', context)



#Product view //////////////////////////////////////////////////////////////////////////
@login_required    
def ProductView(request):
    ProductsList = Product.objects.all()
    page = request.GET.get('page', 1)
    Now = date.today()

    myFilter = ProductFilter(request.GET, queryset=ProductsList)
    ProductsList = myFilter.qs

    paginator = Paginator(ProductsList, 50)
    try:
        Products = paginator.page(page)
    except PageNotAnInteger:
        Products = paginator.page(1)
    except EmptyPage:
        Products = paginator.page(paginator.num_pages)
    return render(request, 'SchoolApp/Services/Products/list.html', {'Products': Products, 'myFilter': myFilter})  

@login_required    
def createProduct(request):
    
    form = ProductForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            
            newform = form.save(commit=False)
            newform.Stock = 0
            newform.save()
            messages.success(request, "Product created succesful" )
            return redirect('/createProduct')
        else:    
            messages.error(request, "form Error" )
            return redirect('/createProduct')

    return render(request, 'SchoolApp/Services/Products/create.html', {'form': form})

@login_required    
def editProduct(request, pk):
    pickProduct = Product.objects.get(pk=pk)
    editForm = ProductForm(request.POST or None, instance=pickProduct)

    if editForm.is_valid():
        newform = editForm.save(commit=False)
        newform.Stock = 0
        newform.save()
        return redirect('/Product')
    return render(request, 'SchoolApp/Services/Products/update.html', {'form': editForm})

@login_required    
def deleteProduct(request, pk):
    pickProduct = Product.objects.get(pk=pk)
    if request.method == 'POST':
        pickProduct.delete()
        return redirect('/Product')
    context = {'item': pickProduct} 
    return render(request, 'SchoolApp/Services/Products/delete.html', context)


#Purchase view //////////////////////////////////////////////////////////////////////////
@login_required    
def PurchaseView(request):
    PurchasesList = Purchase.objects.all()
    page = request.GET.get('page', 1)
    Now = date.today()

    myFilter = PurchaseFilter(request.GET, queryset=PurchasesList)
    PurchasesList = myFilter.qs

    paginator = Paginator(PurchasesList, 50)
    try:
        Purchases = paginator.page(page)
    except PageNotAnInteger:
        Purchases = paginator.page(1)
    except EmptyPage:
        Purchases = paginator.page(paginator.num_pages)
    return render(request, 'SchoolApp/Services/Purchases/list.html', {'Purchases': Purchases, 'myFilter': myFilter})  

@login_required    
def createPurchase(request):
    
    form = PurchaseForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
           
            newform = form.save(commit=False)
            newform.Amount = 0
            newform.save()
            newform.ReceiptNumber = f'R-000{newform.id}'
            newform.save()
            messages.success(request, "Purchase created succesful" )
            return redirect(f'/updatePurchase/{newform.id}')
        else:    
            messages.error(request, "form Error" )
            return redirect('/createPurchase')    
    return render(request, 'SchoolApp/Services/Purchases/create.html', {'form': form})

@login_required    
def editPurchase(request, pk):
    pickPurchase = Purchase.objects.get(pk=pk)
    
    editForm = PurchaseForm(request.POST or None, instance=pickPurchase)
    purchaseItemForm = PurchaseItemForm(request.POST or None)
    PurchaseItems = PurchaseItem.objects.filter(Purchase_id=pk)

    if 'save_item' in request.POST:
        if purchaseItemForm.is_valid():
            newform = purchaseItemForm.save(commit=False)
            newform.Purchase = pickPurchase
            newform.Amount = newform.Quantity * newform.UnitPrice
            newform.save()

            Amount = PurchaseItem.objects.filter(Purchase_id=pk).aggregate(Sum('Amount')).get('Amount__sum')
            _purchase = Purchase()
            _purchase.id = pk
            _purchase.Amount = Amount
            _purchase.Supplier = pickPurchase.Supplier
            _purchase.PurchaseType = pickPurchase.PurchaseType
            _purchase.ReceiptNumber = pickPurchase.ReceiptNumber
            _purchase.PurchaseDate = pickPurchase.PurchaseDate
            _purchase.save()
            return redirect(f'/updatePurchase/{pk}')

    if 'save_purchase' in request.POST:
        if editForm.is_valid():
            newform = editForm.save(commit=False)
            newform.Amount = 0
            newform.save()
            return redirect('/Purchase')
    return render(request, 'SchoolApp/Services/Purchases/update.html', {'PurchaseItems': PurchaseItems,'form': editForm,'ItemForm':purchaseItemForm})

@login_required    
def editPurchaseItem(request, pk):
    pickPurchaseItem = PurchaseItem.objects.get(pk=pk)
    editForm = PurchaseItemForm(request.POST or None, instance=pickPurchaseItem)
    Purchase_id = pickPurchaseItem.Purchase_id
    pickPurchase = pickPurchaseItem.Purchase
    pickProduct = pickPurchaseItem.Product
    if editForm.is_valid():
            newform = editForm.save(commit=False)
            newform.Purchase = pickPurchase
            newform.Amount = newform.Quantity * newform.UnitPrice
            newform.save()

            Amount = PurchaseItem.objects.filter(Purchase_id = Purchase_id).aggregate(Sum('Amount')).get('Amount__sum')
            _purchase = Purchase()
            _purchase.id = Purchase_id
            _purchase.Amount = Amount
            _purchase.Supplier = pickPurchase.Supplier
            _purchase.PurchaseType = pickPurchase.PurchaseType
            _purchase.ReceiptNumber = pickPurchase.ReceiptNumber
            _purchase.PurchaseDate = pickPurchase.PurchaseDate
            _purchase.save()

            Quantity = newform.Quantity
            pickProduct.Stock = pickProduct.Stock + Quantity
            pickProduct.save()

        
            return redirect(f'/updatePurchase/{Purchase_id}')
    return render(request, 'SchoolApp/Services/Purchases/PurchaseItemUpdate.html', {'Purchase_id':pickPurchaseItem.Purchase_id, 'ItemForm': editForm})

@login_required    
def deletePurchaseItem(request, pk):
    pickPurchaseItem = PurchaseItem.objects.get(pk=pk)
    _purchaseId = pickPurchaseItem.Purchase_id
    pickProduct = pickPurchaseItem.Product
    if request.method == 'POST':
        pickPurchaseItem.delete()

        Quantity = pickPurchaseItem.Quantity
        pickProduct.Stock = pickProduct.Stock - Quantity
        pickProduct.save()
        return redirect(f'/updatePurchase/{_purchaseId}')
    context = {'item': pickPurchaseItem, 'Purchase_id':_purchaseId} 
    return render(request, 'SchoolApp/Services/Purchases/deletePurchaseItem.html', context)

@login_required    
def deletePurchase(request, pk):
    pickPurchase = Purchase.objects.get(pk=pk)
    if request.method == 'POST':
        pickPurchase.delete()
        return redirect('/Purchase')
    context = {'item': pickPurchase} 
    return render(request, 'SchoolApp/Services/Purchases/delete.html', context)

#Sale view //////////////////////////////////////////////////////////////////////////
@login_required    
def SaleView(request):
    SalesList = Sale.objects.all()
    page = request.GET.get('page', 1)
    Now = date.today()

    myFilter = SaleFilter(request.GET, queryset=SalesList)
    SalesList = myFilter.qs

    paginator = Paginator(SalesList, 50)
    try:
        Sales = paginator.page(page)
    except PageNotAnInteger:
        Sales = paginator.page(1)
    except EmptyPage:
        Sales = paginator.page(paginator.num_pages)
    return render(request, 'SchoolApp/Services/Sales/list.html', {'Sales': Sales, 'myFilter': myFilter})  

@login_required    
def createSale(request):
    
    form = SaleForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
           
            newform = form.save(commit=False)
            newform.Amount = 0
            newform.save()
            newform.ReceiptNumber = f'R-000{newform.id}'
            newform.save()
            messages.success(request, "Sale created succesful" )
            return redirect(f'/updateSale/{newform.id}')
        else:    
            messages.error(request, "form Error" )
            return redirect('/createSale')    
    return render(request, 'SchoolApp/Services/Sales/create.html', {'form': form})

@login_required    
def editSale(request, pk):
    pickSale = Sale.objects.get(pk=pk)
    
    editForm = SaleForm(request.POST or None, instance=pickSale)
    SaleItemForm = SaleItemForm(request.POST or None)
    SaleItems = SaleItem.objects.filter(Sale_id=pk)

    if 'save_item' in request.POST:
        if SaleItemForm.is_valid():
            newform = SaleItemForm.save(commit=False)
            newform.Sale = pickSale
            newform.Amount = newform.Quantity * newform.UnitPrice
            newform.save()

            Amount = SaleItem.objects.filter(Sale_id=pk).aggregate(Sum('Amount')).get('Amount__sum')
            _Sale = Sale()
            _Sale.id = pk
            _Sale.Amount = Amount
            _Sale.Supplier = pickSale.Supplier
            _Sale.SaleType = pickSale.SaleType
            _Sale.ReceiptNumber = pickSale.ReceiptNumber
            _Sale.SaleDate = pickSale.SaleDate
            _Sale.save()
            return redirect(f'/updateSale/{pk}')

    if 'save_Sale' in request.POST:
        if editForm.is_valid():
            newform = editForm.save(commit=False)
            newform.Amount = 0
            newform.save()
            return redirect('/Sale')
    return render(request, 'SchoolApp/Services/Sales/update.html', {'SaleItems': SaleItems,'form': editForm,'ItemForm':SaleItemForm})

@login_required    
def editSaleItem(request, pk):
    pickSaleItem = SaleItem.objects.get(pk=pk)
    editForm = SaleItemForm(request.POST or None, instance=pickSaleItem)
    Sale_id = pickSaleItem.Sale_id
    pickSale = pickSaleItem.Sale
    pickProduct = pickSaleItem.Product
    if editForm.is_valid():
            newform = editForm.save(commit=False)
            newform.Sale = pickSale
            newform.Amount = newform.Quantity * newform.UnitPrice
            newform.save()

            Amount = SaleItem.objects.filter(Sale_id = Sale_id).aggregate(Sum('Amount')).get('Amount__sum')
            _Sale = Sale()
            _Sale.id = Sale_id
            _Sale.Amount = Amount
            _Sale.Supplier = pickSale.Supplier
            _Sale.SaleType = pickSale.SaleType
            _Sale.ReceiptNumber = pickSale.ReceiptNumber
            _Sale.SaleDate = pickSale.SaleDate
            _Sale.save()

            Quantity = newform.Quantity
            pickProduct.Stock = pickProduct.Stock + Quantity
            pickProduct.save()

        
            return redirect(f'/updateSale/{Sale_id}')
    return render(request, 'SchoolApp/Services/Sales/SaleItemUpdate.html', {'Sale_id':pickSaleItem.Sale_id, 'ItemForm': editForm})

@login_required    
def deleteSaleItem(request, pk):
    pickSaleItem = SaleItem.objects.get(pk=pk)
    _SaleId = pickSaleItem.Sale_id
    pickProduct = pickSaleItem.Product
    if request.method == 'POST':
        pickSaleItem.delete()

        Quantity = pickSaleItem.Quantity
        pickProduct.Stock = pickProduct.Stock - Quantity
        pickProduct.save()
        return redirect(f'/updateSale/{_SaleId}')
    context = {'item': pickSaleItem, 'Sale_id':_SaleId} 
    return render(request, 'SchoolApp/Services/Sales/deleteSaleItem.html', context)

@login_required    
def deleteSale(request, pk):
    pickSale = Sale.objects.get(pk=pk)
    if request.method == 'POST':
        pickSale.delete()
        return redirect('/Sale')
    context = {'item': pickSale} 
    return render(request, 'SchoolApp/Services/Sales/delete.html', context)
