# coding: utf-8
import logging

from odoo import _, api, SUPERUSER_ID
from odoo.exceptions import UserError
from odoo.modules.registry import Registry

_logger = logging.getLogger(__name__)

_setup_models_original = Registry.setup_models


def setup_models(self, cr):
    print("overloaded")

    res = _setup_models_original(self, cr)
    env = api.Environment(cr, SUPERUSER_ID, {})
    models = list(env.values())
    for model in models:
        print(model._name)
    return res

Registry.setup_models = setup_models

# from odoo import registry

# import pdb; pdb.set_trace()
# class AbstractModel(models.AbstractModel):
#     # def __init__(self, pool, cr):
#     #     print("__init__.py")
#     #     return super().__init__(pool, cr)

#     @classmethod
#     def _build_model(cls, pool, cr):
#         print("====================")
#         print("_build_model")
#         res = super(AbstractModel, cls)._build_model(pool, cr)
#         print("**********************")
#         return res

#     @classmethod
#     def _build_model_attributes(cls, pool):
#         print("====================")
#         print("_build_model_attributes")
#         res = super(AbstractModel, cls)._build_model_attributes(pool)
#         print("**********************")
#         return res


def check_state(allowed_states, display_field='name'):
    def wrap(func):
        def wrapped_function(self, *args, **kwargs):
            print("========================")
            print("========================")
            print("========================")
            print("CHECKING STATE %s...." % ','.join(allowed_states))
            import pdb; pdb.set_trace()
            undeletable_items = self.filtered(
                lambda x: x.state not in allowed_states)
            if undeletable_items:
                raise UserError(_(
                    "Unable to realize the operation on the following"
                    " item(s) '%(item_names)s' because there are not in the"
                    " allowed state(s) '%(allowed_state_names)s'.") % {
                        'item_names': ', '.join(
                            undeletable_items.mapped(display_field)),
                        'allowed_state_names': ', '.join(allowed_states),
                })
            return func(self, *args, **kwargs)
        print("~~~~~~~~~~")
        print("~~~~~~~~~~wrapped_function")
        # attrsetter('_check_states', func)
        # attach allowed_states value to the function, to
        # allow post-process, once the class is initialized
        setattr(func, '_check_states', allowed_states)

        return wrapped_function
    print("~~~~~~~~~~")
    print("~~~~~~~~~~check_state")
    return wrap
