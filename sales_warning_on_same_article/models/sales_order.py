from odoo import api, fields, models, _


class SaleOrderInherit(models.Model):
    _inherit = ['sale.order']

    @api.onchange('order_line')
    def raise_warning_duplication(self):
        """
        This function will warn the user of he added the same product
        to the same quotation twice.
        The warning will not prevent the user from adding the product.
        this return can also be replaced by:
           return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                 'title': _('Warning!'),
                 'message': (
                    'Vous avez ajouté l’article ', line[1].product_id.name, 'en double, avec un prix unitaire de',
                    line[0].price_unit),
                 'sticky': False,
             }
        for a sticky notification.
        """
        for order in self.order_line:
            line = self.order_line.filtered(lambda l: l.product_id == order.product_id)
            if len(line) > 1:
                return {'warning': {
                    'title': 'Warning',
                    'message': (
                    'Vous avez ajouté l’article ', line[1].product_id.name, 'en double, avec un prix unitaire de',
                    line[0].price_unit),
                }}
            break
