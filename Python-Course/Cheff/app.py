#Topic: Inheritance. 

from cheff import Cheff 
from chinese_cheff import ChineseCheff

myCheff = Cheff()
myCheff.make_chicken()

myChineseCheff = ChineseCheff()
myChineseCheff.make_special_dish()
myChineseCheff.make_fried_rice()
myChineseCheff.make_chicken()