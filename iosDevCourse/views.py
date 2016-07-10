from django.views.generic import TemplateView
from django.contrib import auth
from django.shortcuts import render_to_response
from article.views import return_path_f


# Create your views here.




def contact(request):

    return_path_f(request)

    return render_to_response("contact.html", {'username': auth.get_user(request).username})


def portfolio(request):

    return_path_f(request)

    return render_to_response("portfolio.html", {'username': auth.get_user(request).username})


class MainView(TemplateView):
    template_name = 'callactions.html'


main = MainView.as_view()

