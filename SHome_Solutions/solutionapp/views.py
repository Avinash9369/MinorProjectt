from django.shortcuts import render,HttpResponse,redirect
from .models import User,Query,Feedback,Employee_Type,Employee,Offers_Scheme
from django.contrib import messages

# Create your views here.
def home(request):

     offer_object_list= Offers_Scheme.objects.all()
     offer_context={
        "offer_key": offer_object_list, 
    }
     return render(request,"solutionapp/html/index.html",offer_context)
    
def registration(request):
    if request.method=="GET":
     return render (request,"solutionapp/html/registration.html")
    if request.method=="POST":
       u_id=request.POST["userid"]
       u_pass=request.POST["userpassword"]
       u_name=request.POST["username"]
       u_email=request.POST["useremail"]
       u_phone=request.POST["userphone"]
       u_address=request.POST["useraddress"]
       register_obj=User(user_id=u_id,user_pass=u_pass,name=u_name,email=u_email,phone=u_phone,address=u_address)
       register_obj.save()

       messages.success(request,"Thank you for registration !!")
       return render (request,"solutionapp/html/registration.html")
       

def login(request):
    if request.method=="GET":
     return render(request,"solutionapp/html/login.html")
    if request.method=="POST":
        id=request.POST["userid"]#request.POST is built-in dictionary
        user_pass=request.POST["userpass"]
        print(id,user_pass)
        user_list=User.objects.filter(user_id=id,user_pass=user_pass)
       #select*from student where student_id=s_id, and student_password=s_pass

       
        length=len(user_list)
        if length>0:
         request.session["user_key"]=id #bind student id in session
         #  request.session[]
         return redirect("user_home")#it accept logical name from urls.py
         #it is used to redirect the request on the specified url
         #  return render(request,'MyApp/student/student_home.html' )

        else:
          messages.error(request,"Invalid Credentials")
          return render(request,'solutionapp/html/login.html')


def feedback(request):
    if request.method=="GET":
     return render(request,"solutionapp/html/feedback.html") 

    if request.method=="POST":
       u_name=request.POST["username"]
       u_email=request.POST["useremail"]
       u_text=request.POST["userfeedback"]
       u_rating=request.POST["userrating"]
       user_object=Feedback(name=u_name,email=u_email,feedback_text=u_text,rating=u_rating)
       user_object.save()
       

       messages.success(request,"Thank you !!")  
       return render(request,"solutionapp/html/feedback.html")    

def query(request):
    if request.method=="GET":
     return render(request,"solutionapp/html/query.html")
    if request.method=="POST":
       u_name=request.POST["username"]
       u_email=request.POST["useremail"]
       u_phone=request.POST["userphone"]
       u_query=request.POST["userquery"]
       query_obj=Query(name=u_name,email=u_email,phone=u_phone,question=u_query)
       query_obj.save()

       messages.success(request,"Thank you for your appriciation")
       return render(request,"solutionapp/html/query.html")

def about(request):
   return render(request,"solutionapp/html/about.html")


def services(request):
   
   emp_type_list=Employee_Type.objects.all()
   print(emp_type_list)
   type_dict={

        "emp_type":emp_type_list
    }
   return render(request,"solutionapp/html/services.html",type_dict)


def view_employee(request,etype):
   
    print("helllo"+etype)

    employee_type_object=Employee_Type.objects.get(employee_type=etype)

    employee_list=Employee.objects.filter(employee_type=employee_type_object)

    emp_dict={
       "emp_data":employee_list
    }
    return render(request,"solutionapp/html/view_employee.html",emp_dict)

# def search_employee(request):
   
#     #print("helllo"+etype)

#     etype=request.POST["emp_type"]
#     employee_type_object=Employee_Type.objects.get(employee_type=etype)

#     employee_list=Employee.objects.filter(employee_type=employee_type_object)

#     emp_dict={
#        "emp_data":employee_list
#     }
#     return render(request,"solutionapp/html/view_employee.html",emp_dict)