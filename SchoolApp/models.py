from email.policy import default
from faulthandler import disable
from django.db import models
from django.core.files import File
from django.forms import DecimalField
from datetime import datetime, timedelta
from datetime import date
from django.utils.timezone import now

# Create your models here.
class Programme(models.Model):
    Name = models.CharField(max_length=200, verbose_name="Programe Name")
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Name
 
class Section(models.Model):
    Name = models.CharField(max_length=200, verbose_name="Section Name")
    TotalCapacity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Name

Subject_status =(("Compulsory", "Compulsory"),("Elective", "Elective"),)
Subject_types =(("Theory", "Theory"),("Practical", "Practical"),)

class Subject(models.Model):
    Name = models.CharField(max_length=200, verbose_name="Subject Name", default="")
    Code = models.CharField(max_length=200, verbose_name="Code", default="")
    Type = models.CharField(choices=Subject_types,max_length=200, verbose_name="Subject type", default="")
    Status = models.CharField(choices=Subject_status,max_length=200, verbose_name="Subject Status", default="")
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Name
# Create your models here.
class Course(models.Model):
    ClassName = models.CharField(max_length=200, verbose_name="Class Name")
    ProgrammeId = models.ForeignKey(Programme, verbose_name="Programme", on_delete=models.CASCADE)
    Section = models.ManyToManyField(Section)
    Subject  = models.ManyToManyField(Subject)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.ClassName



class SchoolType(models.Model):
    TypeName = models.CharField(max_length=200, verbose_name="Type Name")
    def __str__(self):
        return self.TypeName

HostelTypes =(("Boys", "Boys"),("Girls", "Girls"),("Mixer", "Mixer"),)
class Hostel(models.Model):
    Name =  models.CharField(max_length=200, verbose_name="Hostel Name")
    Type =  models.CharField(max_length=200, choices=HostelTypes, verbose_name="Hostel Type")
    Address =  models.CharField(max_length=200, verbose_name="Hostel Address")
    Intake =  models.IntegerField()
    Description =  models.TextField(max_length=200, verbose_name="Description ", blank=True)
    def __str__(self):
        return self.Name

class RoomType(models.Model):
    RoomTitle =  models.CharField(max_length=200, verbose_name="Room Title")
    Description =  models.TextField(max_length=200, verbose_name="Description ",blank=True)
    def __str__(self):
        return self.RoomTitle

class AcademicYear(models.Model):
    Year = models.IntegerField()
    def __str__(self):
        return self.Year 

class HostelRoom(models.Model):
    Hostel = models.ForeignKey(Hostel, verbose_name="Hostel", on_delete=models.CASCADE)
    RoomType = models.ForeignKey(RoomType, verbose_name="Room Type", on_delete=models.CASCADE)
    RoomNumberOrName =  models.CharField(max_length=200, verbose_name="Room Number Or Name")
    CostPerBed =  models.DecimalField(max_digits=65, decimal_places=2, verbose_name="Cost Per Bed")
    NumberOfBed =  models.IntegerField(verbose_name="Number Of Beds")
    Capacity =  models.IntegerField()
    CurrentCapacity =  models.IntegerField(verbose_name="Current Capacity",  default=0)
    AvailableCapacity =  models.IntegerField( verbose_name="Available Capacity",default=0)
    Description =  models.TextField(max_length=200, verbose_name="Description ",blank=True)
    def __str__(self):
        Name = f'{self.Hostel} : {self.RoomNumberOrName}'
        return Name


class Route(models.Model):
    RouteTitle =  models.CharField(max_length=200, verbose_name="Room Title")
    Fare =  models.DecimalField(max_digits=65, decimal_places=2 )
    def __str__(self):
        return self.RouteTitle

class Driver(models.Model):
    FirstName =  models.CharField(max_length=200, verbose_name="First Name")
    MiddleName =  models.CharField(max_length=200, verbose_name="Middle Name")
    LastName =  models.CharField(max_length=200, verbose_name="Last Name")
    Mobile =  models.CharField(max_length=200, verbose_name="Mobile")
    LicenceNumber =  models.CharField(max_length=200, verbose_name="Licence Number")
    LicenceExpiryDate = models.DateField('Licence Expiry Date')
    NextOfKinFirstName =  models.CharField(max_length=200, verbose_name="Next Of Kin First Name")
    NextOfKinMiddleName =  models.CharField(max_length=200, verbose_name="Next Of Kin Middle Name")
    NextOfKinLastName =  models.CharField(max_length=200, verbose_name="Next Of Kin Last Name")
    NextOfKinPhoneNumber =  models.CharField(max_length=200, verbose_name="Next Of Kin Phone Number")
    def __str__(self):
        Fullname = f'{self.FirstName} {self.MiddleName} {self.LastName}'
        return Fullname


