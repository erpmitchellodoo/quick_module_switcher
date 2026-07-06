# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = "res.users"

    quick_switch_menu_ids = fields.Many2many(
        comodel_name="ir.ui.menu",
        relation="res_users_quick_switch_menu_rel",
        column1="user_id",
        column2="menu_id",
        string="Quick Switch Applications",
        domain=[("parent_id", "=", False)],
        help="Applications displayed in the quick module switcher in the backend header.",
    )

    @property
    def SELF_READABLE_FIELDS(self):
        return super().SELF_READABLE_FIELDS + ["quick_switch_menu_ids"]

    @property
    def SELF_WRITEABLE_FIELDS(self):
        return super().SELF_WRITEABLE_FIELDS + ["quick_switch_menu_ids"]

    @api.model
    def get_quick_switch_menu_ids(self):
        visible_menus = self.env.user.quick_switch_menu_ids._filter_visible_menus()
        return visible_menus.filtered(lambda menu: not menu.parent_id).sorted(
            key=lambda menu: (menu.sequence, menu.id)
        ).ids
