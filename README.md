# cardGame_server

这是一个简单的网络斗地主游戏，并且拥有文字聊天和语音聊天功能。

这里是服务器端，主要处理逻辑有：

## 1.用户管理。

	即基本的注册、登录、登出等。
  
## 2.房间管理。

	进入后即可进入游戏大厅，在大厅中可进行游戏房间的创建、搜索
	创建房间的玩家成为房主，可对房间的名字、简介、密码等进行设置。如果房主退出房间，则自动转交给下一位
	其他玩家可进行准备，所有玩家准备完毕后房主可开始游戏
  
## 3.游戏管理。

	游戏初始化，抢地主逻辑，回合制逻辑，出牌逻辑，胜利或失败判断逻辑
	（因为个人开发原因，牌型比较没有放到服务器端，但这是错误的）
	文字聊天功能

引擎为[kbengine](https://github.com/kbengine/kbengine)

客户端在[cardGame_client](https://github.com/findsky6544/cardGame_client)

## 启动方式
	1.安装kbengine-1.16
	2.将该文件夹放入kbengine的根目录
	3.启动start_server
