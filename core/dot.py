import __init__
from core.ctx import *
from core import dmg


class Dotbase():
    def __init__(this, host):
        this.host = host
        if not this.host.Dot:
            this.host.Dot = this

    def __call__(this, classname, iv):
        return Dot(this.host, classname, iv)
    

class Dot():
    def __init__(this, host, classname, iv):
        this.host = host
        this.classname = classname
        this.iv = iv

        this._dmg = dmg._Dmg()
        this._dmg.to_od = 0
        this._dmg.to_bk = 0
        this._dmg.hit = 0

        this.stacks = 0
        this.all_stacks = []

        this.log = Logger('dot')



    def tick_proc(this, t):
        dmg_sum = 0
        #stacks = this._static.stacks
        for i in this.all_stacks:
            this.host.dt_no_od(i._dmg)
        t()

    def __call__(this, src, name, coef, duration):
        return _Dot(this, src, name, coef, duration)


class _Dot():
    def __init__(this, static, src, name, coef, duration):
        this._static = static
        this.src = src
        this.name = name
        this.coef = coef
        this.duration = duration

        this.classname = static.classname
        this.iv = static.iv

        this._dmg = dmg._Dmg()
        this._dmg.name = '%s_%s'%(name, this.classname)
        this._dmg.hostname = src.name
        this._dmg.to_bk = 0
        this._dmg.to_od = 0
        this._dmg.hit = 0
        dmgconf = {
                 'coef' : coef
                ,'type' : 's'
                }
        this.label = '%s, %s'%(src.name, this._dmg.name)
        this.Dc = this.src.Dmg(dmgconf)
        this.t_dot_end = Timer(this.dot_end_proc)
        this.log = Logger('dot')


    def dot_end_proc(this, t):
        idx = this._static.all_stacks.index(this)
        this._static.all_stacks.pop(idx)
        this._static.stacks -= 1
        if this.log:
            this.log(this.name,'stack_end',
                    "dot stack <%d>"%this._static.stacks)
        if this._static.stacks < 0:
            print('err in dot_end_proc')
            raise
        if this._static.stacks == 0:
            this._static.t_tick.off()


    def __call__(this):
        if this.log:
            this.log(this.label, 'apply',this._static.host.name)

        this._dmg.dmg = this.Dc.calc()

        this._static.all_stacks.append(this)
        this.t_dot_end(this.duration)
        if this._static.stacks == 0:
            this._static.t_tick = Timer(this._static.tick_proc)(this.iv)
        this._static.stacks += 1
        if this.log:
            if this._static.stacks > 1:
                this.log(this.name,'stack_add',
                        "dot stack <%d>"%this._static.stacks)