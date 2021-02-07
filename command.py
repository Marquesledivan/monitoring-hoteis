# #!/usr/local/bin/python3.7
# # -*- coding: utf-8 -*-

import os

lists = [ "influx" ]

for i in lists:
    execute = 'python3 /usr/src/app/requestMonitor.py -r {0}'.format(i)
    os.system(execute)
