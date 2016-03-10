$(document).ready(function(){
	"uses strict";

	function makeid(){
		var text = "";
		var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

		for( var i=0; i < 32; i++ )
			text += possible.charAt(Math.floor(Math.random() * possible.length));

		return text;
}

	function attachHandlers(){
		$("#makeTwitter").on("click", function(){
			var text = makeid();
			var appKey = "vzbqdzbtpCKoa5dbHw1JGwv2i";
			alert("Making a twitter post, my ass!");
			alert(text);
		});
	}

	attachHandlers();
});