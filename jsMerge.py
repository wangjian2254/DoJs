#coding:utf-8
'''
Created on 2010-8-23

@author: WangJian
'''
import os
def dojs(path='htfsweb'):
    #base文件 写入文件夹
    srcbase='D:\\Flex4_6Workspace\\%s\\WebRoot\\Compressed by JSA\\js\\view\\base\\'%path
    #base文件 读取文件夹
    src='D:\\Flex4_6Workspace\\%s\\WebRoot\\js\\view\\base\\'%path

    noMergeJs=['page1Base.js','CVS']
    JsList=os.listdir(src)
    Jsfile='baseJs.js'
    if Jsfile in os.listdir(srcbase):
        os.remove(srcbase+Jsfile)
    baseJsMerge=open(srcbase+Jsfile,'w')
    print JsList
    for file in JsList:
        if (file not in noMergeJs) and file.find('_')==0 and file.find('.bak')==-1:
            for line in open(src+file):
    #            print line
                lineNoSpace=line.rstrip().lstrip()
                if lineNoSpace.find('//')!= 0:
                    baseJsMerge.write(lineNoSpace+'\n')
            print '------------------------------------',file
    baseJsMerge.close()

    ###############################

