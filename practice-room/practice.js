

// You will need to call this makeLine() function in buildTriangle().
//
// This will be the most complicated program you've written yet, so take some time thinking through the problem before diving into the code. What tools will you need from your JavaScript tool belt? Professionals plan out their code before writing anything. Think through the steps your code will need to take and write them down in order. Then go through your list and convert each step into actual code. Good luck!
//
// Your Code:

/*
 * Programming Quiz: Build A Triangle (5-3)
 */

// creates a line of * for a given length

function makeLine(length) {
  var line = ""; //* gets pushed into here
  for (var j = 1; j <= length; j++) {
    line += "* "//stores * into the var line
  }
 return line + "\n"; // "\n" to jump to the new line
}

function buildTriangle(width){
  var triangle="";
  for (var i = 1; i <= width; i++) {
    triangle += (makeLine(i)); // this is for the length;
  }
  return triangle;
}
buildTriangle(10);

// your code goes here.  Make sure you call makeLine() in your own code.
// test your code by uncommenting the following line
console.log(buildTriangle(10));
