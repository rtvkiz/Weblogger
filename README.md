# Weblogger

Weblogger helps you find a specific IP from huge load of Apache HTTP logs. It is helpful in analysing traffic during any intrusion or attacks. Weblogger also supports mapping CIDR range to the logs. Thus helping analysts to flag IP values.

# Usage:
python weblogger_helper.py --ip <IP> 
  
Optional Parameters: --path: Specify the path to the log file, else 'public_access.log.txt' is assumed to be the default file in the same directory.

( The application can run on python2 as well as python3. But python3 is preferred) 
