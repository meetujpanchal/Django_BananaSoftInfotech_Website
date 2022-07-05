from django.shortcuts import render , get_object_or_404
from .models import TblTeam, Tblclient,Tblslider,Tblcontact,Tbltestimonial,Tblenquiry,Tblrecentwork,Category,Story
from .forms import Contact_us_form
from django.http import HttpResponse
import csv

# Create your views here.
def show_page(request):
    contacts = Tblcontact.objects.all()
    sliders = Tblslider.objects.all()
    pot = Tblrecentwork.objects.all()
    cln = Tblclient.objects.all()
    categories = Category.objects.all()
    story = Story.objects.all()
    return render(request, 'web_banana/show.html',{'sliders':sliders,'contacts':contacts,'pot':pot,'cln':cln,'story':story,'categories':categories})

def team(request):
    stud = TblTeam.objects.all()
    sliders = Tblslider.objects.all()
    return render(request,'web_banana/ourteam.html',{'stu':stud,'sliders':sliders})

def about(request):
    sliders = Tblslider.objects.all()
    return render(request,'web_banana/aboutbananit.html',{'sliders':sliders})

def testi(request):
    contacts = Tblcontact.objects.all()
    testimonials = Tbltestimonial.objects.all()
    sliders = Tblslider.objects.all()
    return render(request,'web_banana/testimonial.html',{'contacts':contacts,'testimonials':testimonials,'sliders':sliders})

def services(request):
    stud = TblTeam.objects.all()
    sliders = Tblslider.objects.all()
    return render(request,'web_banana/service.html',{'stu':stud,'sliders':sliders})

def contactus(request):
    if request.method == "POST":
        fm = Contact_us_form(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ds = fm.cleaned_data['description']
            reg = Tblenquiry(name=nm,email=em,description=ds)
            reg.save()
    else:
        fm = Contact_us_form()    
    return render(request,'web_banana/contact_us.html',{'form':fm})

def careerpg(request):
    sliders = Tblslider.objects.all()
    stud = TblTeam.objects.all()
    return render(request,'web_banana/career.html',{'sliders':sliders,'stud':stud})

def price(request):
    sliders = Tblslider.objects.all()
    return render(request,'web_banana/pricing.html',{'sliders':sliders})

def clnt(request):
    sliders = Tblslider.objects.all()
    cln = Tblclient.objects.all()
    return render(request,'web_banana/client.html',{'sliders':sliders,'cln':cln})

#def port(request):
    sliders = Tblslider.objects.all()
    pot = Tblrecentwork.objects.all()
    return render(request,'web_banana/potfolio.html',{'sliders':sliders,'pot':pot})
    
def export_csv(request):

    responese=HttpResponse(content_type='text/csv')
    responese['Content-Disposition']='attachment; filename="Enquiry.csv" '

    writer=csv.writer(responese)
    writer.writerow(['Name','Email','Description'])

    for enquiry in Tblenquiry.objects.all().values_list('name','email','description'):
        writer.writerow(enquiry)

    return responese    

def story_list(request,category_slug=None):
    sliders = Tblslider.objects.all()
    category=None
    categories = Category.objects.all()
    story = Story.objects.all()
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        story = story.filter(category=category)
    return render(request, 'web_banana/potfolio.html',{'categories':categories,'story':story,'category':category,'sliders':sliders})