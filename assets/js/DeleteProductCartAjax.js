$("#delete-product-form").submit(function (e) {
    e.preventDefault();
    $.ajax({
        data: $(this).serialize(),
        method: $(this).attr('method'),
        url: $(this).attr('action'),
        dataType: "json",

        beforeSend: function () {
            console.log("deleting");
        },
        success: function (response) {
            console.log("success!");
            if (response.bool === true) {
                $("#cart-details").html(response.data)
                $("#totalcartitems").text(response.totalcartitems)
            }
        }
    })
})