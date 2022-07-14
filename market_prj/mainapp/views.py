from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect, redirect
from django.db.models import Q
from django.views.generic import ListView
from django_filters.views import FilterView
from .filters import AccommodationFilter
from .models import Accommodation, ListOfCountries

from comment.models import Comment
from comment.forms import CommentForm
from django.template import RequestContext
from django.urls import reverse
from market_prj import settings
from .forms import EventForm

def main(request):
    return render(request, "mainapp/index.html")


def accommodations(request):
    title = "размещение"
    list_of_accommodations = Accommodation.objects.filter(Q(is_active=True))
    content = {
        "title": title,
        "list_of_accommodations": list_of_accommodations,
    }

    return render(request, "mainapp/accommodations.html", content)


# def accommodations(request):
#     title = "размещение"
#     query = request.GET.get('q')
#     list_of_accommodations = Accommodation.objects.filter(Q(is_active=True))
#     content = {
#         "title": title,
#         "list_of_accommodations": list_of_accommodations,
#         "query": query,
#     }
#
#     return render(request, "mainapp/accommodations.html", content)


def accommodation(request, pk):
    title = "продукты"

    comments = Comment.objects.filter(Q(accommodation_id=pk))
    instance = get_object_or_404(Comment, id=pk)
    user = get_user_model()

    if request.method == "POST":

        if not request.user.is_authenticated:
            return redirect('%s?next=%s' % (settings.LOGIN_URL, f'/list_of_accommodations/accommodation_details/{pk}/'))
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment_form.save()
            print('save')
            return HttpResponseRedirect("#")

    else:
        comment_form = CommentForm()


    content = {
            "comment_form": comment_form,
            "comments": comments,
            "title": title,
            "links_menu": ListOfCountries.objects.all(),
            "accommodation": get_object_or_404(Accommodation, pk=pk),
            'request': request,
            "pk": pk
        }
    form = EventForm
    content = {
        "form": form,
        "title": title,
        "links_menu": ListOfCountries.objects.all(),
        "accommodation": get_object_or_404(Accommodation, pk=pk),
    }

    return render(request, "mainapp/accommodation_details.html", content)


class AccommodationListView(FilterView):
    """
    Show list of accommodation. And do sort and filter thing
    """
    model = Accommodation
    template_name = "mainapp/accommodations.html"
    context_object_name = "list_of_accommodations"
    queryset = Accommodation.objects.all()
    filterset_class = AccommodationFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "размещение"
        return context