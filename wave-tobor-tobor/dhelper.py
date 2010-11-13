new_way = False

def decode(dproxy):
      result = ''
      convert = False
      for letter in dproxy:
        if convert == True:
          result += letter.upper()
          convert = False
          continue
        else:
          if letter == '_':
            convert = True
            continue
          else:
            result += letter
            continue            
      return result

def encode(text):
	  caps = 'QWERTYUIOPASDFGHJKLZXCVBNM_'
	  result = ''
	  for letter in text:
	    if not letter in caps:
	      result += letter
	    else:
	      result += '_'+letter.lower()
	  return result

def get_code(result):
      from google.appengine.ext import db
      import models
      waveId = result.replace('%252B', '+').replace('%2B', '+')
      query = db.Query(models.WaveExport)
      query.filter('id =', waveId)
      query_result = query.get()    
      if query_result is None:
        text = '<error>Please check the ID</error>'
      else:
        text = query_result.body
      return text

fail_text = ''

starter_robot="""EDIT ME: A sample wave robot to get you started
import traceback

def when_a_blip_is_submitted(event, wavelet):
  try:

    #This is where you should put your function content:
    #It will reply when you add the robot to a wave, edit a blip, and click done.
    blip = event.blip
    new_blip = wavelet.reply("Hi! I am your robot. You just finished editing a blip.")
    if blip.text == '\\n':
      new_blip.append('\\nYou didnt write anything in the blip')
    else:
      new_blip.append('\\nYou wrote: '+blip.text)

  except:
    wavelet.reply(traceback.format_exc()) 

if __name__ == '__main__':
    myRobot = robot.Robot('')
    myRobot.register_handler(events.BlipSubmitted, when_a_blip_is_submitted)
    def ProfileHandler(name): #set the profile information here
        return {'name': 'CHANGEME',
                'imageUrl': 'http://www.mustwarnothers.com/news/_img/changeme.jpg',
                'profileUrl': 'http://change.gov/'}
    myRobot.register_profile_handler(ProfileHandler)
    appengine_robot_runner.run(myRobot)"""

show_fail="""def my_function(event, wavelet):
    import dhelper
    wavelet.reply(dhelper.fail_text)

if __name__ == '__main__':
    myRobot = robot.Robot('FAIL', 
        image_url='http://dclips.fundraw.com/zobo500dir/tasto_8_architetto_franc_01.jpg',
        profile_url='') 
    myRobot.register_handler(events.WaveletSelfAdded, my_function)
    myRobot.register_handler(events.BlipSubmitted, my_function)
    appengine_robot_runner.run(myRobot)"""

def new_decode(dproxy):
      result = ''
      convert = False
      dc = False
      for letter in dproxy:
        if convert == True:
          if dc == True:
            result += {'d':'.', 'e':'!', 'p':'%', 'u':'_', 'h':'-'}[letter]
            dc = False
            convert = False
            continue
          else:
            if letter is '-':
              dc=True
              continue
            else:
              result += letter.upper()
              convert = False
              continue
        else:
          if letter == '-':
            convert = True
            continue
          else:
            result += letter
            continue            
      return result

def new_encode(start):
	result = ''
	for letter in start:
		if letter in 'qwertyuiopasdfghjklzxcvbnm1234567890':
			result += letter
		elif letter in 'QWERTYUIOPASDFGHJKLZXCVBNM':
			result += '-'+letter
		elif letter in '!%._-':
			result += '--'+{'.':'d', '!':'e', '%':'p', '_':'u', '-':'h'}[letter]
	return result	