#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.log('Usage: ./starwars_characters.js <Film ID>');
  process.exit(1);
}

const filmId = process.argv[2];
const filmURL = `https://swapi.dev/api/films/${filmId}/`;

request(filmURL, { json: true }, (err, res, body) => {
  if (err) {
    throw new Error('Error requising film information');
  }
  const charactersPromises = body.characters.map(link => {
    return new Promise((resolve, reject) => {
      request(link, { json: true }, (err, res, body) => {
        if (err || res.statusCode !== 200) {
          throw new Error('Error fetching link: ' + link);
        }
        resolve(body.name);
      });
    });
  });

  Promise.all(charactersPromises)
    .then(names => {
      names.forEach(name => console.log(name));
    });
});
