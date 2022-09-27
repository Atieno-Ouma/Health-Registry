from functools import wraps
from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv, xlwt

from .models import *
from .forms import  ClientUpdateForm,FacilityCreateForm,ClientCreateForm, StockIssuedSearchForm,FacilitySearchForm,FacilityUpdateForm,PatientSearchForm,ReportSearchForm
from django.contrib import messages
import datetime

# Views.

def home(request):
    title = 'Welcome to the e-health registry'
    form = "Hello i am form"
    context = {
        "title": title,
    }
    return render(request, "home.html",context)




def list_facility(request,self):
    title = 'Facility List'
    # Filter by Search
    form = FacilitySearchForm(request.POST or None)

    queryset = Facility.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
        "form": form
    }
    if request.method == 'POST':
        queryset = Facility.objects.filter(item_name__icontains=form['facility_name'].value())


        if form['facility_name'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List of facility.csv"'
            writer = csv.writer(response)
            writer.writerow(['KMFL_code', 'facility_Name'])
            instance = queryset
            for facility in instance:
                writer.writerow([facility.KMFL_code, facility.facility_name])
            return response
        context = {
            "form": form,
            "title": title,
            "queryset": queryset,
        }
    return render(request, "list_facility.html", context)

def list_client(request):
    title = 'Clients List'
    # Filter by Search
    form = PatientSearchForm(request.POST or None)

    queryset = Client.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
        "form": form
    }
    if request.method == 'POST':
        queryset = Client.objects.filter(item_name__icontains=form['client_name'].value())
        if form['client_name'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List of client.csv"'
            writer = csv.writer(response)
            writer.writerow(['id', 'client_name'])
            instance = queryset
            for client in instance:
                writer.writerow([client.id, client.client_name])
            return response
        context = {
            "form": form,
            "title": title,
            "queryset": queryset,
        }
    return render(request, "list_patient.html", context)



def add_client(request):
    form = ClientCreateForm(request.POST or None)
    if form.is_valid():

        form.save()
        return redirect('/list_client')
    context = {
        "form": form,
        "title": "Add Client",
    }
    return render(request, "add_client.html", context)


def add_Facility(request):
    form = FacilityCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/list_facility')
    context = {
        "form": form,
        "title": "Add Facility",
    }
    return render(request, "add_facility.html", context)

def update_facility(request, pk):
    queryset = Facility.objects.get(KMFL_code=pk)
    form = FacilityUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = FacilityUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/list_facility')

    context = {
        'form':form
    }
    return render(request, 'add_facility.html', context)

def update_client(request, pk):
    queryset = Client.objects.get(id=pk)
    form = ClientUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = ClientUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/list_client')

    context = {
        'form':form
    }
    return render(request, 'add_client.html', context)



def delete_facility(request, pk):
    queryset = Facility.objects.get(KMFL_code=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('/list_facility')
    return render(request, 'delete_items.html')

def delete_client(request, pk):
    queryset = Client.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('/list_client')
    return render(request, 'delete_items.html')

def stock_detail(request, pk):
    queryset = Facility.objects.get(KMFL_code=pk)
    context = {
        "title": queryset.item_name,
        "queryset": queryset,
    }
    return render(request, "stock_detail.html", context)



def facility_report(request):
    title = 'Reports'
    queryset = Stock_Issued.objects.all()
    form = StockIssuedSearchForm(request.POST or None)
    context = {
        "title": title,
        "queryset": queryset,
        "form": form,
    }
    if request.method == 'POST':
        item_name = form['facility_name'].value()
        queryset = Stock_Issued.objects.filter(
                                item_name__icontains=form['item_name'].value()
                                )
        if (item_name != ''):
            queryset = queryset.filter(item_name_id_id=item_name)
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="Issued Stock.csv"'
            writer = csv.writer(response)
            writer.writerow(
                [
                'ITEM NAME',
                'QUANTITY',
                'ISSUE QUANTITY',
                'ISSUE TO',
                'DATE'])
            instance = queryset
            for stock in instance:
                writer.writerow(
                [
                stock.item_name,
                stock.quantity,
                stock.issue_quantity,
                stock.issue_to,
                stock.timestamp])
            return response
        context = {
        "form": form,
        "title": title,
        "queryset": queryset,
    }
    return render(request, "stock_issued.html",context)