from django.forms import forms
from django.shortcuts import render ,render_to_response,redirect
from DjangoUeditor.forms import UEditorField
from .models import Article


# Create your views here.

class TestUEditorForm(forms.Form):
    content = UEditorField('内容', width=600, height=600, toolbars="full", imagePath="images/", filePath="files/",
                           upload_settings={"imageMaxSize": 1204000},
                           settings={})


# def index(request):
#     form=Article.objects
#     return render(request, 'home.html')#, {'form': form})
def home(request):
    return  render(request,'home.html')
def welcome(request):
    return  render(request,'welcome.html')
def page(request):
    item=Article.objects
    return render(request, 'page.html',{'item':item})
def passpage(request):
    if request.method=="POST":
        if request.POST['answer'] == 'love':
            return  redirect(page)
        else:
            return render(request,'gun.html')
      
    else:
        return render(request,'passpage.html')