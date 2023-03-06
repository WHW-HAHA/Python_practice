# Device was on for 7 seconds
# Timestamps of error events:
#    Jul 11 16:11:54:661
#    Jul 11 16:11:56:067

# function to accept a .log file as cmd imput
# and return a list of the timestamps of the error events
import datetime
import sys

def get_next_event(file_name):
    with open(file_name, "r") as datafile:
        for line in datafile:
            if "dut: Device State:" in line:
                line = line.rstrip()
                action = line.split()[-1]
                timestamp = line[:19]
                yield (action, timestamp)

def compute_time_diff_seconds(start, end):
    format = "%b %d %H:%M:%S:%f"
    start_time = datetime.datetime.strptime(start, format)
    end_time = datetime.datetime.strptime(end, format)
    return(end_time - start_time).total_seconds()

def extract_data(file_name):
    time_on_started = None
    errs = []
    total_time_on = 0

    for action, timestamp in get_next_event(file_name):
        if "ERR" == action:
            errs.append(timestamp)
        elif ("ON" == action) and (not time_on_started):
            time_on_started = timestamp
        elif ("OFF" == action) and time_on_started:
            time_on = compute_time_diff_seconds(time_on_started, timestamp)
            total_time_on += time_on
            time_on_started = None

if __name__ == "__main__":
    tottal_time_on, errs = extract_data(sys.argv[1])
    print(f"Device was on for {total_time_on} seconds")
    if errs:
        print("Timestamps of error events:")
        for err in errs:
            print(f"\t{err}")
