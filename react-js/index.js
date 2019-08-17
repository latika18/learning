//function
function Holiday(destination, days) {
	this.destination = destination
	this.days = days

}

Holiday.prototype.info = function() {
	console.log(this.destination+"|"+this.days+'days');
}
var Nepal = new Holiday('Nepal',30)
console.log(Nepal.info())

//super clas
class Holidays {
     constructor(destination, days){
     	this.destination = destination;
     	this.days = days;
     }
     info(){
     	console.log(this.destination + "will take"+ this.days +"days.")
     }
 }

//sub class
class Expedition extends Holidays {
	constructor(destination,days,gear){
		super(destination,days);
		this.gear = gear;
	}
	info() {
		super.info();
		console.log("Bring your "+this.gear.join(' and your '));

	}

}

const tripWithGear = new Expedition('Everest',30,['Sunglasses','Flags','Camera']);
tripWithGear.info();
