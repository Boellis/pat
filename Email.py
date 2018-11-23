# Uses python3
import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'brandon.ellis15@hotmail.com'
PASSWORD = 'Programmer1468!'

def get_contacts(filename):
    '''
    Return two list names, emails containing names and email addresses read from a file specified by filename
    '''
    names = []
    emails = []

    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
        return names, emails

def read_template(filename):
    '''
    Returns a template object comprising the contents of the file specified by filename
    '''

    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def emailBody():
    with open('message.txt', 'r') as file:
        data = file.readlines()

    body_message = input("What message would you like as your email body?")
    #data[1] = 'bepp beep beep beep\n'
    data[1] = "{}\n".format(body_message)

    with open('message.txt', 'w') as file:
        file.writelines(data)

def main():
    names, emails = get_contacts('mycontacts.txt') # read contacts
    emailBody()
    message_template = read_template('message.txt')

    # setup the SMTP server
    s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart() # Create Message

        # Add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())

        # Prints out the message for our sake
        print(message)

        # Setup the parameters of the message
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']="This is a test"

        # Add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # Send the message via the server setup earlier
        s.send_message(msg)
        del msg
    # Terminate the SMTP session and close the connection


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Stopped the program")
