# coding: utf-8
from . import models
from . import decorators


def post_init_hook(cr, registry):

    print("======================")
    print("======================")
    print("post_init_hook")
