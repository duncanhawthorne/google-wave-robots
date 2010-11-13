import os, logging, re, time, random, urllib, urllib2, traceback
from waveapi import events, robot, appengine_robot_runner, ops, element
import dhelper, dexporty
dhelper.domain = (os.environ['SERVER_NAME'])[:-12].split('.')[-1]

if len((os.environ['SERVER_NAME'])[:-12].split('.')) > 1: #as in something before the dot
	dhelper.new_way = True
	code_from = (os.environ['SERVER_NAME'])[:-12].split('.')[0]
	logging.debug('dhq: code_from '+code_from)
	text = dhelper.get_code(dhelper.new_decode(code_from))
	logging.debug('text to run is'+text)
	import traceback
	try:
		exec(text)
	except:
		logging.debug('crash running code in a wave:')
		dhelper.fail_text = traceback.format_exc()
		logging.debug(dhelper.fail_text)
		text = dhelper.show_fail
		exec(text)
	quit()
else:
	dhelper.new_way = True
	logging.debug('no code')
	text = dexporty.defaulttext
	exec(text)
	quit()