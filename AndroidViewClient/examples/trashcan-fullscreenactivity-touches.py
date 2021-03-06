#! /usr/bin/env monkeyrunner
'''
Copyright (C) 2012  Diego Torres Milano
Created on Mar 13, 2012

@author: diego
'''


import re
import sys
import os
import string

# This must be imported before MonkeyRunner and MonkeyDevice,
# otherwise the import fails.
# PyDev sets PYTHONPATH, use it
try:
    for p in os.environ['PYTHONPATH'].split(':'):
        if not p in sys.path:
            sys.path.append(p)
except:
    pass
    
try:
    sys.path.append(os.path.join(os.environ['ANDROID_VIEW_CLIENT_HOME'], 'src'))
except:
    pass

from com.dtmilano.android.viewclient import ViewClient
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

package = 'com.example.trashcan'                                          
activity = '.FullScreenActivity'                           
component = package + "/" + activity

device, serialno = ViewClient.connectToDeviceOrExit()
#device.startActivity(component=component)
#MonkeyRunner.sleep(3)

vc = ViewClient(device, serialno)
button = vc.findViewWithTextOrRaise('Button')
button.touch()
toggle = vc.findViewWithTextOrRaise(re.compile('(ON)|(OFF)'))
toggle.touch()
