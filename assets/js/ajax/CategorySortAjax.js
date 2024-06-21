$(document).ready(function () {
    $(".order-sort").on("click", function () {
        let order = $(this).attr("data-product")
        console.log(order);
        $.ajax({
            url: `/products/order_ajax/${order}/1`,
            dataType: "json",

            success: function (response) {
                if (response.bool === true) {
                    $("#order_store_ajax").html(response.data)
                }
            },
        })
    })
})
