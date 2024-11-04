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

    // Make sure first letter of name is capitalized. Have not tested for more than one word/name.
    upperCase() {
        const ask = prompt("Name: ");
        const first = ask[0].toUpperCase();
        return first + ask.substring(1);
    };

    // transform info above into object, pushed into array
    toDict() {
        const toJson = [];
        const values = [this.date, this.time, this.name, this.id, this.plate, this.reason, this.address];
        const [The_Date, Time, Name, ID, Plate, Reason, Address] = values;
        const dicted = {The_Date, Time, Name, ID, Plate, Reason, Address}
        toJson.push(dicted);
        console.log(`Guest ${Name} arrived at ${Time} on ${The_Date}.`);
    };

    // IdCheck
    idCheck(guest_id) {
        const id_check = parseFloat(guest_id);
        if (id_check == false) {
            throw new Error('wrong');
        } else if (id_check.toString().length != 12) {
            // console.log(id_check.toString().length);
            throw new Error('Id too short');
        };
    };

    // Main register function
    register() {
        try{
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
            
            // check if id is valid
            this.idCheck(this.id);

            // if valid, data transformed into obj
            this.toDict();

        } catch (error) {
            console.log(error)
        }

        // console.log(`Guest ${this.name} has been registered on ${this.date} at ${this.time}.`);
        // console.log(toJson[0].Reason)


        // console.log(this.name);
    }
};

const g = new Guest().register();