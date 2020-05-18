from django.contrib.auth.models import User
from django.forms import ModelForm, HiddenInput
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Video


def home(request):
    context = {
        'videos': Video.objects.all()
    }
    return render(request, 'video/home.html', context=context)


class AdminStaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


class VideoListView(ListView):
    model = Video
    template_name = 'video/home.html'
    context_object_name = 'videos'
    ordering = ['title']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['videos'] = Video.objects.all().filter(renter=1)  # Admin id is 1
        context['rented_videos'] = Video.objects.all().exclude(renter=1)
        return context


class RentedVideoListView(ListView):
    model = Video
    template_name = 'video/video_rented.html'
    context_object_name = 'videos'
    ordering = ['-received_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user_id = self.request.user.id
        if current_user_id == 1:
            context['rented_videos'] = Video.objects.all()
        else:
            context['rented_videos'] = Video.objects.all().filter(renter=current_user_id)
        return context


class VideoDetailView(DetailView):
    model = Video


class VideoDeleteView(AdminStaffRequiredMixin, DeleteView):
    model = Video
    success_url = '/'


class VideoCreateView(AdminStaffRequiredMixin, CreateView):
    model = Video
    fields = ['title', 'genre', 'duration']

    def form_valid(self, form):
        form.instance.renter = self.request.user
        return super().form_valid(form)


class VideoUpdateView(AdminStaffRequiredMixin, UpdateView):
    model = Video
    fields = ['title', 'genre', 'duration']

    def form_valid(self, form):
        form.instance.renter = self.request.user
        return super().form_valid(form)


class HiddenForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(HiddenForm, self).__init__(*args, **kwargs)
        self.fields['renter'].widget = HiddenInput()

    class Meta:
        fields = ('renter', )
        model = Video


class VideoRentView(LoginRequiredMixin, UpdateView):
    model = Video
    template_name = 'video/video_rent.html'
    form_class = HiddenForm
    success_url = '/'

    def form_valid(self, form):
        if form.instance.renter == self.request.user:
            admin_user = User.objects.get(id=1)
            form.instance.renter = admin_user
        else:
            form.instance.renter = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'video/about.html')

