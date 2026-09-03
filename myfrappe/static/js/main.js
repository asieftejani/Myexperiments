// This is a comment
/*
This is
a multi-line
comment
*/
let refresh = "JS loaded from alert - v105"
alert(refresh);
console.log(refresh);


function gotoPage() {
  const page = document.getElementById("routeSelect").value;
    if (page) {
      window.location.href = page;
    }
}


document.getElementById('fetchform').addEventListener('submit', async e => {
    e.preventDefault();
    console.log("This works");
    const selected = document.querySelector(
      'input[name="fchoice"]:checked');
    if(!selected) {
      alert("Please select an option");
      return;
    }
    if (selected.value === "func1") {
      const myfunc1 = document.createElement('script');
      myfunc1.src = "https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js";
      document.head.appendChild(myfunc1);
      myfunc1.onload = () => confetti();
    }
    if (selected.value === "func2") {
      let message = prompt("The message you want is:") + (' - not from html');
      console.log(message);
      alert(message);
      document.getElementById("changetext").innerHTML = message
    }
    if (selected.value === "func3") {
      console.log("Button clicked")
      const response = await fetch("/run-task",
      { method: "POST" })
      console.log("Response received: - ", response)
      const result = await response.text()
      console.log("Result received: - ", result)
      alert(result)
      document.getElementById("changetext").innerHTML = result
   }
    if (selected.value === "func4") {
      console.log("started crashing the BE");
      fetch ("/crash", {method: "POST"})
        .then(async r => {
          const data = await r.json();
        if (!r.ok) {
        alert(data.error);
        }
        })
        .catch(console.error);
    }
    if (selected.value === "func5") {
      fetch("https://jsonplaceholder.typicode.com/users")
        .then(response => response.json())
        .then(users => {
          let index = 0;
          const timer = setInterval( () => {
            document.getElementById("changetext").innerHTML = 
            `<p>${users[index].address.street}</p>`;
            index++;
            if (index >= users.length) {
              clearInterval(timer);
            }
          }, 1000);
        })
    }
})


window.onload = function() {
    const now = new Date();

    // Format as YYYY-MM-DDTHH:MM
    const local = new Date(now.getTime() - now.getTimezoneOffset() * 60000)
        .toISOString()
        .slice(0, 16);

    document.getElementById("dtstamp").value = local;
};

fetch("/read-files")
      .then(r => r.text())
      .then(text => {
        document.getElementById('editor').value = text;
      });
