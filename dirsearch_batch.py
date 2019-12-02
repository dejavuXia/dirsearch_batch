#读取文件批量调用dirsearch进行批量扫描
#运行环境 python3

import os
import time
import multiprocessing 
import argparse

pool_num = 2                     #进程池，默认数目为2 ，可根据cpu核心数更改
dirsearch_path = "dirsearch.py"  #dirsearch脚本的存放路径，默认为当前目录下
file_path = "1.txt"              #批量信息存储的路径
dict_path = ""                   #字典的存储路径
agents_option = False            #是否使用代理
parser = argparse.ArgumentParser(description = "这是一个用来批量执行dirsearch的脚本")
    
#初始化参数
def init():
    help =" the f params is set the path of file which store url info and  params"
    parser.add_argument('-f','--file', type=str, help=help)
    help =" the p params is set the num of processing pool"
    parser.add_argument('-p','--pool', type=int, help=help)
    help =" the d params is set the path of dirsearch.py"
    parser.add_argument('-d','--dir', type=str, help=help)

#设置默认参数的值
def set(args):
    if args.file != None:
        global file_path 
        file_path = args.file
    if args.pool != None: 
        global pool_num 
        pool_num = args.pool 
    if args.dir != None: 
        global dirsearch_path 
        dirsearch_path = args.dir 

#文件读取功能,读取url列表及相关参数信息
def read_file(dir):
    file_type = os.path.splitext(dir)[1][1:]
    url_list = []    
    
    if(file_type == "txt"):  #txt默认以,隔开
        file = open(dir)
        for line in file:
            info = line.split(',')
            for i in range(0, len(info)):
                info[i] = info[i].strip()
            url_list.append( info )

    elif(file_type == "xlsx"):  
        import openpyxl
        workbook = openpyxl.load_workbook(dir)
        rows = workbook.active.iter_rows()     
        for row in rows: 
            info = []
            for r in row:
                info.append(r.value)
            url_list.append(info)
        workbook.close()

    elif(file_type == "csv"):
        file = open(dir)
        for line in file:
            url_list.append( line.split(',') )
    
    return url_list

#调用dirsearch执行   所有参数都需要兼容
def run_dirsearch(dirsearch_params, dirsearch_path ):
    payload = "python %s -u %s -e %s" % (dirsearch_path, dirsearch_params[0], dirsearch_params[1])   # -u -e 参数为必选项
    if len(dirsearch_params) > 2 and dirsearch_params[2]!= None and  dirsearch_params[2]!= "" :    #执行指定字典
        payload += " -w %s" % dirsearch_params[2]
    if len(dirsearch_params) > 3 and dirsearch_params[3]!= None and  dirsearch_params[2]== "True" :  #执行递归调用
        payload += " -r "
    if len(dirsearch_params) > 4 and dirsearch_params[4]!= None and  dirsearch_params[2]== "True" :  #使用代理
        payload += " --random-agents "
    os.system(payload)


#调用进程池
def processing_deal(url_list):
    p = multiprocessing.Pool(pool_num)
    for url in url_list:
        p.apply_async(run_dirsearch, args = (url, dirsearch_path, ))
    p.close()
    p.join()
    print("all tasks had been finished !")
        
if __name__ == '__main__':
    init()
    args = parser.parse_args()
    set(args)
    processing_deal(read_file(file_path))

