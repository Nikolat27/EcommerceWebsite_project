function remove_from_cart(id) {
    $.get(`/cart/remove_from_cart/${id}/`).then(response => {
        if (response.bool === true) {
            console.log("product has deleted successfully")
            $(".base_page_cart").html(response.data)
            $("#len1").text(response.len)
            $("#len2").text(response.len)
        }
    })
}
