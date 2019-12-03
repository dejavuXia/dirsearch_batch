# dirsearch_batch  
a python shell to  run dirsearch in batch model  / 批量运行dirsearch的脚本  
利用多进程提高dirsearch批量扫描的效率

可用参数   
-f --file  指定批量扫描文件信息存放的文件位置 暂时支持txt/csv/xlsx（xlsx需要openpyxl库）  （默认1.txt）  
-d --dir   指定dirsearch.py文件所在的位置 （默认当前文件夹）  
-p --pool  指定调用进程的个数（默认2个）    
-h --help  获取帮助提示

以txt为例，每行表示一条需要执行的dirsearch.py 指令（包含参数）  
对应的dirsearch参数依次是  
url（网站链接）, language（网站语言） , dict_path (字典的位置)， True（递归调用 True表示递归 ）, True(使用代理 True表示使用)  
其中 前2项为必选项，后三项可以根据需要进行添加。

demo  
在txt可写如下内容（txt默认,分割）（前2项为必选项，后三项可以根据需要进行添加）：  
http://www.baidu.com, php
执行的dirsearch 语句 即为 python dirsearch.py -u htttp://baidu.com -e php

http://www.baidu.com, php, c://1.txt, True, True  
执行的dirsearch 语句 即为 python dirsearch.py -u htttp://baidu.com -e php -w C://1.txt -r --random-agents


