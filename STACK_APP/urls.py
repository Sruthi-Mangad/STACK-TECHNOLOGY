from django.urls import path
from . import views

urlpatterns = [

    # -------------------  common pages ----------------------------------------------
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('single_blog/<int:id>', views.single_blog, name='single_blog'),
    path('courses/', views.courses, name='courses'),
    path('datascience_ai/', views.datascience_ai, name='datascience_ai'),
    path('digital_marketing/', views.digital_marketing, name='digital_marketing'),
    path('graphic_design/', views.graphic_design, name='graphic_design'),
    path('web_development/', views.web_development, name='web_development'),
    path('kids_coding/', views.kids_coding, name='kids_coding'),
    path('internship_project/', views.internship_project, name='internship_project'),
    path('contact_us/', views.contact_us, name='contact_us'),

    #---------------------- login -logout-signup ------------------------------------
    path('admin/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # ------------------ admin ------------------------------------------------------
    # path('header/', views.header, name='header'),
    path('dashboard/', views.Admin_Dashboard, name='dashboard'),

    path('Admin_Courses/', views.Admin_Courses, name='Admin_Courses'),
    path('view_courses/<int:id>/', views.Admin_view_courses, name='view_courses'),
    path('Course_Registration/', views.Admin_Course_Register, name='course_register'),
    path('Course_Update/<int:id>/', views.Edit_Course_Details, name='Course_Update'),
    path('course_delete/<int:id>/', views.Delete_Course_Details, name='course_delete'),
    path('search_course/', views.Search_Course, name='search_course'),

    path('Admin_Testimonial/', views.Admin_Testimonial, name='Admin_Testimonial'),
    path('Testimonial_Registration/', views.Admin_Testimonial_Register, name='testimonial_register'),
    path('view_testimonial/<int:id>/', views.Admin_view_testimonial, name='view_testimonial'),
    path('testimonial_Update/<int:id>/', views.Edit_Testimonial_Details, name='testimonial_Update'),
    path('testimonial_delete/<int:id>/', views.Delete_Testimonial_Details, name='testimonial_delete'),
    path('search_testimonial/', views.Search_Testimonial, name='search_testimonial'),

    path('Admin_Instructors/', views.Admin_Instructors, name='Admin_Instructors'),
    path('Instructors_Registration/', views.Admin_Instructors_Register, name='instructors_register'),
    path('view_instructors/<int:id>/', views.Admin_view_Instructors, name='view_instructors'),
    path('instructors_Update/<int:id>/', views.Edit_Instructors_Details, name='instructors_Update'),
    path('instructors_delete/<int:id>/', views.Delete_Instructors_Details, name='instructors_delete'),
    path('search_instructor/', views.Search_Instructor, name='search_instructor'),

    path('Admin_Features/', views.Admin_Features, name='Admin_Features'),
    path('Feature_Registration/', views.Admin_Feature_Register, name='feature_register'),
    path('view_features/<int:id>/', views.Admin_view_features, name='view_features'),
    path('Features_Update/<int:id>/', views.Edit_Features_Details, name='Features_Update'),
    path('feature_delete/<int:id>/', views.Delete_Feature_Details, name='feature_delete'),
    path('search_feature/', views.Search_Feature, name='search_feature'),

    path('Admin_Blogs/', views.Admin_Blogs, name='Admin_Blogs'),
    path('Blog_Registration/', views.Admin_Blog_Register, name='blog_register'),
    path('view_blog/<int:id>/', views.Admin_view_Blog, name='view_blog'),
    path('Blog_Update/<int:id>/', views.Edit_Blog_Details, name='Blog_Update'),
    path('blog_delete/<int:id>/', views.Delete_Blog_Details, name='blog_delete'),
    path('search_blog/', views.Search_Blog, name='search_blog'),

    path('Admin_Notifications/', views.Admin_Notifications, name='Admin_Notifications'),
    path('delete_notification/<int:id>/', views.delete_notification, name='delete_notification'),
]