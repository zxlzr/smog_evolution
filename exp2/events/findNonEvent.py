import sys
import codecs
import time

ISOTIMEFORMAT='%Y-%m-%dT%XZ'
STEP = 6

def readFile(file_name):
    f=codecs.open(file_name,'r','utf-8')
    lines = f.readlines()
    f.close()
    return lines

def readTime(file_name):
    lines = readFile(file_name)
    hours = []
    for line in lines:
        hours.append(line.strip() + 'Z')
    return hours

def saveFile(file_name,lines):
    f=codecs.open(file_name,'w','utf-8')
    f.writelines(lines)
    f.close()

def inEvent(t, in_times, de_times):
    times = in_times + de_times
    for item in times:
        unix_current = time.mktime(time.strptime(item,ISOTIMEFORMAT))
#        for i in range(0,STEP):
#            unix_tmp = unix_current-i*3600
#            tmp_time = time.strftime(ISOTIMEFORMAT,time.localtime(unix_tmp))
        if unix_current == t:
            return True
    return False


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'usage: python findEvent.py low/high station'
        sys.exit(0)
    eventType = sys.argv[1]
    station = sys.argv[2]
    records = readFile(station + '_records.txt')
    in_times = readTime(station + '_increase.txt')
    de_times = readTime(station + '_decrease.txt')
    results = []
    for i,record in enumerate(records):
        print 'i:' + str(i)
        tmp = record.strip().split(' ')
        t = tmp[0][0:19]
        aqi = int(tmp[1])
        if eventType == 'low':
            if aqi<150 and inEvent(t,in_times,de_times)==False:
                results.append(t + '\r\n')
                saveFile(station + '_low.txt',results)
        if eventType == 'high':
            if aqi>150 and inEvent(t,in_times,de_times)==False:
                results.append(t + '\r\n')
                saveFile(station + '_high.txt',results)

