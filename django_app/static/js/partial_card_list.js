$(function () {

    $(".js-create-cardlist").click(function() {
        var board_id = $(this).data('board_id');
        $.ajax({
            url: '/dashboard/c/create/'+board_id+'/',
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


    $(".js-detail-board").click(function () {
        var board_id = $(this).data('board_id');
        $.ajax({
            url: '/dashboard/c/'+board_id+'/',
            type: 'get',
            dataType: 'json',
            beforeSend: function (xhr) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                $("#modal_board").modal("show");
            },
            success: function (data) {
                $("#modal_board .modal-content").html(data.html_form);
            }
        })
    })

});