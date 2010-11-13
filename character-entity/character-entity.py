#!python character-entity robot
import re, os, htmlentitydefs, logging, traceback
from waveapi import events, robot, appengine_robot_runner

def ucn_to_python(ucn):
    "Convert a Unicode Universal Character Number (e.g. 'U+4E00' or '4E00') to Python unicode (u'\\u4e00')"
    ucn = ucn.strip("U+")   
    if len(ucn) > 4:
        return eval("u'\U%08x'" % int(ucn, 16)) #this would be a security hole if we didn't use `int` to make the input safe
    else:
        return eval("u'\u%s'" % ucn) #4 characters isn't enough room to do damage with the eval
        #TODO: this dies on decimal input (e.g. ucn_to_python("100")
 
def OnDocumentChanged(event, wavelet):
    OnBlipSubmitted(event, wavelet)
    
def OnBlipSubmitted(event, wavelet):
    """Scan the wave to look for any special characters we should convert."""
    logging.debug('The wave contents are:\n'+event.blip.text)

    blip = event.blip
    if blip == None: return 
    text = blip.text

    latex_regex = re.compile('&(.+?);')

    matches = [m for m in latex_regex.finditer(text)]
    matches.sort(None, lambda x: x.start(1), True)
 
    for m in matches:
        bit = m.group(1)  

        good_to_go = False
        dec_ref = False
    
        if bit[0] == '#':
            try:
                int(bit[1:])
                if 1000 < int(bit[1:]) <10000:
                    dec_ref = True
            except:
                None
    
        if dec_ref:
            number = int(bit[1:])
            hex_bit = hex(number)[2:]
            ucn_to_python(hex_bit)
            proc_bit = str(ucn_to_python(hex_bit).encode('utf-8')) 
            good_to_go = True
 
        if bit in htmlentitydefs.name2codepoint:
            proc_bit = str(unichr(htmlentitydefs.name2codepoint[bit]).encode('utf-8'))  
            good_to_go = True
          
        if good_to_go:  
            start = m.start(1)
            end = m.end(1)
            blip.range(start-1,end+1).replace(proc_bit)

if __name__ == '__main__':
    myRobot = robot.Robot('character-entity', 
        image_url='http://thesaurus.maths.org/mmkb/media/png/Alpha.png',
        profile_url='http://code.google.com/p/wave-character-entity/')
    myRobot.register_handler(events.BlipSubmitted, OnBlipSubmitted)
    myRobot.register_handler(events.DocumentChanged, OnDocumentChanged, filter = ';', context=events.Context.SELF) #FIXME filter doesnt work
    appengine_robot_runner.run(myRobot) 
