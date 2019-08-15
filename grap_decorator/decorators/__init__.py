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

    print("2)~~~~~~~~~~")
    print(")~~~~~~~~~~overloaded setup_model")

    models = list(env.values())
    for model in models:
        if model._name == 'account.check.deposit':
            import pdb; pdb.set_trace()
        print(model._name)

    return res

Registry.setup_models = setup_models


def check_state(allowed_states, display_field='name'):
    def wrap(func):
        def wrapped_function(self, *args, **kwargs):
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
        print("1)~~~~~~~~~~")
        print("~~~~~~~~~~wrapped_function")
        # attach allowed_states value to the function, to
        # allow post-process, once the class is initialized
        setattr(func, '_check_states', allowed_states)
        import pdb; pdb.set_trace()

        return wrapped_function
    return wrap
