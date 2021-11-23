#!/usr/bin/env python
# _*_ coding:UTF-8 _*_
import os
import platform


# 重要参数配置
db_name = "ylt"
db_user_name = "root"
db_user_password = "rootroot"


if platform.system() == 'Windows':
    os.system('chcp 65001')

work_space = os.getcwd()+os.sep+"history"
if not os.path.exists(work_space):
    os.makedirs(work_space)

print("### 欢迎使用数据库备份恢复系统1.0 ###\n"
      "------当前数据库：%s\n"
      "------当前的用户：%s\n"
      "------当前的密码：%s\n"
      "------工作的空间：%s\n"
      %(db_name,db_user_name,db_user_password,work_space))

command = input("请输入要执行的操作：\n"
      "1:备份 2:恢复 其他:退出（exit)\n"
                "请输入：")
def backup():
    backfilename = input("输入备份文件名字：")
    targetFilePath = "%s%sbackup_%s.sql"%(work_space,os.sep,backfilename);
    cmd = "mysqldump -u%s -h127.0.0.1 -p%s %s --single-transaction > %s"%(db_user_name,db_user_password,db_name,targetFilePath)
    print(cmd)
    result = os.popen(cmd).read()
    print(result)
    if os.path.getsize(targetFilePath) == 0:
        print("【 x 备份失败 x 】")
    else:
        print("【 √ 备份完成 √ 】")


def revert():
    print("备份文件名字只需输入backup_之后的名字即可，且无需包含后缀.sql")
    backfilename = input("输入备份文件名字：")
    targetFilePath = "%s%sbackup_%s.sql"%(work_space,os.sep,backfilename);
    cmd = "mysql -u%s -h127.0.0.1 -p%s %s < %s"%(db_user_name,db_user_password,db_name,targetFilePath)
    print(cmd)
    result = os.popen(cmd).read()
    print(result)

if command == "1":
    print("【启动备份】...")
    print("【备份中】，请等待程序执行完毕...")
    backup()
elif command == "2":
    print("开始恢复...")
    print("恢复中，请等待程序执行完毕...")
    revert()
    print(" √ 恢复执行完毕 √ ")
else:
    print("未知命令，程序退出")


