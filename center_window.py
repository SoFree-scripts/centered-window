from win32api import GetMonitorInfo, MonitorFromPoint
import os
import ctypes
import tkinter

monitor_info = GetMonitorInfo(MonitorFromPoint((0,0)))
work_area = monitor_info.get("Work")
monitor_area = monitor_info.get("Monitor")



taskbarheight = monitor_area[3]-work_area[3]

path = "."
cwCfg = os.path.join(path,"sofplus/data/cw_work_area.cfg")
if not os.path.exists(cwCfg):
	with open(cwCfg, "w+") as f:
		f.write("set ~cw_res_taskbar_y \"" + str(taskbarheight) + "\"")
else:
	print("file exists")

