from django.shortcuts import render,redirect,HttpResponse
from .models import User,Feedback
from django.contrib import messages

# Create your views here.
def user_home(request):
    id=request.session["user_key"]#fething the value from dict
   #  print(st_id)
    user_obj=User.objects.get(user_id=id)
    user_dict={
       "user_data":user_obj
    }#binding user object in dict
    
    return render(request,"solutionapp/user/user_home.html",user_dict)

def user_feedback(request):
    #  return render(request,"solutionapp/user/user_feedback.html")
    if request.method=="GET":
     return render(request,"solutionapp/user/user_feedback.html")
    if request.method=="POST":
       id=request.session["user_key"]
       user_obj=User.objects.get(user_id=id)
       u_feedback=request.POST["userfeedback"]
       u_rating=request.POST["userrating"]

    #  user_object=user_feedback_rating.objects.get(user_id=user_obj)
    user_object_list=Feedback.objects.filter(user_id=user_obj)
    if user_object_list:
       user_dict={
        "user_data":user_obj
       }

       messages.info(request,"You have already given feedback !!!")
       return render(request,"solutionapp/user/user_home.html",user_dict)

    else:
       user_feedback_obj=Feedback(feedback_text=u_feedback,rating=u_rating)
       user_feedback_obj.save()
       user_dict={
          "user_data":user_obj
       }

       messages.success(request,"Thank you !!!")
       return render(request,"solutionapp/user/user_home.html",user_dict)

       
def user_logout(request):
    del request.session["user_key"]
    return redirect("login")

def user_edit_profile(request):
   if request.method=="GET":
     s_id=request.session["user_key"]
     user_obj=User.objects.get(user_id=s_id)
     user_dict={
        "user_data":user_obj
     }
     return render (request,"solutionapp/user/user_edit_profile.html",user_dict)
   if request.method=="POST":
       em=request.POST["useremail"]
       ph=request.POST["userphone"]
       add=request.POST["useraddress"] 

       s_id=request.session["user_key"]
       user_obj=User.objects.get(user_id=s_id)
       user_obj.email=em
       user_obj.phone=ph
       user_obj.address=add
       user_obj.save()

       user_dict={
          "user_data":user_obj
       }
       return render (request,"solutionapp/user/user_home.html",user_dict)
   return render(request,"solutionapp/user/user_edit_profile.html")
