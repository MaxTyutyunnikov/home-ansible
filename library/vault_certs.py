#!/usr/bin/python
# -*- coding: utf-8 -*-


import json
import os

from ansible.module_utils.basic import AnsibleModule


def main():
    module_args = {
        'action': {
            'choices': ['read', 'write'],
            'required': True,
            'type': 'str',
        },
        'backend': {
            'default': 'pki'
            'type': 'str',
        },
        'type': {
            'choices': ['ca', 'cert']
            'default': 'cert',
            'type': 'str',
        },
        'rule': {
            'default': 'client',
            'type': 'str',
        },
    }
    module = AnsibleModule(
        argument_spec = module_args,
    )

    action = module.params['action']
    backend = module.params['backend']
    cert_type = module.params['type']
    rule = module.params['rule']

    ret = {'changed': False}

    module.exit_json(**ret)

if __name__ == '__main__':
    main()
