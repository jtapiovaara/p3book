from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail


from .models import SiteFollowers
from .forms import CreateNewFollower

# Create your views here.

def maili(response):
    if response.method == 'POST':
        form = CreateNewFollower(response.POST)
        if form.is_valid():
            n = form.cleaned_data['maili']
            t = SiteFollowers(maili=n)
            t.save()
            subject = 'Uusi seuraaja'
            message = t.maili
            from_email = settings.DEFAULT_FROM_MAIL
            to_list = ['jabadabaduu1962@gmail.com', 'jtapiovaara@gmail.com']
            send_mail(
                subject,
                message,
                from_email,
                to_list,
                fail_silently=False
                )
            tunnus = message.partition("@")[0]
            eemaili = message
            print(tunnus+' ja '+eemaili+' ovat uuden seuraajan tiedot')
            return render(response, 'posti/index_mail.html', {'form': message})
    else:
        form = CreateNewFollower()
    return render(response, 'posti/maili.html', {'form':form})




