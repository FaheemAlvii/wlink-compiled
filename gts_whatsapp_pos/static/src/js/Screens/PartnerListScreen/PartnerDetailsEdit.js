/** @odoo-module */

import { _t } from "@web/core/l10n/translation";
import { PartnerDetailsEdit } from "@point_of_sale/app/screens/partner_list/partner_editor/partner_editor";
import { ErrorPopup } from "@point_of_sale/app/errors/popups/error_popup";
import { patch } from "@web/core/utils/patch";

patch(PartnerDetailsEdit.prototype, {
    setup() {
        const res = super.setup(...arguments);
        this.changes.whatsapp = this.props.partner.whatsapp;
        return res;
    },

    get is_valid_mobile() {
        const value = this.changes.whatsapp;
        // console.log('==whatsapp_server_id==',value)
        if (value) {
            const valueLen = value.replace(/[^0-9]/g, "").length;
            return valueLen > 8 && valueLen < 15;
        }
        return false;
    },
    saveChanges() {
        if (!this.is_valid_mobile) {
            return this.popup.add(ErrorPopup, {
                title: _t("Invalid Number"),
                body: _t("A Whatsapp Number should be Number"),
            });
        }
        return super.saveChanges(...arguments);
    },
});
