# Before run, pls install :
#pip install pyttsx3
#pip install PyPDF2

# Along with that, we also install the voice machine that is espeak-ng. 
# Here's link https://github.com/espeak-ng/espeak-ng/releases


import pyttsx3
import PyPDF2

#We will give the machine a voice and then perform operations with pdf files

bot = pyttsx3.init()
#getProperty() - get voice
#setProperty() - choice voice
v = bot.getProperty('voices')
bot.setProperty('voice', v[0].id)

bot.say("hello")
bot.runAndWait()