/*
MySQL Backup
Source Server Version: 5.5.5
Source Database: wechat
Date: 2017/9/9 16:58:24
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
--  Table structure for `wechat_gourproles`
-- ----------------------------
DROP TABLE IF EXISTS `wechat_gourproles`;
CREATE TABLE `wechat_gourproles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rules` text,
  `text1` text,
  `image1` char(200) DEFAULT NULL,
  `text2` text,
  `image2` char(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `wechat_message`
-- ----------------------------
DROP TABLE IF EXISTS `wechat_message`;
CREATE TABLE `wechat_message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `stop` text,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records 
-- ----------------------------
INSERT INTO `wechat_gourproles` VALUES ('1','本群为游戏娱乐群，进群后请阅读以下内容：\r\n凡加入本群者，需了解本群为游戏娱乐群，致力于提高大众业余时间生活品质与价值，让您休闲时间既从游戏中得到欢乐也从可以得到收益。\r\n','点击连接：https://a.mlinks.cc/AKRF/?DO_NOT_TRACKING=1 根据提示下载app即可参与游戏','C:\\Users\\Administrator\\Desktop\\Python\\liuanmajiang\\image\\111.png','点击连接：http://www.sincebest.com/app/dhahqp/ 根据提示下载app即可参与游戏','C:\\Users\\Administrator\\Desktop\\Python\\liuanmajiang\\image\\222.png');
INSERT INTO `wechat_message` VALUES ('1','群主提醒：此红包为玩家游戏红包，请勿随意领取，谢谢配合！！！');
