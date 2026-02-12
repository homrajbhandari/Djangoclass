from django.shortcuts import render,redirect
from .models import Student
from django.contrib.auth.hashers import check_password

def student_login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        
        try:
            student=Student.objects.get(username=username)
            if check_password(password,student.password):
                request.session['student_id']=student.id
                request.session['student_name']=student.name
                return redirect('dashboard')
            else:
                 return render(request,'session/login.html',{
              "error":"Invalid Password"
          }) 
                
        except:
          return render(request,'session/login.html',{
              "error":"Not Found"
          })  
       
    return render(request,'session/login.html')

def student_dashboard(request):
    if 'student_id' not in request.session:
        return redirect('login')
    name= request.session.get('student_name')
    return render(request,'session/dashboard.html',{
        'name':name
    })

def student_logout(request):
    request.session.flush()
    return redirect('login')
    