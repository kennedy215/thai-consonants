// function changeText(idElement) {
//     var element = document.getElementById('element' + idElement);
//     if (idElement === 1 || idElement === 2) {
//         if (element.innerHTML === 'Chicken') element.innerHTML = 'click';
//         else {
//             element.innerHTML = 'ก';
//         }
//     }
// }


var today = new Date();
var hourNow = today.getHours();
var greeting;

if (hourNow > 18) {
    greeting = 'Good evening!';
} else if (hourNow > 12) {
    greeting = 'Good afternoon!';
} else if (hourNow > 0){
    greeting = 'Good morning!';
} else {
    greeting = 'Welcome!';
}

document.write('<h3>' + greeting + '<h3>');
