var message = "Hello";
var interval = Math.random();
var count = Math.floor(Math.random() * 100) + 1;
var notify = count;
var i = 0;
var timer = setInterval(function(){
	document.getElementsByClassName('composer_rich_textarea')[0].innerHTML = message;
	$('.im_submit').trigger('mousedown');
	i++;
	if(i == count)
	clearInterval(timer);
	if(i % notify == 0)
	console.log(i + ' MESSAGES SENT');
} , interval * 1000 );

