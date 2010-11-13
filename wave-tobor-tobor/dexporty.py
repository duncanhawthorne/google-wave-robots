defaulttext = """
#!/usr/bin/python2.4
import dhelper

def export_wave(event, wavelet):
  import dhelper
  #logging.debug('the wavelet creator is '+str(wavelet.participants))
  if dhelper.domain+'+donothing@appspot.com' == wavelet.robot_address:
    return
  
  logging.debug('running dexporty > export_wave')
  from google.appengine.ext import db #FIXME shuoldnt have to have this
  from google.appengine.ext import db

###
  try:
    logging.debug('event.button_name = '+str(event.button_name))
    if event.button_name != 'robot_deploy':
      return
  except:
    logging.debug('crashed trying to do event.button_name')
    None
###

  class WaveExport(db.Model):
    title = db.StringProperty()
    body = db.TextProperty()
    id = db.StringProperty()
    participants = db.StringListProperty()
    created = db.DateTimeProperty(auto_now_add=True)

  import os
  try:
    blip = wavelet.root_blip
    logging.debug([len(blip.text), blip.text, 'bob'+blip.text+'bob'])
    if blip.text == '\\n':#FIXME doubleslash
      logging.debug('empty wave')
      logging.debug('fred')
      logging.debug(dhelper.starter_robot)
      logging.debug('fred2')
      blip.append(str(dhelper.starter_robot))
      #return #as havent started writing anything yet
    body = blip.text.split('\\n', 2)[2]#FIXME doubleslash
    id = wavelet.wave_id
    query = db.Query(WaveExport)
    query.filter('id =', id)
    waveExport = query.get()
    server = os.environ['SERVER_NAME']

###
    logging.debug('id = '+str(id))
    if id != dhelper.code_stored_at:
      logging.debug('wrong id, quitting')
      logging.debug(id)
      logging.debug(dhelper.code_stored_at)
      return
###

    text = id.replace('+', '%252B')
    result = dhelper.new_encode(text)


    url = 'http://' + server + '/export?waveId=' + id.replace('+', '%252B')
    logging.debug('exporting wave contents to '+url)
    if waveExport is None:
      waveExport = WaveExport()
    else:
      if waveExport.body == body:
        waveExport = WaveExport()
        None
        #Nothing changed, do nothing
        #Blip_submitted gets called when gadget state changes as well
        #return
 
    waveExport.id = id
    waveExport.title = wavelet.title
    waveExport.body = body
    waveExport.put()
  except:
    wavelet.reply('There was an error. Write a title line and then some code all in the first blip')
   
  logging.debug('finished dexporty > export_wave')
  show_button(event,wavelet)


def show_button(event,wavelet):
###
    blip = wavelet.root_blip
###    
    MESSAGE = '\\nWhen you are happy with the changes to your robot: '
    MESSAGE_TWO = ''
###   
    should_i_reply = True

    

    def test_reply_state(blip):
      for blipy in blip.child_blips:
        if blipy.text[:len(MESSAGE+MESSAGE_TWO)] == MESSAGE+MESSAGE_TWO: #FIXME doubleslash
          should_i_reply = False
          return False
        new_result = test_reply_state(blipy)
        if new_result == False:
          return False
      return True

    should_i_reply = test_reply_state(blip)

#    for blipy in blip.child_blips:
#      if blipy.text[:len(MESSAGE+MESSAGE_TWO)] == MESSAGE+MESSAGE_TWO: #FIXME doubleslash
#        should_i_reply = False
#        break
#    logging.debug('should_i_reply = '+str(should_i_reply))

###
    #should_i_reply = False
###

    if should_i_reply:
      new_blip = wavelet.reply(MESSAGE)
      new_blip.append(MESSAGE_TWO, bundled_annotations=[('style/fontWeight', 'bold')])
      if True:#wavelet.creator == 'duncan.hawthorne@googlewave.com':
###
        #new_blip.append('\\nor click ', bundled_annotations=[('style/fontWeight', None)])
        new_blip.append(element.Button('robot_deploy', 'Deploy robot'))
###
  


def make_new_wave(event, wavelet):
  id = wavelet.wave_id
  text = id.replace('+', '%252B')
  result = dhelper.new_encode(text)
  None
  if event.button_name == dhelper.domain+'.appspot.com/newwave/':
    myRobot.new_wave('googlewave.com', participants=[result+'.'+dhelper.domain+'@appspot.com', event.modified_by], message='THE_MESSAGE', proxy_for_id='donothing', submit=True) 

if __name__ == '__main__': 
  myRobot = robot.Robot((os.environ['SERVER_NAME'])[:-12],
    image_url='http://'+os.environ['SERVER_NAME']+'/assets/icon.png',
    profile_url='http://code.google.com/p/wave-robot-robot/')
  myRobot.register_handler(events.WaveletSelfAdded, export_wave, context = [events.Context.ALL])
  myRobot.register_handler(events.BlipSubmitted, show_button, context = [events.Context.ALL])
  myRobot.register_handler(events.FormButtonClicked, export_wave, context = [events.Context.ALL]) 
  CONSUMER_KEY = ''
  CONSUMER_SECRET = ''
  myRobot.setup_oauth(CONSUMER_KEY, CONSUMER_SECRET, server_rpc_base='http://gmodules.com/api/rpc') 
  appengine_robot_runner.run(myRobot)
"""