class Vehicle(models.Model):
    Driver = models.ForeignKey(Driver, verbose_name="Driver", on_delete=models.CASCADE)
    OwnerName =  models.CharField(max_length=200, verbose_name="Owner Name")
    VehicleNumber =  models.CharField(max_length=200, verbose_name="Vehicle Number")
    VehicleModel =  models.CharField(max_length=200, verbose_name="Vehicle Model")
    YearMade =  models.CharField(max_length=200, verbose_name="Year Made")
    Note =  models.CharField(max_length=200, verbose_name="Note",blank=True)
    Capacity =  models.IntegerField()
    CurrentCapacity =  models.IntegerField(verbose_name="Current Capacity",default=0)
    AvailableCapacity =  models.IntegerField( verbose_name="Available Capacity",default=0)
    def __str__(self):
        Name = f'{self.VehicleModel}: {self.VehicleNumber}'
        return Name
    

class AssignVehicle(models.Model): 
    Route = models.ForeignKey(Route, verbose_name="Route", on_delete=models.CASCADE)
    Vehicle = models.ForeignKey(Vehicle, verbose_name="Vehicle", on_delete=models.CASCADE)
    def __str__(self):
        Name = f'{self.Vehicle} : {self.Route}'
        return Name


Healths = (("None", "None"),("Disability", "Disability"),("Allergy", "Allergy"))
genders =(("Male", "Male"),("Female", "Female"),)
paymentStatus =(("Paid", "Paid"),("Unpaid", "Unpaid"))
formStatus =(("Submitted", "Submitted"),("Unsubmitted", "Unsubmitted"))
AdmissionStatus =(("Approved", "Approved"),("Declined", "Declined"),("Waiting", "Waiting"))
RelativeRelations =(("Father", "Father"),("Mother", "Mother"),("Brother", "Brother"),("Sister", "Sister"),("GrandMother", "GrandMother"),("GrandFather", "GrandFather"),("Other", "Other"))
MaritalStatus =(("Single", "Single"),("Married", "Married"),)

class RegisteredStudent(models.Model):
    AdmissionNumber = models.CharField(max_length=200, verbose_name="Admission Number", blank=True)
    RegistrationNumber = models.CharField(max_length=200, verbose_name="Registration Number", blank=True)
    FirstName =  models.CharField(max_length=200, verbose_name="First Name")
    MiddleName =  models.CharField(max_length=200, verbose_name="Middle Name")
    LastName =  models.CharField(max_length=200, verbose_name="Last Name")
    DateOfBirth = models.DateField('Date Of Birth')
    Photo  = models.ImageField()
    PhotoURL = models.URLField(max_length=500, blank=True)
    Gender = models.CharField(max_length=500,choices=genders)
    BirthPlace = models.CharField(max_length=200, verbose_name="Birth Place")
    Health =  models.CharField(max_length=200, choices=Healths, verbose_name="Health")
    ClassName = models.ForeignKey(Course, verbose_name="Class", on_delete=models.CASCADE)
    Programme = models.ForeignKey(Programme, verbose_name="Programme", on_delete=models.CASCADE)
    SchoolType  = models.ForeignKey(SchoolType, verbose_name="School Type", on_delete=models.CASCADE) 
    Nationality =  models.CharField(max_length=200, verbose_name="Nationality")
    Region =  models.CharField(max_length=200, verbose_name="Region")
    Street =  models.CharField(max_length=200, verbose_name="Street")
    HomeAddress =  models.CharField(max_length=200, verbose_name="Home Address")
    Mobile =  models.CharField(max_length=200, verbose_name="Mobile")
    Religion =  models.CharField(max_length=200, verbose_name="Religion")
    BirthCertificate = models.FileField()
    BirthCertificateUrl = models.URLField(max_length=500, blank=True)
    ResultCertificate = models.FileField(blank=True)
    ResultCertificateUrl = models.URLField(max_length=500, blank=True)
    IsEnable = models.BooleanField(default=True, verbose_name="Is Enabled")
    def __str__(self):
        Fullname = f'{self.FirstName} {self.MiddleName} {self.LastName}'
        return Fullname

