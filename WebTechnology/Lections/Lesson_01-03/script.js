let year = prompt('What year is it now')
if (year == 2022) {
    alert('You are rigth');
} else {
    alert('It is not true'); // if year not 2022
}

let accessAllowed = (age > 18) ? true : false;     //short write

let i = 0;
while (i < 3) { //output 0, after 1, after 2
    alert(i);
    i++
}

let j = 0;
do {
    alert(j);
    j++;
} while (j < 3);

for (let i = 0; i < 3; i++) { //output 0; after 1; after 2
    alert(i);
}

let a = 2 + 2;
switch (a) {
    case 3:
        alert('Need more');
        break;
    case 4:
        alert('bingo!');
        break;
    case 5:
        alert('too much');
        break;
    default:
        alert('you are stupid');
}

function showMessage() {
    alert('Everyone hi');
}
showMessage();
showMessage();