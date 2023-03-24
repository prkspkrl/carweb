from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
# Create your views here.


def send_message(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        user_id = request.POST['user_id']
        car_title = request.POST['car_title']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        slug = request.POST['slug']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request,
                               'You have already made an inquiry about this car. Please wait until we get back to you.')
                return redirect('/cars/' + car_id)


        contact = Contact(car_id=car_id, car_title=car_title, user_id=user_id,
        first_name=first_name, last_name=last_name, customer_need=customer_need, slug=slug, city=city,
        state=state, email=email, phone=phone, message=message)

        contact.save()
        messages.success(request, 'Your request has been submitted, we will get back to you shortly.')
        return redirect('/cars/'+slug)





def contact(request):
    return render(request,'pages/contact.html')