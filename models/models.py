# -*- coding: utf-8 -*-

from odoo import models, fields, api
import random
from datetime import datetime, timedelta

class wallapop(models.Model):
    _name = 'wallapop.wallapop'
    _description = 'wallapop.wallapop'

    name = fields.Char()

class usuario(models.Model):
    _name = 'res.partner'
    _description = 'usuario'
    _inherit = 'res.partner'
    
    #id ja te per ser res.pqartner
    id_usuario = fields.Integer(default = 7777, readonly = True, help = "Númeo que identifica a cada usuario.")
    name_user = fields.Char(default = "", required = True, help = "Nickname de l'usuari (?")
    num_tel = fields.Integer(default = 765555555, readonly = False, help = "Númeo de teléfono del usuario.")
    email = fields.Char(default = "aaa@gmail.com", readonly = False,required = True, help = "Email de l'usuari")
    # productos_favoritos = 
    # productos_vender = 
    avatar = fields.Image(size_width=200, max_height = 200, required = False)
    es_usuarioWallapop = fields.Boolean(default = False)

class producto(models.Model):
    _name = 'wallapop.producto'
    _description = 'producto'

    id_producto = fields.Integer(default = 7777, readonly = True, help = "Númeo que identifica a cada producto.")
    name_producto = fields.Char(default = "", required = True, help = "Nombre de cada producto")
    precio = fields.Float(readonly = True, required = True, default = 7, help = "Precio del producto")
    descripcion = fields.Char(default = "", required = False, help = "Descripción del producto")
    fecha_publicacuion = fields.Datetime(required = True, default = fields.Datetime.now, readonly=True, help = "La fecha que se publica el producto")
    vendedor = fields.Many2one("res.partner", required = True, help = "Usuario que vende el producto")

        # @api.onchange('vendedor')
        # def _filter_vendedor(self):                                             
        # return { 'domain': {'player2': [('id','!=',self.player1.id)]} }  



    # Wizard Usuario

    class usuario_wizard(models.TransientModel):
        _name = 'wallapop.usuario_wizard'
        _description = 'Wizzard create usuario'
        
        def _default_client(self):
            return self.env['res.partner'].browse(self._context.get('active_id')) 

        name = fields.Many2one('res.partner',default=_default_client, required=True)
        id_usuario = fields.Integer(default = 7777, readonly = True, help = "Númeo que identifica a cada usuario.")
        name_user = fields.Char(default = "", required = True, help = "Nickname de l'usuari (?")
        num_tel = fields.Integer(default = 765555555, readonly = False, help = "Númeo de teléfono del usuario.")
        email = fields.Char(default = "aaa@gmail.com", readonly = False,required = True, help = "Email de l'usuari")
        # productos_favoritos = 
        # productos_vender = 
        avatar = fields.Image(size_width=200, max_height = 200)
        

        @api.model
        def default_get(self, default_fields):
            result = super(usuario_wizard, self).default_get(default_fields)
            return result

        def create_usuario(self):
            self.ensure_one()
            self.name.write({'num_tel': self.num_tel,
                            'email': self.email,
                            'avatar': self.avatar,
                            'es_usuarioWallapop': True
                            })
