// This is homework 1
const rp = require('request-promise');
const crypto = require('crypto');

function change(cents) {
  if (cents < 0) {
    throw new RangeError('amount cannot be negative');
  }
  const result = [];
  let remaining = cents;
  function calc(coin) {
    result.push(Math.floor(remaining / coin));
    remaining %= coin;
  }
  [25, 10, 5, 1].forEach(calc);
  return result;
}

function stripQuotes(str) {
  let final = str.replace(/'/g, '');
  final = final.replace(/"/g, '');
  return final;
}

function scramble(word) {
  if (word.length === 0) {
    return '';
  }
  const newPermutations = Math.floor(Math.random() * word.length);
  const findRandom = word.charAt(newPermutations);
  const newword = (word.slice(0, newPermutations) + (word.slice(newPermutations + 1, word.length)));
  return findRandom + scramble(newword);
}

function powers(base, limit, callback) {
  for (let i = 0; base ** i <= limit; i += 1) {
    const input = base ** i;
    callback(input);
  }
}
function* powersGenerator(base, limit) {
  for (let i = 0; base ** i <= limit; i += 1) {
    const input = base ** i;
    yield input;
}
}
// Thanks @Joey for guidance on this one.
function say(word) {
  if (!word) {
    return '';
  }
  return function phraser(other) {
    if (!other) {
      return word;
    }
    return say(`${word} ${other}`);
  };
}
function interleave(...args){
  let r = args.shift();
  let newr = args;
  let rest = [];
  if (r.length === 0){
    return newr;
  } else if (newr.length ===0) {
    return r;
  } else {
    while (r.length !== 0 && newr.length !==0) {
      rest.push(r.shift());
      rest.push(newr.shift());
      if (r.length === 0) {
        return rest.concat(newr);
      } else if (newr.length === 0) {
      return rest.concat(r);
      }
   }
  }
}
// Thanks to Justin Torres for help with getters
function cylinder(spec) {
  let { radius, height } = spec;
  if (!radius) { radius = 1; }
  if (!height) { height = 1; }
  const surfaceArea = () => (2 * Math.PI * radius * height) + (2 * Math.PI * (radius ** 2));
  const volume = () => (Math.PI * (radius ** 2) * height);
  const stretch = (factor) => { height *= factor; };
  const widen = (factor) => { radius *= factor; };
  const toString = () => `cylinder with radius ${radius} and height ${height}`;

  return Object.freeze({
    volume,
    surfaceArea,
    widen,
    stretch,
    toString,
    get radius() { return radius; },
    get height() { return height; },
  });
}
function makeCryptoFunctions(password, algorithm){
  const localPass = password;
  const localAlg = algorithm;
  return [
    function encrypt(text){

      let cipher = crypto.createCipher(localAlg,localPass);
      let crypt = cipher.update(text,'utf8','hex');
      crypt += cipher.final('hex');
      return crypt;
    },
   
    function decrypt(text){
      let decipher = crypto.createDecipher(localAlg,localPass);
      let decry = decipher.update(text,'hex','utf8');
      decry += decipher.final('utf8');
      return decry;
    }
  ];
}

function randomName(spec) {
  // Get the parameters
  const { gender, region } = spec;
  const options = {
    uri: 'http://uinames.com/api/',
    qs: {
      amount: 1,
      gender,
      region,
    },
    json: true, // Automatically parses the JSON string in the response
  };

  return rp(options)
    .then(({ surname, name }) => `${surname}, ${name}`);
}

module.exports = {
  change,
  stripQuotes,
  scramble,
  powers,
  powersGenerator,
  say,
  interleave,
  makeCryptoFunctions,
  cylinder,
  randomName,
};
