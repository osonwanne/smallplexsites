from django.core.mail import send_mail
from django.shortcuts import redirect, render

# Create your views here.
from contact.forms import ContactForm

def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES)

        if form.is_valid():

            contact_name = request.POST.get(
                'Name'
            , '')
            contact_email = request.POST.get(
                'Email'
            , '')
            form_content = request.POST.get('Message', '')

            form.save()

            send_mail('Smallplex - new contact: %s' % contact_name, form_content, contact_email,
                      ['nosonwan@gmail.com'])

        return redirect('success')

    return render(request, 'contact.html', {
        'form': form_class,
    })

def success(request):
    return render(request, 'contact_form_sent.html')