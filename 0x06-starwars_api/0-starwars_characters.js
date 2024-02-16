#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

function fetchCharacter (characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, function (error, response, body) {
      if (!error && response.statusCode === 200) {
        const character = JSON.parse(body);
        resolve(character.name);
      } else {
        reject(error || `Failed to fetch character from ${characterUrl}`);
      }
    });
  });
}

request(url, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode === 404) {
    console.error('Error: Movie not found (404)');
  } else if (response.statusCode !== 200) {
    console.error('Error: Unexpected response:', response.statusCode);
  } else {
    const film = JSON.parse(body);
    if (film && film.characters && Array.isArray(film.characters)) {
      const promises = film.characters.map(characterUrl => fetchCharacter(characterUrl));
      Promise.all(promises)
        .then(characters => {
          characters.forEach(characterName => console.log(characterName));
        })
        .catch(err => {
          console.error('Error fetching characters:', err);
        });
    } else {
      console.error('Invalid film data:', film);
    }
  }
});
