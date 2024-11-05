const prompt = require("prompt-sync")();
const data = require("./guest.json");
const fs = require("fs");
const filepath = "./guest.json";

const reading = () => {
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

const testing = reading(filepath);