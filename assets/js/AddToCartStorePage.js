$(document).ready(function () {
    $('.add-to-cart').click(function () {
        // Get the product ID from the button's data attribute
        let product_id = $(this).data('product-id');
        console.log(product_id);
        // Send an AJAX request to the 'add_to_cart' view
        $.ajax({
            type: 'GET',
            url: `/cart/cart_add_store/${product_id}/`,
            data: {
                'product_id': product_id,
                "count": 1,
            },
            success: function (response) {
                // Handle the success response
                console.log("Product Added!");
                if (response.bool === true) {
                    $("#cart-details").html(response.data)
                    $("#totalcartitems").text(response.totalcartitems)
                    $("#totalcartitems2").text(response.totalcartitems)
                }
            },
            error: function (xhr, status, error) {
                // Handle the error response
                console.log("Error!");
            }
        });
    });
});