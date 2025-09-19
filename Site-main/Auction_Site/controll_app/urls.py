"""
URL configuration for Auction_Site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.views.generic import TemplateView

from controll_app import views

urlpatterns = [
    path('orders/', TemplateView.as_view(template_name='auction/orders.html'), name='orders'),
    path('lots/',  views.Auction.as_view(), name="lots"),

    path('lots/<str:lot>',  views.Product.as_view(), name="lot"),

    path('place_a_bet', views.place_a_bet, name='place_a_bet')
]
