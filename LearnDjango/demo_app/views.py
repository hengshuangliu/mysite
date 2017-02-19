from django.shortcuts import render
from django.http import HttpResponse
from demo_app import models
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
# user_list = [
#     {"user": "jack", "pwd": "abc"},
#     {"user": "tom", "pwd": "123"}
# ]


def index(request):
    # return HttpResponse("Hello World")
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        # print(username, password)
        # temp_user = {"user": username, "pwd": password}
        # user_list.append(temp_user)
        models.UserInfo.objects.create(user=username, pwd=password) # save data in database.
    user_list = models.UserInfo.objects.all() # get data from database.
    if request.method == 'GET':
        a = request.GET.get('a', 0)
        b = request.GET.get('b', 0)
    add_result = str(int(a) + int(b))
    return render(request, "index.html", {"data": user_list, "a": a, "b": b, "add_result": add_result})


def demo_add(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def new_add(request, a, b):
    return HttpResponseRedirect(reverse("demo_add", args=(a, b))) # realize redirecting.


# def add2(request):
#     a = request.GET.get('a',None)
#     b = request.GET.get('b',None)
#     a = int(a)
#     b = int(b)
#     return HttpResponse(str(a + b))

