var Firebase = require("firebase");
var fs = require('fs');

var gpio = {
    first: "gpio19",
    second: "gpio19"
};

// make sure the gpio is setup to turn the led on and off
//fs.writeFile("/sys/class/gpio/export", "415", function(err) {});
//fs.writeFile("/sys/class/gpio/gpio415/direction", "out", function(err) {});
//fs.writeFile("/sys/class/gpio/export", "414", function(err) {});
//fs.writeFile("/sys/class/gpio/gpio414/direction", "out", function(err) {});

var myFirebaseRef = new Firebase("https://cxapi-c8d4d.firebaseio.com/");
myFirebaseRef.set({
    lights: {
        first: true,
        second: true
    }
});

myFirebaseRef.child("lights").on("value", function(snapshot) {
    updateLights(snapshot.val());
});

function updateLights(lights) {
    for (var key in lights) {
        if (lights.hasOwnProperty(key)) {
            if(lights[key]) {
                fs.writeFile("/sys/class/gpio/"+gpio[key]+"/value", "1", function(err) {});
            } else {
                fs.writeFile("/sys/class/gpio/"+gpio[key]+"/value", "0", function(err) {});
            }
        }
    }
}