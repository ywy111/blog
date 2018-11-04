
from django.shortcuts import render
from lll.models import *
from .models import user
from .forms import *
import pdb
from django.template import loader ,Context
from django.http import HttpResponse

response = HttpResponse('ok')
response.set_cookie('hello', 'django', expires=60*60*24*7)



def main(request):
    response = request.COOKIES.get
    response = request.get_signed_cookie(key='name', default='无', max_age=None)
    response.set_cookie('my_cookie','cookie value')
    return response




def Loginpage(request):
    return render(request, "ywy.html")


def Login(request):

    form = LoginForm(request.POST)
    if form.is_valid():
        result = "成功"
        main()
        return render(request, 'MainPage.html', {"result": result})

    else:
        result = "密码错误，请重新输入密码"
        return render(request, "ywy.html", {"result": result, "form": form})



def Changepage(request):
    return render(request, "changPwd.html")




def changePwd(request):
    form=changeForm(request.POST)
    if form.is_valid():
        form.save()
        result = "successfully changed the password"
        return render(request, "ywy.html", {"result": result, "form":form})
    else:
        result = "sorry"
        return render(request, "changPwd.html", {"result": result, "form": form})


def Registerpage(request):
    return render(request, "Question.html")

def Register(request):
    form=ModelRegisterForm(request.POST)
    if form.is_valid():
        form.save()
        result = "successfully registered"
        return render(request, "MainPage.html", {"result": result})
    else:
        result = "sorry, the name has been used"
        return render(request, "Question.html", {"result": result,"form":form})










def findPage(request):
    return render(request, "findPwd.html")


def findPwd(request):
    if request.POST.get("tofind"):
        username = request.POST.get("name")
        useranswer = request.POST.get("theanswer")

        for f in user:
            if username == f.name and useranswer == f.answer:
                result = "答案正确"
                return render(request, "setNewpwd.html", {'result': result})


def setpwd(request):
    return render(request, "setNewpwd.html")



def setPwd(request):
    if request.method == "POST":
        form = ModelRegisterForm(request.POST)
        if form.is_valid():
            User = user(name=form.cleaned_data['name'],
                        pwd=form.cleaned_data['pwd'],
                        answer=form.cleaned_data['answer']
                        )
            User.save()
            result = "修改成功"
            return render(request, 'ywy.html', {"result": result})
        else:
            for f in form:
                print(type(f.errors))




def blog(request):
    return render(request,'ywy.html')
    # blog_title = request.POST.get("blog_title")
    # blog_content = request.POST.get("blog_content")
    # blogInfo = blog_user(blog_title=blog_title,
    #                      blog_author=)
