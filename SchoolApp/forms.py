# forms.py
from random import sample
from django import forms
from .models import *
from .widget import DatePickerInput, TimePickerInput, DateTimePickerInput

class courseForm(forms.ModelForm):	
	class Meta:
		model = Course
		fields = '__all__'

	# Section = forms.ModelMultipleChoiceField(
    #     queryset=Section.objects.all(),
    #     widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'})
    # )	
	# Subject = forms.ModelMultipleChoiceField(
    #     queryset=Subject.objects.all(),
    #     widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check'})
    # )	

class SchoolTypeForm(forms.ModelForm):
	class Meta:
		model = SchoolType
		fields = '__all__'		


class StudentForm(forms.ModelForm):
	class Meta:
		model = RegisteredStudent
		fields = '__all__'
		widgets = {
            'DateOfBirth' : DatePickerInput(),
        }

class StudentAdmissionForm(forms.ModelForm):
	class Meta:
		model = StudentAdmission
		fields = '__all__'
		exclude = ('AdmissionNumber','PaymentStatus','BirthCertificateUrl','ResultCertificateUrl','PhotoURL','AdmissionDate','FormStatus','RegistrationStatus')
		widgets = {
            'DateOfBirth' : DatePickerInput(),
        }

class ProgrammeForm(forms.ModelForm):
	class Meta:
		model = Programme
		fields = '__all__'

class SectionForm(forms.ModelForm):
	class Meta:
		model = Section
		fields = '__all__'		


class SubjectForm(forms.ModelForm):
	class Meta:
		model = Subject
		fields = '__all__'

class HostelForm(forms.ModelForm):
	class Meta:
		model = Hostel
		fields = '__all__'

class HostelRoomForm(forms.ModelForm):
	class Meta:
		model = HostelRoom
		fields = '__all__'
		exclude = ('CurrentCapacity','AvailableCapacity')	

class HostelRoomFormTwo(forms.ModelForm):
	class Meta:
		model = HostelRoom
		fields = '__all__'

class RoomTypeForm(forms.ModelForm):
	class Meta:
		model = RoomType
		fields = '__all__'


class RouteForm(forms.ModelForm):
	class Meta:
		model = Route
		fields = '__all__'

class DriverForm(forms.ModelForm):
	class Meta:
		model = Driver
		fields = '__all__'
		widgets = {
            'LicenceExpiryDate' : DatePickerInput(),
        }


class VehicleForm(forms.ModelForm):
	class Meta:
		model = Vehicle
		fields = '__all__'
		exclude = ('CurrentCapacity','AvailableCapacity')

class VehicleUpdateForm(forms.ModelForm):
	class Meta:
		model = Vehicle
		fields = '__all__'

class AssignVehicleForm(forms.ModelForm):
	class Meta:
		model = AssignVehicle
		fields = '__all__'		

class StudentEnrollmentForm(forms.ModelForm):
	class Meta:
		model = StudentEnrollment
		fields = '__all__'	
		#exclude = ('SchoolType',)		

class DesignationForm(forms.ModelForm):
	class Meta:
		model = Designation
		fields = '__all__'	
		#exclude = ('SchoolType',)			

class StaffAttendanceForm(forms.ModelForm):
	class Meta:
		model = StaffAttendance
		fields = '__all__'
		# exclude = ('TotalHour','OverTime','LateSignIn','EarlySignOut')
		widgets = {
            'OutTime' : TimePickerInput(),'InTime' : TimePickerInput(),
			'PermissionIn' : TimePickerInput(),'PermissionOut' : TimePickerInput(),
			'OverTime' : TimePickerInput(),'LateSignIn' : TimePickerInput(),
			'EarlySignOut' : TimePickerInput(),

        }	
		
class StaffForm(forms.ModelForm):
	class Meta:
		model = Staff
		fields = '__all__'
		widgets = {
            'JoiningDate' : DatePickerInput(),'DateOfBirth' : DatePickerInput(),
        }	

