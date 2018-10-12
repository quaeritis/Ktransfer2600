# -*- coding: utf-8 -*-
#
# Copyright © Spyder Project Contributors
# Licensed under the terms of the MIT License
# (see spyder/__init__.py for details)

"""
CustomXepr configuration options

Note: Leave this file free of Qt related imports, so that it can be used to
quickly load a user config file
"""
import getpass

# Local import
from Ktransfer2600.config.base import SUBFOLDER
from Ktransfer2600.config.user import UserConfig

# =============================================================================
#  Defaults
# =============================================================================
DEFAULTS = [
    ('Ktransfer2600',
     {
         'DARK': False,
         'KEITHLEY_ADDRESS': 'TCPIP0::192.168.2.121::INSTR',
         'VgStart': 10,
         'VgStop': -60,
         'VgStep': 1,
         'VdList': [-5, -60],
         'VdStart': 0,
         'VdStop': -60,
         'VdStep': 1,
         'VgList': [0, -20, -40, -60],
         'tInt': 0.1,
         'pulsed': False,
         'delay': -1,
         'gate': 'smua',
         'drain': 'smub'
     })
]


# =============================================================================
# Config instance
# =============================================================================
# IMPORTANT NOTES:
# 1. If you want to *change* the default value of a current option, you need to
#    do a MINOR update in config version, e.g. from 3.0.0 to 3.1.0
# 2. If you want to *remove* options that are no longer needed in our codebase,
#    or if you want to *rename* options, then you need to do a MAJOR update in
#    version, e.g. from 3.0.0 to 4.0.0
# 3. You don't need to touch this value if you're just adding a new option
CONF_VERSION = '2.1.0'

# Main configuration instance
try:
    CONF = UserConfig('CustomXepr', defaults=DEFAULTS, load=True,
                      version=CONF_VERSION, subfolder=SUBFOLDER, backup=True,
                      raw_mode=True)
except Exception:
    CONF = UserConfig('CustomXepr', defaults=DEFAULTS, load=False,
                      version=CONF_VERSION, subfolder=SUBFOLDER, backup=True,
                      raw_mode=True)
