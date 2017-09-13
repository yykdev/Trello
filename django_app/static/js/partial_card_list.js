$(function () {

    // 카드리스트 모달 오픈
    $(".js-create-cardlist").click(function() {
        var board_id = $(this).data('board_id');
        $.ajax({
            url: '/dashboard/cl/create/'+board_id+'/',
            type: 'get',
            dataType: 'json',
            beforeSend: function (xhr) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                $("#modal_card_list").modal("show");
            },
            success: function (data) {
                $("#modal_card_list .modal-content").html(data.html_form);
            }
        })
    });

    // 카드 모달 오픈
    $(".js-create-card").click(function() {
        var cardlist_id = $(this).data('cardlist_id');
        $.ajax({
            url: '/dashboard/c/create/'+cardlist_id+'/',
            type: 'get',
            dataType: 'json',
            success: function (data) {
                $("#modal_card_create").modal("show");
                $("#modal_card_create .modal-content").html(data.html_form);
            }
        })
    });

    // 카드 디테일 오픈
    $(".js-detail-card").click(function() {
        var card_id = $(this).data('card_id');
        $.ajax({
            url: '/dashboard/c/detail/'+card_id+'/',
            type: 'get',
            dataType: 'json',
            success: function (data) {
                $("#modal_card_detail").modal("show");
                $("#modal_card_detail .modal-content").html(data.html_form);
            }
        })
    });

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

    // $(".js-detail-board").click(function () {
    //     var board_id = $(this).data('board_id');
    //     $.ajax({
    //         url: '/dashboard/c/'+board_id+'/',
    //         type: 'get',
    //         dataType: 'json',
    //         beforeSend: function (xhr) {
    //             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    //             $("#modal_board").modal("show");
    //         },
    //         success: function (data) {
    //             $("#modal_board .modal-content").html(data.html_form);
    //         }
    //     })
    // })

});