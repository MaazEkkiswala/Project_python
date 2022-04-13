from statistics import mode
from django.shortcuts import render, redirect
from .models import Expense, feedback,rg_signup
from django.http import HttpResponse

def home(request):
    sum = Expense.objects.all()
    total=0
    for i in sum:
        total=total+i.amount
    
    
    expenses = Expense.objects.all()
    if request.POST:
        month = request.POST['month']
        year = request.POST['year']
        expenses = Expense.objects.filter(date__year=year, date__month=month)
    return render(request, 'index1.html', {'expenses': expenses,'a':total})

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.POST:
        model=feedback()
        model.name=request.POST['name']
        model.email=request.POST['email']
        model.subject=request.POST['subject']
        model.message=request.POST['message']
        model.save()
    return render(request,'contact.html')

def login(request):
    return render(request,'login.html')

def service(request):
    return render(request,'services.html')

def signup(request):
    if request.POST:
        model=rg_signup()
        model.Firstname=request.POST['Firstname']
        model.Lastname=request.POST['Lastname']
        model.email=request.POST['email']
        model.passw=request.POST['passw']
        model.re_pwd=request.POST['re_pwd']
        model.save()
    return render(request,'signup.html')

def add(request):
    if request.method == 'POST':
        item = request.POST['item']
        amount = request.POST['amount']
        category = request.POST['category']
        date = request.POST['date']

        expense = Expense(item=item, amount=amount, category=category, date=date)
        expense.save()

    return redirect(home)

def update(request, id):
    id = int(id)
    expense_fetched = Expense.objects.get(id = id)
    if request.method == 'POST':
        item = request.POST['item']
        amount = request.POST['amount']
        category = request.POST['category']
        date = request.POST['date']

        expense_fetched.item = item
        expense_fetched.amount = amount
        expense_fetched.category = category
        expense_fetched.date = date

        expense_fetched.save()

    return redirect(home)

def delete(request, id):
    id = int(id)
    expense_fetched = Expense.objects.get(id = id)
    expense_fetched.delete()
    return redirect(home)

