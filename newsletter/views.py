from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import ContactForm, SignUpForm
from .models import SignUp

# Create your views here.

STATIC_ROOT = "/var/www/example.com/static/"

def home(request):

    title = 'Sign Up now'

    #if request.user.is_authenticated():
        #title = 'my title %s' %(request.user)

    #add a form
    print request

    #if request.method == 'POST':
    #    print  request.POST

    form = SignUpForm(request.POST or None)

    context = {
        'title': title,
        'form': form
    }

    if form.is_valid():
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get('full_name')
        print request.POST['email']

        if not instance.full_name:
            instance.full_name = 'New full name'
        instance.full_name = full_name
        instance.save()

        context = {
        'title': 'Thank you',
        }

    if request.user.is_authenticated() and request.user.is_staff:
        # print SignUp.objects.all()
        queryset = SignUp.objects.all()
        num = 0

        for object in SignUp.objects.all():
            print '#', num, object, object.full_name, object.timestamp
            num += 1

        context = {
            'queryset': queryset
        }





    return render(request, 'home.html', context)

def contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        #print form.cleaned_data
        # for key, value in form.cleaned_data.iteritems():
        #     print key, value
        form_email = form.cleaned_data.get('email')
        form_message = form.cleaned_data.get('message')
        form_full_name = form.cleaned_data.get('full_name')
        #print form_email, form_message, form_full_name

        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = ['is_@list.ru', 'is22@me.com']
        # to_email = [from_email, 'is22@me.com']
        #to_email = 'is22@me.com'


        contact_message = '%s: %s via %s'%(
            form_full_name,
            form_message,
            form_email)

        print subject, from_email, to_email
        print(", ".join(map(str, to_email)))
        print
        print 'contact_message', contact_message

        send_mail(subject,
                  contact_message,
                  from_email,
                  #['is_@list.ru', 'is22@me.com'],
                  [", ".join(map(str, to_email))],
                  fail_silently=False)

    context = {
        'form': form,
    }

    return render(request, 'forms.html', context)