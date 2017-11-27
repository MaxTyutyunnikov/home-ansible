#!/usr/bin/env python

def parse_output(data, key):
    ret = {}
    for line in data[2:]:
        if '\t' in line:
            split = line.split('\t')
            k = split[0].strip()
            v = split[1]
            ret[k] = v + '\n'
            ret['latest'] = k
        else:
            ret[ret['latest']] += line + '\n'
    del ret['latest']

    if key in ret:
        return ret[key]
    else:
        raise Exception


class FilterModule(object):
    def filters(self):
        return {'vault_parse': parse_output}