class RoleForm(forms.ModelForm):
	class Meta:
		model = Role
		fields = '__all__'

class DepartmentForm(forms.ModelForm):
	class Meta:
		model = Department
		fields = '__all__'

class AttendanceConfigurationForm(forms.ModelForm):
	class Meta:
		model = AttendanceConfiguration
		fields = '__all__'
		
		widgets = {
            'OutTime' : TimePickerInput(),'InTime' : TimePickerInput(),
        }

class ProductCategoryForm(forms.ModelForm):
	class Meta:
		model = ProductCategory
		fields = '__all__'		

class UnitForm(forms.ModelForm):
	class Meta:
		model = Unit
		fields = '__all__'

class SupplierForm(forms.ModelForm):
	class Meta:
		model = Supplier
		fields = '__all__'	
		widgets = {
            'EntryDate' : DatePickerInput(),
        }

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = '__all__'	

class PurchaseForm(forms.ModelForm):
	class Meta:
		model = Purchase
		fields = '__all__'
		widgets = {
            'PurchaseDate' : DatePickerInput(),
        }
		exclude = ('ReceiptNumber',)

class SaleForm(forms.ModelForm):
	class Meta:
		model = Sale
		fields = '__all__'
		widgets = {
            'SaleDate' : DatePickerInput(),
        }
		exclude = ('ReceiptNumber',)

class PurchaseItemForm(forms.ModelForm):
	class Meta:
		model = PurchaseItem
		fields = '__all__'
		widgets = {
            'ExpiryDate' : DatePickerInput(),'AlertDate' : DatePickerInput(),
        }

class SaleItemForm(forms.ModelForm):
	class Meta:
		model = SaleItem
		fields = '__all__'

class FeeTypeForm(forms.ModelForm):
	class Meta:
		model = FeeType
		fields = '__all__'

class FeeDiscountForm(forms.ModelForm):
	class Meta:
		model = FeeDiscount
		fields = '__all__'

class FeeForm(forms.ModelForm):
	class Meta:
		model = Fee
		fields = '__all__'		

class MonthlyForm(forms.ModelForm):
	class Meta:
		model = Monthly
		fields = '__all__'		

class QuarterlyForm(forms.ModelForm):
	class Meta:
		model = Quarterly
		fields = '__all__'		

class FeeCollectionDetailForm(forms.ModelForm):
	class Meta:
		model = FeeCollectionDetail
		fields = '__all__'		

class FeeCollectionForm(forms.ModelForm):
	class Meta:
		model = FeeCollection
		fields = '__all__'
		widgets = {
            'PaymentDate' : DatePickerInput(),
        }		

class AverageForm(forms.ModelForm):
	class Meta:
		model = Average
		fields = '__all__'	

class DivisionGradeForm(forms.ModelForm):
	class Meta:
		model = DivisionGrade
		fields = '__all__'				

class GPAGradeForm(forms.ModelForm):
	class Meta:
		model = GPAGrade
		fields = '__all__'		

class ExaminationForm(forms.ModelForm):
	class Meta:
		model = Examination
		fields = '__all__'
		widgets = {
            'StartDate' : DatePickerInput(),'EndDate' : DatePickerInput(),
        }		

class ResultForm(forms.ModelForm):
	class Meta:
		model = Result
		fields = '__all__'
					

class ResultSubjectForm(forms.ModelForm):
	class Meta:
		model = ResultSubject
		fields = '__all__'		

class GalleryForm(forms.ModelForm):
	class Meta:
		model = Gallery
		fields = '__all__'


class NewsForm(forms.ModelForm):
	class Meta:
		model = News
		fields = '__all__'



class FrontPageForm(forms.ModelForm):
	class Meta:
		model = FrontPage
		fields = '__all__'		

class ContentForm(forms.ModelForm):
	class Meta:
		model = Content
		fields = '__all__'			

class AboutSchoolForm(forms.ModelForm):
	class Meta:
		model = AboutSchool
		fields = '__all__'	