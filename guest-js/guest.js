const prompt = require("prompt-sync")();
const data = require("./guest.json");
const fs = require("fs");
const filepath = "./guest.json";

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

        // const jsonString = JSON.stringify(toJson);

        fs.writeFile(filepath, JSON.stringify(toJson), err => {
            if (err) {
                console.log(err);
            } else {
                console.log('Success');
            }
        })

        // console.log(`Guest ${Name} arrived at ${Time} on ${The_Date}.`);
        // console.log(jsonString);
        return toJson;
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

    // load JSON file
    reading = (filepath) => {
        fs.readFile(filepath, 'utf-8', (err, jsonString) => {
            if (err) {
                console.log(err);
            } else {
                try {
                    const read_data = JSON.parse(jsonString);
                    console.log(read_data);
                } catch {
                    console.log(err)
                }
            }
        });
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
            const transposed = this.toDict();

        } catch (error) {
            console.log(error)
        }
    }
};

const g = new Guest().register();