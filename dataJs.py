#coding:utf-8
'''
Created on 2010-11-5

@author: WangJian
'''

import os
def dojs(path='htfsweb'):
    #base文件 写入文件夹
    srcbase='D:\\Flex4_6Workspace\\%s\\WebRoot\\Compressed by JSA\\js\\view\\base\\'%path
    #base文件 读取文件夹
    src='D:\\Flex4_6Workspace\\%s\\WebRoot\\js\\data\\'%path

    JsList=os.listdir(src)
    Jsfile='dataJs.js'
    if Jsfile in os.listdir(srcbase):
        os.remove(srcbase+Jsfile)
    baseJsMerge=open(srcbase+Jsfile,'w')
    print JsList
    for file in JsList:
        if file.find('CVS')!=-1 or file.find('svn')!=-1 or file.find('.bak')!=-1:
            continue
        if not os.path.isdir(src+file) :
            for line in open(src+file):
    #            print line
                lineNoSpace=line.rstrip().lstrip()
                if lineNoSpace.find('//')!= 0:
                    baseJsMerge.write((line+'\n'))
            print '------------------------------------',file
        else:
            JsList.extend([file+'\\'+x for x in os.listdir(src+file)])
    baseJsMerge.close()

    ###############################

