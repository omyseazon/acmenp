from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include

urlpatterns = [
      
       #Programme urls
      path('Programme', views.ProgrammeView, name = 'Programme'),
      path('createProgramme', views.createProgramme, name = 'createProgramme'),
      path('updateProgramme/<int:pk>', views.editProgramme, name = 'updateProgramme'),
      path('deleteProgramme/<int:pk>', views.deleteProgramme, name='deleteProgramme'),

        #Section urls
      path('Section', views.SectionView, name = 'Section'),
      path('createSection', views.createSection, name = 'createSection'),
      path('updateSection/<int:pk>', views.editSection, name = 'updateSection'),
      path('deleteSection/<int:pk>', views.deleteSection, name='deleteSection'),

      #Subject urls
      path('Subject', views.SubjectView, name = 'Subject'),
      path('createSubject', views.createSubject, name = 'createSubject'),
      path('updateSubject/<int:pk>', views.editSubject, name = 'updateSubject'),
      path('deleteSubject/<int:pk>', views.deleteSubject, name='deleteSubject'),

      #course urls
      path('course', views.courseView, name = 'course'),
      path('create', views.createCourse, name = 'create'),
      path('update/<int:pk>', views.editcourse, name = 'update'),
      path('delete/<int:pk>', views.deletecourse, name='delete'),

      #school type urls
      path('SchoolType', views.SchoolTypeView, name = 'SchoolType'),
      path('createSchoolType', views.createSchoolType, name = 'createSchoolType'),
      path('updateSchoolType/<int:pk>', views.editSchoolType, name = 'updateSchoolType'),
      path('deleteSchoolType/<int:pk>', views.deleteSchoolType, name='deleteSchoolType'),

         #StudentAdmission urls
      path('StudentAdmission', views.StudentAdmissionView, name = 'StudentAdmission'),
      path('createStudentAdmission', views.createStudentAdmission, name = 'createStudentAdmission'),
      path('updateStudentAdmission/<int:pk>', views.editStudentAdmission, name = 'updateStudentAdmission'),
      path('deleteStudentAdmission/<int:pk>', views.deleteStudentAdmission, name='deleteStudentAdmission'),


      #student urls
      path('Student', views.StudentView, name = 'Student'),
      path('createStudent', views.createStudent, name = 'createStudent'),
      path('updateStudent/<int:pk>', views.editStudent, name = 'updateStudent'),
      path('deleteStudent/<int:pk>', views.deleteStudent, name='deleteStudent'),

      
      #Hostel urls
      path('Hostel', views.HostelView, name = 'Hostel'),
      path('createHostel', views.createHostel, name = 'createHostel'),
      path('updateHostel/<int:pk>', views.editHostel, name = 'updateHostel'),
      path('deleteHostel/<int:pk>', views.deleteHostel, name='deleteHostel'),

      #RoomType urls
      path('RoomType', views.RoomTypeView, name = 'RoomType'),
      path('createRoomType', views.createRoomType, name = 'createRoomType'),
      path('updateRoomType/<int:pk>', views.editRoomType, name = 'updateRoomType'),
      path('deleteRoomType/<int:pk>', views.deleteRoomType, name='deleteRoomType'),

      #HostelRoom urls
      path('HostelRoom', views.HostelRoomView, name = 'HostelRoom'),
      path('createHostelRoom', views.createHostelRoom, name = 'createHostelRoom'),
      path('updateHostelRoom/<int:pk>', views.editHostelRoom, name = 'updateHostelRoom'),
      path('deleteHostelRoom/<int:pk>', views.deleteHostelRoom, name='deleteHostelRoom'),


      #Route urls
      path('Route', views.RouteView, name = 'Route'),
      path('createRoute', views.createRoute, name = 'createRoute'),
      path('updateRoute/<int:pk>', views.editRoute, name = 'updateRoute'),
      path('deleteRoute/<int:pk>', views.deleteRoute, name='deleteRoute'),

      #Driver urls
      path('Driver', views.DriverView, name = 'Driver'),
      path('createDriver', views.createDriver, name = 'createDriver'),
      path('updateDriver/<int:pk>', views.editDriver, name = 'updateDriver'),
      path('deleteDriver/<int:pk>', views.deleteDriver, name='deleteDriver'),


      #Vehicle urls
      path('Vehicle', views.VehicleView, name = 'Vehicle'),
      path('createVehicle', views.createVehicle, name = 'createVehicle'),
      path('updateVehicle/<int:pk>', views.editVehicle, name = 'updateVehicle'),
      path('deleteVehicle/<int:pk>', views.deleteVehicle, name='deleteVehicle'),

      #AssignVehicle urls
      path('AssignVehicle', views.AssignVehicleView, name = 'AssignVehicle'),
      path('createAssignVehicle', views.createAssignVehicle, name = 'createAssignVehicle'),
      path('updateAssignVehicle/<int:pk>', views.editAssignVehicle, name = 'updateAssignVehicle'),
      path('deleteAssignVehicle/<int:pk>', views.deleteAssignVehicle, name='deleteAssignVehicle'),

       #StudentEnrollment urls
      path('StudentEnrollment', views.StudentEnrollmentView, name = 'StudentEnrollment'),
      path('createStudentEnrollment', views.createStudentEnrollment, name = 'createStudentEnrollment'),
      path('updateStudentEnrollment/<int:pk>', views.editStudentEnrollment, name = 'updateStudentEnrollment'),
      path('deleteStudentEnrollment/<int:pk>', views.deleteStudentEnrollment, name='deleteStudentEnrollment'),

      #Designation urls
      path('Designation', views.DesignationView, name = 'Designation'),
      path('createDesignation', views.createDesignation, name = 'createDesignation'),
      path('updateDesignation/<int:pk>', views.editDesignation, name = 'updateDesignation'),
      path('deleteDesignation/<int:pk>', views.deleteDesignation, name='deleteDesignation'),

      #Department urls
      path('Department', views.DepartmentView, name = 'Department'),
      path('createDepartment', views.createDepartment, name = 'createDepartment'),
      path('updateDepartment/<int:pk>', views.editDepartment, name = 'updateDepartment'),
      path('deleteDepartment/<int:pk>', views.deleteDepartment, name='deleteDepartment'),

      #Role urls
      path('Role', views.RoleView, name = 'Role'),
      path('createRole', views.createRole, name = 'createRole'),
      path('updateRole/<int:pk>', views.editRole, name = 'updateRole'),
      path('deleteRole/<int:pk>', views.deleteRole, name='deleteRole'),

      #Staff urls
      path('Staff', views.StaffView, name = 'Staff'),
      path('createStaff', views.createStaff, name = 'createStaff'),
      path('updateStaff/<int:pk>', views.editStaff, name = 'updateStaff'),
      path('deleteStaff/<int:pk>', views.deleteStaff, name='deleteStaff'),

      #AttendanceConfiguration urls
      path('AttendanceConfiguration', views.AttendanceConfigurationView, name = 'AttendanceConfiguration'),
      path('createAttendanceConfiguration', views.createAttendanceConfiguration, name = 'createAttendanceConfiguration'),
      path('updateAttendanceConfiguration/<int:pk>', views.editAttendanceConfiguration, name = 'updateAttendanceConfiguration'),
      path('deleteAttendanceConfiguration/<int:pk>', views.deleteAttendanceConfiguration, name='deleteAttendanceConfiguration'),

      #StaffAttendance urls
      path('StaffAttendance', views.StaffAttendanceView, name = 'StaffAttendance'),
      path('createStaffAttendance', views.createStaffAttendance, name = 'createStaffAttendance'),
      path('updateStaffAttendance/<int:pk>', views.editStaffAttendance, name = 'updateStaffAttendance'),
      path('deleteStaffAttendance/<int:pk>', views.deleteStaffAttendance, name='deleteStaffAttendance'),
      
       #Unit urls
      path('Unit', views.UnitView, name = 'Unit'),
      path('createUnit', views.createUnit, name = 'createUnit'),
      path('updateUnit/<int:pk>', views.editUnit, name = 'updateUnit'),
      path('deleteUnit/<int:pk>', views.deleteUnit, name='deleteUnit'),

       #ProductCategory urls
      path('ProductCategory', views.ProductCategoryView, name = 'ProductCategory'),
      path('createProductCategory', views.createProductCategory, name = 'createProductCategory'),
      path('updateProductCategory/<int:pk>', views.editProductCategory, name = 'updateProductCategory'),
      path('deleteProductCategory/<int:pk>', views.deleteProductCategory, name='deleteProductCategory'),

      #Supplier urls
      path('Supplier', views.SupplierView, name = 'Supplier'),
      path('createSupplier', views.createSupplier, name = 'createSupplier'),
      path('updateSupplier/<int:pk>', views.editSupplier, name = 'updateSupplier'),
      path('deleteSupplier/<int:pk>', views.deleteSupplier, name='deleteSupplier'),

      #Product urls
      path('Product', views.ProductView, name = 'Product'),
      path('createProduct', views.createProduct, name = 'createProduct'),
      path('updateProduct/<int:pk>', views.editProduct, name = 'updateProduct'),
      path('deleteProduct/<int:pk>', views.deleteProduct, name='deleteProduct'),

      #Purchase urls
      path('Purchase', views.PurchaseView, name = 'Purchase'),
      path('createPurchase', views.createPurchase, name = 'createPurchase'),
      path('updatePurchase/<int:pk>', views.editPurchase, name = 'updatePurchase'),
      path('updatePurchaseItem/<int:pk>', views.editPurchaseItem, name = 'updatePurchaseItem'),
      path('deletePurchaseItem/<int:pk>', views.deletePurchaseItem, name='deletePurchaseItem'),
      path('deletePurchase/<int:pk>', views.deletePurchase, name='deletePurchase'),

      #Sale urls
      path('Sale', views.SaleView, name = 'Sale'),
      path('createSale', views.createSale, name = 'createSale'),
      path('updateSale/<int:pk>', views.editSale, name = 'updateSale'),
      path('deleteSale/<int:pk>', views.deleteSale, name='deleteSale'),
      path('updateSaleItem/<int:pk>', views.editSaleItem, name = 'updateSaleItem'),
      path('deleteSaleItem/<int:pk>', views.deleteSaleItem, name='deleteSaleItem'),

      #FeeType urls
      path('FeeType', views.FeeTypeView, name = 'FeeType'),
      path('createFeeType', views.createFeeType, name = 'createFeeType'),
      path('updateFeeType/<int:pk>', views.editFeeType, name = 'updateFeeType'),
      path('deleteFeeType/<int:pk>', views.deleteFeeType, name='deleteFeeType'),

      #FeeDiscount urls
      path('FeeDiscount', views.FeeDiscountView, name = 'FeeDiscount'),
      path('createFeeDiscount', views.createFeeDiscount, name = 'createFeeDiscount'),
      path('updateFeeDiscount/<int:pk>', views.editFeeDiscount, name = 'updateFeeDiscount'),
      path('deleteFeeDiscount/<int:pk>', views.deleteFeeDiscount, name='deleteFeeDiscount'),

      #Fee urls
      path('Fee', views.FeeView, name = 'Fee'),
      path('createFee', views.createFee, name = 'createFee'),
      path('updateFee/<int:pk>', views.editFee, name = 'updateFee'),
      path('deleteFee/<int:pk>', views.deleteFee, name='deleteFee'),

      #FeeCollection urls
      path('FeeCollection', views.FeeCollectionView, name = 'FeeCollection'),
      path('createFeeCollection', views.createFeeCollection, name = 'createFeeCollection'),
      path('updateFeeCollection/<int:pk>', views.editFeeCollection, name = 'updateFeeCollection'),
      path('deleteFeeCollection/<int:pk>', views.deleteFeeCollection, name='deleteFeeCollection'),
      path('updateFeeCollectionDetail/<int:pk>', views.editFeeCollectionDetail, name = 'updateFeeCollectionDetail'),
      path('deleteFeeCollectionDetail/<int:pk>', views.deleteFeeCollectionDetail, name='deleteFeeCollectionDetail'),
      path('updateMonthly/<int:pk>', views.editMonthly, name = 'updateMonthly'),
      path('deleteMonthly/<int:pk>', views.deleteMonthly, name='deleteMonthly'),
      path('updateQuarterly/<int:pk>', views.editQuarterly, name = 'updateQuarterly'),
      path('deleteQuarterly/<int:pk>', views.deleteQuarterly, name='deleteQuarterly'),

      #Average urls
      path('Average', views.AverageView, name = 'Average'),
      path('createAverage', views.createAverage, name = 'createAverage'),
      path('updateAverage/<int:pk>', views.editAverage, name = 'updateAverage'),
      path('deleteAverage/<int:pk>', views.deleteAverage, name='deleteAverage'),

      #DivisionGrade urls
      path('DivisionGrade', views.DivisionGradeView, name = 'DivisionGrade'),
      path('createDivisionGrade', views.createDivisionGrade, name = 'createDivisionGrade'),
      path('updateDivisionGrade/<int:pk>', views.editDivisionGrade, name = 'updateDivisionGrade'),
      path('deleteDivisionGrade/<int:pk>', views.deleteDivisionGrade, name='deleteDivisionGrade'),

      #GPAGrade urls
      path('GPAGrade', views.GPAGradeView, name = 'GPAGrade'),
      path('createGPAGrade', views.createGPAGrade, name = 'createGPAGrade'),
      path('updateGPAGrade/<int:pk>', views.editGPAGrade, name = 'updateGPAGrade'),
      path('deleteGPAGrade/<int:pk>', views.deleteGPAGrade, name='deleteGPAGrade'),

      #Examination urls
      path('Examination', views.ExaminationView, name = 'Examination'),
      path('createExamination', views.createExamination, name = 'createExamination'),
      path('updateExamination/<int:pk>', views.editExamination, name = 'updateExamination'),
      path('deleteExamination/<int:pk>', views.deleteExamination, name='deleteExamination'),

       #Result urls
      path('Result', views.ResultView, name = 'Result'),
      path('createResult', views.createResult, name = 'createResult'),
      path('updateResult/<int:pk>', views.editResult, name = 'updateResult'),
      path('deleteResult/<int:pk>', views.deleteResult, name='deleteResult'),
      path('updateResultSubject/<int:pk>', views.editResultSubject, name = 'updateResultSubject'),
      path('deleteResultSubject/<int:pk>', views.deleteResultSubject, name='deleteResultSubject'),
     
         #Gallery urls
      path('Gallery', views.GalleryView, name = 'Gallery'),
      path('createGallery', views.createGallery, name = 'createGallery'),
      path('updateGallery/<int:pk>', views.editGallery, name = 'updateGallery'),
      path('deleteGallery/<int:pk>', views.deleteGallery, name='deleteGallery'),

        #News urls
      path('News', views.NewsView, name = 'News'),
      path('createNews', views.createNews, name = 'createNews'),
      path('updateNews/<int:pk>', views.editNews, name = 'updateNews'),
      path('deleteNews/<int:pk>', views.deleteNews, name='deleteNews'),

       #FrontPage urls
      path('FrontPage', views.FrontPageView, name = 'FrontPage'),
      path('createFrontPage', views.createFrontPage, name = 'createFrontPage'),
      path('updateFrontPage/<int:pk>', views.editFrontPage, name = 'updateFrontPage'),
      path('deleteFrontPage/<int:pk>', views.deleteFrontPage, name='deleteFrontPage'),
      
      #AboutSchool urls
      path('AboutSchool', views.AboutSchoolView, name = 'AboutSchool'),
      path('createAboutSchool', views.createAboutSchool, name = 'createAboutSchool'),
      path('updateAboutSchool/<int:pk>', views.editAboutSchool, name = 'updateAboutSchool'),
      path('deleteAboutSchool/<int:pk>', views.deleteAboutSchool, name='deleteAboutSchool'),

       #Content urls
      path('Content', views.ContentView, name = 'Content'),
      path('createContent', views.createContent, name = 'createContent'),
      path('updateContent/<int:pk>', views.editContent, name = 'updateContent'),
      path('deleteContent/<int:pk>', views.deleteContent, name='deleteContent'),

      #basic urls
      path('dashboard', views.index, name='index'),
      path('', views.home, name='home'),
      path('accounts/', include('django.contrib.auth.urls')),
      path('publicGallery', views.publicGallery, name='publicGallery'),
    # path('update/<str:pk>/', views.updatingTask, name='update'),
    # path('delete/<str:pk>/', views.deleteTask, name='delete'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)