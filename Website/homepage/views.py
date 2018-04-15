from django.shortcuts import render,redirect
from homepage.forms import UserForm, UserProfileInfoForm, CalculatePricePack
from django.contrib.auth.models import User


# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'homepage/home.html')

@login_required
def special(request):
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('home'))


# def register(request):
#     if request.method =='POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/homepage')
#     else:
#         form = UserCreationForm()
#         args = {'form': form}
#         return render(request, 'homepage/registration.html', args)
def register(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            # Save User Form to Database
            user=user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user

            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            profile.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors, profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'homepage/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('home'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'homepage/login.html', {})


def calculateprice(request):
    if request.method == 'POST':
        form = CalculatePricePack(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return redirect('home')
        else:
            print(form.errors)
    form = CalculatePricePack()
    return render(request, 'homepage/sample.html', {'form' : form})


def europe(request):
    return render(request, 'homepage/europe.html', {})


def profile(request):

    return render(request, 'homepage/profile.html', {'user': request.user})


def sample(request):

    return render(request, 'homepage/sample.html', {})



def aboutus(request):
    return render(request, 'homepage/aboutus.html', {})


def index(request):
    return render(request, 'homepage/blog/index.html', {})


def first(request):
    return render(request, 'homepage/blog/first.html', {})


def second(request):
    return render(request, 'homepage/blog/second.html', {})


def third(request):
    return render(request, 'homepage/blog/third.html', {})


def fourth(request):
    return render(request, 'homepage/blog/fourth.html', {})


def fifth(request):
    return render(request, 'homepage/blog/fifth.html', {})


def sixth(request):
    return render(request, 'homepage/blog/sixth.html', {})


