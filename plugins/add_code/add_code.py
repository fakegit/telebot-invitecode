# -*- coding:utf-8 -*-
import os
import json
global last_line
global chongfu
def add_code(bot, message):
    hx = "\n"
    chongfu = 0
    if str(message["from"]["id"]) == bot.root_id:
        with open(bot.plugin_dir + "add_code/__init__.py", encoding="utf-8") as f:
            h = f.readline()[1:]
        with open(bot.plugin_dir + 'invite_code/usertext.json', 'r') as f1:
            userjson = json.load(f1)
        if len(message["text"]) < len(h):
            status = bot.sendChatAction(message["chat"]["id"], "typing")
            status = bot.sendMessage(message["chat"]["id"], "添加失败，请输入邀请码", "HTML")
            return False
        code = message["text"][len(h) - 1:] + "\n"
        with open(bot.plugin_dir + 'invite_code/code.txt', 'r') as fp:
            lines = fp.readlines()
            last_line = lines[-1]
        if hx not in last_line:
            f = open(bot.plugin_dir + 'invite_code/code.txt', 'a+')
            f.write(hx)
            f.write(code)
            f.close()
            status = bot.sendMessage(message["chat"]["id"], "添加完成，当前邀请码剩余"+str(lentj(bot=bot)), "HTML")
        else:
            f = open(bot.plugin_dir + 'invite_code/code.txt', 'a+')
            f.write(code)
            f.close()
            status = bot.sendMessage(message["chat"]["id"], "添加完成，当前邀请码剩余"+str(lentj(bot=bot)), "HTML")
    else:
        status = bot.sendChatAction(message["chat"]["id"], "typing")
        status = bot.sendMessage(message["chat"]["id"], "添加失败，您没有权限添加", "HTML")
def lentj(bot):
    count = 0
    for index, line in enumerate(open(bot.plugin_dir + 'invite_code/code.txt', 'r')):
        count += 1
    return count
