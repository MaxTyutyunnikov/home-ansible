#!/usr/bin/python
# -*- coding: utf-8 -*-


import json
import os

from ansible.module_utils.basic import AnsibleModule


def main():
    # These options need a refactor
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='path', required=True, aliases=['dest']),
            location=dict(type='str'),
            key=dict(type='str'),
            data=dict(type='raw'),
        ),
    )

    path = module.params['path']
    location = module.params['location']
    key = module.params['key']
    data = module.params['data']

    ret = {
        'changed': False,
        'path': path,
    }

    if os.path.isfile(path):
        with open(path, 'r') as f:
            content = json.load(f)
    else:
        content = {}

    if location not in content:
        content[location] = {}

    old_data = content[location][key] if key in content[location] else None
    if old_data == data:
        module.exit_json(**ret)

    content[location][key] = data
    with open(path, 'w') as f:
        json.dump(content, f, indent=4, sort_keys=True)
    ret['changed'] = True

    module.exit_json(**ret)

if __name__ == '__main__':
    main()
