let tasks = document.querySelector('.tasks');
let inputText = document.querySelector('.input-field');
let addButton = document.querySelector('.add-button');

function addTask(){
  // console.log("ok")
  if(inputText.value != null){

    let div = document.createElement("div");
    div.className="task";

    // console.log(div);
    let label = document.createElement("label");
    label.className = "task-new";

    let check = document.createElement("input");
    check.type = "checkbox";
    check.className = "task-checkbox";

    let span = document.createElement("span");
    span.innerHTML = inputText.value;
    // console.log(span.innerHTML)

    let image = document.createElement("img");
    image.className = "delete-img";
    image.src = "https://icons-for-free.com/iconfiles/png/512/delete+remove+trash+trash+bin+trash+can+icon-1320073117929397588.png";
    image.addEventListener('click', remove);

    tasks.appendChild(div);
    div.appendChild(label);
    label.appendChild(check);
    label.appendChild(span);
    div.appendChild(image);

    inputText.value = null;
  }
}

function remove(){
  this.parentNode.remove();
}

function clearAll(){
  deleteImage[0].addEventListener('click', remove);
}

function clearAllTasks(){
  // let btn = document.getElementById('.clear-button');
  tasks.remove();
}

clearAll();
