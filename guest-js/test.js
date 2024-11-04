<<<<<<< HEAD
let myname = 'Jim';
console.log(`Hello there ${myname}`);const prompt = require("prompt-sync")();

class Guest {
    constructor(date, time, name, id, plate, reason, address) {
        this.date = date;
        this.time = time;
        this.name = name;
        this.id = id;
        this.plate = plate;
        this.reason = reason;
        this.address = address;
    };

    register() {
        console.log("Please register here");

        this.date = prompt("Date: ");
        this.time = prompt("Time: ");
        // this.name = prompt("Name: ");
        // this.id = prompt("ID: ");
        // this.plate = prompt("Plate: ");
        // this.reason = prompt("Reason: ");
        // this.address = prompt("Address: ");

        // console.log(`Guest ${this.name} has been registered`);

        const toDict = {
            date: this.register.date,
            time: this.register.name,
        };

        console.log(toDict[0])

        // const id_check = parseFloat(this.id);
        // if (id_check == false || id_check.length != 12 ? "ID should be numbers only.": "ID too long or too short.") 

        // console.log(this.name);
    }
};

const g1 = new Guest().register();
// console.log(g1.register.this.name)
=======
const upperCase = (guestName) => {
    const first = guestName[0].toUpperCase();
    return upperName = first + guestName.substring(1);

};

const myname = 'jimmy';
myname.upperCase()
>>>>>>> refs/remotes/origin/master
