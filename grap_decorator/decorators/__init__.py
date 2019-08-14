# coding: utf-8
import logging


# # def check_state(allowed_states):
# #     def wrap(func):
# #         def wrapped_function(*args, **kwargs):
# #             print("IN THE DECORATOR")
# #             # env = args[0]
# #             return func(*args, **kwargs)
# #         return wrapped_function
# #     return wrap

# import functools


# # def check_state(func):
# #     @functools.wraps(func)
# #     def wrapper(self, *args, **kwargs):
# #         print("wrapper")
# #         return func(self, *args, **kwargs)
# #     return wrapper
_logger = logging.getLogger(__name__)


def check_state(allowed_states):
    def wrap(func):
        def wrapped_function(self, *args, **kwargs):
            print("wrapped_function")
            if getattr(self, '_ids', False):
                undeletable_items = self.filtered(
                    lambda x: x.state not in allowed_states)
                if undeletable_items:
                    raise UserError(_(
                        "Unable to delete because "))
            else:
                logger.warning(
                    "Function '%s' has been decorated with @check_state, but"
                    " it doesn't have records in self. Decorator has been"
                    " ignored.")
            return func(self, *args, **kwargs)
        return wrapped_function
    return wrap
