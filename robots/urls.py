from django.urls import path
from robots import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('manu/', views.manu, name='manu'),

    path('manu/<int:pk>/',
         views.ManufacturerDetail.as_view(),
         name='manufacturer-detail'),

    path('robocat/', views.robocat, name='robocat'),

    path('thanks/', views.thanks, name='thanks'),

    path('robocategory/',
         views.RobotCategoryList.as_view(),
         name='robotcategory-list'),
    path('robocategory/<int:pk>/',
         views.RobotCategoryDetail.as_view(),
         name='robotcategory-detail'),
    path('manufacturer/',
         views.ManufacturerList.as_view(),
         name='manufacturer-list'),
    path('manufacturer/<int:pk>/',
         views.ManufacturerDetail.as_view(),
         name='manufacturer-detail'),
    path('robot/',
         views.RobotList.as_view(),
         name='robot-list'),
    path('robot/<int:pk>/',
         views.RobotDetail.as_view(),
         name='robot-detail'),
    path('',
         views.ApiRoot.as_view(),
         name=views.ApiRoot.name)
]
