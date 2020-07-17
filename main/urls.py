from django.urls import path
from . import views


app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("main/", views.mainpage, name="main page"),
    path("contact/", views.contact, name="contact"),
    path("wd/", views.webdesign, name="webdesign"),
    path("graphics/", views.graphicsdesign, name="graphicsdesign"),
    path("socialmedia/", views.socialmedia, name="socialmedia"),
    path("team/", views.team, name="team"),
    path("policy/", views.policy, name="policy"),
    path("strategy/", views.strategy, name="strategy"),
    path("contact/contactpost/",views.contactpost,name="contactpost"),
    path("landingpost",views.landingpost,name="landingpost"),
    path("subscribepost",views.subscribepost,name="subscribepost")

]
