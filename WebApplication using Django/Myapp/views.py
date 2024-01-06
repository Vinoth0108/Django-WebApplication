from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout  
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):
   return render(request, 'Myapp/index.html')
def signup(request):
    return render(request, 'Myapp/signup.html')
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your Account has been created successfully...!!!")
        return redirect('signin/')


def index(request):
    return render(request, 'Myapp/index.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is already taken...!!!")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email is already registered...!!!")
                return redirect('signup')
            else:
                myuser = User.objects.create_user(username, email, pass1)
                myuser.first_name = fname
                myuser.last_name = lname
                myuser.save()

                messages.success(request, "Your Account has been created successfully...!!!")
                return redirect('signin')
        else:
            messages.error(request, "Passwords do not match...!!!")
            return redirect('signup')

    return render(request, 'Myapp/signup.html')


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        # Check if the provided credentials are valid
        valid_credentials = [
            {'username': 'TwilightSoftwares', 'password': 'twilight'},
            {'username': 'Sasikala', 'password': 'test@123'}
            # Add more allowed credentials as needed
        ]

        for credentials in valid_credentials:
            if credentials['username'] == username and credentials['password'] == pass1:
                user = authenticate(request, username=username, password=pass1)

                if user is not None:
                    login(request, user)
                    messages.success(request, "Successfully Logged In...!!!")
                    return redirect('index')
                else:
                    messages.error(request, "Invalid Credentials...!!!")
                    return redirect('signin')



        # If no valid credentials are found
        messages.error(request, "Invalid Credentials...!!!")
        return redirect('notallowed')

    return render(request, 'Myapp/signin.html')

def signout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out...!!!")
    return redirect('index')

#first div
def tabular_view(request):
    return render(request, 'Myapp/TabularView.html')

def graph_view(request):
    return render(request, 'Myapp/Graph.html')
def chart_view(request):
    return render(request, 'Myapp/Charts.html')
#.....Second Div
def dashboard(request):
    return render(request, 'Myapp/dashboardpage.html')

def histogram(request):
    return render(request, 'Myapp/Histograms.html')

def treemaps(request):
    return render(request, 'Myapp/Treemaps.html')
#Third div

def time(request):
    return render(request, 'Myapp/TimeSereies.html')

def network(request):
    return render(request, 'Myapp/NetworkDiagram.html')

def boxplot(request):
    return render(request, 'Myapp/Boxplot.html')

def goback(request):
    return render(request, 'Myapp/index.html')


def notallowed(request):
    return render(request, 'Myapp/Not_Allowed.html' )

# To display User_credentials in json 

def all_users_credentials_json(request):
    all_users_data = {}
    users = User.objects.all()

    for user in users:
        user_data = {
            'Username': user.username,
            # 'first_name': user.first_name,
            # 'last_name': user.last_name,
            'Email': user.email,
        }
        all_users_data[user.username] = user_data

    return JsonResponse(all_users_data, json_dumps_params={'indent': 2}) 

