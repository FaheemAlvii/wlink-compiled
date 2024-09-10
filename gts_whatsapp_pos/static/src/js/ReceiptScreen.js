/** @odoo-module */
import { ReceiptScreen } from "@point_of_sale/app/screens/receipt_screen/receipt_screen";
import { OrderReceipt } from "@point_of_sale/app/screens/receipt_screen/receipt/order_receipt";
import { _t } from "@web/core/l10n/translation";
import { patch } from "@web/core/utils/patch";
import { useState } from "@odoo/owl";

patch(ReceiptScreen.prototype, {
    setup() {
        super.setup(...arguments);

        const partner = this.currentOrder.get_partner();
        const orderName = this.currentOrder.get_name();
        var number = "";

        if (partner != null) {
            console.log(`Partner: ${partner}, Whatsapp number: ${partner.mobile}`);
            number = partner.phone || "";
        } else {
            console.log(`Partner is null!`);
        }

        this.orderUiState = useState({
            inputWhatsapp: number,
            inputMessage: `Hello, Here is your receipt for the following order id: ${orderName}.`,
            isSending: false,
            whatsappButtonDisabled: false,
        });
    },

    is_valid_mobile() {
        const value = this.orderUiState.inputWhatsapp;
        if (value) {
            const valueLen = value.replace(/[^0-9]/g, "").length;
            return valueLen > 8 && valueLen < 15;
        }
        return false;
    },

    onInputWhatsapp(ev) {
        this.orderUiState.whatsappButtonDisabled = false;
        this.orderUiState.inputWhatsapp = ev.target.value;
    },

    async onSendWhatsapp() {
        if (this.orderUiState.isSending) {
            return;
        }

        this.orderUiState.isSending = true;

        setTimeout(async () => {
            try {
                await this._sendWhatsappToCustomer();
            } catch (error) {
                console.error(error);
                this.orderUiState.whatsappButtonDisabled = true;
            }

            this.orderUiState.isSending = false;
        }, 100);
    },

    async _sendWhatsappToCustomer() {
        const partner = this.currentOrder.get_partner();

        var name = partner ? partner.name : this.orderUiState.inputWhatsapp;
        var number = this.orderUiState.inputWhatsapp;
        var message = this.orderUiState.inputMessage;

//        this._rpc({
//        	model: 'pos.order',
//        	method: 'whatsapp_template_message',
//        	args: [this.res_id],
//    	}).then(function (result) {
//    	    console.log(`the python function result: ${result}`);
//    	});
//
//        rpc.query({
//            model: 'account.move',
//            method: 'whatsapp_template_message',
//            args: [],
//        });
        const order = this.currentOrder;
        const orderName = order.get_name();
        const order_server_id = this.pos.validated_orders_name_server_id_map[orderName];
        const ticketImage = await this.renderer.toJpeg(
            OrderReceipt,
            {
                data: this.pos.get_order().export_for_printing(),
                formatCurrency: this.env.utils.formatCurrency,
            },
            { addClass: "pos-receipt-print" }
        );

        await this.orm.call("pos.order", "whatsapp_template_message", [number, message, ticketImage]);

//        ajax.jsonRpc("/gts_whatsapp_pos_template_message", "call", {},);
    },

});
