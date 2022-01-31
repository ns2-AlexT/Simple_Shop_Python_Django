"use strict";

window.onload = function () {
    console.log('DOM is ready.')
    $('.basket_record').on('change', "input[type='number']", function (event) {
        let quantityP = event.target.value;
        let basketPk = event.target.name;
        console.log('event', event, event.target, basketPk, quantityP)
        $.ajax({
            url: "/basket/upd/" + basketPk + "/" + quantityP + "/",
            success: function (data) {
                if (data.status) {
                    $('.basket_summary').html(data.basket_summary_)
                }
            },
        });
    });
}
