#Word count robot 
import os, logging, re, time, random, urllib, urllib2, traceback
from waveapi import events, robot, appengine_robot_runner, ops, element
def OnBlipSubmitted(event, wavelet):
  import traceback, logging
  try:
    just_made = False
    import time
    blip = event.blip
    if blip == None: return

    def word_stats(text, first = False):
      logging.debug(text)
      wc = len(text.split())
      tc = len(text)
      if not first:
        tc = tc-1 #FIXME overcome bug in wave regarding inline blip being counted as text
      ttext = text.replace(' ','')
      tcws = len(ttext)
      return 'Words: '+str(wc)+'\nCharacters (no spaces):  '+str(tcws)+'\nCharacters (with spaces):  '+str(tc)

    #create new blip with stats
    for annot in blip.annotations:
      if annot.name == 'word-count-bot.appspot.com' and annot.value == 'word-count-me':
        num = str(time.time())
        blip.range(annot.start, annot.end).annotate("style/backgroundColor", "rgb(204,204,204)")
        blip.range(annot.start, annot.end).annotate("word-count-bot.appspot.com", num)
        new_blip = blip.insert_inline_blip(annot.end)
        new_blip.append(word_stats(blip.text[annot.start:annot.end], True))
        new_blip.range(1,len(new_blip.text)).annotate('word-count-linked', num)
 #       new_blip.range(1,len(new_blip.text)).annotate("style/backgroundColor", "rgb(204,204,204)")
        just_made = True

    if just_made: #dont really think this is necessary, but for safety
      return

    #update stats
    for blipy in blip.child_blips: 
      code = None
      for annoty in blipy.annotations:
        if annoty.name == 'word-count-linked': #if blip has been caused by the bot
          code = annoty.value
      if code != None: #if blip has been caused by the bot
        for annot in blip.annotations:
          if annot.name == 'word-count-bot.appspot.com' and annot.value == code: #find the text that caused the blip
            specific_stats = word_stats(blip.text[annot.start:annot.end])
            if specific_stats != blipy.text[1:]: #something has changed
              blipy.range(1,len(blipy.text)).replace(word_stats(blip.text[annot.start:annot.end])) #change the text to show new stats
              blipy.range(1,len(blipy.text)).annotate('word-count-linked',code)
    #          blipy.range(1,len(blipy.text)).annotate("style/backgroundColor", "rgb(204,204,204)")
    
    #cleanup
    for annot in blip.annotations:
      if annot.name == 'word-count-bot.appspot.com' and annot.value != 'word-count-bot.appspot.com':
        code = annot.value
        found_it = False
        for blipy in blip.child_blips:
          for annotq in blipy.annotations: #look for a blip that is linked to this text
            if annotq.name == 'word-count-linked' and annotq.value == code: 
              found_it = True
        if found_it == False: #no exists, so clean up
          blip.range(annot.start, annot.end).clear_annotation('word-count-bot.appspot.com')
          blip.range(annot.start, annot.end).clear_annotation('style/backgroundColor')
          return
        
  except:
    None
   # wavelet.reply(traceback.format_exc())

if __name__ == '__main__':
    myRobot = robot.Robot('Word Count', 
        image_url='http://word-count-bot.appspot.com/assets/icon.png',
        profile_url='https://wave.google.com/wave/#restored:wave:googlewave.com!w%252B04X-AEjMc.2')

    myRobot.register_handler(events.WaveletSelfAdded, OnBlipSubmitted)
    myRobot.register_handler(events.BlipSubmitted, OnBlipSubmitted)
    myRobot.register_handler(events.AnnotatedTextChanged, OnBlipSubmitted, filter='word-count-bot.appspot.com')
    myRobot.register_handler(events.WaveletBlipRemoved, OnBlipSubmitted, context = [events.Context.ALL]) #need context >= siblings else the cleanup gets a bit carried away, the blip you are counting words in (the parent of the blip you send in this event) doesnt realise it has other children
    appengine_robot_runner.run(myRobot) 
