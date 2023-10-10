$("#add-to-cart-form-1").submit(function (e) {
    e.preventDefault();
    let button = $("#add-to-cart-btn-1");
    $.ajax({
        data: $(this).serialize(),
        method: $(this).attr('method'),
        url: $(this).attr('action'),
        dataType: "json",

        beforeSend: function () {
            button.html("در حال اضافه به سبد خرید");
            console.log("adding to cart...");
        },
        success: function (response) {
            console.log("success!");
            if (response.bool === true) {
                setTimeout(() => button.html("اضافه شد!"), 700);
                setTimeout(() => button.html(""), 1500);
                $("#cart-details").html(response.data)
                $("#totalcartitems").text(response.totalcartitems)
            }
        }
    })
})