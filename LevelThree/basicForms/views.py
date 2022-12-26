from django.shortcuts import render
from . import forms

def index(request):
    return render(request,"basicForms/index.html")

def form_name_view(request):
    form=forms.FormName()

    #Check to see if we get the post back
    if request.method=="POST":
        #In which case we pass in that request
        form=forms.FormName(request.POST)
        #Check to see form is validation
        if form.is_valid():
            #Do ssomething
            print("VALIDATION SUCCESS!")
            print("Name : "+form.cleaned_data["name"])
            print("Email : "+form.cleaned_data["email"])
            print("Text : "+form.cleaned_data["text"])





    return render(request,"basicForms/form_page.html",{'form':form})
