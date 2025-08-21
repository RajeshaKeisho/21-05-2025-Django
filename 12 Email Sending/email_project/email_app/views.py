from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives, EmailMessage
from django.http import HttpResponse
from django.template.loader import render_to_string
from .forms import FormDataForm

# Create your views here.

def send_email(request):
    subject = "Test Email with Attachments"
    from_email = 'rajarajesha@gmail.com'
    to_email = ['pyweb.rajesha.coding@gmail.com']
    html_content = render_to_string('email_template.html', {'recipient_name':"Recipient"})

    email = EmailMultiAlternatives(subject, "Text Content here", from_email, to_email)
    email.attach_alternative(html_content, 'text/html')
    email.extra_headers["x_Mailer"] = "Django Mailer"

    try:
        email.send()
        return HttpResponse("Congrats! Email Sent Successfully!")
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)})")


def form_view(request):
    if request.method == "POST":
        form = FormDataForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            attachment = request.FILES['attachment']

            subject = 'Form Submission'
            message = "Thank you for your submission!"
            from_email = 'rajarajesha@gmail.com'
            to_email = [email]

            email = EmailMessage(subject, message, from_email, to_email)
            email.attach(attachment.name, attachment.read(), attachment.content_type)


            try:
                email.send()
                return render(request, 'success.html')
            except Exception as e:
                return render(request, 'error.html', {'error_message':str(e)})
    else:
        form = FormDataForm()
    return render(request, 'form.html', {'form':form})

