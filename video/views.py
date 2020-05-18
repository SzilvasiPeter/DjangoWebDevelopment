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


class SimpleUserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    def test_func(self):
        video = self.get_object()
        if self.request.user == video.renter:
            return True
        return False


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


class VideoUpdateView(SimpleUserRequiredMixin, UpdateView):
    model = Video
    fields = ['title', 'genre', 'duration']

    def form_valid(self, form):
        form.instance.renter = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'video/about.html')

