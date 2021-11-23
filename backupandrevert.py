import os

db_name = "ylt"
db_user_name = "root"
db_user_password = "rootroot"
work_space = os.getcwd()+"/history"

print("### 欢迎使用数据库备份恢复系统 ###\n"
      "------当前数据库：%s\n"
      "------当前的用户：%s\n"
      "------当前的密码：%s\n"
      "------工作的空间：%s\n"
      %(db_name,db_user_name,db_user_password,work_space))

def work_space_file_list():
    print("### 当前工作空间下的备份文件### ")
    print(os.popen("ls -alh %s"%(work_space)).read())

work_space_file_list()
command = input("请输入要执行的操作：\n"
      "1:备份 2:恢复 其他:退出（exit)\n"
                "请输入：")
def backup():
    backfilename = input("输入备份文件名字：")
    cmd = "mysqldump -u%s -h127.0.0.1 -p%s %s --single-transaction > %s/backup_%s.sql"%(db_user_name,db_user_password,db_name,work_space,backfilename)
    print(cmd)
    result = os.popen(cmd).read()
    print(result)

def revert():
    print("备份文件名字只需输入backup_之后的名字即可，且无需包含后缀.sql")
    backfilename = input("输入备份文件名字：")
    cmd = "mysql -u%s -h127.0.0.1 -p%s %s < %s/backup_%s.sql"%(db_user_name,db_user_password,db_name,work_space,backfilename)
    print(cmd)
    result = os.popen(cmd).read()
    print(result)
if command == "1":
    # print("备份")
    backup()
    work_space_file_list()
elif command == "2":
    # print("恢复")
    revert()
else:
    print("未知命令，程序退出")


