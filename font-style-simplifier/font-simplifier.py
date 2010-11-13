def OnBlipSubmitted(event, wavelet):
  import traceback
  try:
    blip=event.blip
    if blip is None: return
    for annot in blip.annotations:
      if annot.name in ['style/fontFamily', 'style/fontSize' , 'style/fontStyle' , 'style/color', 'link/manual', 'link/wave', 'style/textDecoration']:
        blip.range(annot.start, annot.end).clear_annotation(annot.name)
  except:
    wavelet.reply(traceback.format_exc())

if __name__ == '__main__':
    myRobot = robot.Robot((os.environ['SERVER_NAME'])[:-12], 
        image_url='http://'+os.environ['SERVER_NAME']+'/assets/icon.png',
        profile_url='')
    myRobot.register_handler(events.BlipSubmitted, OnBlipSubmitted)

    def ProfileHandler(name):
        return {'name': 'Style Simplifier',
                'imageUrl': 'http://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Arial_Helvetica_overlay2.svg/200px-Arial_Helvetica_overlay2.svg.png',
                'profileUrl': 'https://wave.google.com/wave/#restored:wave:googlewave.com!w%252BDH0hsz82A.1'}
    myRobot.register_profile_handler(ProfileHandler)
    appengine_robot_runner.run(myRobo 
