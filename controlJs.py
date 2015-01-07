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
    src='D:\\Flex4_6Workspace\\%s\\WebRoot\\js\\view\\'%path

    JsList=['base.js','base\\comb.js','base\\form.js','base\\grid.js','base\\panel.js','base\\tree.js','base\\win.js','base\\util.js']
    Jsfile='controlJs.js'
    if Jsfile in os.listdir(srcbase):
        os.remove(srcbase+Jsfile)
    baseJsMerge=open(srcbase+Jsfile,'w')
    print JsList
    for file in JsList:
        if 0==0 :
            for line in open(src+file):
    #            print line
                lineNoSpace=line.rstrip().lstrip()
                if lineNoSpace.find('//')!= 0:
                    baseJsMerge.write((line+'\n'))
            print '------------------------------------',file
    baseJsMerge.close()

    ###############################

