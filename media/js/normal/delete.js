$('[rel="file_delete"]').click(function(){
  
  var nid = $(this).attr("nid");
  var fid = $(this).attr("fid");
  Dajaxice.normal.FileDeleteConsistence(file_delete_callback,
                                        {'nid':nid, 'fid':fid});
});

function file_delete_callback(data){
  if(data.is_deleted === true){
      var fid = "tr[id=" + data.fid +"]";
      console.log("successs!");
      console.log(data.message);
      console.log(fid);
      $(fid).remove();
    }
  else{
      console.log("Failed!");
      console.log(data.message);
      $("div#delete-error-panel").show();
      $("p#delete-message").text(data.message);

  }
}
