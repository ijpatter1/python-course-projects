"""
The Portland-based company you work for just opened two new branches.
One is in New York City, the other in London.
They need a very simple program to find out if the branches are open or closed.
The hours of both branches are 9:00 a.m.-5:00 p.m. in their own time zone.

Create a script that will find out the current times in the Portland HQ and NYC and London branches.
Then, compare that time with each branch's hours to see if they are open or closed.
Print out to the screen the three branches and whether they are open or closed.
"""

import datetime
from datetime import datetime, timedelta, tzinfo

def main():
    portland_branch = ('Portland', -7)
    nyc_branch = ('New York City', -4)
    london_branch = ('London', 1)

    getTimes(*portland_branch)
    getTimes(*nyc_branch)
    getTimes(*london_branch)

def getTimes(branch,branch_tz):
    now = datetime.utcnow().time()
    branch_hour = now.hour + branch_tz
    if branch_hour < 0:
        branch_hour += 24
    branch_now = now.replace(hour=branch_hour)
    opening = branch_now.replace(hour=9, minute=0, second=0, microsecond=0)
    closing = branch_now.replace(hour=17, minute=0, second=0, microsecond=0)
    if branch_now >= opening and branch_now < closing:
        print(f'The {branch} branch is OPEN!')
    else:
        print(f'The {branch} branch is CLOSED!')

if __name__ == "__main__":
    main()