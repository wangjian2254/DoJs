#coding:utf-8
'''
Created on 2010-11-5

@author: WangJian
'''
import os
def dojs(path='htfsweb'):
    #mgr文件 写入文件夹
    mgrSrcmgr='D:\\Flex4_6Workspace\\%s\\WebRoot\\Compressed by JSA\\js\\view\\'%path
    #mgr文件 读取文件夹
    mgrSrc='D:\\Flex4_6Workspace\\%s\\WebRoot\\js\\view\\'%path


    noMergeJs=['_005_loginMgr.js','CVS']
    mgrJsList=os.listdir(mgrSrc)
    mgrJsfile='mgrMerge.js'
    if mgrJsfile in os.listdir(mgrSrcmgr+'base\\'):
        os.remove(mgrSrcmgr+'base\\'+mgrJsfile)
    mgrjsmerge=open(mgrSrcmgr+'base\\'+mgrJsfile,'w')
    print mgrJsList
    for file in mgrJsList:
        if (file not in noMergeJs) and file.find('_')==0  and file.find('.bak')==-1:
            ismgr=1
            mgrjs=open(mgrSrcmgr+file,'w')
            mgrjsmerge.write(('//'+file+'\n'))
            for line in open(mgrSrc+file):
                lineNoSpace=line.rstrip().lstrip()
                if lineNoSpace.find('Ext.onReady')==0 or ismgr==0:
                    ismgr=0
                    mgrjs.write((line+'\n'))
                elif len(lineNoSpace)!=0 and lineNoSpace.find('//')!=0 and lineNoSpace.find('Ext.BLANK_IMAGE_URL')!=0 and lineNoSpace.find('Ext.QuickTips.init()')!=0 :
                    mgrjsmerge.write(lineNoSpace+'\n')
            mgrjs.close()
            ismgr=1
            print '----------------------------------------',file
    mgrjsmerge.close()