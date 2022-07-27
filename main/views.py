import os
import re

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .form import CreateUserForm
from .forms import SimpleFindingForm, AddNotesForm
from django.contrib import messages
from .models import GeneralInformationTbl, SecretNumberTbl, DocumentTbl, AccompainingSheetTbl, ComplectTbl,\
    DeviceDocumentTbl, NotesTbl
from django.http import JsonResponse, HttpResponse
from django.core import serializers
import json
from django.forms.models import model_to_dict


def is_ajax(request):
    return request.headers.get('x-requested-with') == 'XMLHttpRequest'


def greetings(request):
    return render(request, 'main/greetings.html')


def finding(request):
    if is_ajax(request=request):
        simple_finding_list = ['sn', 'secretnum', 'mark']
        fields = [request.POST.get(i) for i in simple_finding_list]
        result = []
        dict_ = {}
        note = []
        note_fld = {'question_number_fld': 'Запрос', 'date_fld': 'Дата', 'name_fld': 'ФИО',
                    'organization_fld': 'Организация', 'telephone_fld': 'Номер тел.', 'question_fld': 'Вопрос',
                    'add_notes_fld': 'Дополнительно'}
        for i in range(0, 3):
            if fields[i]:
                if i == 0:
                    queryset = DeviceDocumentTbl.objects.select_related().filter(device_fld__serial_number_fld=str(fields[i]))
                    for query in queryset:
                        if query.device_fld.notes_fld:
                            query_notes = NotesTbl.objects.filter(question_number_fld=str(fields[i])).values()
                            for element in list(query_notes):
                                note_dict = {}
                                for el in note_fld:
                                    note_dict[note_fld[el]] = element[el]
                                note.append(note_dict)
                        complect = query.document_fld.complect_fld
                        order_id = query.document_fld.complect_fld.order_fld.order_id
                        documents = DocumentTbl.objects.filter(complect_fld=complect)
                        acc_sheet = \
                            AccompainingSheetTbl.objects.filter(order_fld=order_id).values('file_location_fld')[0][
                                'file_location_fld']
                        conclusion = protocol = preciption = False
                        for document in documents:
                            name_doc = document.file_location_fld
                            if re.findall('заключение', name_doc.rpartition('\\')[2].partition('.')[0].lower()):
                                conclusion = name_doc
                            elif re.findall('протокол', name_doc.rpartition('\\')[2].partition('.')[0].lower()):
                                protocol = name_doc
                            else:
                                preciption = name_doc
                        result.append({'Заказ': query.document_fld.complect_fld.order_fld.name_order_fld,
                                       'Сопровод': acc_sheet,
                                       'Заключение': conclusion,
                                       'Протокол': protocol,
                                       'Предписание': preciption,
                                       'Заметки': note})
                    if result:
                        dict_[fields[i]] = result
                if i == 1:
                    queryset = DocumentTbl.objects.select_related().filter(secret_number_fld__secret_number_fld=fields[i])
                    for query in queryset:
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
                            result.append({'Заказ': query.complect_fld.order_fld.name_order_fld,
                                           'Сопровод': acc_sheet,
                                           'Заключение': conclusion,
                                           'Протокол': protocol,
                                           'Предписание': preciption})
                        if result:
                            dict_[fields[i]] = result
        if dict_:
            return JsonResponse(json.dumps(dict_, default=str), status=200, safe=False)
        else:
            return JsonResponse(json.dumps({"errors": 'Не найдено ни одно значение, удовлетворяющее условиям поиска'}), status=200, safe=False)
    form = SimpleFindingForm()
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
    return JsonResponse({'success': 'success'}, status=200)


def notes(request):
    notes_list = ['question_number_fld', 'date_fld', 'name_fld', 'organization_fld', 'telephone_fld',
                  'question_fld', 'add_notes_fld']
    if is_ajax(request=request) and request.method == 'POST':
        note = AddNotesForm(request.POST)
        print({i: request.POST.get(i) for i in notes_list})
        if note.is_valid():
            fields = {i: note.cleaned_data[i] for i in notes_list}
            # fields = {i: (form.cleaned_data[i] if form.cleaned_data[i] else False) for i in notes_list}
            print(fields)
            if fields is False:
                return JsonResponse(json.dumps({"errors": 'Ошибка'}), status=400, safe=False)
            dict_ = NotesTbl.objects.create(**fields)
            if dict_:
                return JsonResponse(json.dumps({"success": 'Успешно'}), status=200, safe=False)
            else:
                return JsonResponse(json.dumps({"errors": 'Ошибка'}), status=400, safe=False)
    else:
        note = AddNotesForm()
    context = {"note": note}
    return render(request, 'main/notes.html', context)
