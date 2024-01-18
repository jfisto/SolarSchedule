from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

# Create your views here.

class HomePage(TemplateView):
    template_name = 'homepage.html'

    def get(self, request, *args, **kwargs):
        ctx = {}
        return render(request, self.template_name, ctx)

class Dashboards(TemplateView):
    template_name = 'dashboards.html'

    def get(self, request, *args, **kwargs):
        ctx = {}
        return render(request, self.template_name, ctx)

class EngineerDashboard(TemplateView):
    template_name = 'engineerdashboard.html'

    def get(self,request, *args, **kwargs):
        ctx = {}
        return render(request,self.template_name,ctx)

    # def create_card(request):
    #     if request.method == 'POST':
    #         title = request.POST.get('title')
    #         content = request.POST.get('content')
    #         card = Card.objects.create(title=title, content=content)
    #         return HttpResponseRedirect('/card/{0}/'.format(card.id))
    #     return render(request, 'engineerdashboard.html')

class ScheduleEngineer(TemplateView):
    template_name = 'scheduleengineer.html'

    def get(self, request, *args, **kwargs):
        ctx = {}
        return render(request, self.template_name, ctx)

class Other(TemplateView):
    template_name = 'other.html'

    def get(self, request, *args, **kwargs):
        ctx = {}
        return render(request, self.template_name, ctx)

class Auth(TemplateView):
    template_name = 'auth.html'

    def get(self, request, *args, **kwargs):
        ctx = {}
        return render(request, self.template_name, ctx)