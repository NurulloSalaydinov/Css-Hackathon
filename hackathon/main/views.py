from django.shortcuts import render, redirect
from .forms import ContactForm
import telebot
from django.contrib import messages


bot = telebot.TeleBot("5870359200:AAHXFwz6z6qLYe7aQCJNnzQuyw9Eqp1rXrE")
groupId = "5367086278"

def home_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print('ok')
            form.save()
            message = f"""
                Ism familya: {request.POST.get('full_name')}\n
                Tug'ilgan yili: {request.POST.get('age')}\n
                Telefon: {request.POST.get('phone')}\n
                Manzil: {request.POST.get('address')}\n
            """
            bot.send_message(groupId, message)
            messages.add_message(request, messages.INFO, 'Muvaffaqiyatli yuborildi tez orada siz bilan bog\'lanamiz')
            return redirect('/')
    else:
        form = ContactForm()
    return render(request, 'index.html', { 'form': form })
