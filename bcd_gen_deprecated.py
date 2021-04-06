#! /usr/bin/python

"""

"""

import re
import os # for walk
import json

dir_name='./api/'

eventdict = dict()

def expand_tree(p_dict,level,keychain):
    if not isinstance(p_dict, dict):
       #print('NOT DICT: %s' % p_dict)
       pass
       return
       
    try:
       if p_dict['__compat']['status']['deprecated']: #this is dict with a status that is true
            #print("YYYKeychain:  %s" % (keychain))
            print(keychain)
            return
    except:
       #print(p_dict)
       pass
            
    for key, value in p_dict.items():
        newkeychain = keychain + '.' + key
        if newkeychain.startswith('.'):
            newkeychain = newkeychain[1:]
        expand_tree(value, level+1, newkeychain)

for subdir, dirs, files in os.walk(dir_name):
    for file in files:
        originalfile=subdir+'\\'+file
        originalfile=originalfile.replace('\\','/')
        #targetfile=originalfile.replace('./content/files/','')

        if not file.endswith('.json'): #only process json
            #print("Skip not json: %s" % file)
            continue

        #print("\n\nJson file: %s" % originalfile)
        try:
            current_file =  open (originalfile, "r")
            file_data = json.loads(current_file.read())
            current_file.close()
            
        except:
            print("Exception loading json")

        
        #print(file_data)
        expand_tree(file_data,1,'')
