console.log('version 1.0.0'); // log version to console
const secret = 'forty'; // the secret word

const input = document.getElementById('input');
const submitBtn = document.getElementById('submit');
const hintsTable = document.getElementById('hints');

submitBtn.addEventListener('click', () => {
    hintsTable.innerHTML = ''; // clear previous hints

    for (let i = 0; i < input.value.length; i++) {
    const letter = input.value[i];
    const cell = document.createElement('td');
    cell.textContent = letter;

    if (secret.indexOf(letter) === i) {
        // letter is in correct spot
        cell.style.outline = '2px solid green';
        cell.style.backgroundColor = 'lightgreen';
    } else if (secret.includes(letter)) {
        // letter is in word but wrong spot
        cell.style.outline = '2px solid yellow';
    }

    hintsTable.appendChild(cell);
    if (input.value === secret) {
        alert('You got it!');
    }
    }

});