from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .form import CreateUserForm
from .forms import SimpleFindingForm
from django.contrib import messages
from .models import GeneralInformationTbl, SecretNumberTbl, DocumentTbl
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
                    # res_ = SecretNumberTbl.objects.get(secret_number_fld=fields[i])
                    # result = [i for i in SecretNumberTbl.objects.filter(secret_number_fld=fields[i]).values('secret_number_fld')
                    #           ]
                    # print(res_)
                    # print(ConclusionTbl.objects.select_related('secret_number_fld').get(secret_number_fld=fields[i]))
                    print([type(i) for i in list(DocumentTbl.objects.select_related('secret_number_fld').all())])
                    # result = DocumentTbl.objects.select_related().filter(secret_number_fld__secret_number_fld=fields[i]).values()
                    queryset = DocumentTbl.objects.select_related().filter(secret_number_fld__secret_number_fld=fields[i])
                    result = []
                    for query in queryset:
                        result.append({'Файл': query.file_location_fld, 'Исполнитель': query.executor_fld.worker_name_fld, 'Секретный номер': query.secret_number_fld.secret_number_fld})
                    print('result: ', result)
                    if result:
                        dict_[fields[i]] = result
        print(dict_)
        if dict_:
            return JsonResponse(json.dumps(dict_, default=str), status=200, safe=False)
        else:
            return JsonResponse(json.dumps({"errors": 'Не найдено ни одно значение, удовлетворяющее условиям поиска'}), status=200, safe=False)
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
