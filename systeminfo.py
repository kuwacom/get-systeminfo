import json
import threading
import time
import psutil
import cpuid
import re

def get(averageTime):
    systemInfo = {
        'cpuName': re.sub('\u0000','',str(cpuid.cpu_name())),
        'cpuCount': psutil.cpu_count(),
        'cpuFrequency': psutil.cpu_freq(percpu=True),
        'cpuPercentage': 'Null',
        'ramPercentage': psutil.virtual_memory().percent,
        'ramUsed': psutil.virtual_memory().used,
        'perDiskIOPS': 'Null',
        'perNetworkIOPS': 'Null',
        'diskIOPS': 'Null',
        'networkIOPS': 'Null',
    }

    def setCpuPercent(interval):
        systemInfo['cpuPercentage'] = psutil.cpu_percent(interval=interval,percpu=True)

    def setDiskIOPS(interval):
        oldNetData = psutil.disk_io_counters(perdisk=False)
        time.sleep(interval)
        result = []
        for num in range(len(oldNetData)):
            result.append(psutil.disk_io_counters(perdisk=False)[num]-oldNetData[num])
        systemInfo['diskIOPS'] = result

    def setNetworkIOPS(interval):
        oldNetData = psutil.net_io_counters(pernic=False)
        time.sleep(interval)
        result = []
        for num in range(len(oldNetData)):
            result.append(psutil.net_io_counters(pernic=False)[num]-oldNetData[num])
        systemInfo['networkIOPS'] = result

    def setPerDiskIOPS(interval):
        oldNetData = psutil.disk_io_counters(perdisk=True)
        time.sleep(interval)
        newNetData = psutil.disk_io_counters(perdisk=True)
        result = {}
        for diskName in oldNetData:
            disk = []
            for countNum in range(len(oldNetData[diskName])):
                disk.append(newNetData[diskName][countNum] - oldNetData[diskName][countNum])
            result[diskName] = disk
        systemInfo['perDiskIOPS'] = result

    def setPerNetworkIOPS(interval):
        oldNetData = psutil.net_io_counters(pernic=True)
        time.sleep(interval)
        newNetData = psutil.net_io_counters(pernic=True)
        result = {}
        for diskName in oldNetData:
            disk = []
            for countNum in range(len(oldNetData[diskName])):
                disk.append(newNetData[diskName][countNum] - oldNetData[diskName][countNum])
            result[diskName] = disk
        systemInfo['perNetworkIOPS'] = result

    thread_1 = threading.Thread(target=setCpuPercent,args=(averageTime-0.05,))
    thread_2 = threading.Thread(target=setDiskIOPS,args=(averageTime-0.05,))
    thread_3 = threading.Thread(target=setNetworkIOPS,args=(averageTime-0.05,))
    thread_4 = threading.Thread(target=setPerDiskIOPS,args=(averageTime-0.05,))
    thread_5 = threading.Thread(target=setPerNetworkIOPS,args=(averageTime-0.05,))

    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_4.start()
    thread_5.start()

    time.sleep(averageTime)
    return systemInfo
    
print(json.dumps(get(0.5)))