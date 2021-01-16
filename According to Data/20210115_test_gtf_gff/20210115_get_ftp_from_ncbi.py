import os
from Bio import Entrez

# # =====一般参数设置=====
# # 设置 email 参数，为了方便 NCBI 的工作人员可以联系到你
# # 邮件的参数从2010年6月1日是强制的参数，所以每次必须告诉 NCBI 是谁在访问
# Entrez.email = "example@163.com"
# # 如果你是通过其他脚本调用，可以设定 tool 的名字，默认为 `Biopython`
# Entrez.tool = "exampleScript"
# # # 可选参数，使用代理，一般在无法正常访问时设置
# # os.environ["http_proxy"] = "http://proxyhost.example.com:8080"
#
#
# # =====查看数据库概况=====
# # 获取 Entrez 所有数据库的句柄
# hd_info = Entrez.einfo()
# # 获取所有数据库列表
# read_info = Entrez.read(hd_info)
# for db in read_info['DbList']:
# 	print(db)

import time
import ftputil

FtpHost = r'ftp.ncbi.nlm.nih.gov'  # FTP 主机
SubDir = r'/pubmed/baseline/'   # 最后的斜线有无不影响，根目录用单斜线即可
FtpUser = r'anonymous'
FtpPwd = r''
FtpEncoding = r'utf-8'

def Main():
    r"""
        遍历 ftp 目录，列出单个文件大小，统计目录个数、文件个数、文件总大小。
    """
    fileCnt = 0
    fileSize = 0
    dirCnt = 0
    with ftputil.FTPHost(host=FtpHost, user=FtpUser, passwd=FtpPwd) as host:
        for parent, dirnames, filenames in host.walk(SubDir):
            for filename in filenames:
                fileCnt += 1
                pathfile = host.path.join(parent, filename)
                singleFileSize = host.path.getsize(pathfile)
                fileSize += singleFileSize
                print('\tfile: %s, %d bytes' %
                      (pathfile.encode('latin-1').decode(FtpEncoding), singleFileSize))

            for dirname in dirnames:
                dirCnt += 1
                pathdir = host.path.join(parent, dirname)
                print('\tdir: %s' % pathdir.encode(
                    'latin-1').decode(FtpEncoding))

            print('fileCnt: %d, fileSize: %d B/%.2f KB/%.2f MB/%.2f GB, dirCnt: %d'
                  % (fileCnt, fileSize, fileSize/1024, fileSize/1024/1024, fileSize/1024/1024/1024, dirCnt))

    print('fileCnt: %d, fileSize: %d B/%.2f KB/%.2f MB/%.2f GB, dirCnt: %d'
          % (fileCnt, fileSize, fileSize/1024, fileSize/1024/1024, fileSize/1024/1024/1024, dirCnt))


if __name__ == '__main__':
    Main()
    print('current time: %s\n'
          % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))