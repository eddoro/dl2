from core.ctx import *
from target.dummy import *
from target.hms import *
from character.mikoto import *
from character.elisanne import *
from core import benchmark

#logset('all')

logset('dmg')
logset('buff')
#logset('act')
#logset('x')

def foo():
    Ctx()
    tar = Hms()
    tar.init()

    c = Mikoto()
    c.tar(tar)
    #c.conf.slot.w = 'v534_flame_zephyr'
    c.init()

    #c2 = Elisanne()
    #c2.tar(tar)
    #c2.init()

    Timer.run()
foo()

logset([])
benchmark.run(foo)

logcat()