#This file is part stock_lot_quantity module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.pyson import If, Eval, Bool

__all__ = ['Move']
__metaclass__ = PoolMeta


class Move:
    __name__ = 'stock.move'

    @classmethod
    def __setup__(cls):
        super(Move, cls).__setup__()

        if not cls.lot.context:
            cls.lot.context = {}
        if not 'locations' in cls.lot.context:
            cls.lot.context.update({
                    'locations': If(Bool(Eval('warehouse', {})),
                        [Eval('warehouse', {})], []),
                    })
