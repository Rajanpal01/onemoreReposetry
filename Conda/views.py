from django.shortcuts import render,redirect
from .models import Project_details,Projects_ideas
from .models import Form_data
from django.http import HttpResponse,HttpResponseRedirect
from .models import PPT, Documentation




# Create your views here.
def basic(request):
    para = request.session.get('Form_value_name')
    return render(request, 'basic.html',{'para':para})

def index(request):
    obb = Project_details.objects.all()
    para = request.session.get('Form_value_name')
    return render(request,'index.html',{'obb':obb,'para':para})

def moreproject(request):
    obb = Project_details.objects.all()
    para = request.session.get('Form_value_name')
    return render(request, 'more_project.html',{'obb':obb,'para':para})

def moreprojectlink(request):
    obb = Project_details.objects.all()
    para = request.session.get('Form_value_name')
    return render(request, 'more_project_links.html',{'obb':obb,'para':para})

def documentation_download_link(request):
    para = request.session.get('Form_value_name')
    document = Documentation.objects.all()
    value = {
        'para':para,
        'document':document
    }
    return render(request, 'documentation_download_link.html',(value))

def click_for_projects_ideas(request):
    obb = Projects_ideas.objects.all()
    para = request.session.get('Form_value_name')
    return render(request, 'click_for_projects_ideas.html',{'obb':obb,'para':para})

def Login_form(request):
    
    if request.method == "POST":
        username = request.POST.get('Full_name')
        number = request.POST.get('Number')
        usermail = request.POST.get('Email')
        pass1 = request.POST.get('Password')
        pass2 = request.POST.get('password_again')
        
        last_fun_value = Form_data(name = username, Email = usermail, Mobile = number, password = pass1)

        value = {
            'name' : username,
            'number':number,
            'usermail' : usermail,
        }
        #validation here for all field
        error_number = ''
        error_name = ''
        error_Email = ''
        error_password = ''
        error_password2 = ''



        if (not username):
            error_name = 'Name is  required !!'
        elif len(username) < 5:
            error_name = 'Name should be minimum 8 characters !'
        elif (not number):
            error_number = 'Please Enter your mobile number'
        elif (len(number) <10):
            error_number='number should be minimum 10 digit'
        
        elif (len(number) >10):
            error_number='number should be miximum 10 digit'

        elif (len(usermail)<5):
            error_Email='please Enter valid Email address'

        elif (last_fun_value.isExist()):
            error_Email = 'Email Address is already exist'

        elif (not pass1):
            error_password = 'Please Enter password'

        elif (len(pass1) < 8):
            error_password = 'password must be minimum 8 number'
        
        if (not pass2):
            error_password2 = 'please Enter password again field'

        elif (pass1 != pass2 ):
            error_password = 'Password does not match'
        #saving
        if (not error_name) and (not error_number) and (not error_password) and (not error_password) and (not error_password2) and (not error_password2) and (not error_Email):
            request.session['Form_value_Email'] =  last_fun_value.Email
            request.session['Form_value_name'] =  last_fun_value.name
            last_fun_value.save()
            return redirect('on_click_here_project')

        else:
            data = {
                'error_name':error_name,
                'error_Email':error_Email,
                'error_number':error_number,
                'error_password':error_password,
                'error_password2':error_password2,
                'value':value
                

            }
            return render(request, 'Login_form.html',data)

        print('page not found here we go')    

    return render(request, 'Login_form.html')

def on_click_here_project(request,id):
    session_data = request.session.get('Form_value_name')
    para = None
    obb = Project_details.objects.filter(id = id)
    
    if not request.session.get('Form_value_Email'):
        para = 1

    return render(request, 'on_click_here_project.html',{'obb':obb, 'para':para, 'session_data':session_data})

def Small_login_form(request):
    name = request.POST.get('Email_details')
    passw = request.POST.get('password_details')
   
    error_message = None
    if request.method == 'POST':
        Form_value = Form_data.get_form_value(name,passw)
        print(Form_value)

        if Form_value:
            request.session['Form_value_Email'] =  Form_value.Email
            request.session['Form_value_name'] =  Form_value.name
            return redirect('on_click_here_project')
        else:
            error_message = 'Email Address is not exist !'
        return render(request, 'small_login_form.html',{'error':error_message})

        
    return render(request, 'small_login_form.html')

    

def PPT_es(request):
    para = request.session.get('Form_value_name')
    document = PPT.objects.all()
    value = {
        'para':para,
        'document':document
    }
    return render(request, 'PPT_Location.html',(value))


