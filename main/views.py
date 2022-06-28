from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .form import CreateUserForm
from .forms import SimpleFindingForm
from django.contrib import messages
from .models import GeneralInformationTbl
from django.http import JsonResponse, HttpResponse
from django.core import serializers
import json


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def greetings(request):
    return render(request, 'main/greetings.html')


def finding(request):
    if is_ajax(request=request):
        simple_finding_list = ['gk', 'project', 'order', 'complect', 'sn', 'name', 'manufactur', 'secretnum', 'mark']
        fields = [request.POST.get(i) for i in simple_finding_list if request.POST.get(i)]
        print(fields)
        print(len(fields))
        dict_ = {}
        for i, field in enumerate(fields):
            if field:
                if i == 0:
                    result = [i for i in GeneralInformationTbl.objects.filter(gk_fld=field).values('gk_fld', 'date_fld',
                                                                                                   'department_fld')]
                    print(result)
                    if result:
                        dict_[field] = result
        print(dict_)
        res_ = json.dumps(dict_, default=str)
        print(res_)
        if dict_:
            print(type(res_))
            return JsonResponse(res_, status=200, safe=False)
        else:
            return JsonResponse({"errors": 'Не найдено ни одно значение, удовлетворяющее условиям поиска'}, status=200)
    # form = SimpleFindingForm()
    # obj_ = serializers.serialize("json", GeneralInformationTbl.objects.all())
    # simple_finding_list = ['gk', 'project', 'order', 'complect', 'sn', 'name', 'manufactur', 'secretnum', 'mark']
    # print('raz')
    # print(obj_)
    # if is_ajax(request=request):
    #     print('dva')
    #     if form.is_valid():
    #         return JsonResponse({"errors": 'все работает'}, status=200)
    #     else:
    #         return JsonResponse({"errors": 'не работает'}, status=400)
        # ans = {}
        # for element in simple_finding_dict:
        #     ans[element] = request.POST.get(element)
        # print('ans->', ans)
        # form = SimpleFindingForm(request.POST)
        # if form.is_valid():
        #     print('three')
        #     fields = [request.POST.get(i) for i in simple_finding_list]
        #     print('1')
        #     if len(fields) == 0:
        #         print('2')
        #         return JsonResponse({"errors": 'НЕ ЗАПОЛНЕНО НИ ОДНО ПОЛЕ'}, status=400)
        #     print('3')
        #     dict_ = {}
        #     for i, field in enumerate(fields):
        #         print('cicle')
        #         if field:
        #             if i == 0:
        #                 dict_[field] = [i for i in GeneralInformationTbl.objects.filter(gk_fld=field).values('gk_fld', 'date_fld', 'department_fld')]
        #     if len(dict_) == 0:
        #         print('NONE')
        #         errors = form.errors.as_json()
        #         return JsonResponse({"errors": errors}, status=400)
        #     else:
        #         print('YES')
        #         return JsonResponse({'fields': dict_}, status=200)
        # else:
        #     errors = form.errors.as_json()
        #     return JsonResponse({"errors": errors}, status=400)
    form = SimpleFindingForm()
    print('four')
    return render(request, 'main/finding.html', {"form": form})


def loading(request):
    return render(request, 'main/loading.html')


def about(request):
    obj_ = GeneralInformationTbl.objects.all()
    return render(request, 'main/about.html', {'obj_': obj_})
    # return render(request, 'main/about.html')


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Аккаунт для пользователя ' + user + ' создан')
            return redirect('login')
    context = {"form": form}
    return render(request, 'main/register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if username is not None:
            if request.user.is_authenticated:
                login(request, user)
                if request.user.is_superuser:
                    return redirect('/admin')
                else:
                    return redirect('home')
            else:
                messages.info(request, 'Пользователя с таким логином не существует')
        else:
            messages.info(request, 'Не введено имя пользователя')

    context = {}
    return render(request, 'main/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

# def log_reg(request):
#     context = {}
#     return render(request, 'main/register.html', context)
