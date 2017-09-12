// This is HW 1

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
	//const newMath = 0;
	for (let i = 0; base ** i <= limit; i += 1) {
    const input = base ** i;
    yield input;
}
}

	
module.exports = {
	change, scramble, powers, powersGenerator,
};
