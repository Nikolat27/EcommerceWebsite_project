function add_to_cart_store(id) {
    $.get(`/cart/cart_add_store/${id}/`).then(response => {
        if (response.bool === true) {
            $("#base_page_cart").html(response.data)
            // len1 is for computer template, len2 is for mobile
            $("#len1").text(response.len)
            $("#len2").text(response.len)
        }
    })
}