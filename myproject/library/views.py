from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.utils.timezone import now
from .models import users,attendance
from .models import booktype,booksubjects
from .models import bookcategory


# Create your views here.
def index(request):
    return render(request,"index.html")

def registration(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('uemail')
        mobile=request.POST.get('umobile')
        username=request.POST.get('uname')
        password=request.POST.get('upass')
        users.objects.create(name=name,uemail=email,umobile=mobile,uname=username,upass=password)
        return HttpResponse("<h1>You Have Registered Successfully</h1>")
    else:
        return render(request,'registration.html')

def show(request):
    user=users.objects.values('id','user_id','name','uemail','umobile','uname','upass','is_deleted','status','user_type')
    return render(request,"show.html",{"users":user})


def login(request):
    if request.method=='POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        try:
            user=users.objects.get(uname=username,upass=password)
            if(user.uname==username and user.upass==password):
                if(user.user_type=='1'):
                    return redirect("/staff/")
                if(user.user_type=='0'):
                    return redirect("/admindas/")
                if(user_type=='2'):
                    return redirect("/student/")
        except users.DoesNotExist:
            messages.error(request,"Invalid username or password")
        except Exception as e:
            messages.error(request,f" May be your account is inactive or An error has occurred:{str(e)}")
    return render(request,"login.html") 
    
    
    
def admindas(request):
    return render(request,'admin.html')


def edits(request):
    users_list = users.objects.values('id', 'name', 'uemail', 'umobile', 'uname', 'upass', 'status', 'user_type')

    # When the form is submitted to update data
    if request.method == 'POST':
        for user in users_list:
            print(user["id"])
            # Check if the edit button for this user was clicked
            if f'edit_{user["id"]}' in request.POST:
                # Retrieve the updated data from the form
                updated_name = request.POST.get(f'name_{user["id"]}')
                updated_uemail = request.POST.get(f'uemail_{user["id"]}')
                updated_umobile = request.POST.get(f'umobile_{user["id"]}')
                updated_uname = request.POST.get(f'uname_{user["id"]}')
                updated_upass = request.POST.get(f'upass_{user["id"]}')
                updated_status = request.POST.get(f'status_{user["id"]}')
                updated_user_type = request.POST.get(f'user_type_{user["id"]}')
                
                # Update the user's record
                userupdate = users.objects.get(id=user["id"])  # Get the user instance from the database
                userupdate.name = updated_name
                userupdate.uemail = updated_uemail
                userupdate.umobile = updated_umobile
                userupdate.uname = updated_uname
                userupdate.upass = updated_upass
                userupdate.status = updated_status
                userupdate.user_type = updated_user_type
                
                # Save the updated user record to the database
                userupdate.save()
                messages.success(request,f"Successfully Updated record{updated_name}.")
        # After the update, redirect to the show page to refresh the data
        return redirect('edits')

    return render(request, 'edit.html', {'users': users_list})

def student(request):
    return render(request,"student.html")

def staff(request):
    return render(request,"staff.html")

def attendances(request):
    attendance_record=None
    if request.method=="POST":
        user_id=request.POST.get("user_id")
        uname=request.POST.get("uname")
        out_time=request.POST.get("out_time")
        if user_id and uname:
            current_date=now().date()
            current_time=now().time()
            attendance_record=attendance.objects.create(uname=uname,user_id=user_id,date=current_date,in_time=current_time,out_time=out_time)
    return render(request,"attendance.html",{'attendance_record':attendance_record})
     
def  booktyp(request):
    booktype_record=None
    if request.method=="POST":
        booktype_value=request.POST.get("booktype")
        if booktype:
            booktype_record=booktype.objects.create(booktype=booktype_value)
    return render(request,"booktype.html",{'booktype_record':booktype_record})    
    
def booksub(request):
    booktypes=booktype.objects.values("booktype")#fetch book types
    if request.method=="POST":
        subjectname=request.POST.get("subjectname")#get subjectname from form
        booktype_name=request.POST.get("booktype")#get booktype from form
        selected_booktype=booktype.objects.get(booktype=booktype_name)# matches the booktype name from db and form
        booksubjects.objects.create(subjectname=subjectname,booktype=selected_booktype)#store values in django
        messages.success(request,f"Successfully Added Subject:{subjectname}.")
        return redirect('booksub')
    return  render(request,"booksubjects.html",{'booktypes':booktypes})#passes list of booktypes to html

def bookcate(request):
    booktypes=booktype.objects.values("booktype")
    subjectnames=booksubjects.objects.values("subjectname")
    if request.method=="POST":
        bookcategory_name=request.POST.get("bookcategory")
        booktype_name=request.POST.get("booktype")
        subject_name=request.POST.get("subjectname")
        selected_booktype=booktype.objects.get(booktype=booktype_name)
        selected_subjectname=booksubjects.objects.get(subjectname=subject_name)
        bookcategory.objects.create(bookcategory=bookcategory_name,booktype=selected_booktype,subjectname=selected_subjectname)
        messages.success(request,f"Successfully Added BookCategory:{bookcategory_name}.")
        return redirect('bookcate')
    return render(request,"bookcategory.html",{'booktypes':booktypes,'subjectnames':subjectnames})

# record=booksubjects.objects.get(pk=3)
# record.delete()

# user=users.objects.get(pk=3)
# user.user_id=233002
# user.save()