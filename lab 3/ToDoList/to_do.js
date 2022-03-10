let tasks = document.querySelector('.tasks');
let input = document.querySelector('.NewTask');
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

    let copiedItem = document.createElement("div");
    copiedItem.addEventListener('click', copyItem(div, label, check, span, image, copiedItem));


    tasks.appendChild(div);
    div.appendChild(label);
    label.appendChild(check);
    label.appendChild(span);
    div.appendChild(image);

    input.value = null;
  }
}

function copyItem(div, label, check, span, image){
  this.div = div;
  div.className = "task";

  this.label = label;
  label.className = "task-new";

  this.check = check;
  check.type = "checkbox";
  check.className = "task-checkbox";

  this.span = span;
  span.innerHTML = span.value;

  this.image = image;
  image.className = "bin";
  image.src = "bin.png";
  image.addEventListener('click', remove);


}


function remove() {
  this.parentNode.remove();
}

function clearAll(){
  deleteImage[0].addEventListener('click', remove);
}

clearAll();

