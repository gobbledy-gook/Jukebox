const fetchB = document.querySelector("#fetch")
const submitB = document.querySelector("#submit")


submitB.onclick = () => {
        let table = document.getElementsByClassName("result")[0];
        table.style.display = "block";
        // console.log(text1)
        // fetch(text1);
    }

// fetchB.onclick = () => {
//     let text1 = document.getElementById("A").value;
//     console.log(text1)
//     fetch(text1);
// }



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


function askQuestion(question) {
    let data = { quest: question};
    fetch("http://127.0.0.1:5000/ask-question", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
    .then((res) => {
      return res.json();
    })
    .then((json) => {
      console.log("Response JSON:", json.answer);
      var answerDiv = document.getElementById("Answer");
      answerDiv.style.display = "block";
      answerDiv.innerHTML = json.answer;
    })
    .catch((error) => { });
  }
