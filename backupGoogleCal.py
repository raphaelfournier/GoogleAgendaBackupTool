#!/usr/bin/env python
# wget Google calendar for backup
# rfs 2015-08-26
import time
import sys
from subprocess import call,Popen,PIPE
import os.path
import configparser
import datetime

# ini config file
folder = os.path.dirname(os.path.realpath(__file__))
Config = configparser.ConfigParser(interpolation=None)
Config.read(folder+"/settings.ini")

# date, to timestamp the backups
date = str(datetime.date.today())
year = str(datetime.date.today().year)

# get general settings
backupdir = Config['general']['BackupDir']
if not os.path.isdir(backupdir):
    sys.exit("Folder for backup does not exist.\nmkdir "+backupdir)
backupdir += year + "/"
if not os.path.isdir(backupdir):
    os.makedirs(backupdir)
if "PidFileName" not in Config['general']:
    pidfile = backup_gcal.pid
pidfile = backupdir + Config['general']['PidFileName']

# get all calendars names and urls from ini file into a dic
calendars = Config['urls']
calurls = {}
for calname in calendars:
    calurls[calname] = calendars[calname]

# test if pid exists
if os.path.isfile(pidfile):
    print(pidfile + " already exists")
    sys.exit(1)

def getCalendarToFile(name,url):
    print("... processing %s"%name)
    call(["touch", pidfile])
    filename = "%s-%s.ics"%(name,date)
    location = backupdir + filename
    args = ['wget', '-c', '--no-check-certificate', '-o', '/dev/null',
            '-O',location, url]
    output = Popen(args, stdout=PIPE)
    call(["rm", pidfile])
    return True

# get all the calendars to files in Backupdir
for name, url in calurls.items():
    getCalendarToFile(name, url)

print("done!")
sys.exit(0)
