# coding: utf-8
import itchat, time
import MySQLdb
from itchat.content import *

itchat.auto_login(hotReload=True, enableCmdQR=2)

# 获取当前登陆账号信息
userdetail = itchat.search_friends()
username = userdetail.userName

#数据库连接部分
conn = MySQLdb.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = 'root',
    db = 'wechat',
    )
cur = conn.cursor()
conn.set_character_set('utf8')

# 判断用户是否为存在用户
def addUsers():
	result = "select * from wechat_users where username='%s'" % username
	sqlselect = cur.execute(result)
	if sqlselect == 1:
		print('已存在')
		clearFriends()
	else:
		cur.execute("insert into wechat_users(username) values('%s')" % username)
		print('已导入')

# 定义清理好友列表函数
def clearFriends():
	friends = itchat.get_friends()[1:]
	for i in friends:
		itchat.send('此信息用于验证好友关系，请勿回复，谢谢', i['UserName'])
	

#ceshi = itchat.search_friends(name='黄磊')[0]['UserName']
#itchat.send('111', ceshi)
@itchat.msg_register(NOTE, isFriendChat=True)
def information(msg):
	nick = msg.User['NickName']
	if '发送朋友验证' in msg['Content']:
		itchat.send('此好友：%s，已将您删除或者拉黑' % nick, toUserName='filehelper')


#addUsers()
#clearFriends()
itchat.run()
