// This is HW 1
const crypto = require('crypto');

function change (amount) {
	if (amount < 0){
	throw new RangeError (' amount cannot be negative') ;
	}

	const result = [];
	let remaining = amount;
	[25,10,5,1].forEach((coin) => {
	result.push(Math.floor(remaining / coin));
	remaining %= coin ;
	});
	return result;
};

function stripQuotes(str) {
  let final = str.replace(/'/g, '');
  final = final.replace(/"/g, '');
  return final;
}

function scramble (word) {
	if (word.length === 0) {
		return '';
	}
	let newPermutations = Math.floor(Math.random() * word.length);
	let findRandom = word.charAt(newPermutations);
	let newword = (word.slice(0, newPermutations) + (word.slice(newPermutations +1, word.length)));
	return findRandom + scramble(newword);
};
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
	
module.exports = {
	change, stripQuotes, scramble, powers, powersGenerator, interleave,makeCryptoFunctions,
};
