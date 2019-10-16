import __init__
from core.ctx import *
from core.characterbase import *
from target.dummy import *


class Aeleen(Character):
    def dconf(this):
        conf = {
         'slot.w'  : 'c534_wind'
        ,'slot.d'  : 'Zephyr'
        ,'slot.a1' : 'FB'
        ,'slot.a2' : 'BN'
        ,'acl.cancel' : """
            `s1
            `fs, x=5
        """
        }
        return conf

    def conf(this):
        return {
         'name'            : 'Aeleen'
        ,'star'            : 4
        ,'ele'             : 'wind'
        ,'wt'              : 'lance'
        ,'atk'             : 470
        ,'a1'              : ('bt', 0.25)

        ,'s1.hit'          : [(0,'h1')]
        ,'s1.attr.h1.coef' : 8.38
        ,'s1.recovery'     : 1.8
        ,'s1.sp'           : 2579

        ,'s2.sp'           : 8534
        ,'s2.recovery'     : 1
        }




if __name__ =='__main__':
    #logset(['buff','dmg','od','bk'])
    logset(['buff','dmg','bk','sp'])
    #logset('x')
    #logset('fs')
    #logset('act')
    #logset('s')
    #logset(['buff','debug','dmg','hit'])
    root = {'ex':['bow']}

    tar = dummy()
    tar.init()

    c = Aeleen(root)
    c.tar(tar)
    c.init()

    Timer.run(60)
    logcat()