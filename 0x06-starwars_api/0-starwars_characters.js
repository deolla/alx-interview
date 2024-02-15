#!/usr/bin/node
// A script that prints all characters of a Star Wars movie
const request = require("request");
const url = "https://swapi-api.alx-tools.com/api/films/" + process.argv[2];

request(url, async function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    console.log("Response Body:", body); // Add this line for debugging

    try {
      const characters = JSON.parse(body).characters;
      for (const character of characters) {
        await new Promise((resolve, reject) => {
          request(character, function (error, response, body) {
            if (error) {
              console.error(error);
              reject(error);
            } else {
              try {
                console.log(JSON.parse(body).name);
              } catch (parseError) {
                console.error(parseError);
              }
              resolve();
            }
          });
        });
      }
    } catch (parseError) {
      console.error(parseError);
    }
  }
});
