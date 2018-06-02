#-*- encoding:UTF-8 -*-
import os
import sys
import string 
import psutil
import re

def get_pid(name):
　　process_list = psutil.get_process_list()
　　regex = "pid=(\d+),\sname=\'" + name + "\'"
　　print regex
　　pid = 0
　　for line in process_list:
    process_info = str(line)
    ini_regex = re.compile(regex)
    result = ini_regex.search(process_info)
    if result != None:
        pid = string.atoi(result.group(1))
        print result.group()
        break
def main(argv):name = argv[1]get_pid(name)

if __name__ == "__main__":
　　main(sys.argv)
