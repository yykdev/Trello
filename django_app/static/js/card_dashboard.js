// 초기화
$( function() {

    $('.card_list_body').sortable({
        connectWith: '.card_list_body',
        update: function(event, div) {
            var order = $(this).sortable('toArray');
            var data = {
                list_id: $(this).data('list_id'),
                positions: order.join(';')
            }

            $.ajax({
                type: "POST",
                url: '/dashboard/c/move/'+$(this).data('board_id')+'/',
                dataType: "json",
                contentType: 'application/json; charset=utf-8',
                data: JSON.stringify(data),
                beforeSend: function (xhr) {
                     xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                },
            });
        }
    });

});