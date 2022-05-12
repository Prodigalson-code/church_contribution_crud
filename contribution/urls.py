from django.urls import path
from . import views

urlpatterns = [

    path('home/', views.index, name='home'),
   
    path('create-member/',views.createMember, name='create-member'),
    path('members/',views.retrieveMember, name='members'),
    path('edit-member/<int:id>',views.editMember, name='edit-member'),
    path('delete-member/<int:id>',views.deleteMember, name='delete-member'),

    path('create-contribution/',views.createContribution, name='create-contribution'),
    path('list-contributions/', views.retrieveContribution, name='contributions'),
    path('edit-contribution/<int:id>',views.editContribution, name='edit-contribution'),
    path('delete-contribution/<int:id>',views.deleteContribution, name='delete-contribution'),

    path('create-contributor/',views.createContributor, name='create-contributor'),
    path('list-contributors/', views.retrieveContributor, name='contributors'),
    path('edit-contributor/<int:id>',views.editContributor, name='edit-contributor'),
    path('delete-contributor/<int:id>',views.deleteContributor, name='delete-contributor'),

    path('rank/', views.ratingMember, name='rank'),

    path('',views.userlogin, name='login'),
    path('logout/',views.userlogout, name='logout'),
    
    
]