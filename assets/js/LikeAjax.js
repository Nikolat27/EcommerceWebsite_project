function like(slug, id) {
    let element = document.getElementById("like")
    let count = document.getElementById("count")
    // let like_count = document.getElementById("liked-products")

    $.get(`/products/like/${slug}/${id}`).then(response => {
        if (response['response'] === "liked") {
            element.className = "bi bi-heart-fill"
            count.innerText = Number(count.innerText) + 1
            // like_count.innerText = response.likedproducts

        } else {
            element.className = "bi bi-heart"
            count.innerText = Number(count.innerText) - 1
            // like_count.innerText = response.likedproducts
        }
    })
}