#!/usr/bin/env python
from ast import main
import psutil

# cpu usage
cpu_usage = psutil.cpu_percent()
cpu_usage = float(cpu_usage)

# ram usage
v_memory = psutil.virtual_memory()
ram_total_space = int(v_memory[0])
ram_used_space = int(v_memory[1])
ram_free_space = int(v_memory[2])
ram_percent_space = float(v_memory[3])

# cpu freq
cpu_freq = psutil.cpu_freq()
cpu_cur_freq = float(cpu_freq[0])
cpu_min_freq = float(cpu_freq[1])
cpu_max_freq = float(cpu_freq[2])

# disk
main_disk_path = str(psutil.disk_partitions()[0]).split()[0]
main_disk_path = main_disk_path[18:]
main_disk_path = main_disk_path[:-2]
disk_usage = psutil.disk_usage(main_disk_path)
disk_total_space = int(disk_usage[0])
disk_used_space = int(disk_usage[1])
disk_free_space = int(disk_usage[2])
disk_percent_space = float(disk_usage[3])