$("#add-to-cart-form-1").submit(function (e) {
    e.preventDefault();
    let button = $("#add-to-cart-btn-1");
    $.ajax({
        data: $(this).serialize(),
        method: $(this).attr('method'),
        url: $(this).attr('action'),
        dataType: "json",

        beforeSend: function () {
            setTimeout(() => button.html("✔️"), 700);
            console.log("adding to cart...");
        },
        success: function (response) {
            console.log("success!");
            if (response.bool === true) {
                setTimeout(() => button.html(" خرید کالا"), 1500);
                $("#cart-details").html(response.data)
                $("#totalcartitems").text(response.totalcartitems)
                $("#totalcartitems2").text(response.totalcartitems)
            }
        }
    })
})