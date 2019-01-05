# -*- coding: utf-8 -*-

from odoo import api, fields, models, _



# ---------------------------------------------------------
# Recouvrement Facturation
# ---------------------------------------------------------
class RecouvrementFacturation(models.Model):
    _name = "owatrans.recouvrement.facturation"
    _description = "Owatrans Recouvrement Facturation"


    partner_id = fields.Many2one('res.partner', string='Client', required=True)
    date_depot = fields.Date(string='Date de dêpot')
    mode_paiement = fields.Many2one('mode.paiement', string='Mode de paiement')
    num_facture = fields.Char(string='N° Facture')
    delai = fields.Char(string='Delai')
    date_echeance = fields.Date(string='Date d\'écheance')
    currency_id = fields.Many2one('res.currency', 'Devise', required=True,\
        default=lambda self: self.env.user.company_id.currency_id.id)
    montant = fields.Monetary(string='Montant de facture', store=True)
    observation = fields.Text(string='Obeservation')


class ModePaiement(models.Model):
    _name = "mode.paiement"
    _description = "Mode Paiement"

    name = fields.Char(string='Mode de Paiement')
