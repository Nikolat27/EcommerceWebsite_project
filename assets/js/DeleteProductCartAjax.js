$(document).ready(function () {
    $(".delete-product").on("click", function () {
        let product_id = $(this).attr("data-product")
        console.log(product_id);
        $.ajax({

                url: `/cart/cart_delete/${product_id}/`,
                dataType: "json",

                success: function (response) {
                    if (response.bool === true) {
                        $("#cart-details").html(response.data)
                        $("#totalcartitems").text(response.totalcartitems)
                    }
                },
            })
    })
})