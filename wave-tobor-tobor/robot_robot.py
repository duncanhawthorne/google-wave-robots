import os, logging, re, time, random, urllib, urllib2, traceback
from waveapi import events, robot, appengine_robot_runner, ops, element
import dhelper, dexporty
dhelper.domain = (os.environ['SERVER_NAME'])[:-12].split('.')[-1]

logging.debug('dhelper.domain = '+str(dhelper.domain))

robot_to_wave_dict = {'character-entity':'googlewave.com!w+zKjwwLceA', 'latex-helper':'googlewave.com!w+FwBYssjvb', 'duckandgooseberry':'googlewave.com!w+EZmmZ35vA'}

if dhelper.domain in robot_to_wave_dict:
	dhelper.code_stored_at = robot_to_wave_dict[dhelper.domain]
else:
	logging.debug('not deployed to a correct domain')

if (len((os.environ['SERVER_NAME'])[:-12].split('.')) > 1 and (os.environ['SERVER_NAME'])[:-12].split('.')[0] == 'export'): #as in something before the dot
	logging.debug('no code')
	text = dexporty.defaulttext
	exec(text)
	quit()

else:
	text = dhelper.get_code(dhelper.code_stored_at)
	import traceback
	exec(text)
	quit()