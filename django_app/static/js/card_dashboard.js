// 초기화
$( function() {

    // 카드리스트 생성
    $("#modal_card_list").on("submit", ".js-create-cardlist-form", function () {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            beforeSend: function (xhr) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            },
            success: function (data) {
                if (data.form_is_valid) {
                    $("#div_card_dashboard").html(data.html_cardlist_list);
                    $("#modal_card_list").modal("hide");
                }
                else {
                    $("#modal_card_list .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    });

    // 카드 생성
    $("#modal_card_create").on("submit", ".js-create-card-form", function () {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#div_card_dashboard").html(data.html_cardlist_list);
                    $("#modal_card_create").modal("hide");
                }
                else {
                    $("#modal_card_create .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    });


    // 카드 디테일 생성
    // $("#modal_card_detail").on("submit", ".js-detail-card-form", function () {
    //     var form = $(this);
    //     $.ajax({
    //         url: form.attr("action"),
    //         data: form.serialize(),
    //         type: form.attr("method"),
    //         dataType: 'json',
    //         success: function (data) {
    //             if (data.form_is_valid) {
    //                 $("#div_card_dashboard").html(data.html_cardlist_list);
    //                 $("#modal_card").modal("hide");
    //             }
    //             else {
    //                 $("#modal_card .modal-content").html(data.html_form);
    //             }
    //         }
    //     });
    //     return false;
    // });

    // $('.card_list_body').sortable({
    //     connectWith: '.card_list_body',
    //     update: function(event, div) {
    //         var order = $(this).sortable('toArray');
    //         var data = {
    //             list_id: $(this).data('list_id'),
    //             positions: order.join(';')
    //         }
    //
    //         $.ajax({
    //             type: "POST",
    //             url: '/dashboard/c/move/'+$(this).data('board_id')+'/',
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