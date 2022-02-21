// add js to listen to the search form to query the database

let likeButtons = document.querySelectorAll(".like"),
    csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0];

    
    // const axios_config = {
        // }
        
function handleLikeEvent(event){
    let bookId, url, headers;
    
    bookId = event.target.id 
    bookId = bookId.split("-")[1]
    console.log(bookId);
    
    url = "http://127.0.0.1:8000/like/" + bookId
    
    headers = {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken.value
        },
    axios.post(url, {}, {headers: headers, xsrfHeaderName: 'x-CSRFToken'})
    
    .then(response=>{
        console.log(response);
      const isLiked = response.data.isLiked
      const likeButton = document.querySelector(`#like-${bookId}`)
      const likeCount = document.querySelector(`#like-count-${bookId}`)

      likeCount.innerHTML = response.data.likeCount

      if(isLiked){
        likeButton.classList.remove("far")
        likeButton.classList.add("fas", "text-danger")
      }else{
        likeButton.classList.remove("fas", "text-danger")
        likeButton.classList.add("far")
      }
    })
    // .cath(error => console.log(error))
}

likeButtons.forEach(likeButton=>
  likeButton.addEventListener("click", handleLikeEvent)
);
