
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 构建一个MIMEMultipart邮件
msg = MIMEMultipart("alternative")

# 构建一个HTML邮件内容
html_content = """
            <!DOCTYPE html>
            <html lang="en"
            <head>
                <meta charset="UTF-8">
                <title>Title</title>
            </head>
            <body>
            
            <h1>这是一封HTML格式邮件</h1>
            
            </body>
            </html>
        """
#
msg_html = MIMEText(html_content, "html", "utf-8")
msg.attach(msg_html)

msg_text = MIMEText("just text content", "plain", "utf-8")
msg.attach(msg_text)


# 发送email地址，此处地址直接使用我的qq邮箱，密码临时输入
from_addr = "1295278@qq.com"
# from_pwd = input('163邮箱密码：')
from_pwd = "ahtxbprhlicbbagc"

# 收件人信息：
# 此处使用我注册的163邮箱
to_addr = "1295278@qq.com"

# 输入smtp服务器地址
# 此地址根据每隔邮件服务商有不同的值，这个是发信邮件服务商的smtp地址
# 我用的是qq邮箱发送，此处应该填写腾qq邮箱的smtp值，即smtp.163.com,
# 需要开启授权码
smtp_srv = "smtp.qq.com"


try:
    import smtplib

    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465)

    srv.login(from_addr, from_pwd)
    srv.sendmail(from_addr, [to_addr], msg.as_string())
    srv.quit()

except Exception as e:
    print(e)













