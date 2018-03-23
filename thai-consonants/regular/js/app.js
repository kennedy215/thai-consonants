// var magic = [];
//
// function timeNow(string){
//   var today = new Date();
//   var hourNow = today.getHours();
//   var minuteNow = today.getMinutes();
//   var greeting = " ";
//
//   if (hourNow > 18) {
//       greeting = '<h3>'+'Good evening!'+'<h3>';
//   } else if (hourNow > 12) {
//       greeting = '<h3>'+'Good afternoon! '+'</h3>';
//   } else if (hourNow > 0) {
//       greeting = '<h3> '+'Good morning!'+'</h3>';
//   } else {
//       greeting = '<h3> '+'Welcome!' +'</h3>';
//   }
//   document.write(greeting +" ");
// }
//
// function welcomeW(name){
//     document.write("Welcome " + name + "!");
// }


function thaiAlpha(english,character,spelling,sound,tone,order){
  this.english = english;
  this.character = character;
  this.spelling = spelling;
  this.sound = sound;
  this.tone = tone;
  this.order = order;

};

var thaiAlphabet=[];
var thaiAlphabetTracking=[];


allList = [];

// The loop allows me to pull out the keys with extractIt
function takeValues(){
  var chickenThai = new thaiAlpha('chicken','ก','ก ไก','k/k','mid',1);
    allList.push(chickenThai);
    return allList 
  var eggThai = new thaiAlpha('egg','ข','ข ไข่','kh/k','high',2);
    allList.push(eggThai);
  var bottleThai = new thaiAlpha('bottle','ฃ','ฃ ฃวด','kh/k','high',3);
    allList.push(bottleThai);


    console.log(allList);
}



    console.log(thaiAlphabet)







  // for(var key in chickenThai){
  //   return key;
  // }

// var detail = chickenThai.name;
// console.log(chickenThai.tone)
//


//
// console.log(chickenThai)
// var person = new Person("Jane");
//    for(var key in person) {
//        console.log(key);
//    }



//
// var alphaOrder = {
//   lowTone:[chickenThai, eggThai],
//
//   midTone: [],
//   highTone: [bottleThai, eggThai],
// };



// function extractItNow(gogo){
//   var extractIt = alphaOrder.lowTone;
//   return extractIt.chickenThai;
// }
//
// console.log(extractItNow())


//
// var obj = { first: "John", last: "Doe" };
//    // Visit non-inherited enumerable keys
//    Object.keys(obj).forEach(function(key) {
//        console.log(key);
//    });
//

// var obj = { first: "John", last: "Doe" };
//    // Visit non-inherited enumerable keys
//    Object.keys(obj).forEach(function(key) {
//        console.log(key);
//    });




// var extractIt = alphaOrder.lowTone.chickenThai;
// console.log(extractIt)
//







// console.log(alphaOrder.highTone);

// for (var key in alphaOrder) {
//   var check = alphaOrder["lowTone"]
// }
//
// console.log(alphaOrder.lowTone);
//
//
// var dictionary = {
//     a: [1,2,3, 4],
//     b:[5,6,7]
// }
// var values = Object.keys(dictionary).map(function(key){
//     return dictionary[key];
// });
//will return [[1,2,3,4], [5,6,7]]





// function runThrough(){
//   for (i = 0;)
// }
