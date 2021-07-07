
$('input[type="file"]').change(function(e){
        var fileName = e.target.files[0].name;
        $('.custom-file-label').html(fileName);
    });

$('#but_upload_lane').click(function (event) {
    event.preventDefault();
    var fd = new FormData();
    var files = $('#file')[0].files[0];
    fd.append('file',files);
   debugger;
  $.post({
    type: "POST",
    url: "http://127.0.0.1:5000/uploadlaneinputimage",
    data: fd,
      contentType: false,
      processData: false,
    success: function(response){
       if(response != 0){
                    $("#obj_resultedimage").attr("src",'static/images/' + response.obj_result_imagePath);
                    $("#resultedimage").attr("src",'static/images/' + response.imagePath);
                }else{
                    alert('Error:file not uploaded');
                }
    },
  });
    return false;
});


$('#but_upload_sign').click(function (event) {
    event.preventDefault();
    var fd = new FormData();
    var files = $('#file')[0].files[0];
    fd.append('file',files);
   debugger;
  $.post({
    type: "POST",
    url: "http://127.0.0.1:5000/uploadsigninputimage",
    data: fd,
      contentType: false,
      processData: false,
    success: function(response){
       if(response != 0){
                    $("#resultedimage").attr("src",'static/sign_input/' + response.imagePath);
                    $("#sign_result").text(response.identifiedSign);
                }else{
                    alert('Error:file not uploaded');
                }
    },
  });
    return false;
});