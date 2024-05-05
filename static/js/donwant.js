var point = "Karthik: good boy";

var regex = /^(\w+): (.+)$/;

var match = regex.exec(point);

if (match) {
  var name = match[1]; // Contains "Karthik:"
  var message = match[2]; // Contains "good boy"

  console.log("Name:", name);
  console.log("Message:", message);
} else {
  console.log("No match found.");
}
