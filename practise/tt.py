import time 
current_time = time.localtime()
minutes = current_time.tm_min
seconds = current_time.tm_sec
print((minutes / 60) * 360, seconds)