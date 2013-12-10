#This file is part stock_lot_quantity module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.model import fields
from trytond.pyson import If, Eval, Bool

__all__ = ['Move']
__metaclass__ = PoolMeta


class Move:
    __name__ = 'stock.move'
    lot = fields.Many2One('stock.lot', 'Lot',
        domain=[
            ('product', '=', Eval('product')),
            ],
        states={
            'readonly': Eval('state').in_(['cancel', 'done']),
            },
        context={
            'locations': If(Bool(Eval('warehouse', {})),
                [Eval('warehouse', {})], []),
            },
        depends=['state', 'product'])
