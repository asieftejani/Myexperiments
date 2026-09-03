alert("version 15 loading")

document.getElementById("dbForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  
  const formData = new FormData(e.target);
  
  for (const [key, value] of formData.entries()) {
    console.log(key, ":", value);
  };
  
  const response = await fetch("/dbop", {
    method: "POST",
    body: formData
  });
  
  const text = await response.text();
  
  const divChild = document.getElementById("status").querySelectorAll('p');
  
  divChild.forEach(p => {
  p.textContent = text;
  });
});



const status = document.getElementById("status");
const orgText = status.innerHTML

document.getElementById("operation").addEventListener("change", function (){

  if (this.value === "test_con"){
    document.getElementById("status").innerHTML = orgText;
  }
  else{
  const select = document.createElement("select");
  ["Create", "Read", "Update", "Delete"].forEach(optionText => {
    const option = document.createElement("option");
    option.value = optionText.toLowerCase();
    option.textContent = optionText;
    select.appendChild(option);
  });
  select.value = "read";
  status.replaceChildren(select);
  
  select.addEventListener("change", function(){
    const existing = document.getElementById("create_name");
    if (existing) existing.remove();
    
    if (this.value === "create") {
      const input = document.createElement("input");
      input.type = "text";
      input.id = "create_name";
      input.placeholder = "Enter create name";
      status.appendChild(input);
    }
  });
  }
});


fetch('https://jsonplaceholder.typicode.com/posts')
  .then((response) => response.json())
  .then((json) => console.log(json));
