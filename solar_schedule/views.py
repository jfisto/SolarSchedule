from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, JsonResponse
import pandas as pd
from solar_schedule.dirs import DATA_DIR
from solar_schedule.exp.action_to_db import ActionDB
import json

# Create your views here.

class EngineerDashboard(TemplateView):
    template_name = 'engineerdashboard.html'
    # key_db = ['csrfmiddlewaretoken', 'time_period', 'type_lesson',
    #           'name_lesson', 'group_name', 'cause',
    #           'science_degree_subject', 'job_subject', 'subject',
    #           'science_degree_object', 'job_object', 'object']
    # @csrf_protect
    def get(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("/login")

        obj = ActionDB()
        data = obj.select_from_db()
        people = list(data['FullName'])
        print(people)
        department = list(data['Departament'])
        jobs = list(data['JobName'])
        phone = list(data['Phone'])
        ctx = {'people': zip(people,department,jobs,phone)}
        # ctx = ['Alice', 'Bob', 'Charlie', 'David','Eve', 'Frank', 'Grace', 'Hannah', 'Isaac', 'Jane']
        # ctx = {
        #     'data_lesson': {
        #         'title': 'Дата и время проведения занятия',
        #         'name': self.key_db[1],
        #     },
        #     'list_parm': [
        #         {'title': 'Тип пары',
        #          'name': self.key_db[2],
        #          'placeholder': "Лек/Лаб"
        #          },
        #         {'title': 'Дисциплина',
        #          'name': self.key_db[3],
        #          'placeholder': "Наименование"
        #          },
        #         {'title': 'Имя группы',
        #          'name': self.key_db[4],
        #          'placeholder': "Группа(ы)"
        #          },
        #         {'title': 'Причина замены преподавателя',
        #          'name': self.key_db[5],
        #          'placeholder': "Текст"
        #          }
        #     ],
        #     'subject_people': 'Инициатор замены',
        #     'object_people': 'Замещающий преподаватель',
        #     'title_since': 'Научная степень инициатора',
        #     'list_since_su': [
        #         {'name': self.key_db[6],
        #          'contains': " к.э.н."
        #          },
        #         {'name': self.key_db[6],
        #          'contains': "д.э.н."
        #          },
        #         {'name': self.key_db[6],
        #          'contains': "степень отсутствует"
        #          }
        #     ],
        #     'list_job_su': [
        #         {'name': self.key_db[7],
        #          'contains': "Заведующий кафедры"
        #          },
        #         {'name': self.key_db[7],
        #          'contains': "Профессор кафедры"
        #          },
        #         {'name': self.key_db[7],
        #          'contains': "Доцент кафедры"
        #          },
        #         {'name': self.key_db[7],
        #          'contains': "Ст. преподаватель"
        #          },
        #         {'name': self.key_db[7],
        #          'contains': "Ассистент"
        #          },
        #     ],
        #     'list_people_su': [
        #         {'name': self.key_db[8],
        #          'contains': "Щербаков Сергей Михайлович"
        #          },
        #         {'name': self.key_db[8],
        #          'contains': "Шполянская Ирина Юрьевна"
        #          },
        #         {'name': self.key_db[8],
        #          'contains': "Хубаев Георгий Николаевич"
        #          },
        #         {'name': self.key_db[8],
        #          'contains': "Долженко Алексей Иванович"
        #          },
        #         {'name': self.key_db[8],
        #          'contains': "Жебровская Людмила Анатольевна"
        #          },
        #         {'name': self.key_db[8],
        #          'contains': "Мирошниченко Ирина Иосифовна"
        #          },
        #         {'name': self.key_db[8],
        #          'contains': "Фрид Любовь Михайловна"
        #          },
        #         {'name': self.key_db[8],
        #          'contains': "Веретенникова Елена Григорьевна"
        #          },
        #         {'name': self.key_db[8],
        #          'contains': "Аручиди Наталья Александровна"
        #          },
        #         {'name': self.key_db[8],
        #          'contains': "Курбесов Александр Валерьянович"
        #          },
        #         {'name': self.key_db[8],
        #          'contains': "Прохорова Анна Михайловна"
        #          },
        #         {'name': self.key_db[8],
        #          'contains': "Данилова Татьяна Викторовна"
        #          },
        #         {'name': self.key_db[8],
        #          'contains': "Шкодина Татьяна Андреевна"
        #          },
        #         {'name': self.key_db[8],
        #          'contains': "Потапов Леонид Игоревич"
        #          },
        #         {'name': self.key_db[8],
        #          'contains': "Глушенко Сергей Андреевич"
        #          },
        #         {'name': self.key_db[8],
        #          'contains': "Гречкина Вера Юрьевна"
        #          },
        #         {'name': self.key_db[8],
        #          'contains': "Яковец Светлана Владимировна"
        #          },
        #     ],
        #     'list_since_obj': [
        #         {'name': self.key_db[9],
        #          'contains': " к.э.н."
        #          },
        #         {'name': self.key_db[9],
        #          'contains': "д.э.н."
        #          },
        #         {'name': self.key_db[9],
        #          'contains': "степень отсутствует"
        #          }
        #     ],
        #     'list_job_obj': [
        #         {'name': self.key_db[10],
        #          'contains': "Заведующий кафедры"
        #          },
        #         {'name': self.key_db[10],
        #          'contains': "Профессор кафедры"
        #          },
        #         {'name': self.key_db[10],
        #          'contains': "Доцент кафедры"
        #          },
        #         {'name': self.key_db[10],
        #          'contains': "Ст. преподаватель"
        #          },
        #         {'name': self.key_db[10],
        #          'contains': "Ассистент"
        #          },
        #     ],
        #     'list_people_obj': [
        #         {'name': self.key_db[11],
        #          'contains': "Щербаков Сергей Михайлович"
        #          },
        #         {'name': self.key_db[11],
        #          'contains': "Шполянская Ирина Юрьевна"
        #          },
        #         {'name': self.key_db[11],
        #          'contains': "Хубаев Георгий Николаевич"
        #          },
        #         {'name': self.key_db[11],
        #          'contains': "Долженко Алексей Иванович"
        #          },
        #         {'name': self.key_db[11],
        #          'contains': "Жебровская Людмила Анатольевна"
        #          },
        #         {'name': self.key_db[11],
        #          'contains': "Мирошниченко Ирина Иосифовна"
        #          },
        #         {'name': self.key_db[11],
        #          'contains': "Фрид Любовь Михайловна"
        #          },
        #         {'name': self.key_db[11],
        #          'contains': "Веретенникова Елена Григорьевна"
        #          },
        #         {'name': self.key_db[11],
        #          'contains': "АручидиНаталья Александровна"
        #          },
        #         {'name': self.key_db[11],
        #          'contains': "Курбесов Александр Валерьянович"
        #          },
        #         {'name': self.key_db[11],
        #          'contains': "Прохорова Анна Михайловна"
        #          },
        #         {'name': self.key_db[11],
        #          'contains': "Данилова Татьяна Викторовна"
        #          },
        #         {'name': self.key_db[11],
        #          'contains': "Шкодина Татьяна Андреевна"
        #          },
        #         {'name': self.key_db[11],
        #          'contains': "Потапов Леонид Игоревич"
        #          },
        #         {'name': self.key_db[11],
        #          'contains': "Глушенко Сергей Андреевич"
        #          },
        #         {'name': self.key_db[11],
        #          'contains': "Гречкина Вера Юрьевна"
        #          },
        #         {'name': self.key_db[11],
        #          'contains': "Яковец Светлана Владимировна"
        #          },
        #     ]
        # }
        return render(request,self.template_name,ctx)


    def post(self, request): # POST requset from page

        return HttpResponseRedirect("engineers/")

class HomePage(TemplateView):
    template_name = 'homepage.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("/login")

        ctx = {}
        return render(request, self.template_name, ctx)

class Dashboards(TemplateView):
    template_name = 'dashboards.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("/login")

        ctx = {}
        return render(request, self.template_name, ctx)

class ScheduleEngineer(TemplateView):
    template_name = 'scheduleengineer.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("/login")

        ctx = {}
        return render(request, self.template_name, ctx)

class Other(TemplateView):
    template_name = 'other.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("/login")

        ctx = {}
        return render(request, self.template_name, ctx)

# class Auth(TemplateView):
#     template_name = 'auth.html'
#
#     def get(self, request, *args, **kwargs):
#         ctx = {}
#         return render(request, self.template_name, ctx)
#
#     def post(self, request, *args, **kwargs):
#         # data = json.loads(request.body)
#         username = request.POST["username"]
#         password = request.POST["password"]
#         # print(data)
#         user = authenticate(username=username, password=password)
#         print(user)
#         if user is not None:
#             return JsonResponse({"validate": "A backend authenticated the credentials"})
#         else:
#             return JsonResponse({"validate":"No backend authenticated the credentials"})


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django import forms
from django.contrib import messages


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have been successfully logged in.')
                return redirect('/home/')  # Redirect to home page after successful login
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
        return render(request, 'login.html', {'form': form})