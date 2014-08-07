#!/user/bin/env python
__author__ = 'wenjiexu'
#! -*- coding: utf-8 -*-
import copy
import random

class UserCls:
    user_dict = {
        "name": "",
        "age": 0,
        "nick_name": "",
    }
    def __init__(self):
        pass

    def get_all(self):
        user_ls = []
        p_ls = ["zhangsan", "lisi"]
        for user in p_ls:
            t_dict = copy.deepcopy(UserCls.user_dict)
            t_dict["name"] = user
            t_dict["age"] = random.randint(10,100)
            t_dict["nick_name"] = user + " nick"
            user_ls.append(t_dict)


        return user_ls

