$(document).ready(function () {
    $('.delete-product-a').click(function () {
        // Get the product ID from the button's data attribute
        let unique_id = $(this).data('product-id');
        console.log(unique_id);
        // Send an AJAX request to the 'add_to_cart' view
        $.ajax({
            type: 'GET',
            url: `/cart/cart_delete_base/${unique_id}/`,
            data: {
                'unique_id': unique_id,
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