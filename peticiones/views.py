from django.shortcuts import render
from .forms import PeticionForm
from django.contrib import messages
import mechanize

# Create your views here.
def reclamo_create(request):
    if request.method == 'POST':
        form = PeticionForm(request.POST)
        if form.is_valid():
            br = mechanize.Browser()
            url = "http://anonymouse.org/anonemail.html"
            headers = "Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)"
            br.addheaders = [('User-agent', headers)]
            br.open(url)
            br.set_handle_equiv(True)
            br.set_handle_gzip(True)
            br.set_handle_redirect(True)
            br.set_handle_referer(True)
            br.set_handle_robots(False)
            br.set_debug_http(False)
            br.set_debug_redirects(False)
            # br.set_proxies({"http": proxy})

            br.select_form(nr=0)

            br.form['to'] = 'nicolasrinrin35@gmail.com'
            br.form['subject'] = form.cleaned_data['asunto']
            br.form['text'] = form.cleaned_data['descripcion']

            result = br.submit()


        else:
            print(form.errors)
    else:
        form = PeticionForm()

    context = {
        'form': form,
    }

    return render(request, 'peticiones/reclamos.html', context)