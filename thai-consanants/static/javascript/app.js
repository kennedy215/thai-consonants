// function changeText(idElement) {
//     var element = document.getElementById('element' + idElement);
//     if (idElement === 1 || idElement === 2) {
//         if (element.innerHTML === 'Chicken') element.innerHTML = 'click';
//         else {
//             element.innerHTML = 'ก';
//         }
//     }
// }


function changeText(idElement) {
    var element = document.getElementById('element' + idElement);
    if (idElement === 1 || idElement === 2) {
        if (element.innerHTML === 'Chicken') element.innerHTML = 'ก';
        if(element.innerHTML === 'ก') element.innerHTML = 'Chicken'
      }else{
        console.log("no no no")
      }
    }
