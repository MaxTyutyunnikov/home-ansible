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
            data=dict(type='str'),
        ),
    )

    path = module.params['path']
    location = module.params['location']
    key = module.params['key']
    data = module.params['data']

    with open(path, 'r') as f:
        content = json.load(f)

    if not content:
        content = {}
    if location not in content:
        content[location] = {}
    content[location][key] = data

    with open(path, 'w') as f:
        json.dump(content, f)

    results = dict(
        changed=True,
        path=path,
    )

    module.exit_json(**results)

if __name__ == '__main__':
    main()
