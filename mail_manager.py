import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import SENDER_EMAIL, EMAIL_APP_PASSWORD

def send_story_to_gmail(story_content):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = SENDER_EMAIL
    msg['Subject'] = "✨ Story Agent V2"
    msg.attach(MIMEText(f"Hi Madhu!\n\n{story_content}", 'plain'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, EMAIL_APP_PASSWORD)
        server.sendmail(SENDER_EMAIL, SENDER_EMAIL, msg.as_string())
        server.quit()
        print("✅ Email sent!")
    except Exception as e:
        print(f"❌ Error: {e}")