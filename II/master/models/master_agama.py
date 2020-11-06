from odoo import models, fields, api

class MasterAgama(models.Model):
    _name = 'master.agama'

    no_rm = fields.Char(string='No RM', required=True)

    pasien_id = fields.Char(string='Nama Pasien', required=True)

    nip = fields.Char(string='NIP')

    tgl_lahir = fields.Date(string='Tgl Lahir', default=fields.Date.today())

    jenis_kelamin = fields.Selection([
            ('L', 'Laki-laki'),
            ('P', 'Perempuan'),
        ], string='Jenis Kelamin', default='L')

    alamat = fields.Text(string='Alamat')

    email = fields.Char(string='Email', default="@gmail.com")

    no_hp = fields.Char(string='No HP')

    line_ids = fields.One2many(
        comodel_name='data.kunjungan',
        inverse_name='order_id',
        string='Data Kunjungan',
        )

    l_ids = fields.One2many(
        comodel_name='data.kunjungan',
        inverse_name='l_id',
        string='Hasil Test',
        )