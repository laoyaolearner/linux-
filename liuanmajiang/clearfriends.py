import itchat
from itchat.content import *

itchat.send('此信息用于验证好友关系，请勿回复，谢谢', )
@itchat.msg_register(NOTE, isFriendChat=True)
def information(msg):
	nick = msg.User['NickName']
	if '发送朋友验证' in msg['Content']:
		itchat.send('%s不是您的好友' % nick, toUserName='filehelper')

itchat.run()