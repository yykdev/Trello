$(function () {

    $(".js-create-board").click(function () {
        var id = $(this).data('team_id');

        $.ajax({
            url: '/contents/modal/board/' + id,
            type: 'get',
            dataType: 'json',
            beforeSend: function (xhr) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                $("#modal_board").modal("show");
            },
            success: function (data) {
                $("#modal_board .modal-content").html(data.html_form);
            }
        });
    });

    $("#modal_board").on("submit", ".js-board-create-form", function () {
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
                    $("#modal_board").modal("hide");
                    $(document.body).removeClass("modal-open");
                    $(".modal-backdrop").remove();
                    $("#div_container").html(data.main_dashboard);
                }
                else {
                    $("#modal_board .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    });

});