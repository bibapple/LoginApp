from django.conf import settings


def send_email(email, code):
    from django.core.mail import EmailMultiAlternatives
    subjects = "来自火星的注册确认邮件！"
    text_content = "感谢注册地球账号！"
    html_content = """
                    <p>感谢注册<a href="http://{}/confirm/?code={}" target=blank>www.baidu.com</a>，\
                    这是地球上最好的搜索引擎！</p>
                    <p>请点击站点链接完成注册确认！</p>
                    <p>此链接有效期为{}天！</p>
                   """.format("127.0.0.1:8000", code, settings.CONFIRM_DAYS)
    msg = EmailMultiAlternatives(subjects, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()



