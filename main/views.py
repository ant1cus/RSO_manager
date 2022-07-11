import os
import re

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .form import CreateUserForm
from .forms import SimpleFindingForm
from django.contrib import messages
from .models import GeneralInformationTbl, SecretNumberTbl, DocumentTbl, AccompainingSheetTbl, ComplectTbl
from django.http import JsonResponse, HttpResponse
from django.core import serializers
import json
from django.forms.models import model_to_dict


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def greetings(request):
    return render(request, 'main/greetings.html')


def finding(request):
    if is_ajax(request=request):
        simple_finding_list = ['gk', 'project', 'order', 'complect', 'sn', 'name', 'manufactur', 'secretnum', 'mark']
        fields = [request.POST.get(i) for i in simple_finding_list]
        print(fields)
        print(len(fields))
        dict_ = {}
        for i in [7, 4, 8, 2, 3, 5, 1, 0, 6]:
            print(i)
            if fields[i]:
                if i == 0:
                    result = [i for i in GeneralInformationTbl.objects.filter(gk_fld=fields[i]).values('gk_fld',
                                                                                                       'date_fld',
                                                                                                       'department_fld')
                              ]
                    print(result)
                    if result:
                        dict_[fields[i]] = result
                if i == 7:
                    queryset = DocumentTbl.objects.select_related().filter(secret_number_fld__secret_number_fld=fields[i])
                    order_id = queryset[0].complect_fld.order_fld.order_id
                    acc_sheet = AccompainingSheetTbl.objects.filter(order_fld=order_id).values('file_location_fld')[0]['file_location_fld']
                    complect = queryset[0].complect_fld
                    documents = DocumentTbl.objects.filter(complect_fld=complect)
                    conclusion = protocol = preciption = False
                    for document in documents:
                        name_doc = document.file_location_fld
                        if re.findall('заключение', name_doc.rpartition('\\')[2].partition('.')[0].lower()):
                            conclusion = name_doc
                        elif re.findall('протокол', name_doc.rpartition('\\')[2].partition('.')[0].lower()):
                            protocol = name_doc
                        else:
                            preciption = name_doc
                    result = []
                    for query in queryset:
                        result.append({'Заказ': query.complect_fld.order_fld.name_order_fld,
                                       'Сопровод': acc_sheet,
                                       'Заключение': conclusion,
                                       'Протокол': protocol,
                                       'Предписание': preciption})
                    print('result: ', result)
                    if result:
                        dict_[fields[i]] = result
        print(dict_)
        if dict_:
            return JsonResponse(json.dumps(dict_, default=str), status=200, safe=False)
        else:
            return JsonResponse(json.dumps({"errors": 'Не найдено ни одно значение, удовлетворяющее условиям поиска'}), status=200, safe=False)
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


def open_doc(request):
    file = request.GET.get('file')
    print(file)
    os.startfile(file, 'open')
    return JsonResponse(status=200)
