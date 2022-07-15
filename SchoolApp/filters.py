import django_filters
from django_filters import DateFilter
from .models import *

class StudentAdmissionFilter(django_filters.FilterSet):
    class Meta:
        #minimum of two attr
        model = StudentAdmission
        
        #2) all & exclude(override all)
        fields = ('AdmissionNumber','Programme','ClassName', 'SchoolType')


class StudentEnrollFilter(django_filters.FilterSet):
    class Meta:
        #minimum of two attr
        model = StudentEnrollment        
        #2) all & exclude(override all)
        fields = ('AcademicYear','RegisteredStudent','SchoolType','Programme','ClassName', )

class DesignationFilter(django_filters.FilterSet):
	class Meta:
		model = Designation
		fields = '__all__'	
		#exclude = ('SchoolType',)			

class StaffAttendanceFilter(django_filters.FilterSet):
	class Meta:
		model = StaffAttendance
		fields = ('Date','Staff')	
		
class StaffFilter(django_filters.FilterSet):
	class Meta:
		model = Staff
		fields = ('DepartmentName','FirstName','MiddleName','LastName')	

class RoleFilter(django_filters.FilterSet):
	class Meta:
		model = Role
		fields = '__all__'

class DepartmentFilter(django_filters.FilterSet):
	class Meta:
		model = Department
		fields = '__all__'

class ProductCategoryFilter(django_filters.FilterSet):
	class Meta:
		model = ProductCategory
		fields = '__all__'	

class UnitFilter(django_filters.FilterSet):
	class Meta:
		model = Unit
		fields = '__all__'	

class SupplierFilter(django_filters.FilterSet):
	class Meta:
		model = Supplier
		fields = ('Name',)		

class ProductFilter(django_filters.FilterSet):
	class Meta:
		model = Product
		fields = ('ProductName',)			

class PurchaseFilter(django_filters.FilterSet):
	class Meta:
		model = Purchase
		fields = ('ReceiptNumber',)			

class SaleFilter(django_filters.FilterSet):
	class Meta:
		model = Sale
		fields = ('ReceiptNumber',)	

class FeeTypeFilter(django_filters.FilterSet):
	class Meta:
		model = FeeType
		fields = '__all__'			

class FeeDiscountFilter(django_filters.FilterSet):
	class Meta:
		model = FeeDiscount
		fields = '__all__'	

class FeeFilter(django_filters.FilterSet):
	class Meta:
		model = Fee
		fields = '__all__'				

class FeeCollectionFilter(django_filters.FilterSet):
	class Meta:
		model = FeeCollection
		fields = ('AcademicYear',)

class AverageFilter(django_filters.FilterSet):
	class Meta:
		model = Average
		fields = '__all__'		

class DivisionGradeFilter(django_filters.FilterSet):
	class Meta:
		model = DivisionGrade
		fields = '__all__'						

class GPAGradeFilter(django_filters.FilterSet):
	class Meta:
		model = GPAGrade
		fields = '__all__'			

class ExaminationFilter(django_filters.FilterSet):
	class Meta:
		model = Examination
		fields = '__all__'			

class ResultFilter(django_filters.FilterSet):
	class Meta:
		model = Result
		fields = ('AcademicYear',)

class NewsFilter(django_filters.FilterSet):
    class Meta:
        #minimum of two attr
        model = News
        #2) all & exclude(override all)
        fields = ('Title',)