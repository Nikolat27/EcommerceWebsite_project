// function like(slug, id) {
//     let element = document.getElementById(slug)
//     let count = document.getElementById("count")
//     // let like_count = document.getElementById("liked-products")
//
//     $.get(`/products/like/${slug}/${id}`).then(response => {
//         if (response['response'] === "liked") {
//             element.className = "bi bi-heart-fill"
//             count.innerText = Number(count.innerText) + 1
//             // like_count.innerText = response.likedproducts
//
//         } else {
//             element.className = "bi bi-heart"
//             count.innerText = Number(count.innerText) - 1
//             // like_count.innerText = response.likedproducts
//         }
//     })
// }
function like(slug, id) {
    let element = document.getElementById(slug)
    let count = document.getElementById("count")
    // let like_count = document.getElementById("liked-products")

    $.get(`/products/post_like/${slug}/${id}`).then(response => {
        console.log("Product liked!");
        if (response['response'] === "liked") {
            element.className = "bi bi-heart-fill"
            count.innerText = Number(count.innerText) + 1
            // like_count.innerText = response.likedproducts

        } else {
            console.log("Product Dis Liked!");
            element.className = "bi bi-heart"
            count.innerText = Number(count.innerText) - 1
            // like_count.innerText = response.likedproducts
        }
    })
}