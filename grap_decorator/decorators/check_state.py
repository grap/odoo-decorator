# coding: utf-8
# Copyright (C) 2019-Today GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


def check_state(my_list):
    def wrap(func):
        def wrapped_function(*args, **kwargs):
            print("IN WRAPPED_FUNCTION")
            # env = args[0]
            return func(*args, **kwargs)
        print("IN WRAP")
        return wrapped_function
    return wrap
