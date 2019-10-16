

class Skada(object):
    _skada = {}
    @classmethod
    def get(this):
        return this._skada

    @classmethod
    def init(this):
        this._skada = {}

    reset = init

    @classmethod
    def sum(this, q=0):
        def dmg(c):
            _sum = 0
            for i in c:
                _sum += c[i]
            return _sum

        r = {}
        for i in this._skada:
            d = dmg(this._skada[i]['dmg'])
            od = dmg(this._skada[i]['odmg'])
            r[i] = {'dmg':d, 'odmg':od}
            if not q:
                print(i,' dmg:', d )
                print(i,'odmg:', od )
        return r


    @classmethod
    def div(this, d, d2):
        for i in this._skada:
            for j in this._skada[i]['dmg']:
                this._skada[i]['dmg'][j] = \
                    int(this._skada[i]['dmg'][j] / d / d2)
            for j in this._skada[i]['odmg']:
                this._skada[i]['odmg'][j] = \
                    int(this._skada[i]['odmg'][j] / this._skada[i]['otime'] /d2)
    @classmethod
    def __str__(this):
        return str(this._skada)


