from win32api import GetMonitorInfo, MonitorFromPoint
import os
import ctypes
import tkinter
import platform
import sys

# force aware so can get accurate measurements of taskbar height
if platform.release() == '10':
	ctypes.windll.shcore.SetProcessDpiAwareness(2)
elif platform.release() == '7':
	ctypes.windll.user32.SetProcessDPIAware()
else:
	sys.exit(1)


monitor_info = GetMonitorInfo(MonitorFromPoint((0,0)))
work_area = monitor_info.get("Work")
# monitor_area = monitor_info.get("Monitor")

# taskbarheight = monitor_area[3]-work_area[3]

path = "."
cwCfg = os.path.join(path,"sofplus/data/cw_work_area.cfg")
if not os.path.exists(cwCfg):
	with open(cwCfg, "w+") as f:
		f.write("set ~cw_res_taskbar_y \"" + str(work_area[3]) + "\"")
else:
	print("file exists")

