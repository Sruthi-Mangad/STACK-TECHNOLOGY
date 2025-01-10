from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q

# Create your views here.

def index(request):
    reviews = TESTIMONIAL.objects.all()
    about = ABOUT_US.objects.all()
    features = FEATURES.objects.all()
    instructors = INSTRUCTORS.objects.all()
    return render(request, 'index.html', locals())


def about(request):
    reviews = TESTIMONIAL.objects.all()
    about = ABOUT_US.objects.all()
    features = FEATURES.objects.all()
    instructors = INSTRUCTORS.objects.all()
    return render(request, 'about.html', locals())


def contact(request):
    return render(request, 'contact.html')


def blog(request):
    data = BLOG.objects.all().order_by('-date')
    course_category = COURSES.objects.all()
    return render(request, 'blog.html', locals())


def single_blog(request, id):
    data = BLOG.objects.filter(id=id)
    course_category = COURSES.objects.all()
    return render(request, 'single-blog.html', locals())


def courses(request):
    instructors = INSTRUCTORS.objects.all()
    return render(request, 'courses.html', locals())


def datascience_ai(request):
    return render(request, 'datascience_ai.html')


def digital_marketing(request):
    return render(request, 'digital_marketing.html')


def graphic_design(request):
    return render(request, 'graphic_design.html')


def web_development(request):
    return render(request, 'web_development.html')


def kids_coding(request):
    return render(request, 'kids_coding.html')


def internship_project(request):
    return render(request, 'index.html')

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        phone = request.POST.get('phone')
        data = CONTACT_US.objects.create(name=name, email=email, message=message, phone=phone)
        data.save()
        messages.success(request, 'Your message has been sent.')
        return redirect('index')
    else:
        return render(request, 'contact.html')
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

