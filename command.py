# #!/usr/local/bin/python3.7
# # -*- coding: utf-8 -*-

import os

lists = [ "HOTEL_DETAIL", "HOTEL_AVAILABILITY", "OSB_SEARCH_CVC", "OSB_SEARCH_OMNIBEES", "OSB_SEARCH_EXPEDIA",
          "OSB_SEARCH_JUNIPER","OSB_SEARCH_EXTRANET","OSB_DETAILS_CVC","OSB_DETAILS_OMNIBEES","OSB_DETAILS_EXPEDIA",
          "OSB_DETAILS_JUNIPER", "OSB_DETAILS_EXTRANET","OSB_ROOMS_CVC","OSB_ROOMS_OMNIBEES","OSB_ROOMS_EXPEDIA",
          "OSB_ROOMS_JUNIPER","OSB_ROOMS_EXTRANET","BOLT_SEARCH","BOLT_DETAILS","STATIC_HOTELS_DETAILS"]

for i in lists:
    execute = 'python3 /usr/src/app/requestMonitor.py -r {0}'.format(i)
    os.system(execute)
