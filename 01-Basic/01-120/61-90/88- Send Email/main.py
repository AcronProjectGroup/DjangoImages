#!/usr/local/bin/python

from sys import stdin
from os import popen, system
from subprocess import check_output

logo = """
   ___     __    _____                    _   _
  / __\   / /    \_   \   /\/\     __ _  (_) | |      _ __    _   _
 / /     / /      / /\/  /    \   / _` | | | | |     | '_ \  | | | |
/ /___  / /___ /\/ /_   / /\/\ \ | (_| | | | | |  _  | |_) | | |_| |
\____/  \____/ \____/   \/    \/  \__,_| |_| |_| (_) | .__/   \__, |
                                                     |_|      |___/

Send emails via Sendmail.
"""
print(logo) 

SENDMAIL = str(check_output(['which', 'sendmail'])).strip()

if SENDMAIL == '':
    print("""Sendmail is not installed.
Try 'sudo apt-get install sendmail'.""")

print('=============================================================')
print('From: ')
sender = stdin.readline()
print('=============================================================')

print('To: ')
receiver = stdin.readline()
print('=============================================================')

print('Subject: ')
subject = stdin.readline()
print('=============================================================')

print("""Text:
Use <ctrl-d> to send.""")
text = stdin.readlines()
print("\n")
print('=============================================================')


p = popen("%s -t" % SENDMAIL, "w")

p.write("From: %s" % sender)
p.write("To: %s" % receiver)
p.write("Subject: %s" % subject)
# blank line separating headers from body
p.write("\n")
for line in text:
    p.write(line)

sts = p.close()

if sts != 0:
    print("\n")
    print('Your mail has been successfully sent. Sendmail exit status', sts)
    print("\n")
    print('Summary:')
    print("\n")
    print('From:', sender)
    print('=============================================================')
    print('To:', receiver)
    print('=============================================================')
    print('Subject:', subject)
    print('=============================================================')
    print('Text:', text)
    print("\n")
    print('=============================================================')

# via smtp
# import sys, smtplib
# fromaddr = raw_input("From: ")
# toaddrs  = string.splitfields(raw_input("To: "), ',')
# print "Enter message, end with ^D:"
# msg = ''
# while 1:
#     line = sys.stdin.readline()
#     if not line:
#         break
#     msg = msg + line
# # The actual mail send
# server = smtplib.SMTP('localhost')
# server.sendmail(fromaddr, toaddrs, msg)
# server.quit()

