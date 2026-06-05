import smtplib
import streamlit as st
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_story_to_gmail(story_content):
    sender_email = st.secrets["SENDER_EMAIL"]
    email_password = st.secrets["EMAIL_APP_PASSWORD"]
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = sender_email
    msg['Subject'] = "✨ Story Agent V2"
    msg.attach(MIMEText(f"Hi Murugeswari!\n\n{story_content}", 'plain'))
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, email_password)
        server.sendmail(sender_email, sender_email, msg.as_string())
        server.quit()
        return True
    except:
        return False