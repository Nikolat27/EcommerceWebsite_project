function like(slug, id) {
    let element = document.getElementById(slug)
    let count = document.getElementById("count")

    $.get(`/products/like/${slug}/${id}/`).then(response => {
        console.log("Product liked!");
        if (response['response'] === "liked") {
            element.className = "bi bi-heart-fill"
            count.innerText = Number(count.innerText) + 1

        } else {
            console.log("Product Disliked!");
            element.className = "bi bi-heart"
            count.innerText = Number(count.innerText) - 1
        }
    })
}