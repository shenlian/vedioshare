function my_js(){
	alert("js enter");
	Dajaxice.home.dajaxice_example(my_js_callback);
}

function my_js_callback(data){
		alert(data.message);
}
$("#show").click(function(){
	alert("hahha");
	$("#myModal").modal("show");
})
$("#hide").click(function(){
	alert("hahha");
	$("#myModal").modal("hide");
})
