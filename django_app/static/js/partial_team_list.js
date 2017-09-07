$(function () {

    $(".js-create-board").click(function () {
        var team_id = $(this).data('team_id');
        $.ajax({
            url: '/dashboard/b/create/'+team_id+'/',
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
    });

});