import os
import logging
import ctypes
from win32evtlog import OpenEventLog, ReadEventLog, EVENTLOG_FORWARDS_READ
from win32evtlogutil import SafeFmtMessage
from win32con import EVENT_TRACE_REAL_TIME_MODE, TRACE_EVENT_HEADER


TRUSTED_DIRECTORIES = [
    r"C:\Windows\System32",
    r"C:\Windows\SysWOW64"
]

KNOWN_VULNERABLE_MODULES = [
    "vuln_driver.sys",
    "badmodule.dll"
]


logging.basicConfig(filename='byol_detector.log', level=logging.INFO)


def log_event(message):
    logging.info(message)


def is_module_suspicious(module_path):
    for trusted_dir in TRUSTED_DIRECTORIES:
        if trusted_dir in module_path:
            return False
    return True

def parse_event(event):
    try:
     
        module_path = event.get('ImageName', '')
        process_id = event.get('ProcessID', 0)

        if module_path:
            print(f"Process ID: {process_id} | Module: {module_path}")

           
            for vulnerable_module in KNOWN_VULNERABLE_MODULES:
                if vulnerable_module.lower() in module_path.lower():
                    print(f"ALERT: Known vulnerable module detected: {module_path}")
                    log_event(f"ALERT: Known vulnerable module detected: {module_path}")

            
            if is_module_suspicious(module_path):
                print(f"WARNING: Suspicious module path detected: {module_path}")
                log_event(f"WARNING: Suspicious module path detected: {module_path}")

    except Exception as e:
        print(f"Error parsing event: {e}")


def start_etw_session():
    print("Starting ETW session...")
  
    try:
        event_log = OpenEventLog(None, "System")
        while True:
            events = ReadEventLog(event_log, EVENTLOG_FORWARDS_READ, 0)
            for event in events:
                
                if event.EventID == 10:  
                    event_data = {
                        'ImageName': event.StringInserts[0] if len(event.StringInserts) > 0 else '',
                        'ProcessID': event.EventHeader.ProcessID
                    }
                    parse_event(event_data)
    except Exception as e:
        print(f"Failed to start ETW session: {e}")

if __name__ == "__main__":
    print("BYOL Detection Tool with ETW - Python")
    print("Monitoring module load events...")
    
    start_etw_session()
    
    print("ETW session ended.")
