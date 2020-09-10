(function () {


//profile dropdown
$(".user_link_left p,.user_link_left img").click(function(){
  $(".user_top_container").toggleClass("dn");
  $(".user_link_left p i").toggleClass("dn");

});

//Toggle admin sidebar

$(".mTitle").click(function(){
  $(this).toggleClass("active");
  $(this).siblings('ul').toggleClass("dn");
  $(this).children("i.acoc").toggleClass("dn");
});

//
$(".is_permanent").change(function() {
    if(this.checked) {
        $('.permanent_address_option').addClass('dn');
    }else{
        $('.permanent_address_option').removeClass('dn');
    }
});

 $(".is_local").change(function() {
    if(this.checked) {
        $('.local_guardian_option').removeClass('dn');
        $('.local_guardian_image').removeClass('dn');

        $('.guardian_image').removeClass('col-md-6').addClass('col-md-4');


    }else{
        $('.local_guardian_option').addClass('dn');
        $('.local_guardian_image').addClass('dn');

        $('.guardian_image').addClass('col-md-6').removeClass('col-md-4');
    }
});

// image upload

$(".imginput").on('change', function () {
        var imageiid=$(this).attr('id');
        //alert(imageiid);
        var reader = new FileReader();
        reader.onload = function(){
          var output = document.getElementById(imageiid+'_img');
          output.src = reader.result;
        };
        reader.readAsDataURL(event.target.files[0]);
  });

$(".imguploader").click(function(){
      $(this).siblings('input[type=file]').click();
});

// image upload
// muted code
//
//    $('#complain_form').submit(function(e){
//        e.preventDefault();
//        $form = $(this);
//        var formData = new FormData(this);
//
//        $.ajax({
//            url: "{% url 'frontoffice:add_complain' %}",
//            type: 'POST',
//            data: formData,
//            success: function (data) {
//                if($.isEmptyObject(data.error) ){
//
//                    if($.isEmptyObject(data.error2)){
//                        var re_url = "{% url 'frontoffice:complains' %}";
//                        printSuccess(data,re_url);
//                    }else{
//                        printErrorMsg(data.error2);
//                    }
//                }else{
//                    printErrorMsg(data.error);
//                }
//            },
//            complete:function(){
//               $('body, html').animate({scrollTop:$('form').offset().top}, 'fast');
//            },
//            cache: false,
//            contentType: false,
//            processData: false
//
//        });
//    });

//
//
//    $('#institute_form_edit').submit(function(e){
//        e.preventDefault();
//        $form = $(this)
//        var formData = new FormData(this);
//        $.ajax({
//            url: "/account/edit_institute/45",
//            type: 'POST',
//            data: formData,
//            success: function (data) {
//                if($.isEmptyObject(data.error)){
//                    printSuccess(data);
//                }else{
//                    printErrorMsg(data.error);
//                }
//            },
//            complete:function(){
//               $('body, html').animate({scrollTop:$('form').offset().top}, 'fast');
//            },
//            cache: false,
//            contentType: false,
//            processData: false
//
//        });
//    });


// muted code



})(jQuery);


//common function
function printSuccess(msg,path_redirecting) {
        $(".form_msg").html('');
        $(".form_msg").removeClass('dn alert-danger').addClass('alert-success');
        $(".form_msg").append('<p class="m0 tcap">'+msg+'</p>');
        window.setTimeout(function() {
            window.location.href = path_redirecting;
        },500);

}

 function printErrorOnly(msg) {
        $(".form_msg").html('');
        $(".form_msg").removeClass('dn');
        $(".form_msg").append('<p class="m0 tcap">'+msg+'</p>');
}

function printErrorMsg (msg) {
    $(".form_msg").html('');
    $(".form_msg").removeClass('dn');
    $.each( msg, function( key, value ) {
        if (value) {
            $(".form_msg").append('<p class="m0 tcap">'+key+' - '+value+'</p>');
            return false;
        }
    });
}
//common function



