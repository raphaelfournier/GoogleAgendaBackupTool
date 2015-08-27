# Google Calendar Backup

It is a tool to backup some Google Calendars on a Linux machine using cron.
Written in Python 3.

## Installation

* Download
  
        git clone https://github.com/raphaelfournier/GoogleAgendaBackupTool.git

* Install dependency

        sudo pip install configparser
        sudo apt-get install wget

* Edit settings.ini file

        cd GoogleAgendaBackupTool
        vim settings.ini

## Settings

There are two sections in the *settings.ini* file, called `general` and `urls`.

The `general` section contains two variables, `BackupDir` (defaults to /home/user in the included version) and `PidFileName`, which defaults to `backup_gcal.pid`.

The `urls` section contains the urls to retrieve your calendars from Google
Agenda, with their private addresses. The format is the following:

      CalendarName: https://www.google.com/calendar/ical/theRestOfYourUrl

### To get the addresses of your calendar

* Go to https://www.google.com/calendar/
* Click on the down arrow next to the name of a calendar, in the menu on the
  left. Select `calendar settings` in the dropdown menu.
* At the bottom, you should have a `Private address` section, with an ICAL
  button. Right-click on it, select `Copy link address`, paste it in the
  settings.ini, using the formatting above.

If there is no `Private address` section, you may be using a Google Apps account
and then you need to check your organisation's settings.

Note: you can use any http address you like, provided it works with the wget
command.

## Usage

* Test run :

        python GoogleAgendaBackupTool/backupGoogleCal.py

* Cron

        crontab -e
        # every Thursday at 4pm, the command is launched, files saved in the BackupDir folder and you receive a mail notification
        00 16 * * 4 python /home/user/GoogleAgendaBackupTool/backupGoogleCal.py | mail yourmail@exemple.com
    <save>
