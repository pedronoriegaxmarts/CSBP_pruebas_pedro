from odoo import api, fields, models
import base64


class SlideChannelPartner(models.Model):
    _inherit = 'slide.channel.partner'

    certificate_sent = fields.Boolean('Certificate sent', default=False, readonly=True)
    res_partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Professor',
    )
    res_partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Professor',
    )

    @api.model
    def action_email_certificate(self,):
        for partner in self:
            if partner.completed == True:
                name = partner.partner_id.name
                pdf = self.env.ref('xmarts_elearning_certificate.certificate_pdf')._render_qweb_pdf(partner.id)
                b64_pdf = base64.b64encode(pdf[0])

                ir_id = self.env['ir.attachment'].create({
                    'name': name+'-Certificado.pdf',
                    'type': 'binary',
                    'datas': b64_pdf,
                    'res_model': 'mail.template',
                    'res_id': 0,
                    'mimetype': 'application/pdf',
                    'index_content':'application',
                })

                template = self.env.ref('xmarts_elearning_certificate.email_template_certificate_elearning')
                template.attachment_ids = [(4, ir_id.id)]
                template.send_mail(partner.id, force_send=True)
                template.attachment_ids = [(2, ir_id.id)]
                self.env['ir.attachment'].search([('id', '=', ir_id.id)]).unlink()

                print('Correo de certificado enviado')
            else:

                print('No tiene capacitación concluida')




    def _email_certificate_send(self):
        #Busca todos los usuarios que han concluido cursos
        partner_ids = self.env['slide.channel.partner'].search([('completed', '=',True),('completion', '=','100'),('certificate_sent','=',False)])
        print(partner_ids)
        for partner in partner_ids:
            print(partner.id)
            name = partner.partner_id.name
            pdf = self.env.ref('xmarts_elearning_certificate.certificate_pdf')._render_qweb_pdf(partner.id)
            b64_pdf = base64.b64encode(pdf[0])

            ir_id = self.env['ir.attachment'].create({
                'name': name + '-Certificado.pdf',
                'type': 'binary',
                'datas': b64_pdf,
                'res_model': 'mail.template',
                'res_id': 0,
                'mimetype': 'application/pdf',
                'index_content': 'application',
            })

            template = self.env.ref('xmarts_elearning_certificate.email_template_certificate_elearning')
            template.attachment_ids = [(4, ir_id.id)]
            template.send_mail(partner.id, force_send=True)
            #template.attachment_ids = [(2, ir_id.id)]
            self.env['ir.attachment'].search([('id', '=', ir_id.id)]).unlink()
            self.env['slide.channel.partner'].search([('id', '=', partner.id)]).write({'certificate_sent': True})






