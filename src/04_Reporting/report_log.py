import sys

log_path = "reports/report.txt"

def modbus_report_log(ans):
    stdoutOrigin=sys.stdout 
    sys.stdout = open(log_path, "a")
    ans.show()
    sys.stdout.close()
    sys.stdout=stdoutOrigin

def report_log(text):
    """Log function to add the result of a test to the report
    :params
		text - The text to add to the log
    :return
        No return"""
    with open(log_path,'a') as outfile:
        print >>outfile, text
    outfile.close()

def reset_log():
    """Function to reset the log file
    :return
        No return"""
    with open(log_path,'w') as outfile:
        outfile.write("Begin of the automatic report from PDT\n\n")
    outfile.close()

def show_report():
    """Function to print the report to the user
    :return
        No return, just print the report"""
    f = open(log_path, "r")
    print(f.read())


