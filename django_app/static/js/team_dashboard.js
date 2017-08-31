$(function () {

    /**
     * 팀 생성 버튼 클릭
     */
    $(".js-create-team").click(function () {
        $.ajax({
            url: '/dashboard/t/create/',
            type: 'get',
            dataType: 'json',
            beforeSend: function (xhr) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                $("#modal_team").modal("show");
            },
            success: function (data) {
                $("#modal_team .modal-content").html(data.html_form);
            }
        });
    });

    /**
     * 팀 생성 모달 데이터 저장
     */
    $("#modal_team").on("submit", ".js-create-team-form", function () {
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
                    $("#div_team_dashboard").html(data.html_team_list);
                    $("#modal_team").modal("hide");
                }
                else {
                    $("#modal_team .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    });






    $("#modal_board").on("submit", ".js-create-board-form", function () {
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
                    $("#div_team_dashboard").html(data.html_team_list);
                    $("#modal_board").modal("hide");
                }
                else {
                    $("#modal_board .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    });

});