odoo.define('gts_whatsapp_pos.ReceiptScreen', function(require) {
	"use strict";

    const { Printer } = require('point_of_sale.Printer');
	const ReceiptScreen = require('point_of_sale.ReceiptScreen');
    const Registries = require('point_of_sale.Registries');

    const { onMounted, useRef, status } = owl;

    const WhatsappReceiptScreen = ReceiptScreen =>
        class extends ReceiptScreen {
            constructor() {
                super(...arguments);
                const partner = this.currentOrder.get_partner();
                const orderName = this.currentOrder.get_name();
                var number = "";

                if (partner != null) {
                     console.log(`Partner: ${partner}, Whatsapp number: ${partner.mobile}`);
                    number = partner.phone || "";
                } else {
                     console.log(`Partner is null!`);
                }

                this.inputWhatsapp = number
                this.inputMessage = `Hello, Here is your receipt for the following order id: ${orderName}.`
                this.isSending = false
                this.whatsappButtonDisabled = true
                
            }
            is_valid_mobile() {
                const value = this.inputWhatsapp;
                if (value) {
                    const valueLen = value.replace(/[^0-9]/g, "").length;
                    return valueLen > 8 && valueLen < 15;
                }
                return false;
            }

            onInputWhatsapp(ev) {
                this.whatsappButtonDisabled = false;
                this.inputWhatsapp = ev.target.value;
            }

            async onSendWhatsapp() {
                if (this.isSending) {
                    return;
                }

                this.isSending = true;

                setTimeout(async () => {
                    try {
                        await this._sendWhatsappToCustomer();
                    } catch (error) {
                        console.error(error);
                        this.whatsappButtonDisabled = true;
                    }

                    this.isSending = false;
                }, 100);
            }

            async _sendWhatsappToCustomer() {
                var number = this.inputWhatsapp;
                var message = this.inputMessage;

                const receiptString = this.orderReceipt.el.innerHTML;
                const printer = new Printer(null, this.env.pos);
                const ticketImage = await printer.htmlToImg(receiptString);

                await this.rpc({
                    model: 'pos.order',
                    method: 'whatsapp_template_message',
                    args: [number, message, ticketImage],
                });
            }
		};

	Registries.Component.extend(ReceiptScreen, WhatsappReceiptScreen);
	return ReceiptScreen;
});