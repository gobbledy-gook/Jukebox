const fetchB = document.querySelector("#fetch")

fetchB.onclick = () => {
    let text1 = document.getElementById("A").value;
    console.log(text1)
    fetch(text1);
}

// function fetch(text){
//     let text1 = {data : text}
//     console.log(text);
//     fetch("http://127.0.0.1:5000/fetch", {
//     method: "POST",
//     headers: {
//         "Content-Type": "application/json",
//       },
//     body: JSON.stringify(text),
//     });
// }