Enrolls =(("Enrolled", "Enrolled"),("Not Enrolled", "Not Enrolled"),)
class StudentEnrollment(models.Model):
    RegisteredStudent = models.ForeignKey(RegisteredStudent, verbose_name="Student", on_delete=models.CASCADE, blank=True)
    ClassName = models.ForeignKey(Course, verbose_name="Class", on_delete=models.CASCADE)
    Section = models.ForeignKey(Section, verbose_name="Stream", on_delete=models.CASCADE)
    Programme = models.ForeignKey(Programme, verbose_name="Programme", on_delete=models.CASCADE)
    SchoolType  = models.ForeignKey(SchoolType, verbose_name="School Type", on_delete=models.CASCADE) 
    Hostel = models.ForeignKey(HostelRoom, null=True, verbose_name="Hostel", on_delete=models.CASCADE, blank=True)
    Transport = models.ForeignKey(AssignVehicle,null=True, verbose_name="Transport", on_delete=models.CASCADE, blank=True)
    AcademicYear = models.IntegerField(default="Academic Year")
    Status = models.CharField(max_length=500,default="Not Enrolled",choices=Enrolls)
    def __str__(self):
        Fullname = f'{self.RegisteredStudent.FirstName} {self.RegisteredStudent.MiddleName} {self.RegisteredStudent.LastName}'
        return Fullname

class Parent(models.Model):
    Student = models.ForeignKey(RegisteredStudent, verbose_name="Student", on_delete=models.CASCADE)
    FatherFirstName =  models.CharField(max_length=200, verbose_name="First Name",blank=True)
    FatherMiddleName =  models.CharField(max_length=200, verbose_name="Middle Name",blank=True)
    FatherLastName =  models.CharField(max_length=200, verbose_name="Last Name",blank=True)
    FatherPhoneNumber =  models.CharField(max_length=200, verbose_name="Mobile Number",blank=True)
    FatherOccupation =  models.CharField(max_length=200, verbose_name="Occupation",blank=True)
    FatherHomeAddress =  models.CharField(max_length=200, verbose_name="HomeAddress",blank=True)
    MotherFirstName =  models.CharField(max_length=200, verbose_name="First Name",blank=True)
    MotherMiddleName =  models.CharField(max_length=200, verbose_name="Middle Name",blank=True)
    MotherLastName =  models.CharField(max_length=200, verbose_name="Last Name",blank=True)
    MotherOccupation =  models.CharField(max_length=200, verbose_name="Occupation",blank=True)
    MotherPhoneNumber =  models.CharField(max_length=200, verbose_name="Mobile Number",blank=True)
    MotherHomeAddress=  models.CharField(max_length=200, verbose_name="HomeAddress",blank=True)


class Relative(models.Model):
    Student = models.ForeignKey(RegisteredStudent, verbose_name="Student", on_delete=models.CASCADE)
    RelativeFirstName =  models.CharField(max_length=200, verbose_name="First Name")
    RelativeMiddleName =  models.CharField(max_length=200, verbose_name="Middle Name")
    RelativeLastName =  models.CharField(max_length=200, verbose_name="Last Name")
    RelativeGender =  models.CharField(max_length=200,choices=genders, verbose_name="Gender")
    RelativeRelation =  models.CharField(choices = RelativeRelations, max_length=200, verbose_name="Relation")
    RelativeMobile =  models.CharField(max_length=200, verbose_name="Mobile Number")
    RelativeEmail =  models.CharField(max_length=200, verbose_name="Email",blank=True)
    RelativeHomeAddress =  models.CharField(max_length=200, verbose_name="Home Address")
    RelativeOccupation =  models.CharField(max_length=200, verbose_name="Occupation",blank=True)
    RelativeWorkAddress =  models.CharField(max_length=200, verbose_name="Work Address",blank=True)
   


