# apTrendLogger
Provides two programs that work as a joint system: one "set and forget" daily logger, one log data trender and summarizer. Originally built specifically for a specific network using Cisco Prime, not sure how well it might translate to anywhere else.

==========================
Requirements:
==========================
'pip install python-dateutil --trusted-host pypi.python.org'
-AP log folder and contents

==========================
Use:
==========================
> Set up APLogger.py to run daily
> When you want to check the log:
    > Navigate to the folder containing APDelta.py
    > Run APDelta.py with the syntax
         python APTrend.py -h
      to see the help for the program.
    > Example usage:
         python APTrend.py -s 2016-01-04 -e 2017-01-04 -t month
> Note: Please keep dates in the format YYYY-MM-DD, and keep track of the beginning of your epoch of use
> Note: When first initializing to use, delete the three ApHistory files in the log folder. Right now, they're just full of example shit to prove usability of APTrend.
