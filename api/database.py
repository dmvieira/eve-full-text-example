#!/usr/bin/env python

schema = {
    'name': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 512,
        'required': True
    },
    'city': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 256,
        'required': True
    }
    'location': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 1024
    }
    'phone': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 256
}
