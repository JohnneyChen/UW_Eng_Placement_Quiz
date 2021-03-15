//not ideal logic, please improve click handling on drag events if possible

let drag = false; //declares a variable to store if user is dragging or not

document.addEventListener(
    'mousedown', () => drag = false);

//when mouse moves, dragging is set to true
document.addEventListener(
    'mousemove', () => drag = true);

//after mouse is released, dragging is set back to false after 10ms just to prevent trigger of click events
document.addEventListener(
    'mouseup', () => setTimeout(() => drag = false, 10));