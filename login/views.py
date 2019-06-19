from django.shortcuts import render, redirect
from . import models, forms


def index(request):
    if not request.session.get("is_login", None):
        return redirect("/login/")
    return render(request, "login/index.html")


def login(request):
    if request.session.get("is_login", None):       # 不允许重复登录
        return redirect("/index/")
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = "用户名或密码不能为空！"
        if login_form.is_valid():
            username = login_form.cleaned_data.get("username")
            password = login_form.cleaned_data.get("password")
            # if username.strip() and password:   # 确保用户名和密码不为空
            # 其他更多验证 。。。
            try:
                user = models.User.objects.get(name=username)
            except:
                message = "用户不存在！"
                return render(request, "login/login.html", locals())

            if user.password == password:
                request.session["is_login"] = True
                request.session["user_id"] = user.id
                request.session["user_name"] = user.name
                return redirect("/index/")
            else:
                message = "密码不正确！"
                return render(request, "login/login.html", locals())
        else:
            return render(request, "login/login.html", locals())
    login_form = forms.UserForm()
    return render(request, "login/login.html", locals())


def register(request):
    pass
    return render(request, "login/register.html")


def logout(request):
    if not request.session.get("is_login", None):
        return redirect("/login/")
    request.session.flush()     # 删除当前的会话数据和会话cookie。经常用在用户退出后，删除会话。
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/login/")



