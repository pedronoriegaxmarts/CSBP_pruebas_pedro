from odoo import api, fields, models

class SlideChannel(models.Model):
    _inherit = 'slide.channel'

    representative_csbp = fields.Many2one(
        comodel_name='hr.employee',
        required=True,
        string='Representante CSBP',
    )
    representative_course = fields.Many2one(
        comodel_name='res.users',
        required=True,
        string='Representante Curso',
    )