class StudentAdmission(models.Model):
    AdmissionNumber = models.CharField(max_length=200, verbose_name="Admission Number", blank=True)
    FirstName =  models.CharField(max_length=200, verbose_name="First Name")
    MiddleName =  models.CharField(max_length=200, verbose_name="Middle Name")
    LastName =  models.CharField(max_length=200, verbose_name="Last Name")
    DateOfBirth = models.DateField('Date Of Birth')
    Photo  = models.ImageField()
    PhotoURL = models.URLField(max_length=500, blank=True)
    Gender = models.CharField(max_length=500,choices=genders)
    BirthPlace = models.CharField(max_length=200, verbose_name="Birth Place")
    Health =  models.CharField(max_length=200, choices=Healths, verbose_name="Health")
    ClassName = models.ForeignKey(Course, verbose_name="Class", on_delete=models.CASCADE)
    Programme = models.ForeignKey(Programme, verbose_name="Programme", on_delete=models.CASCADE)
    SchoolType  = models.ForeignKey(SchoolType, verbose_name="School Type", on_delete=models.CASCADE) 
    Nationality =  models.CharField(max_length=200, verbose_name="Nationality")
    Region =  models.CharField(max_length=200, verbose_name="Region")
    Street =  models.CharField(max_length=200, verbose_name="Street")
    HomeAddress =  models.CharField(max_length=200, verbose_name="Home Address")
    Mobile =  models.CharField(max_length=200, verbose_name="Mobile")
    Religion =  models.CharField(max_length=200, verbose_name="Religion")
    AdmissionDate =  models.DateTimeField(auto_now_add=True)
    FormStatus = models.CharField(choices=formStatus, max_length=200,default='Submitted', verbose_name="Form Status",blank=True)
    PaymentStatus = models.CharField(choices=paymentStatus,blank=True, default='Not paid', max_length=200, verbose_name="Form Payment")
    AdmissionStatus = models.CharField(max_length=200,blank=True,default='Waiting', choices=AdmissionStatus, verbose_name="Admission Status")
    RegistrationStatus =  models.CharField(max_length=200, verbose_name="RegistrationStatus",default='Unregistered')
    BirthCertificate = models.FileField()
    BirthCertificateUrl = models.URLField(max_length=500, blank=True)
    ResultCertificate = models.FileField(blank=True)
    ResultCertificateUrl = models.URLField(max_length=500, blank=True)
    
    RelativeFirstName =  models.CharField(max_length=200, verbose_name="First Name")
    RelativeMiddleName =  models.CharField(max_length=200, verbose_name="Middle Name")
    RelativeLastName =  models.CharField(max_length=200, verbose_name="Last Name")
    RelativeGender =  models.CharField(max_length=200,choices=genders, verbose_name="Gender")
    RelativeRelation =  models.CharField(choices = RelativeRelations, max_length=200, verbose_name="Relation")
    RelativeMobile =  models.CharField(max_length=200, verbose_name="Mobile Number")
    RelativeEmail =  models.CharField(max_length=200, verbose_name="Email",blank=True)
    RelativeHomeAddress =  models.CharField(max_length=200, verbose_name="Home Address")
    RelativeOccupation =  models.CharField(max_length=200, verbose_name="Occupation",blank=True)
    RelativeWorkAddress =  models.CharField(max_length=200, verbose_name="Work Address",blank=True)

    FatherFirstName =  models.CharField(max_length=200, verbose_name="First Name",blank=True)
    FatherMiddleName =  models.CharField(max_length=200, verbose_name="Middle Name",blank=True)
    FatherLastName =  models.CharField(max_length=200, verbose_name="Last Name",blank=True)
    FatherPhoneNumber =  models.CharField(max_length=200, verbose_name="Mobile Number",blank=True)
    FatherOccupation =  models.CharField(max_length=200, verbose_name="Occupation",blank=True)
    FatherHomeAddress =  models.CharField(max_length=200, verbose_name="HomeAddress",blank=True)

    MotherFirstName =  models.CharField(max_length=200, verbose_name="First Name",blank=True)
    MotherMiddleName =  models.CharField(max_length=200, verbose_name="Middle Name",blank=True)
    MotherLastName =  models.CharField(max_length=200, verbose_name="Last Name",blank=True)
    MotherOccupation =  models.CharField(max_length=200, verbose_name="Occupation",blank=True)
    MotherPhoneNumber =  models.CharField(max_length=200, verbose_name="Mobile Number",blank=True)
    MotherHomeAddress=  models.CharField(max_length=200, verbose_name="HomeAddress",blank=True)

class Designation(models.Model):
    DesignationName = models.CharField(max_length=200, verbose_name="Designation ")
    def __str__(self):
        return self.DesignationName

class Department(models.Model):
    DepartmentName = models.CharField(max_length=200, verbose_name="Department ")
    def __str__(self):
        return self.DepartmentName

class Role(models.Model):
    RoleName = models.CharField(max_length=200, verbose_name="Department ")
    def __str__(self):
        return self.RoleName


