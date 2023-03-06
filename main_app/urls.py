from django.urls import path
from . import views

urlpatterns = [
    # using an empty string here makes this our root route
    # views.home refers to a file to render
    # the name='home' kwarg gives the route a name
    # naming routes is optional, but best practices
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # route for cats index
    path('cats/', views.cats_index, name='index'),
    path('cats/create/', views.CatCreate.as_view(), name='cats_create'),
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cats_update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cats_delete'),
    path('cats/<int:cat_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('cats/<int:cat_id>/', views.cats_detail, name='detail'),
    # add association
    path('cats/<int:cat_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    # add unassociation
    path('cats/<int:cat_id>/unassoc_toy/<int:toy_id>/', views.unassoc_toy, name='unassoc_toy'),
    # add photo
    path('cats/<int:cat_id>/add_photo/', views.add_photo, name='add_photo'),
    # toys down here
    # index, show, create, update, delete
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    # sign up new user
    path('accounts/signup/', views.signup, name='signup')
]