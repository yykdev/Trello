$(function () {

    $(".js-create-cardlist").click(function() {
        var board_id = $(this).data('board_id');
        $.ajax({
            url: '/dashboard/c/create/'+board_id+'/',
            type: 'get',
            dataType: 'json',
            beforeSend: function (xhr) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            },
            success: function (data) {
                $(".create_list_form").html(data.html_form);
            }
        })
    })

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