# -------------------- LOGIN | SIGN-UP | LOGOUT -------------------------------
# ------------------------------------------------------------------------------

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_superuser == 1:
                login(request, user)
                return redirect('dashboard')
        else:
            messages.add_message(request, messages.WARNING,
                                 'Please verify credentials you entered!'
                                 )
            return redirect('dashboard')
    return render(request,'login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect(index)

# -----------------------------------------------------------------------------

# -------------------------------  ADMIN   ---------------------------------------------
# @login_required
def Admin_Dashboard(request):
    mails = CONTACT_US.objects.filter(status=0)
    mail_count = mails.count()
    staff_count =INSTRUCTORS.objects.all().count()
    courses = COURSES.objects.all()
    courses_count = courses.count()
    enq_count = CONTACT_US.objects.all().count()
    review_count = TESTIMONIAL.objects.all().count()
    return render(request, 'Dash_board.html',locals())


# ------------------------------  COURSES -----------------------------------------------

@login_required
def Admin_Courses(request):
    mails = CONTACT_US.objects.filter(status=0)
    mail_count = mails.count()
    staff_count = INSTRUCTORS.objects.all().count()
    courses_count = COURSES.objects.all().count()
    enq_count = CONTACT_US.objects.all().count()
    review_count = TESTIMONIAL.objects.all().count()

    try:

        data = COURSES.objects.all().order_by('-id')
        return render(request, 'Admin_Courses.html', locals())
    except:

        return render(request, 'Admin_Courses.html',locals())

@login_required
def Admin_view_courses(request, id):
    mails = CONTACT_US.objects.filter(status=0)
    mail_count = mails.count()
    staff_count = INSTRUCTORS.objects.all().count()
    courses_count = COURSES.objects.all().count()
    enq_count = CONTACT_US.objects.all().count()
    review_count = TESTIMONIAL.objects.all().count()

    try:
        data = COURSES.objects.filter(id=id)
        return render(request, 'Admin_courses_details.html', locals())

    except:
        return render(request, 'Admin_courses_details.html',locals())

@login_required
def Admin_Course_Register(request):

    if request.method == 'POST':
        course_id = request.POST['course_id']
        title = request.POST['title']
        description = request.POST['description']
        duration = request.POST['duration']
        category = request.POST['category']
        fee = request.POST['fee']
        image = request.FILES.get('image')

        data = COURSES.objects.create(course_id=course_id,
                                      title=title,
                                      description=description,
                                      duration=duration,
                                      category=category,
                                      fee=fee,
                                      image=image)
        data.save()
        return redirect(Admin_Courses)
    else:
        mails = CONTACT_US.objects.filter(status=0)
        mail_count = mails.count()
        staff_count = INSTRUCTORS.objects.all().count()
        courses_count = COURSES.objects.all().count()
        enq_count = CONTACT_US.objects.all().count()
        review_count = TESTIMONIAL.objects.all().count()
        return render(request,'Courses_Register_Form.html',locals())

@login_required
def Edit_Course_Details(request, id):
    if request.method == 'POST':
        course_id = request.POST['course_id']
        title = request.POST['title']
        description = request.POST['description']
        duration = request.POST['duration']
        category = request.POST['category']
        fee = request.POST['fee']
        image = request.FILES.get('image')
        COURSES.objects.filter(id=id).update(title=title,
                                             description=description,
                                             duration=duration,
                                             category=category,
                                             fee=fee,
                                             course_id=course_id
                                             )
        instance = get_object_or_404(COURSES, id=id)
        if image:
            instance.image = image
        instance.save()
        return redirect(Admin_view_courses,id)
    else:
        data = COURSES.objects.filter(id=id)
        mails = CONTACT_US.objects.filter(status=0)
        mail_count = mails.count()
        staff_count = INSTRUCTORS.objects.all().count()
        courses_count = COURSES.objects.all().count()
        enq_count = CONTACT_US.objects.all().count()
        review_count = TESTIMONIAL.objects.all().count()
        return render(request, 'Course_Edit_Form.html', locals())

@login_required
def Delete_Course_Details(request, id):
    try:
        course = COURSES.objects.get(id=id)
        course.delete()
        return JsonResponse({'message': 'Course deleted successfully'}, status=200)
    except COURSES.DoesNotExist:
        return JsonResponse({'error': 'Course not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@login_required
def Search_Course(request):
    mails = CONTACT_US.objects.filter(status=0)
    mail_count = mails.count()
    if request.method == 'POST':
        s_data = request.POST.get('search')
        # print(s_data)
        # searched = COURSES.objects.filter(title__icontains=s_data )
        searched = COURSES.objects.filter(Q(title__icontains=s_data) | Q(course_id=s_data) | Q(category=s_data))

        # for i in searched:
        #     print(i.title)
        return render(request,'Admin_Courses.html',locals())
    else:
        return render(request,'Admin_Courses.html',locals())

# --------------------------------------FEATURES-----------------------------

@login_required
def Admin_Features(request):
    mails = CONTACT_US.objects.filter(status=0)
    mail_count = mails.count()
    staff_count = INSTRUCTORS.objects.all().count()
    courses_count = COURSES.objects.all().count()
    enq_count = CONTACT_US.objects.all().count()
    review_count = TESTIMONIAL.objects.all().count()
    try:
        data = FEATURES.objects.all().order_by('-id')
        # Assuming data is a queryset of FEATURES objects
        for feature in data:
            feature.shortened_content = feature.content[:30] + '...' if len(feature.content) > 20 else feature.content

        return render(request, 'Admin_Features.html', {'data': data, 'mail_count': mail_count, 'staff_count': staff_count, 'courses_count': courses_count, 'enq_count': enq_count, 'review_count': review_count})
    except Exception as e:
        print("An error occurred:", e)
        data = []  # Empty list if there's an error
        return render(request, 'Admin_Features.html', {'data': data, 'mail_count': mail_count, 'staff_count': staff_count, 'courses_count': courses_count, 'enq_count': enq_count, 'review_count': review_count})

@login_required
def Admin_view_features(request, id):
    mails = CONTACT_US.objects.filter(status=0)
    mail_count = mails.count()
    staff_count = INSTRUCTORS.objects.all().count()
    courses_count = COURSES.objects.all().count()
    enq_count = CONTACT_US.objects.all().count()
    review_count = TESTIMONIAL.objects.all().count()
    try:
        data = FEATURES.objects.filter(id=id)
        return render(request, 'Admin_features_details.html', locals())

    except:
        return render(request, 'Admin_features_details.html',locals())

@login_required
def Admin_Feature_Register(request):

    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        data = FEATURES.objects.create(title=title,
                                      content=content)
        data.save()
        return redirect(Admin_Features)
    else:
        mails = CONTACT_US.objects.filter(status=0)
        mail_count = mails.count()
        staff_count = INSTRUCTORS.objects.all().count()
        courses_count = COURSES.objects.all().count()
        enq_count = CONTACT_US.objects.all().count()
        review_count = TESTIMONIAL.objects.all().count()
        return render(request, 'Feature_Register_Form.html',locals())


@login_required
def Edit_Features_Details(request, id):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        FEATURES.objects.filter(id=id).update(title=title,
                                             content=content)
        return redirect(Admin_view_features,id)
    else:
        mails = CONTACT_US.objects.filter(status=0)
        mail_count = mails.count()
        staff_count = INSTRUCTORS.objects.all().count()
        courses_count = COURSES.objects.all().count()
        enq_count = CONTACT_US.objects.all().count()
        review_count = TESTIMONIAL.objects.all().count()
        try:
            features = FEATURES.objects.get(id=id)
            if features:
                data = FEATURES.objects.filter(id=id)
                return render(request, 'Features_Edit_Form.html', locals())
            else:
                return render(request, 'Features_Edit_Form.html', locals())
        except:
            return render(request, 'Features_Edit_Form.html',locals())

@login_required
def Delete_Feature_Details(request, id):
    try:
        feature = FEATURES.objects.get(id=id)
        feature.delete()
        return JsonResponse({'message': 'Feature deleted successfully'}, status=200)
    except FEATURES.DoesNotExist:
        return JsonResponse({'error': 'Feature not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@login_required
def Search_Feature(request):
    mails = CONTACT_US.objects.filter(status=0)
    mail_count = mails.count()
    if request.method == 'POST':
        s_data = request.POST.get('search')
        print(s_data)
        searched = FEATURES.objects.filter(title__icontains=s_data )
        # for i in searched:
        #     print(i.title)
        for feature in searched:
            feature.shortened_content = feature.content[:30] + '...' if len(feature.content) > 20 else feature.content
        return render(request,'Admin_Features.html',locals())
    else:
        return render(request,'Admin_Features.html',locals())


# ------------------------------ Testimonial --------------------------------------------
@login_required
def Admin_Testimonial(request):
    mails = CONTACT_US.objects.filter(status=0)
    mail_count = mails.count()
    staff_count = INSTRUCTORS.objects.all().count()
    courses_count = COURSES.objects.all().count()
    enq_count = CONTACT_US.objects.all().count()
    review_count = TESTIMONIAL.objects.all().count()
    try:
        data = TESTIMONIAL.objects.all().order_by('-id')
        # Assuming data is a queryset of FEATURES objects
        for feature in data:
            feature.shortened_content = feature.review[:30] + '...' if len(feature.review) > 20 else feature.review

        return render(request, 'Admin_Testimonial.html', locals())
    except Exception as e:
        print("An error occurred:", e)
        data = []  # Empty list if there's an error
        return render(request, 'Admin_Testimonial.html', locals())

@login_required
def Admin_view_testimonial(request, id):
    mails = CONTACT_US.objects.filter(status=0)
    mail_count = mails.count()
    staff_count = INSTRUCTORS.objects.all().count()
    courses_count = COURSES.objects.all().count()
    enq_count = CONTACT_US.objects.all().count()
    review_count = TESTIMONIAL.objects.all().count()
    try:
        data = TESTIMONIAL.objects.filter(id=id)
        return render(request, 'Admin_testimonial_details.html', locals())

    except:
        return render(request, 'Admin_features_details.html',locals())

@login_required
def Admin_Testimonial_Register(request):
    mails = CONTACT_US.objects.filter(status=0)
    mail_count = mails.count()
    staff_count = INSTRUCTORS.objects.all().count()
    courses_count = COURSES.objects.all().count()
    enq_count = CONTACT_US.objects.all().count()
    review_count = TESTIMONIAL.objects.all().count()
    if request.method == 'POST':
        name = request.POST['name']
        uploaded_at = request.POST['uploaded_at']
        review = request.POST['review']
        image = request.FILES.get('image')
        data = TESTIMONIAL.objects.create(name=name,
                                          uploaded_at=uploaded_at,
                                          review=review,
                                          image=image)
        data.save()
        return redirect(Admin_Testimonial)
    else:
        return render(request, 'Testimonial_Register_Form.html',locals())

@login_required
def Edit_Testimonial_Details(request, id):
    if request.method == 'POST':
        name = request.POST['name']
        uploaded_at = request.POST['uploaded_at']
        review = request.POST['review']
        TESTIMONIAL.objects.filter(id=id).update(name=name,
                                             uploaded_at=uploaded_at,
                                                 review=review)
        return redirect(Admin_view_testimonial,id)
    else:
        mails = CONTACT_US.objects.filter(status=0)
        mail_count = mails.count()
        staff_count = INSTRUCTORS.objects.all().count()
        courses_count = COURSES.objects.all().count()
        enq_count = CONTACT_US.objects.all().count()
        review_count = TESTIMONIAL.objects.all().count()
        try:
            features = TESTIMONIAL.objects.get(id=id)
            if features:
                data = TESTIMONIAL.objects.filter(id=id)
                return render(request, 'Testimonial_Edit_Form.html', locals())
            else:
                return render(request, 'Testimonial_Edit_Form.html',locals())
        except:
            return render(request, 'Testimonial_Edit_Form.html',locals())


@login_required
def Delete_Testimonial_Details(request, id):
    try:
        review_data = TESTIMONIAL.objects.get(id=id)
        review_data.delete()
        return JsonResponse({'message': 'Feature deleted successfully'}, status=200)
    except TESTIMONIAL.DoesNotExist:
        return JsonResponse({'error': 'Feature not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@login_required
def Search_Testimonial(request):
    mails = CONTACT_US.objects.filter(status=0)
    mail_count = mails.count()
    if request.method == 'POST':
        s_data = request.POST.get('search')
        # print(s_data)
        searched = TESTIMONIAL.objects.filter(name__icontains=s_data)
        #     print(i.title)
        for feature in searched:
            feature.shortened_content = feature.review[:30] + '...' if len(feature.review) > 20 else feature.review
        return render(request,'Admin_Testimonial.html',locals())
    else:
        return render(request,'Admin_Testimonial.html',locals())


# ---------------------------   INSTRUCTORS -----------------------------------------------------------------
@login_required
def Admin_Instructors(request):
    mails = CONTACT_US.objects.filter(status=0)
    mail_count = mails.count()
    staff_count = INSTRUCTORS.objects.all().count()
    courses_count = COURSES.objects.all().count()
    enq_count = CONTACT_US.objects.all().count()
    review_count = TESTIMONIAL.objects.all().count()
    try:
        data = INSTRUCTORS.objects.all().order_by('-id')
        # for feature in data:
        #     feature.shortened_content = feature.review[:30] + '...' if len(feature.review) > 20 else feature.review

        return render(request, 'Admin_Instructors.html',locals())
    except Exception as e:
        print("An error occurred:", e)
        data = []  # Empty list if there's an error
        return render(request, 'Admin_Instructors.html',locals())

@login_required
def Admin_view_Instructors(request, id):
    mails = CONTACT_US.objects.filter(status=0)
    mail_count = mails.count()
    staff_count = INSTRUCTORS.objects.all().count()
    courses_count = COURSES.objects.all().count()
    enq_count = CONTACT_US.objects.all().count()
    review_count = TESTIMONIAL.objects.all().count()
    try:
        data = INSTRUCTORS.objects.filter(id=id)
        return render(request, 'Admin_Instructors_details.html', locals())

    except:
        return render(request, 'Admin_Instructors_details.html',locals())

@login_required
def Admin_Instructors_Register(request):
    mails = CONTACT_US.objects.filter(status=0)
    mail_count = mails.count()
    staff_count = INSTRUCTORS.objects.all().count()
    courses_count = COURSES.objects.all().count()
    enq_count = CONTACT_US.objects.all().count()
    review_count = TESTIMONIAL.objects.all().count()
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        designation = request.POST['designation']
        specialization = request.POST['specialization']
        image = request.FILES.get('image')
        name = fname + " " + lname
        data = INSTRUCTORS.objects.create(name=name,
                                          email=email,
                                          phone=phone,
                                          address=address,
                                          designation=designation,
                                          specialization=specialization,
                                          profile=image)
        data.save()
        return redirect(Admin_Instructors)
    else:
        return render(request, 'Instructors_Register_Form.html',locals())

@login_required
def Edit_Instructors_Details(request, id):
    mails = CONTACT_US.objects.filter(status=0)
    mail_count = mails.count()
    staff_count = INSTRUCTORS.objects.all().count()
    courses_count = COURSES.objects.all().count()
    enq_count = CONTACT_US.objects.all().count()
    review_count = TESTIMONIAL.objects.all().count()
    if request.method == 'POST':

        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        designation = request.POST['designation']
        specialization = request.POST['specialization']
        image_file = request.FILES.get('image')
        name = fname + " " + lname
        INSTRUCTORS.objects.filter(id=id).update(name=name,
                                                 email=email,
                                                 phone=phone,
                                                 address=address,
                                                 designation=designation,
                                                 specialization=specialization
                                                 )
        instance = get_object_or_404(INSTRUCTORS, id=id)
        if image_file:
            instance.profile = image_file
        instance.save()
        return redirect(Admin_view_Instructors,id)
    else:
        try:
            features = INSTRUCTORS.objects.get(id=id)
            if features:
                data = INSTRUCTORS.objects.filter(id=id)
                for i in data:
                    name = i.name
                first_name, last_name = name.split()
                return render(request, 'Instructors_Edit_Form.html', locals())
            else:
                return render(request, 'Instructors_Edit_Form.html',locals())
        except:
            return render(request, 'Instructors_Edit_Form.html',locals())

@login_required
def Delete_Instructors_Details(request, id):
    try:
        data = INSTRUCTORS.objects.get(id=id)
        data.delete()
        return JsonResponse({'message': 'Feature deleted successfully'}, status=200)
    except TESTIMONIAL.DoesNotExist:
        return JsonResponse({'error': 'Feature not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@login_required
def Search_Instructor(request):
    mails = CONTACT_US.objects.filter(status=0)
    mail_count = mails.count()
    if request.method == 'POST':
        s_data = request.POST.get('search')
        # print(s_data)
        searched = INSTRUCTORS.objects.filter(name__icontains=s_data)
        # #     print(i.title)
        # for feature in searched:
        #     feature.shortened_content = feature.review[:30] + '...' if len(feature.review) > 20 else feature.review
        return render(request,'Admin_Instructors.html',locals())
    else:
        return render(request,'Admin_Instructors.html',locals())


# -------------------------------------  blog  ---------------------------------------------
@login_required
def Admin_Blogs(request):
    mails = CONTACT_US.objects.filter(status=0)
    mail_count = mails.count()
    staff_count = INSTRUCTORS.objects.all().count()
    courses_count = COURSES.objects.all().count()
    enq_count = CONTACT_US.objects.all().count()
    review_count = TESTIMONIAL.objects.all().count()
    try:
        data = BLOG.objects.all().order_by('-id')
        for detail in data:
            detail.shortened_content = detail.description[:30] + '...' if len(detail.description) > 20 else detail.description
        return render(request, 'Admin_Blogs.html', locals())
    except Exception as e:
        print("An error occurred:", e)
        data = []  # Empty list if there's an error
        return render(request, 'Admin_Blogs.html',locals())

@login_required
def Admin_Blog_Register(request):
    mails = CONTACT_US.objects.filter(status=0)
    mail_count = mails.count()
    staff_count = INSTRUCTORS.objects.all().count()
    courses_count = COURSES.objects.all().count()
    enq_count = CONTACT_US.objects.all().count()
    review_count = TESTIMONIAL.objects.all().count()
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        date = request.POST['date']
        author = request.POST['author']
        image = request.FILES.get('image')
        data = BLOG.objects.create(title=title,
                                   image=image,
                                   description=description,
                                   date=date,
                                   author=author)

        data.save()
        return redirect(Admin_Blogs)
    else:
        return render(request, 'Blog_Register_Form.html',locals())

@login_required
def Admin_view_Blog(request, id):
    mails = CONTACT_US.objects.filter(status=0)
    mail_count = mails.count()
    staff_count = INSTRUCTORS.objects.all().count()
    courses_count = COURSES.objects.all().count()
    enq_count = CONTACT_US.objects.all().count()
    review_count = TESTIMONIAL.objects.all().count()
    try:
        data = BLOG.objects.filter(id=id)
        return render(request, 'Admin_Blog_details.html', locals())

    except:
        return render(request, 'Admin_Blog_details.html',locals())

@login_required
def Edit_Blog_Details(request, id):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        date = request.POST['date']
        author = request.POST['author']
        image_file = request.FILES.get('image')
        BLOG.objects.filter(id=id).update(title=title,
                                          description=description,
                                          author=author)
        instance = get_object_or_404(BLOG, id=id)
        if image_file:
            instance.image = image_file
        if date:
            instance.date = date
        instance.save()
        return redirect(Admin_view_Blog,id)
    else:
        mails = CONTACT_US.objects.filter(status=0)
        mail_count = mails.count()
        staff_count = INSTRUCTORS.objects.all().count()
        courses_count = COURSES.objects.all().count()
        enq_count = CONTACT_US.objects.all().count()
        review_count = TESTIMONIAL.objects.all().count()
        try:
            blog_data = BLOG.objects.get(id=id)
            if blog_data:
                data = BLOG.objects.filter(id=id)

                return render(request, 'Blog_Edit_Form.html', locals())
            else:
                return render(request, 'Blog_Edit_Form.html',locals())
        except:
            return render(request, 'Blog_Edit_Form.html',locals())

@login_required
def Delete_Blog_Details(request, id):
    try:
        data = BLOG.objects.get(id=id)
        data.delete()
        return JsonResponse({'message': 'Feature deleted successfully'}, status=200)
    except BLOG.DoesNotExist:
        return JsonResponse({'error': 'Feature not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@login_required
def Search_Blog(request):
    mails = CONTACT_US.objects.filter(status=0)
    mail_count = mails.count()
    if request.method == 'POST':
        s_data = request.POST.get('search')
        # print(s_data)
        searched = BLOG.objects.filter(title__icontains=s_data)
        # #     print(i.title)
        for feature in searched:
            feature.shortened_content = feature.description[:30] + '...' if len(feature.description) > 20 else feature.description
        return render(request,'Admin_Blogs.html',locals())
    else:
        return render(request,'Admin_Blogs.html',locals())


@login_required
def Admin_Notifications(request):

    try:
        mails = CONTACT_US.objects.filter(status=0)
        mail_count = mails.count()
        data = CONTACT_US.objects.all().order_by('-date')

        def Mark_as_read(data):
            for i in data:
                if i.status == 0:
                    i.status = 1
                    i.save()
                # print(i.status)
        Mark_as_read(data)
        return render(request, 'Admin_Notifications.html', locals())
    except:
        mails = CONTACT_US.objects.filter(status=0)
        mail_count = mails.count()
        return render(request, 'Admin_Notifications.html',locals())

@login_required
def delete_notification(request,id):
    try:
        data = CONTACT_US.objects.get(id=id)
        data.delete()
        return redirect(Admin_Notifications)
    except:
        return redirect(Admin_Notifications)
