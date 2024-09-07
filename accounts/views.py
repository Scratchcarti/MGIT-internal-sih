from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Application,Document
from django.views.decorators.csrf import csrf_exempt


from django.contrib.auth.models import User

def index(request):
    

    return render(request,'index.html')
    

#retard shit but username is actually email and there is a different email column in .db file but for some reason its not able to authenticate it properly if it aint in username and password
def register(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        username = request.POST.get('username')  # 'username' is used for email in the form
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')

        if not fullname or not username or not mobile or not password:
            messages.error(request, 'All fields are required.')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Email is already registered.')
            return render(request, 'register.html')
        
        pls = User.objects.create_user(
            username=username,
            first_name=fullname,
            last_name = mobile
        )

        pls.set_password(password)

        pls.save()
        
        messages.success(request, 'You have successfully registered!')
        return redirect('login')    
        
            
    else:
        return render(request, 'register.html')
    
def login_view(request):
    
    if request.user.is_authenticated:
        # Redirect to dashboard if the user is already logged in
        return redirect('dashboard')
     
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        form.is_valid()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')

    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

@login_required
def dashboard(request):
    
    return render(request, 'dashboard.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def application(request):
    if request.method == 'POST':
        user = request.user
        if Application.objects.filter(user=user).exists():
            messages.error(request, 'You have already submitted an application form!!!')
            return redirect('dashboard')
        else:
            Application.objects.create(
                user=user,
                candidate_name=request.POST['candidateName'],
                father_name=request.POST['fatherName'],
                mother_name=request.POST['motherName'],
                dob=request.POST['dob'],
                state12th=request.POST['state12th'],
                category=request.POST['category'],
                father_occupation=request.POST['fatherOccupation'],
                mother_occupation=request.POST['motherOccupation'],
                address=request.POST['address'],
                city=request.POST['city'],
                state=request.POST['state'],
                pin_code=request.POST['pinCode'],
                locality=request.POST.get('locality', ''),
                country=request.POST['country'],
                district=request.POST.get('district', ''),
                mobile_number=request.POST['mobileNumber'],
                alternate_contact=request.POST.get('alternateContact', ''),
                email=request.POST['email'],
            )
            messages.success(request, 'You have successfully submitted the application form')
        return redirect('dashboard')  # Redirect to document upload page after form submission
    

    return render(request, 'application.html')


@login_required
def upload(request):

    if request.method == 'POST':
        user = request.user

        if Document.objects.filter(user=user).exists():
            messages.error(request, 'You have already submitted the documents!!!')
            return redirect('dashboard')

        for doc_type, file in request.FILES.items():
            Document.objects.create(user=user, doc_type=doc_type, document=file)
            print(doc_type)
        return redirect('dashboard')  # Redirect to dashboard or any other page after successful upload
    
    return render(request,'upload.html')

@login_required
def status(request):
    
    user = request.user
    try:
        application = Application.objects.get(user=user)
        application_status = "Submitted"
    except Application.DoesNotExist:
        application_status = "Not-Submitted"
    
    required_documents = [
        "aadhaar",
        "income",
        "caste",
        "domicile",
        "tenth",
        "twelfth"
    ]
    
    uploaded_documents = Document.objects.filter(user=user)
    document_statuses = {}

    for doc_name in required_documents:
        if uploaded_documents.filter(doc_type=doc_name).exists():
            document_statuses[doc_name] = "Pending"
        else:
            document_statuses[doc_name] = "Not-Uploaded"
            
    insane = {
        'application_status': application_status,
        'document_statuses': document_statuses,
    }

    return render(request, 'status.html', insane)


def sag(request):
    test=19
    name = User.objects.filter(id=test)
    uploaded_documents = Document.objects.filter(user_id=test)
    print(list(uploaded_documents))
    
    return render(request,'sag.html',{'documents': uploaded_documents})