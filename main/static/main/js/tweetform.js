$(function(){
    var countMax = 140;
    $('#id_content').bind('keydown keyup keypress change',function(){
        var thisValueLength = $(this).val().length;
        var countDown = (countMax)-(thisValueLength);
        $('.count').html(countDown);
 
    });
    $(window).on('load',function(){
        $('.count').html(countMax);
    });

    $('input[type=file]').before('<span id="preview_area"></span>');
    // アップロードするファイルを選択
    $('input[type=file]').change(function() {
      var file = $(this).prop('files')[0];
  
      // 画像以外は処理を停止
      if (! file.type.match('image.*')) {
        // クリア
        $(this).val('');
        $('span').html('');
        return;
      }
  
      // 画像表示
      var reader = new FileReader();
      reader.onload = function() {
        var img_src = $('<img>').attr({
            'src': reader.result,
            'width': '100'
        });
        $('#preview_area').html(img_src);
      }
      reader.readAsDataURL(file);
    });
    //ファイルアップロードの画像変更
    // $('input[type=file]').wrap('<label for="id_image" />');
    // $('input[type=file]').before(
    //     '<img src="/media/icon/button/fileupload.png" height="50" />'
    // );

});