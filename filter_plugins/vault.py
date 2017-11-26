#!/usr/bin/env python

import re

def split_output(data, match_type):
    if match_type not in ['ca', 'cert', 'key']:
        raise Exception

    if match_type == 'ca':
        r = re.compile(
            r'issuing_ca\s+(-----BEGIN CERTIFICATE-----'
             '.*?'
             '-----END CERTIFICATE-----)',
            re.DOTALL
        )
    elif match_type == 'cert':
        r = re.compile(
            r'certificate\s+(-----BEGIN CERTIFICATE-----'
             '.*?'
             '-----END CERTIFICATE-----)',
            re.DOTALL
        )
    elif match_type == 'key':
        r = re.compile(
            r'private_key\s+(-----BEGIN RSA PRIVATE KEY-----'
             '.*'
             '-----END RSA PRIVATE KEY-----)',
            re.DOTALL
        )

    match = r.search(data)
    if match:
        return match.group(1) + '\n'
    else:
        raise Exception


class FilterModule(object):
    def filters(self):
        return {'vault_cert': split_output}