class Staff(models.Model):
    Role =  models.ForeignKey(Role,verbose_name="Role ", on_delete=models.CASCADE)
    DepartmentName =  models.ForeignKey(Department, verbose_name="Department ", on_delete=models.CASCADE)  
    DesignationName =  models.ForeignKey(Designation,verbose_name="Designation", on_delete=models.CASCADE)       
    FirstName =  models.CharField(max_length=200)
    MiddleName =  models.CharField(max_length=200)
    LastName =  models.CharField(max_length=200)
    Phone =  models.CharField(max_length=20)
    Email =  models.CharField(max_length=200, verbose_name="Email",blank=True)
    EmergencePhoneNumber =  models.CharField(max_length=200, verbose_name="Emergence Phone Number")
    DateOfBirth = models.DateField(verbose_name='Date Of Birth')
    JoiningDate = models.DateField(verbose_name='Joining Date')
    Photo  = models.ImageField(upload_to='images/', blank=True)
    #IDCard = models.URLField(max_length=500, blank=True,)
    Gender = models.CharField(max_length=20,choices=genders)
    MaritalStatus = models.CharField(max_length=20,choices=MaritalStatus, verbose_name='Marital Status')
    CurrentAddress =  models.CharField(max_length=200, verbose_name="Current Address",blank=True)
    PermanentAddress =  models.CharField(max_length=200, verbose_name="Permanent Address")
    Qualification =  models.CharField(max_length=200, verbose_name="Qualification")
    WorkExperience =  models.CharField(max_length=200, verbose_name="Working Experience")
    Note =  models.CharField(max_length=200, verbose_name="Note",blank=True)
    MedicalInsuranceNumber =  models.CharField(max_length=200, verbose_name="Medical Insurance Number")
    def __str__(self):
        Fullname = f"{self.FirstName} {self.MiddleName} {self.LastName}"
        return Fullname        

class AttendanceConfiguration(models.Model):
    InTime = models.TimeField( verbose_name="In Time ")
    OutTime = models.TimeField( verbose_name="Out Time")
    TotalHour= models.DecimalField(decimal_places=2,max_digits=3, verbose_name="Total Hour",blank=True)
            
DayInfos =(("Present", "Present"),("Absent", "Absent"),)
class StaffAttendance(models.Model):
    Staff =  models.ForeignKey(Staff,verbose_name="Staff", on_delete=models.CASCADE)
    Date = models.DateTimeField(auto_now_add=True, verbose_name="Date")
    InTime = models.TimeField(verbose_name="In Time")
    OutTime = models.TimeField(verbose_name="Out Time")
    PermissionIn = models.TimeField( verbose_name="Permission In",blank=True,default='00:00:00')
    PermissionOut = models.TimeField( verbose_name="Permission Out",blank=True,default='00:00:00')
    TotalHour= models.DecimalField(decimal_places=2,max_digits=4, verbose_name="Total Hour",blank=True)
    OverTime = models.DecimalField(decimal_places=2,max_digits=4,default = 0, verbose_name="Over Time",blank=True)
    LateSignIn = models.DecimalField(decimal_places=2,max_digits=4,default = 0, verbose_name="Late Sign In",blank=True)
    EarlySignOut= models.DecimalField(decimal_places=2, default = 0, max_digits=4,verbose_name="Early Sign Out",blank=True)
    Remarks =  models.CharField(max_length=200,blank=True)
    DayInfo =  models.CharField(max_length=200, choices=DayInfos)
             
class ProductCategory(models.Model):
    Name = models.CharField(max_length=200, verbose_name="Category Name")
    def __str__(self):
        return self.Name

class Unit(models.Model):
    Name = models.CharField(max_length=200, verbose_name="Unit Name")
    Number = models.IntegerField( verbose_name="Unit Number")
    def __str__(self):
        return self.Name

class Supplier(models.Model):
    Name = models.CharField(max_length=200, verbose_name="Supplier Name")
    MobileNumber = models.CharField(max_length=200, verbose_name="Phone Number")
    OpeningBalance = models.DecimalField(max_digits=65, decimal_places=2, blank=True, null=True,default=0)
    SellerName = models.CharField(max_length=200, verbose_name="Seller Name")
    SellerPhone = models.CharField(max_length=200, verbose_name="Seller Phone")
    EntryDate = models.DateTimeField(verbose_name="Entry Date")
    def __str__(self):
        return self.Name        

Statuses = (('Active', 'Active'), ('Not Active','Not Active'))
class Product(models.Model):
    ProductName = models.CharField(max_length=200, verbose_name="Product Name")
    Category =  models.ForeignKey(ProductCategory,verbose_name="Category", null=True, on_delete=models.CASCADE)
    SystemCategory = models.CharField(max_length=200, null=True, verbose_name="Category",blank=True)
    Unit =  models.ForeignKey(Unit,verbose_name="Unit",null=True, on_delete=models.CASCADE,blank=True)
    Stock = models.IntegerField(blank=True, default=0)
    Size = models.DecimalField(max_digits=30,null=True, decimal_places=2,blank=True)
    SellingPrice = models.DecimalField(max_digits=65,null=True, decimal_places=2, verbose_name="Selling Price",blank=True)
    Color = models.CharField(max_length=200,null=True, verbose_name="Color",blank=True)
    Status = models.CharField(max_length=200, choices=Statuses, default='Active' ,blank=True)
    AgeOrClass = models.CharField(max_length=200,null=True, verbose_name="Age Or Class",blank=True)
    Created = models.DateTimeField(auto_now_add=True,verbose_name="Created at ")
    def __str__(self):
        Name = f'{self.ProductName}: TZS {self.SellingPrice}'
        return self.ProductName

