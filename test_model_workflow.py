# -*- coding: utf-8 -*-
from osv import fields, osv

class test_model_end(osv.osv):
    _name = "test.model.end"
    _columns = { 'creado' : fields.char('Creado', size=64, required=False, readonly=False) }
    _defaults = { 'creado' : 'Por el aire' }
test_model_end()

class test_model_start(osv.osv):
    def create_other(self, cr, uids, ids):
        ends = self.pool.get('test.model.end')
        for start in self.browse(cr, uids, ids):
            ends.create(cr, uids, {'creado' : start.nombre })
        
    _name = "test.model.start"
    _columns = { 'crear_otro' : fields.boolean('Crear otro', required=False),
                'nombre' : fields.char('Nombre', size=64, required=False, readonly=False)
                }
    _defaults = { 'crear_otro' : False,
                 'nombre' : 'Moron' }
    
test_model_start()