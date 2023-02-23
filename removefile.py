import os
from log_color import log ,LogLevel
import argparse

def remove_file(dirpath:str=None,keyword:str=None):
    counter = 0
    if isinstance(dirpath,str):
        if isinstance(keyword,str):
            if os.path.exists(dirpath):
                for filename in  os.listdir(dirpath):
                    if keyword in filename:
                        file_path = os.path.join(dirpath,filename)
                        display_info = f"\n【文件名】{filename}\n【文件路径】{file_path}\n【的文件已经删除】"
                        os.remove(file_path)
                        log(display_info,LogLevel.PASS)
                        counter += 1
            else:
                log(f"文件夹路径{dirpath}不存在！！！",LogLevel.ERROR)
        else:
            log(f"keyword 参数必须是str ！！！",LogLevel.ERROR)
    else:
        log(f"dirpath 参数必须是str ！！！",LogLevel.ERROR)
    if counter > 0:
        log(f"累计共删除<{counter}>个文件",LogLevel.PASS)
    else:
        log(f"没有找到要含有关键字的文件名！！！",LogLevel.WARN)
        
def cmd_rmove():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dirpath", required=True, help="dirpath 是文件夹路径",type=str)
    parser.add_argument("--keyword", required=True, help="文件名关键字", type = str)
    opt = parser.parse_args()
    remove_file(opt.dirpath,opt.keyword)
    
# cmd_rmove()
    
if __name__ =='__main__':   
    print(remove_file("/home/zhangmanman/Videos/Bilibili/娱乐/",keyword=".xml"))