PurchaseTypes = (('Cash', 'Cash'), ('Credit','Credit'))
class Purchase(models.Model):
    PurchaseType = models.CharField(max_length=200, choices=PurchaseTypes, verbose_name="Purchase Type")
    Supplier =  models.ForeignKey(Supplier,verbose_name="Supplier", on_delete=models.CASCADE)
    Amount = models.DecimalField(max_digits=30, decimal_places=2,blank=True, default=0)
    ReceiptNumber = models.CharField(max_length=200, verbose_name="Receipt Number")
    PurchaseDate = models.DateField(verbose_name="Purchase Date ")
    def __str__(self):
        return self.ReceiptNumber                 

class PurchaseItem(models.Model):
    Purchase =  models.ForeignKey(Purchase,blank=True, on_delete=models.CASCADE)
    Product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    Amount = models.DecimalField(max_digits=30, decimal_places=2, blank=True)
    Quantity = models.IntegerField()
    UnitPrice = models.DecimalField(max_digits=30,blank=True, decimal_places=2, verbose_name="Unit Price")
    ExpiryDate = models.DateTimeField(verbose_name="Expiry Date")
    AlertDate = models.DateTimeField(verbose_name="Alert Date")
    def __str__(self):
        return self.Product.ProductName                

class Sale(models.Model):
    SaleType = models.CharField(max_length=200, choices=PurchaseTypes, verbose_name="Sale Type")
    Student =  models.ForeignKey(RegisteredStudent,verbose_name="Student", on_delete=models.CASCADE)
    Amount = models.DecimalField(max_digits=30, decimal_places=2,blank=True, default=0)
    ReceiptNumber = models.CharField(max_length=200, verbose_name="Receipt Number")
    SaleDate = models.DateField(verbose_name="Sale Date ")
    def __str__(self):
        return self.ReceiptNumber        

