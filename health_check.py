#!/usr/bin/env python3

# 7. monitors system parameters, sends email if needed
# add resource to cron job for automatic setup

import psutil
import socket
import os
import emails


def cpu_usage():
    print('cpu_usage:', psutil.cpu_percent(interval=2))
    return psutil.cpu_percent(interval=2)


def disk_avail():
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info[3]
    print('disk_usage:', disk_usage)
    return 100 - disk_usage


def ram_free():
    ram = psutil.virtual_memory()
    MB = 1048576
    print('memory:', round(ram.free/MB))
    return ram.free/MB


def check_localhost():
    try:
        socket.gethostbyname('localhost')
        print('localhost:', socket.gethostbyname('localhost'))
        return True
    except socket.gaierror:
        return False


def main():
    if cpu_usage() > 80:
        subject = 'Error - CPU usage is over 80%'
    elif disk_avail() < 20:
        subject = 'Error - Available disk space is less than 20%'
    elif ram_free() < 500:
        subject = 'Error - Available memory is less than 500MB'
    elif not check_localhost():
        subject = 'Error - localhost cannot be resolved to 127.0.0.1'
    else:
        subject = ''

    print(subject)

    if bool(subject):
        sender = "automation@example.com"
        receiver = "{}@example.com".format(os.environ.get('USER'))
        body = """
            Please check your system and
            resolve the issue as soon as possible"""
        message = emails.generate_error_report(sender, receiver, subject, body)
        emails.send_email(message)


main()
