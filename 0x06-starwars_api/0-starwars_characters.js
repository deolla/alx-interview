#!/usr/bin/node
// A script that prints all characters of a Star Wars movie.
const util = require('util');
const requestPromise = util.promisify(require('request'));
const movieID = process.argv[2];

async function starWarsCharacters (filmId) {
  const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + filmId;
  let apiResponse = await (await requestPromise(apiUrl)).body;
  apiResponse = JSON.parse(apiResponse);
  const charactersList = apiResponse.characters;

  for (let i = 0; i < charactersList.length; i++) {
    const urlCharacter = charactersList[i];
    let characterDetails = await (await requestPromise(urlCharacter)).body;
    characterDetails = JSON.parse(characterDetails);
    console.log(characterDetails.name);
  }
}

starWarsCharacters(movieID);
