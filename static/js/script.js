player_name = prompt("enter your name");
alert("Hello " + player_name);
player_guess = prompt("lets play rock paper scissors");
computer_guess = randominteger(1, 3);
if (player_guess == computer_guess) {
  document.getElementById("user_feedback").innerHTML =
    "<em>Correct, you win</em>";
} else {
  document.getElementById("user_feedback").innerHTML = "incorrect, you lose";
}

function randominteger(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min);
}
