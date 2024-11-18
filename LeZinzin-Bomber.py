# By @LeZinzin - Version 1.0 
# Github : https://github.com/LeZinzin
# Thanks for using my tools !

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import time
from datetime import datetime

try:
    if os.name == 'nt':
        os.system("title LeZinzinBomber@1.0")
    else:
        os.system("echo -ne '\033]0;LeZinzinBomber@1.0\a'")
except Exception as e:
    print(f"Failed to set console title: {e}")

TimeBaby = datetime.now().strftime("%H:%M:%S")

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'

class LeZinzinSender:
    def __init__(self, smtp_server, smtp_port, email_user, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email_user = email_user
        self.password = password

    def send_email(self, recipient, subject, message):
        msg = MIMEMultipart()
        msg['From'] = self.email_user
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.email_user, self.password)
                server.send_message(msg)
            return True
        except Exception as e:
            print(f"{Color.RED}[LeZinzinBomber@1.0] /Error: {str(e)}{Color.RESET}")
            return False

def prompt_for_input(prompt, default=None):
    user_input = input(prompt)
    return user_input.strip() or default

def get_positive_integer(prompt):
    while True:
        try:
            value = int(prompt_for_input(prompt))
            if value > 0:
                return value
            else:
                print(f"{Color.RED}[LeZinzinBomber@1.0] /Please enter a positive integer.{Color.RESET}")
        except ValueError:
            print(f"{Color.RED}[LeZinzinBomber@1.0] /Invalid input. Enter a numeric value.{Color.RESET}")

def LeZinzin_clear():
    os.system("cls" if os.name == "nt" else "clear")

def LeZinzin_main():
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    email_user = prompt_for_input(f"{Color.CYAN}[LeZinzinBomber@1.0] /Your email: {Color.WHITE}", "LeZinzinBomber@gmail.com")
    password = prompt_for_input(f"{Color.CYAN}[LeZinzinBomber@1.0] /Your email password: {Color.WHITE}", "LeZinzin-Password")

    LeZinzin_sender = LeZinzinSender(smtp_server, smtp_port, email_user, password)

    while True:
        recipient = prompt_for_input(f"{Color.CYAN}[LeZinzinBomber@1.0] /Recipient's email: {Color.WHITE}")
        subject = prompt_for_input(f"{Color.CYAN}[LeZinzinBomber@1.0] /Email subject: {Color.WHITE}")
        message = prompt_for_input(f"{Color.CYAN}[LeZinzinBomber@1.0] /Email message: {Color.WHITE}")
        number_of_emails = get_positive_integer(f"{Color.CYAN}[LeZinzinBomber@1.0] /How many emails to send? {Color.WHITE}")

        print(f"{Color.YELLOW}[LeZinzinBomber@1.0] /Sending {number_of_emails} emails...{Color.RESET}")

        successful_sends = 0
        failed_sends = 0
        delay_between_emails = 5  

        for _ in range(number_of_emails):
            if LeZinzin_sender.send_email(recipient, subject, message):
                successful_sends += 1
                print(f'{Color.GREEN}[LeZinzinBomber@1.0] /Email successfully sent to: {Color.RED}{recipient}{Color.RESET}')
            else:
                failed_sends += 1
            
            time.sleep(delay_between_emails)  

        print(f"{Color.CYAN}[LeZinzinBomber@1.0] /Emails sent! {successful_sends} sent, {failed_sends} failed.{Color.RESET}")
        time.sleep(3)
        LeZinzin_clear()

if __name__ == "__main__":
    LeZinzin_clear() 
    LeZinzin_main()  
