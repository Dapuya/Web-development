let tasks = document.querySelector('.items');
let input = document.querySelector('.input');
let addbutton = document.querySelector('.Add');

let task = document.querySelectorAll('.task');
let deleteImage = document.querySelectorAll('.bin');

function newTask(){
  if(input.value != null){
    let div = document.createElement("div");
    div.className = "task";

    let label = document.createElement("label");
    label.className = "task-new";

    let check = document.createElement("input");
    check.type = "checkbox";
    check.className = "task-checkbox";

    let span = document.createElement("span");
    span.innerHTML = input.value;

    let image = document.createElement("img");
    image.className = "bin";
    image.src = "bin.png";
    image.addEventListener('click', remove);

    tasks.appendChild(div);
    div.appendChild(label);
    label.appendChild(check);
    label.appendChild(span);
    div.appendChild(image);

    input.value = null;
  }
}

function remove(){
  this.parentNode.remove();
}

function clearAll(){
  deleteImage[0].addEventListener('click', remove);
}

clearAll();

