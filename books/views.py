from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from books.models import Book
from django.contrib.auth import authenticate, login as user_login, logout

def home(request):
    if request.user.is_authenticated:
        return render(request, 'books/home.html')
    else:
        return render(request, 'books/login.html')

def signup(request):
    context = {}
    if request.method == 'POST':
        name_r = request.POST.get('name')
        email_r = request.POST.get('email')
        password_r = request.POST.get('password')
        user = User.objects.create_user(name_r, email_r, password_r)
        if user:
            user_login(request, user)
            return render(request, 'books/thank.html')
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'books/signup.html', context)
    else:
        return render(request, 'books/signup.html', context)
def user_login(request):
    context = {}
    if request.method == 'POST':
        name_r = request.POST.get('name')
        password_r = request.POST.get('password')
        user = authenticate(request, username=name_r, password=password_r)
        if user:
            user_login(request)
            context["user"] = name_r
            context["id"] = request.user.id
            return render(request, 'books/success.html', context)
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'books/login.html', context)
    else:
        context["error"] = "You are not logged in"
        return render(request, 'books/login.html', context)
def logout(request):
    context = {}
    logout(request)
    context['error'] = "You have been logged out"
    return render(request, 'books/login.html', context)

def thank(request):
    context = {}
    thank(request)
    context['error'] = "You have been logged out"
    return render(request, 'books/thank.html', context)


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'pages']

def book_list(request, template_name='books/book_list.html'):
    book = Book.objects.all()
    data = {}
    data['object_list'] = book
    return render(request, template_name, data)

def book_view(request, pk, template_name='books/book_detail.html'):
    book= get_object_or_404(Book, pk=pk)    
    return render(request, template_name, {'object':book})

def book_create(request, template_name='books/book_form.html'):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, template_name, {'form':form})

def book_update(request, pk, template_name='books/book_form.html'):
    book= get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, template_name, {'form':form})

def book_delete(request, pk, template_name='books/book_confirm_delete.html'):
    book= get_object_or_404(Book, pk=pk)    
    if request.method=='POST':
        book.delete()
        return redirect('book_list')
    return render(request, template_name, {'object':book})
