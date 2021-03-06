import __init__
from core.ctx import *
from core.characterbase import *
from target.dummy import *
from target.mg import *
from mod.afflic import *
from mod.skillshift import *


class Rena(Character):
    def dconf(this):
        return {
         'slot.w'     : 'c534_flame'
        ,'slot.d'     : 'Sakuya'
        ,'slot.a'     : 'RR+EE'
        ,'acl.cancel' : '''
            `s1
            `s2, s='s1'
            `s3, fsc
            `fs, x=5
        '''
        }

    def conf(this):
        return {
         'star' : 5
        ,'ele'  : 'flame'
        ,'wt'   : 'blade'
        ,'atk'  : 471
        ,'a1'   : ('skill_link', 0.15, 'def')
#        ,'a3'   : ('def_c_hot')

        ,'s1.hit'          : [(0,'h1'),(0,'h1'),(0,'h1'),(0,'h1'),(1,'h2')]
        ,'s1.attr.h1.coef' : 0.72
        ,'s1.attr.h2.coef' : 6.65
        ,'s1.sp'           : 3303
        ,'s1.stop'         : 2.500

        ,'s12.on_end'      : [this.s1_crit]
        ,'s12.stop'        : 2.533

        ,'s13.attr.h1.killer' : {'burn':0.8}
        ,'s13.attr.h2.killer' : {'burn':0.8}
        ,'s13.on_end'         : [this.s1_crit]
        ,'s13.stop'           : 2.533

        ,'s2.sp'   : 6582
        ,'s2.stop' : 1

        }

    def init(this):
        this.Afflic = Afflic(this)
        this.burn = this.Afflic['burn']('s1', 1.20, 0.97)
        this.ss = Skillshift(this, 1, this.conf['s12'], this.conf['s13'])

    def s1_crit(this):
        this.Selfbuff('s1_crit',0.1,'cc')(15)

    def s1_proc(this):
        this.burn()

    def s2_proc(this):
        this.Selfbuff('s2',0.5,'cd')(20)
        this.s1.full()


if __name__ =='__main__':
    import run
    run.this_character(mass=1)
