from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
from .forms import UploadBookForm,Books
from django.contrib.auth.decorators import login_required
from .models import CustomUser,BulkData
from sqlalchemy import create_engine
from sqlalchemy.sql import text
import pandas as pd
from django.db import transaction 
import datetime,time
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {email}!')
            return redirect('login')  
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            request.session['email'] = email
            login(request, user)
            return redirect('home') 
        
        else:
            messages.success(request, 'Invalid email or password')
            form = CustomUserCreationForm()
    return render(request, 'login.html')

@login_required
def home(request):
    user = request.user
    all_books = Books.objects.filter(visibility=True)
    return render(request, 'home.html', {'user': user, 'all_books': all_books})

@login_required()
def upload_book(request):
    if request.method == 'POST':
        form = UploadBookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            if request.user.is_authenticated:
                book.user_id = request.user.id
            book.save()
            messages.success(request, 'Book uploaded successfully!')
            return redirect('upload_book')  
    else:
        form = UploadBookForm()
    return render(request, 'upload_book.html', {'form': form})

@login_required
def dashboard(request):
    user=CustomUser.objects.filter(public_visibility=True)
    return render(request, "allReg.html", {"users": user})

@login_required
def allbooks(request):
    all=Books.objects.filter(visibility=True)
    return render(request,"allbooks.html",{"all":all})


@login_required
def uploaded_books(request):
    uploaded_books = Books.objects.filter(user_id=request.user.id)
    if not uploaded_books.exists():
        return redirect('upload_book')
    return render(request, 'userBook.html', {'uploaded_books': uploaded_books})

def logout_view(request):
    logout(request)
    return redirect('register')

@login_required
def fetch_and_display(request):
    engine = create_engine('mysql://root:root@localhost:3306/books')  
    with engine.connect() as connection:
        query=text("SELECT * FROM myapp_books")
        result = connection.execute(query)
        data = result.fetchall()
    return render(request, 'data_display.html', {'data': data})



# #bulk data send to database from excel in lakhs
@csrf_exempt
def bulkdata(request):
    start_time = time.time()
    excel_file_path = r'C:\Users\Administrator\Downloads\bq-results-20240429-053135-1714368881260.csv'

    df = pd.read_csv(excel_file_path, encoding='utf-8')
    print("read data..")
    # Convert DataFrame to list of dictionaries
    data = df.to_dict(orient='records')

    print("savaing data..")
    # Add necessary fields to each dictionary
    for item in data:
        item.update({
            'mobile_number': item['Mobile'],
            'Pincode': item['Pincode'],
            'Name': item['Name'],  
            'Address': item['Address'],
            'WhatsApp_Status': item['WhatsApp_Status'],
            'Blaster_Status': item['Blaster_Status'],
        })

    # Bulk create objects in database within a transaction
    with transaction.atomic():
        BulkData.objects.bulk_create([BulkData(**item) for item in data])
    end_time = time.time()  # Record end time
    time_taken = end_time - start_time
    print("Time taken to send data to database:", time_taken, "seconds")
    return BulkData("Data saved successfully")



@csrf_exempt
def bulkdata(request):
    start_time = time.time()
    excel_file_path = r'C:\Users\Administrator\Downloads\bq-results-20240429-050336-1714367055093.csv'

    df = pd.read_csv(excel_file_path, encoding='utf-8')
    print("Read data from CSV file")

    # Convert DataFrame to list of dictionaries
    data = df.to_dict(orient='records')

    # Add necessary fields to each dictionary
    for item in data:
        item.update({
            'Mobile': item['Mobile'],
            'Pincode': item['Pincode'],
            'Name': item['Name'],  
            'Address': item['Address'],
            
        })

    # Bulk create objects in database within a transaction
    with transaction.atomic():
        BulkData.objects.bulk_create([BulkData(**item) for item in data])
    end_time = time.time()  # Record end time
    time_taken = end_time - start_time
    print("Time taken to send data to database:", time_taken, "seconds")
    return JsonResponse({"message": "Data saved successfullyyyyy"})



@csrf_exempt
def bulkdata(request):
    start_time = time.time()
    excel_file_path = r'C:\Users\Administrator\Downloads\bq-results-20240429-053135-1714368881260.csv'

    df = pd.read_csv(excel_file_path, encoding='utf-8')
    print("read data..")
    # Convert DataFrame to list of dictionaries
    data = df.to_dict(orient='records')

    print("savaing data..")
    # Add necessary fields to each dictionary
    for item in data:
        item.update({
            'emp_id': item['emp_id'],
            'name': item['name'],
            'address': item['address'],  
            'city': item['city'],
            'state': item['state'],
            'personal_contact': item['personal_contact'],
            'dob': item['dob'],
            'doj': item['doj'],
            'zip': item['zip'],
            'role_position': item['role_position'],
            'manager': item['manager'],
            'joined_date': item['joined_date'],
            'email': item['email'],
            'markytics_email   ': item['markytics_email'],
            'password': item['password'],
            'is_employee': item['is_employee'],
            'is_manager': item['is_manager'],
            'is_active': item['is_active'],
            'is_superadmin': item['is_superadmin'],
            'is_admin': item['is_admin'],
            'fresher': item['fresher'],
            'intern': item['intern'],
            'clickup_id': item['clickup_id'],
            'pan': item['pan'],
            'aadhar': item['aadhar'],
            'current_address_proof': item['current_address_proof'],
            'tenth_certificate': item['tenth_certificate'],
            'twelfth_certificate': item['twelfth_certificate'],
            'reference1_name': item['last_company_experience_proof'],
            'reference1_email': item['reference1_email'],
            'reference1_contact': item['reference1_contact'],
            'reference2_name': item['reference2_name'],
            'reference2_company': item['reference2_company'],
            'reference2_email': item['reference2_email'],
            'reference2_contact': item['reference2_contact'],
            'teamlogger_id': item['teamlogger_id'],
            'manager_id': item['manager_id'],
        })

    # Bulk create objects in database within a transaction
    with transaction.atomic():
        BulkData.objects.bulk_create([BulkData(**item) for item in data])
    end_time = time.time()  # Record end time
    time_taken = end_time - start_time
    print("Time taken to send data to database:", time_taken, "seconds")
    return BulkData("Data saved successfully")