class SaleItem(models.Model):
    Sale =  models.ForeignKey(Sale,verbose_name="Sale",blank=True, on_delete=models.CASCADE)
    Product =  models.ForeignKey(Product,verbose_name="Product", on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    UnitPrice = models.DecimalField(max_digits=30,blank=True, decimal_places=2, verbose_name="Unit Price")
    Amount = models.DecimalField(max_digits=30, decimal_places=2, blank=True,default=0)
    def __str__(self):
        return self.Product.Name  

class FeeType(models.Model):
    Name = models.CharField(max_length=200)
    def __str__(self):
        return self.Name  

FeeStatuses = (('Cleared', 'Cleared'), ('Uncleared','Uncleared'))
PaymentDurations = (('Monthly', 'Monthly'), ('Quarterly','Quarterly'), ('Full','Full/Installment'))
class FeeCollection(models.Model):
    #PaySlip = models.FileField(blank=True)
    Student =  models.ForeignKey(RegisteredStudent,verbose_name="Student", on_delete=models.CASCADE)
    Amount = models.DecimalField(max_digits=30, decimal_places=2,blank=True, default=0)
    PendingAmount = models.DecimalField(max_digits=30, decimal_places=2,blank=True, default=0)
    ReceiptNumber = models.CharField(max_length=200, verbose_name="Receipt Number",blank=True,default='')
    PaymentDate = models.DateField(verbose_name="Payment Date")
    Status = models.CharField(max_length=200, choices=FeeStatuses,blank=True, default='Uncleared' )
    PaymentDuration = models.CharField(max_length=200,blank=True,choices=PaymentDurations,)
    AcademicYear = models.IntegerField(verbose_name="Academic Year", default=now().year)
    def __str__(self):
        return self.ReceiptNumber                      

class FeeDiscount(models.Model):
    Name = models.CharField(max_length=200)
    Amount = models.DecimalField(max_digits=30, decimal_places=2,blank=True, default=0)
    Description = models.TextField(max_length=200,blank=True, default="")
    def __str__(self):
        return self.Name  

class Fee(models.Model):
    FeeType =  models.ForeignKey(FeeType,verbose_name="Category", on_delete=models.CASCADE)
    Course =  models.ForeignKey(Course,verbose_name="Class",null=True, on_delete=models.CASCADE)
    AcademicYear = models.IntegerField(verbose_name="Academic Year")
    Amount = models.DecimalField(max_digits=30, decimal_places=2,blank=True, default=0)
    Description = models.TextField(max_length=200,blank=True, default="")
    def __str__(self):
        if self.Course == None:
            Name = f'{self.FeeType.Name} : TZS {self.Amount}'
        else:
            Name = f'{self.FeeType.Name} ({self.Course}) : TZS {self.Amount}'
        return Name  


class Monthly(models.Model):
    FeeCollection =  models.ForeignKey(FeeCollection,verbose_name="Fee Collection",default='',blank=True, on_delete=models.CASCADE)
    Amount = models.DecimalField(max_digits=30, decimal_places=2,blank=True, default=0)
    PendingAmount = models.DecimalField(max_digits=30, decimal_places=2,blank=True, default=0)
    Discount =  models.ForeignKey(FeeDiscount,verbose_name="Discount",blank=True,on_delete=models.CASCADE,null = True)
    Fee  =  models.ForeignKey(Fee,verbose_name="Fee", on_delete=models.CASCADE)
    January = models.DecimalField(max_digits=30, decimal_places=2,blank=True, default=0)
    February = models.DecimalField(max_digits=30, decimal_places=2,blank=True, default=0)
    March = models.DecimalField(max_digits=30, decimal_places=2,blank=True, default=0)
    April = models.DecimalField(max_digits=30, decimal_places=2,blank=True, default=0)
    May = models.DecimalField(max_digits=30, decimal_places=2,blank=True, default=0)
    June = models.DecimalField(max_digits=30, decimal_places=2,blank=True, default=0)
    July = models.DecimalField(max_digits=30, decimal_places=2,blank=True, default=0)
    August = models.DecimalField(max_digits=30, decimal_places=2,blank=True, default=0)
    September = models.DecimalField(max_digits=30, decimal_places=2,blank=True, default=0)
    October = models.DecimalField(max_digits=30, decimal_places=2,blank=True, default=0)
    November = models.DecimalField(max_digits=30, decimal_places=2,blank=True, default=0)
    December = models.DecimalField(max_digits=30, decimal_places=2,blank=True, default=0)
    def __str__(self):
        return self.Fee.FeeType.Name  

class Quarterly(models.Model):
    FeeCollection =  models.ForeignKey(FeeCollection,verbose_name="Fee Collection",default='',blank=True, on_delete=models.CASCADE)
    QuarterOne = models.DecimalField(max_digits=30, decimal_places=2,blank=True, default=0)
    QuarterTwo = models.DecimalField(max_digits=30, decimal_places=2,blank=True, default=0)
    QuarterThree = models.DecimalField(max_digits=30, decimal_places=2,blank=True, default=0)
    QuarterFour = models.DecimalField(max_digits=30, decimal_places=2,blank=True, default=0)
    Amount = models.DecimalField(max_digits=30, decimal_places=2,blank=True, default=0)
    PendingAmount = models.DecimalField(max_digits=30, decimal_places=2,blank=True, default=0)
    Discount =  models.ForeignKey(FeeDiscount,blank=True, on_delete=models.CASCADE,null = True)
    Fee  =  models.ForeignKey(Fee,verbose_name="Fee",default='', on_delete=models.CASCADE,blank=True,)
    def __str__(self):
        return self.Fee.FeeType.Name 

class FeeCollectionDetail(models.Model):
    FeeCollection =  models.ForeignKey(FeeCollection,verbose_name="Fee Collection",default='',blank=True, on_delete=models.CASCADE)
    PendingAmount = models.DecimalField(max_digits=30, decimal_places=2,blank=True, default=0)
    Amount = models.DecimalField(max_digits=30, decimal_places=2,blank=True, default=0)
    Discount =  models.ForeignKey(FeeDiscount,verbose_name="Discount",null = True,blank=True, on_delete=models.CASCADE)
    Fee  =  models.ForeignKey(Fee,verbose_name="Fee",default='', on_delete=models.CASCADE,blank=True,)
    def __str__(self):
        return self.Fee.FeeType.Name                           

class Average(models.Model):
    Name = models.CharField(max_length=200)
    Description = models.CharField(max_length=200,blank=True, default='')
    MarksFrom = models.DecimalField(max_digits=30, decimal_places=2, default=0)
    MarksTo = models.DecimalField(max_digits=30, decimal_places=2, default=0)
    def __str__(self):
        return self.Name         

class DivisionGrade(models.Model):
    Name = models.CharField(max_length=200)
    Description = models.CharField(max_length=200,blank=True, default='')
    MarksFrom = models.DecimalField(max_digits=30, decimal_places=2, default=0)
    MarksTo = models.DecimalField(max_digits=30, decimal_places=2, default=0)
    Point = models.IntegerField()
    def __str__(self):
        return self.Name 

class GPAGrade(models.Model):
    Name = models.CharField(max_length=200)
    Description = models.CharField(max_length=200,blank=True, default='')
    MarksFrom = models.DecimalField(max_digits=30, decimal_places=2, default=0)
    MarksTo = models.DecimalField(max_digits=30, decimal_places=2, default=0)
    Point = models.IntegerField()
    def __str__(self):
        return self.Name                  

semesters = (("1st Term", "1st Term"), ("2nd Term", "2nd Term"))
class Examination(models.Model):
    Name = models.CharField(max_length=200)
    StartDate = models.DateField(verbose_name="Start Date")
    EndDate = models.DateField(verbose_name="End Date")
    Semester = models.CharField(max_length=200, choices=semesters)
    def __str__(self):
        Name = f'{self.Name} ({self.Semester})'
        return Name        


status = (("Pass", "Pass"), ("Fail", "Fail"))
resultModes = (("Average", "Average"),("Division", "Division"), ("GPA", "GPA"))
class Result(models.Model):
    Student =  models.ForeignKey(RegisteredStudent, on_delete=models.CASCADE)
    Semester = models.CharField(max_length=200,blank=True,default='')
    Examination =  models.ForeignKey(Examination, on_delete=models.CASCADE) 
    GPA = models.DecimalField(max_digits=30, decimal_places=2,blank=True, default=0)
    Average = models.DecimalField(max_digits=30, decimal_places=2,blank=True, default=0)
    AverageResult = models.CharField(max_length=200,blank=True)
    Division = models.IntegerField(blank=True, default=0)
    Point = models.IntegerField(blank=True, default=0)
    ResultMode = models.CharField(max_length=200, choices=resultModes)
    AcademicYear = models.IntegerField(verbose_name="Academic Year",default=now().year,blank=True)
    Status = models.CharField(max_length=200, choices=status,blank=True)
    Date= models.DateField(verbose_name="End Date", default=now(),blank=True)
    # def __str__(self):
    #     return self.Name                 


class ResultSubject(models.Model):
    Result =  models.ForeignKey(Result, on_delete=models.CASCADE, default=None)
    Subject =  models.CharField(max_length=200)
    Grade = models.CharField(max_length=200,default='')
    Marks = models.DecimalField(max_digits=30, decimal_places=2, default=0)
    def __str__(self):
        return self.Subject    

class Gallery(models.Model):
     Photo  = models.ImageField(upload_to='images/Events/Gallery/')

class Category(models.Model):
       Name =  models.CharField(max_length=50) 

class Event(models.Model):
     Category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.CASCADE)
     Gallery = models.ManyToManyField(Gallery)
     Photo  = models.ImageField(upload_to='images/Events/')
     Title =  models.CharField(max_length=50)
     Description1 =  models.TextField(max_length=200)
     Description2 =  models.TextField(max_length=200, blank=True)
     PublishDate = models.DateTimeField(auto_now_add=True, blank=True)
     def __str__(self):
        return self.Title

class News(models.Model):
     Photo  = models.ImageField(upload_to='images')
     Title =  models.CharField(max_length=50)
     Description1 =  models.TextField(max_length=200)
     Description2 =  models.TextField(max_length=200, blank=True)
     PublishDate = models.DateTimeField(auto_now_add=True, blank=True)
     def __str__(self):
        return self.Title

class FrontPage(models.Model):
     Photo  = models.ImageField(upload_to='images')
     Title =  models.CharField(max_length=50)
     Description1 =  models.TextField(max_length=200)
     PublishDate = models.DateTimeField(auto_now_add=True, blank=True)
     def __str__(self):
        return self.Title   

class Content(models.Model):
     Title =  models.CharField(max_length=100)
     Description1 =  models.TextField(max_length=1000)
#      Sequence = models.IntegerField()
     def __str__(self):
        return self.Title   

class AboutSchool(models.Model):
     Photo  = models.ImageField(upload_to='images')
     Title =  models.CharField(max_length=50)
     Subtitle =  models.CharField(max_length=50, blank=True)
     Mision =  models.TextField(max_length=200, blank=True)
     Vision =  models.TextField(max_length=200, blank=True)
     Description1 =  models.TextField(max_length=200, blank=True)
     def __str__(self):
        return self.Title 