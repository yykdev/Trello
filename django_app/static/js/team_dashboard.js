$(function () {

    /**
     * 팀 생성 버튼 클릭
     */
    $(".js-create-team").click(function () {
        $.ajax({
            url: '/dashboard/t/create/',
            type: 'get',
            dataType: 'json',
            success: function (data) {
                $("#modal_create_team").modal("show");
                $("#modal_create_team .modal-content").html(data.html_form);
            }
        });
    });

    /**
     * 팀 생성 모달 데이터 저장
     */
    $("#modal_create_team").on("submit", ".js-create-team-form", function () {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#div_team_dashboard").html(data.html_team_list);
                    $("#modal_create_team").modal("hide");
                }
                else {
                    $("#modal_create_team .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    });

    /**
     * 팀 수정 버튼 클릭
     */
    $(".js-modify-team").click(function () {
        var team_id = $(this).data('team_id');
        $.ajax({
            url: '/dashboard/t/modify/'+team_id+'/',
            type: 'get',
            dataType: 'json',
            success: function (data) {
                $("#modal_modify_team").modal("show");
                $("#modal_modify_team .modal-content").html(data.html_form);
            }
        });
    });

    /**
     * 팀 수정 모달 데이터 저장
     */
    $("#modal_modify_team").on("submit", ".js-create-team-form", function () {
        var form = $(this);
        var team_id = form.data('team_id');
        $.ajax({
            url: '/dashboard/t/modify/'+team_id+'/',
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#div_team_dashboard").html(data.html_team_list);
                    $("#modal_modify_team").modal("hide");
                }
                else {
                    $("#modal_modify_team .modal-content").html(data.html_form);
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