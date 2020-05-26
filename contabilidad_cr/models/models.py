# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
log = logging.getLogger(__name__)
class InvoiceLine(models.Model):
    _inherit = 'account.invoice.line'
    
    numero = fields.Char(string='Numero',related='invoice_id.number',store=True)
    fecha = fields.Date(string='Fecha',related='invoice_id.date_invoice',store=True)
    tipo_factura = fields.Selection([
    ], string='Tipo Factura',related='invoice_id.type',store=True)
    tipo = fields.Selection([
        ('servicio', 'Servicio'),
        ('bien', 'Bien'),
    ], string='Tipo')

    total_impuesto = fields.Monetary(compute='_compute_total_impuesto', string='Impuestos')

    @api.depends('price_subtotal')
    def _compute_total_impuesto(self):
       for line in self:
            line.total_impuesto = line.price_total - line.price_subtotal 
            
    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            if self.product_id.type == 'service':
                self.tipo = 'servicio'
            else:
                self.tipo = 'bien'
            self.name = self.product_id.name   