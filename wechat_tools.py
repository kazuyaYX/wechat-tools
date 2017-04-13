import itchat, time, re, os, threading
from itchat.content import *
from apscheduler.schedulers.blocking import BlockingScheduler


class WechatTools():

    schedulee = BlockingScheduler()
    withdraw_friend_setting = []
    withdraw_group_setting = []
    msg_dict = {}

    def set_withdraw_setting(self, friend_setting, group_setting):
        self.withdraw_friend_setting = friend_setting
        self.withdraw_group_setting = group_setting
        print(self.withdraw_friend_setting)
        print(self.withdraw_group_setting)

    # 监听系统的撤回消息提示
    def prevent_withdrawl(self):
        @itchat.msg_register(NOTE, isFriendChat=True)
        def prevent_withdrawl(msg):
            # 建立存放撤回文件的目录
            if not os.path.exists(".\\withdrawl\\"):
                os.mkdir(".\\withdrawl\\")
            # 若不是撤回的消息就直接返回
            if re.search('撤回', msg['Content']) is None:
                return
            # 用正则表达式匹配出撤回的消息id
            msg_id = re.search('<msgid>(.*?)</msgid', msg['Content']).group(1)
            # 如果撤回的消息在字典里不存在就直接返回
            if self.msg_dict.get(msg_id) == None:
                return
            withdrawl_msg = self.msg_dict[msg_id]
            # 若没有用户不希望接收的撤回消息则不管
            if withdrawl_msg['type'] not in self.withdraw_friend_setting:
                return
            send_msg = withdrawl_msg['from'] + '撤回了一条信息，信息类型是' + withdrawl_msg['type']
            if withdrawl_msg['type'] == 'Picture' or withdrawl_msg['type'] == 'Recording' or withdrawl_msg[
                'type'] == 'Video' \
                    or withdrawl_msg['type'] == 'Attachment':
                # 执行下载方法
                withdrawl_msg['content']('.\\withdrawl\\' + withdrawl_msg['filename'])
                send_msg += '。文件名称为' + withdrawl_msg['filename']
                if withdrawl_msg['type'] != 'Recording':
                    send_msg += '。内容如下：'
                itchat.send(send_msg)
                if withdrawl_msg['type'] == 'Picture':
                    itchat.send_image('.\\withdrawl\\' + withdrawl_msg['filename'])
                if withdrawl_msg['type'] == 'Video':
                    itchat.send_video('.\\withdrawl\\' + withdrawl_msg['filename'])
                if withdrawl_msg['type'] == 'Attachment':
                    itchat.send_file('.\\withdrawl\\' + withdrawl_msg['filename'])
            else:
                send_msg += '。消息为：' + withdrawl_msg['content']
                if withdrawl_msg['type'] == 'Sharing':
                    send_msg += '。链接为：' + withdrawl_msg['url']
                itchat.send(send_msg)
            # 在字典里去掉已经撤回的消息
            del self.msg_dict[msg_id]
            # 提醒有好友撤回消息
            # itchat.send(send_msg)

    def prevent_group_withdrawl(self):
        @itchat.msg_register(NOTE, isGroupChat=True)
        def prevent_withdrawl(msg):
            print(msg)
            # 建立存放撤回文件的目录
            if not os.path.exists(".\\withdrawl\\"):
                os.mkdir(".\\withdrawl\\")
            # 若不是撤回的消息就直接返回
            if re.search('撤回', msg['Content']) == None:
                return
            # 用正则表达式匹配出撤回的消息id
            msg_id = re.search('&lt;msgid&gt;(.*?)&lt;/msgid', msg['Content']).group(1)
            # 如果撤回的消息在字典里不存在就直接返回
            if self.msg_dict.get(msg_id) == None:
                return
            withdrawl_msg = self.msg_dict[msg_id]
            # 若没有用户不希望接收的撤回消息则不管
            if withdrawl_msg['type'] not in self.withdraw_group_setting:
                return
            # 匹配用户名
            msg_from = msg['ActualNickName']
            send_msg = msg_from + '撤回了一条信息，信息类型是' + withdrawl_msg['type']
            if withdrawl_msg['type'] == 'Picture' or withdrawl_msg['type'] == 'Recording' or withdrawl_msg[
                'type'] == 'Video' \
                    or withdrawl_msg['type'] == 'Attachment':
                # 执行下载方法
                withdrawl_msg['content']('.\\withdrawl\\' + withdrawl_msg['filename'])
                send_msg += '。文件名称为' + withdrawl_msg['filename'] + withdrawl_msg['filename'] + '。内容如下：'
                itchat.send(send_msg)
                if withdrawl_msg['type'] == 'Picture':
                    itchat.send_image('.\\withdrawl\\' + withdrawl_msg['filename'])
                if withdrawl_msg['type'] == 'Video':
                    itchat.send_video('.\\withdrawl\\' + withdrawl_msg['filename'])
                if withdrawl_msg['type'] == 'Attachment':
                    itchat.send_file('.\\withdrawl\\' + withdrawl_msg['filename'])
            else:
                send_msg += '。消息为：' + withdrawl_msg['content']
                if withdrawl_msg['type'] == 'Sharing':
                    send_msg += '。链接为：' + withdrawl_msg['url']
                itchat.send(send_msg)
            # 在字典里去掉已经撤回的消息
            del self.msg_dict[msg_id]
            # 提醒有好友撤回消息
            # itchat.send(send_msg)

    def save_msg(self):
        # 监听收到的信息
        @itchat.msg_register([TEXT, PICTURE, CARD, SHARING, RECORDING, ATTACHMENT, VIDEO], isFriendChat=True,
                             isGroupChat=True)
        def save_msg(msg):
            print(msg)
            msg_info = {
                'time': time.time(),
                # 'from': itchat.search_friends(userName=msg['FromUserName'])['NickName'],
                'type': msg['Type'],
                'content': msg['Text'],
                'url': msg['Url'],
                'filename': msg['FileName']
            }
            if itchat.search_friends(userName=msg['FromUserName']) != None:
                msg_info['from'] = itchat.search_friends(userName=msg['FromUserName'])['NickName']
            self.msg_dict[msg['MsgId']] = msg_info

    # 清理消息字典
    def clearc_time_out_msg(self):
        for msg_id in list(self.msg_dict):
            if time.time() - self.msg_dict[msg_id]['time'] > 120:
                del self.msg_dict[msg_id]

    # 定期清理字典的方法
    def clear_timer(self):
        while True:
            print('清理前字典大小：' + str(self.msg_dict.__len__()))
            self.clearc_time_out_msg()
            print('清理后字典大小：' + str(self.msg_dict.__len__()))
            time.sleep(120)

    def start(self):
        self.save_msg()
        self.prevent_group_withdrawl()
        self.prevent_withdrawl()
        itchat.auto_login(hotReload=True)
        threading._start_new_thread(itchat.run, ())
        threading._start_new_thread(self.schedulee.start, ())
        threading._start_new_thread(self.clear_timer,())
        return itchat.search_friends()['NickName']

    # 王者荣耀每日签到提醒
    @staticmethod
    def sign():
        itchat.send(msg='签到', toUserName='heromoba')
        time.sleep(5)
        itchat.send(msg='每日一题', toUserName='heromoba')

    # 设置签到时间
    def set_sign_time(self, time):
        times = time.split(':')
        hour = times[0]
        minute = times[1]
        print(hour + ' ' + minute)
        if self.schedulee.get_job('sign') is not None:
            self.schedulee.remove_job('sign')
        self.schedulee.add_job(WechatTools.sign, 'cron', minute=minute, hour=hour, id='sign')

    @staticmethod
    def get_friend_list():
        friend_list = itchat.get_friends(update=True)
        nickname_list = []
        for friend in friend_list:
            nickname = friend['NickName']
            if friend['RemarkName'] != '':
                nickname += '('+friend['RemarkName']+')'
            nickname_list.append(nickname)
        print(nickname_list)
        print(friend_list)
        return nickname_list

    @staticmethod
    def mass_msg(msg, friends):
        friend_list = itchat.get_friends()
        for friend in friend_list:
            if friend['NickName'] in friends:
                itchat.send(msg, friend['UserName'])
            elif friend['NickName']+'('+friend['RemarkName']+')' in friends:
                itchat.send(msg, friend['UserName'])


