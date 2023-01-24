const texts =['I am a Technopath','We are providing projects','i am not a robot'];
let count = 0;
let index = 0;
let currentText = '';
let letter = '';
( function fun(){

	if (count === texts.length){

		count = 0
	}
	currentText = texts[count];
	letter = currentText.slice(0, ++index);
	document.querySelector('.typing').textContent=letter;
	if(letter.length === currentText.length)
	{
		count++;
		index=0;

	}
	setTimeout(fun, 200);
}());

function textContentprint(event){
	console.log(event)
}

