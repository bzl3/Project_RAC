import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Mail_module:
    def __init__ (self, username, password, server_loc):
        self.server_loc = server_loc
        self.username = username
        self.password = password
        self.from_addr = username

    def set_from( self, new_from ):
        self.from_addr = new_from
        
    def sendmail(self, to_addr, subject, message):
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = self.from_addr
        msg['To'] = to_addr

        msg.attach(MIMEText(message, 'plain'))
        
        server = smtplib.SMTP(self.server_loc)
        server.starttls()
        server.login(self.username,self.password)
        problems = server.sendmail(self.from_addr, to_addr, msg.as_string())
        server.quit()
