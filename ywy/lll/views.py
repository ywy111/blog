
from django.shortcuts import render

user = [{"name": "xiaoming", "pwd": "123456"}]

def Loginpage(request):
    return render(request, "ywy.html")


def Login(request):

    username = request.POST.get("username")
    userpwd = request.POST.get("password")
    result = ""
    if username != "" and userpwd != "":
        if request.POST.get("toLogin"):
            for temp in user:
                if username == temp["name"] and userpwd == temp["pwd"]:
                    result = "success"
                    return render(request, 'MainPage.html', {"result": result, "user": user, "name": username})
            result = "sorry"
            return render(request, "ywy.html", {"result": result})
        else:
            temp = {"name": username, "pwd": userpwd}
            user.append(temp)
            result = "success"
            return render(request, "ywy.html", {"result": result})



    else:
        result = "sorry"
        return render(request, "ywy.html", {"result": result})






# Create your views here.
