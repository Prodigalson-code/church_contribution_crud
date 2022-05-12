from multiprocessing import context
from django.shortcuts import get_object_or_404, render,redirect
from django.views import View 
from django.contrib.auth import authenticate,login,logout


from contribution.models import ChurchMember, Contribution, Contributor
from django.db.models import Sum
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login')
def index(request):
    """Main method for displaying the dashboard"""
    return render(request,'pages/index.html')


 # All CREATE methods 
    
@login_required(login_url='login')
def createMember(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        middlename = request.POST['middlename']
        lastname = request.POST['lastname']
        age = request.POST['age']
        gender = request.POST['gender']
        address = request.POST['address']

        member = ChurchMember.objects.create(
            first_name=firstname,
            middle_name=middlename,
            last_name=lastname,
            age=age,
            gender=gender,
            address=address
        )

        member.save()
        return redirect('members')


@login_required(login_url='login')
def createContribution(request):
    if request.method == 'POST':
        contributionName = request.POST['contributionName']
        contributionDetail = request.POST['contributionDetail']
        contributionTargetedAmount = request.POST['contributionTargetedAmount']

        contribution = Contribution.objects.create(
            contribution_name = contributionName,
            contribution_details = contributionDetail,
            contribution_targeted_amount = contributionTargetedAmount
        )

        contribution.save()
        return redirect('contributions')


@login_required(login_url='login')
def createContributor(request):
    if request.method == 'POST':
        contributorName = request.POST['contributorName']
        contribution =request.POST['contribution']
        amountPaid = request.POST['amountPaid']

        contributor = Contributor.objects.create(
            contributor_name = ChurchMember.objects.get(id=int(contributorName)),
            contribution = Contribution.objects.get(id=int(contribution)),
            amount_paid = amountPaid
        )

        contributor.save()
        return redirect('contributors')



# All RETREIVE methods 
@login_required(login_url='login')
def retrieveMember(request):
    members = ChurchMember.objects.all()
    return render(request, 'pages/members.html', {'members':members})

@login_required(login_url='login')
def retrieveContribution(request):
     contribution = Contribution.objects.all()
     context = {
         'contribution':contribution,
     }
     return render(request, 'pages/contribution.html',context)
  


@login_required(login_url='login')
def retrieveContributor(request):
    contributors = Contributor.objects.all()
    contributions = Contribution.objects.all()
    members =ChurchMember.objects.all()
    context = {
        'contributors':contributors,
        'contributions':contributions,
        'members':members
    }

    return render(request, 'pages/contributor.html',context)    



# All EDIT/UPDATE methods

@login_required(login_url='login')
def editMember(request,id):
    member = get_object_or_404(ChurchMember,pk=id)
    
    context ={
        'member':member,
        'values':member
    }

    if request.method == 'GET':

        return render(request, 'pages/edit_member.html', context)


    if request.method == 'POST':
        firstname = request.POST['firstname']
        middlename = request.POST['middlename']
        lastname = request.POST['lastname']
        age = request.POST['age']
        gender = request.POST['gender']
        address = request.POST['address']

        member.first_name = firstname
        member.middle_name = middlename
        member.lastname = lastname
        member.age = age
        member.gender = gender
        member.address = address

        member.save()
        return redirect('members')


@login_required(login_url='login')
def editContribution(request,id):
    contribution = get_object_or_404(Contribution,pk=id)
    context = {
        'contribution' : contribution,
        'values':contribution
    }

    if request.method == 'GET':
        return render(request, 'pages/edit_contribution.html', context)

    if request.method == 'POST':

        contributionName = request.POST['contributionName']
        contributionDetail = request.POST['contributionDetail']
        contributionTargetedAmount = request.POST['contributionTargetedAmount']

        contribution.contribution_name = contributionName
        contribution.contribution_details = contributionDetail
        contribution.contribution_targeted_amount = contributionTargetedAmount

        contribution.save()
        return redirect('contributions')


@login_required(login_url='login')
def editContributor(request,id):
    contributor = get_object_or_404(Contributor,pk=id)
    contributions = Contribution.objects.all()
    members =ChurchMember.objects.all()
    context = {
        'contributor':contributor,
        'values':contributor,
        'contributions':contributions,
        'members':members

    }

    if request.method == 'GET':
        return render(request, 'pages/edit_contributor.html',context)

    if request.method == 'POST':
        contributorName = request.POST['contributorName']
        contribution =request.POST['contribution']
        amountPaid = request.POST['amountPaid']

        cmember=ChurchMember.objects.get(id=contributorName)
        cont=Contribution.objects.get(id=contribution)

        contributor.contributor_name = cmember
        contributor.contribution =  cont
        contributor.amount_paid = amountPaid

        contributor.save()
        return redirect('contributors')



# All DELETE methods

@login_required(login_url='login')
def deleteMember(request,id):
    member = get_object_or_404(ChurchMember, pk=id) 
    member.delete()
    return redirect('members')  

@login_required(login_url='login')
def deleteContribution(request,id):
    contribution = get_object_or_404(Contribution,pk=id)
    contribution.delete()
    return redirect('contributions')  

@login_required(login_url='login')
def deleteContributor(request,id):
    contributor = get_object_or_404(Contributor,pk=id)
    contributor.delete()
    return redirect('contributors')


# RANKING Member

@login_required(login_url='login')
def ratingMember(request):
    
    member = ChurchMember.objects.values('first_name','last_name').annotate(amountpaid=Sum('contributor__amount_paid')).order_by('-amountpaid')
    context={
        'member':member
    }
    return render(request, 'pages/rating.html',context)



# LOGIN METHOD


def userlogin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
                """Getting input field from login form"""
                username=request.POST.get('username')
                password=request.POST.get('password')

                """authenticate input fields"""
                user = authenticate(request, username=username, password=password)

                """Checking if user is existing, then allowed to login and redirect to dashboard"""
                if user is not None:

                    login(request,user)
                    return redirect('home')
    return render(request, 'pages/login.html')     
              


#LOGOUT

def userlogout(request):
        logout(request)
        return redirect('login') 













      









    




            
         













 
        
        
            






   
 





 
 
         
 
      