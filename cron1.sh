#!/bin/bash

var=$(cat /proc/uptime | cut -d " " -f1)
users=$(/usr/bin/who | grep -c "")

if [ "$var" > "720" ]; then
    echo "Server `hostname` has been up for more than 2 hours!"
    echo "Number of users logged on: $users"
fi
        if [ "$users" -ge "1" ]; then
            echo "There are users logged on."

        else
            echo "There are no users logged on."
fi

##Crontab entry to run script every 30 minutes:

1 * * * * /home/ec2-user/server_alert3.sh | mail -s "Server Alert" grant.grismore@seattlecolleges.edu

# ┌───────────── min (0 - 59)
# │ ┌────────────── hour (0 - 23)
# │ │ ┌─────────────── day of month (1 - 31)
# │ │ │ ┌──────────────── month (1 - 12)
# │ │ │ │ ┌───────────────── day of week (0 - 6) (0 to 6 are Sunday to
# │ │ │ │ │                  Saturday, or use names; 7 is also Sunday)
# │ │ │ │ │
# │ │ │ │ │
# * * * * *  command to execute
