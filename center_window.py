from win32api import GetMonitorInfo, MonitorFromPoint
import os
monitor_info = GetMonitorInfo(MonitorFromPoint((0,0)))
work_area = monitor_info.get("Work")

path = "."
cwCfg = os.path.join(path,"sofplus/data/cw_work_area.cfg")
if not os.path.exists(cwCfg):
	with open(cwCfg, "w+") as f:
		f.write("set cw_res_desktop_y \"" + str(work_area[3]) + "\"")
else:
	print("file exists")
