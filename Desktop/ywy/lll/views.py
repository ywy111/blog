
from django.shortcuts import render

user = [{"name": "xiaoming", "pwd": "123456",  "answer":"lalaland" }]

def Loginpage(request):
    return render(request, "ywy.html")

def Changepage(request):
    return render(request, "changPwd.html")

def Login(request):

    username = request.POST.get("userName")
    userpwd = request.POST.get("password")


    result = ""
    if username != "" and userpwd != "":
        if request.POST.get("Login"):
            for temp in user:
                if username == temp["name"] and userpwd == temp["pwd"]:
                    result = "Success!"
                    return render(request, 'MainPage.html', {"result": result,"user":user,"name":username})
            result = "sorry"
            return render(request, "ywy.html", {"result": result})
        else:

            if request.POST.get("register") and len(userpwd) >= 6:
                return render(request, "Question.html")
            else:

                return render(request, "Question.html")

    else:
        result = "Sorry,name and password can't be empty."
        return render(request, "ywy.html", {"result": result})

def changePwd(request):
    result=""
    name = request.POST.get("name")
    oldPwd = request.POST.get("oldPwd")
    newPwd = request.POST.get("newPwd")



    for temp in user:
        if name == temp["name"]:
            if oldPwd == temp["pwd"]:
                result = "Successfully changed the password !"
                temp["pwd"]=newPwd
                return render(request, "changPwd.html", {"result": result})
            result = "The old password is wrong."
            return render(request,"changPwd.html",{"result":result})

        else:
            result = "The name has not been registered."
            return render(request, "changPwd.html",{"result":result})

def Registerpage(request):
    return render(request, "Question.html")


def Register(request):
    username = request.POST.get("name")
    userpwd = request.POST.get("pwd")
    useranswer = request.POST.get("answer")

    for temp in user:
        if temp["name"] == username:
            result = "sorry, the name has been used"
            return render(request, "ywy.html", {"result": result})
    temp = {"name": "username", "pwd": "userpwd", "answer": "useranswer"}
    user.append(temp)
    result = "successfully registered"
    return render(request,"MainPage.html", {"result": result})

def findPage(request):

    return render(request, "findPwd.html")


def findPwd(request):
    if request.POST.get("tofind"):
        username = request.POST.get("name")
        useranswer = request.POST.get("theanswer")
        for temp in user:
            if useranswer == temp["answer"] and username == temp["name"]:
                result = "successful"
                temp["pwd"] = "123456"
                return render(request, "changPwd.html", {"result": result, "pwd": temp["pwd"]})
            else:
                result = "Sorry, the answer is wrong."
                return render(request, "findPwd.html", {"result": result})

