""" from django.shortcuts import render """

from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Entry

class EntryListView(ListView):
    """ Entry view for diary """
    model = Entry
    queryset = Entry.objects.all().order_by("-date_created")

class EntryDetailView(DetailView):
    """ Entry detail view for diary """
    model = Entry

class EntryCreateView(CreateView):
    """ Entry view for creating a new diary entry """
    model = Entry
    fields = ["title", "content"]
    success_url = reverse_lazy("entry-list")

class EntryUpdateView(UpdateView):
    """ Entry view for updating a diary entry """
    model = Entry
    fields = ["title", "content"]

    def get_success_url(self):
        return reverse_lazy(
            "entry-detail",
            kwargs={"pk": self.object.pk}
        )

class EntryDeleteView(DeleteView):
    model = Entry
    success_url = reverse_lazy("entry-list")
