// $('.card_list_footer').click( function() {
//     $('div[name=div_create_card'+this.id+']').show();
//     $('#title'+this.id).focus();
//     $('div[name=card_list_footer'+this.id+']').hide()
// });
//
// $('button[name="btn_cancel"]').click( function() {
//     $('div[name=div_create_cardlist'+this.id+']').hide();
//     $('div[name=card_list_footer'+this.id+']').show();
// });
//
// $('.card_list_new').click( function() {
//     var id = $('.card_list_new').attr('name');
//     $('#div_create_cardlist'+id).show();
//     $('.card_list_new').hide();
//
//     $('#card_list_add').css('height', '90px');
//     $('#div_create_cardlist'+id).css('height', '90px');
//     $('#div_create_cardlist'+id).css('line-height', '90px');
// })



// 초기화
$( function() {



    // $('.card_list').sortable({
    //     connectWith: '.card_list',
    //     update: function(event, div) {
    //         var order = $(this).sortable('toArray');
    //         var data = {
    //             list_id: $(this).data('list_id'),
    //             positions: order.join(';')
    //         }
    //
    //         $.ajax({
    //             type: "POST",
    //             url: '/contents/dashboard/card/update/'+$('#board_id').val(),
    //             dataType: "json",
    //             contentType: 'application/json; charset=utf-8',
    //             data: JSON.stringify(data),
    //             beforeSend: function (xhr) {
    //                  xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    //             },
    //         });
    //     }
    // });

});