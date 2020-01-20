import sys

log_path = "src/04_Reporting/report.txt"

def modbus_report_log(ans):
    stdoutOrigin=sys.stdout 
    sys.stdout = open(log_path, "a")
    ans.show()
    sys.stdout.close()
    sys.stdout=stdoutOrigin

# Log function to add the result of a test to the report
def report_log(text):
    with open(log_path,'a') as outfile:
        print >>outfile, text
    outfile.close()

def reset_log():
    with open(log_path,'w') as outfile:
        outfile.write("Begin of the automatic report from PDT\n\n")
    outfile.close()

def show_report():
    f = open(log_path, "r")
    print(f.read())


