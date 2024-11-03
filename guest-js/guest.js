const prompt = require("prompt-sync")();

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

    upperCase() {
        const ask = prompt("Name: ");
        const first = ask[0].toUpperCase();
        return first + ask.substring(1);

    };

    register() {
        const currDate = new Date();
        const whichAmPm = (currDate.getHours() >= 12) ? 'PM':'AM';

        console.log("Please register here.");

        this.date = `${currDate.getDate()}/${currDate.getMonth() + 1}/${currDate.getFullYear()}`;
        this.time = `${currDate.getHours()}:${currDate.getMinutes()} ${whichAmPm}`;
        this.name = this.upperCase();
        this.id = prompt("ID: ");
        this.plate = prompt("Plate: ").toUpperCase();
        this.reason = prompt("Reason: ");
        this.address = prompt("Address: ");

        console.log(`Guest ${this.name} has been registered on ${this.date} at ${this.time}.`);

        // const id_check = parseFloat(this.id);
        // if (id_check == false || id_check.length != 12 ? "ID should be numbers only.": "ID too long or too short.") 

        // console.log(this.name);
    }
};

const g = new Guest().register();