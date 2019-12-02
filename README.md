# dirsearch_batch
a python shell to  run dirsearch in batch model  / 批量运行dirsearch的脚本
利用多进程提高dirsearch批量扫描的效率

可用参数 
-f --file  指定批量扫描文件信息存放的文件位置 暂时支持txt/csv/xlsx（xlsx需要openpyxl库）  （默认1.txt）
-d --dir   指定dirsearch.py文件所在的位置 （默认当前文件夹）
-p --pool  指定调用进程的个数（默认2个）
