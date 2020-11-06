from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class DataKunjungan(models.Model):
    _name = 'data.kunjungan'
    
    order_id = fields.Many2one('master.agama', string='Data Kunjungan')

    tgl_periksa = fields.Datetime(string='Tgl Periksa', default=fields.Date.today())

    tgl_sampel = fields.Datetime(string='Tgl Sampel', default=fields.Date.today())

    no_mcl = fields.Char(string='No MCL')

    sampel_id = fields.Char(string='Sampel ID')

    no_reg = fields.Char(string='No Register')

    pengirim = fields.Char(string='Pengirim')

    penjamin = fields.Char(string='Penjamin')

    kelas = fields.Selection([
            ('1', 'I'),
            ('2', 'II'),
            ('3', 'III'),
        ], string='Kelas', default='1')

    diagnosa = fields.Text(string='Diagnosa')

    ruang = fields.Selection([
            ('1', 'Cempaka'),
            ('2', 'Melati'),
            ('3', 'Mawar'),
        ], string='Ruang', default='3')

    pembayaran = fields.Selection([
            ('1', 'Cash'),
            ('2', 'Card'),
        ], string='Pembayaran', default='2')

    l_id = fields.Many2one('master.agama', string='Hasil Test')

    reg = fields.Char(string='No Register', related='no_reg')

    test_name = fields.Selection([
            ('1', 'Hemoglobin'),
            ('2', 'Kultur Sens. Test Sputum'),
            ('3', 'Darah Rutin'),
            ('4', 'Darah Lengkap'),
            ('5', 'Hematokrit'),
            ('6', 'Trombosit'),
            ('7', 'Eritrosit'),
            ('8', 'Hitung Jenis (DIFF)'),
            ('9', 'Laju Endap Darah(LED)'),
            ('10', 'Golongan Darah'),
            ('11', 'Rhesus Faktor'),
            ('12', 'Gambaran Darah Tepi'),
            ('13', 'Retikulosit'),
            ('14', 'Eosinofil Absolut'),
            ('15', 'Serum Iron'),
            ('16', 'TIBC'),
            ('17', 'Control Waktu Trombin'),
            ('18', 'LE- Sel'),
            ('19', 'Antibodi anti Trombosit'),
            ('20', 'Rumple Leede'),
            ('20', 'Malaria (HEMATOLOGI)'),
            ('20', 'Plasmodium vivax'),
            ('20', 'Plasmodium falciparum'),
            ('20', 'Gambaran Sumsum'),
        ], string='Nama Test', default='1')