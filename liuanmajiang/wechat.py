import itchat, time
import MySQLdb

from itchat.content import *


# 登陆微信
itchat.auto_login(hotReload=True, enableCmdQR=2)
groupName = input("请输入您需要群发的对象名称:")
userName = itchat.search_chatrooms(name=groupName)[0]['UserName']

# 定义数据库连接
conn = MySQLdb.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = 'root',
    db = 'wechat',
    )
cur = conn.cursor()
conn.set_character_set('utf8')


class Grouprules():
	def sendGroupRules():
		rules = cur.execute("select * from wechat_gourproles")
		info = cur.fetchmany(rules)
		if groupName=='娱乐群':
			for i in info:
				itchat.send(i[1], userName)
				time.sleep(2)
				itchat.send(i[4], userName)
				time.sleep(2)
				itchat.send('@img@%s' % i[5], userName)
		else:
			for i in info:
				itchat.send(i[1], userName)
				time.sleep(2)
				itchat.send(i[2], userName)
				time.sleep(2)
				itchat.send('@img@%s' % i[3], userName)


class JoinMessage():
	@itchat.msg_register(NOTE, isGroupChat=True)
	def information(msg):
		if '加入了群聊' in msg['Content']:
			Grouprules.sendGroupRules()


@itchat.msg_register([NOTE, SHARING],  isGroupChat=True)
def text_reply(msg):
	print(msg)
	if msg['Type'] == 'Note' and msg['ActualNickName'] !='小香':
		rules = cur.execute("select * from wechat_message")
		info = cur.fetchmany(rules)
		#itchat.send('群主提醒：此红包是玩家游戏红包，请勿随意领取，谢谢配合！', userName)
		for i in info:
			itchat.send(i[1], userName)

			
#Grouprules.sendGroupRules()
#JoinMessage()
#itchat.run()