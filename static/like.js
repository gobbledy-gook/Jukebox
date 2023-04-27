const likeButtons = document.getElementsByClassName("likeButton");

for(btn in likeButtons){
    btn.addEventListener('click', addLike(btn));    
}

function addLike(btn){
    // const inputArea = document.
}