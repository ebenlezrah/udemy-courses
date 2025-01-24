# python googletrans - allows to use google translate service by installing this library 
# how to install a module directly from pycharm
import googletrans
from googletrans import Translator
translator = Translator()
print(translator.translate("Bonjour", src = "fr", dest ="es").text)
# this translates french to spanish
