from django.db import models

# Create your models here.
class users(models.Model):
    name=models.CharField(max_length=80)
    uemail=models.CharField(max_length=100)
    umobile=models.CharField(max_length=30)
    uname=models.CharField(max_length=60)
    upass=models.CharField(max_length=70)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    is_deleted=models.BooleanField(default=False)
    Status_Choices=[('active','Active'),('inactive','Inactive'),('pending','Pending')]
    status=models.CharField(max_length=30,
    choices=Status_Choices,default='Inactive')
    updated_at=models.DateTimeField(auto_now_add=True,null=True)
    User_Type_Choices=[(0,'Admin'),(1,'Staff'),(2,'Student'),]
    user_type=models.CharField(max_length=40,
    choices=User_Type_Choices,default='2')
    user_id=models.CharField(max_length=100,default=0)

class attendance(models.Model):
    user_id=models.CharField(max_length=100,null=True)
    uname=models.CharField(max_length=60,null=True)
    date=models.DateField(auto_now_add=True,null=True)
    in_time=models.TimeField(null=True,blank=True)
    out_time=models.TimeField(null=True,blank=True)
    is_deleted=models.BooleanField(default=False)

class booktype(models.Model):
    booktype=models.CharField(max_length=100,null=True)
    is_deleted=models.BooleanField(default=False)

class booksubjects(models.Model):
    subjectname=models.CharField(max_length=100,null=True)
    booktype=models.ForeignKey(booktype,on_delete=models.CASCADE)
    is_deleted=models.BooleanField(default=False)

class bookcategory(models.Model):
    booktype=models.ForeignKey(booktype,on_delete=models.CASCADE)
    subjectname=models.ForeignKey(booksubjects,on_delete=models.CASCADE)
    bookcategory=models.CharField(max_length=100,null=True)
    is_deleted=models.BooleanField(default=False)



