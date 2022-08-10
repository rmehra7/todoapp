$(document).ready(function(){
    
    $(".edit_task").on('click', function () {
        var id = $(this).data('id');
        var $trs = $(this).closest('tr');

        let dataset = [];
        $trs.children('td').each(function(){
            var data = $(this).html();
            dataset.push(data.trim());
        })

        $("#taskid").val(id);
        $("#task").val(dataset[1]);
        $("#date").val(dataset[2]);
        if (dataset[3] == 'True'){
            $("#completed").prop('checked', true);
        } else {
            $("#completed").prop('checked', false);
        }

        var myModal = new bootstrap.Modal(document.getElementById('exampleModal'), {
            keyboard: false
        });
        myModal.show();

    });

    $(".delete_task").on('click', function () { 
        var id = $(this).data('id');
        var url = '/api/v1/task/' + id;
        $.ajax({
            method: "DELETE",
            url: url,
            success: function(data) {
                location.reload();
            }
        });
    });

    $(".add_task").on("click", function() {
        var myModal = new bootstrap.Modal(document.getElementById('exampleModal'), {
            keyboard: false
        });
        myModal.show();
    });

    $("#form_submit").on("click", function(){
        var id = $("#taskid").val();
        if (id === ''){
            var url = '/api/v1/tasks';
            method = 'POST';
        } else {
            var url = '/api/v1/task/' + id;
            var method = 'PUT';
        }
        var data = {
            "task": $("#task").val(),
            "datetime": $("#date").val(),
            "is_completed": $("#completed").prop('checked')
        }
        $.ajax({
            method: method,
            url: url,
            dataType: "json",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(data),
            success: function(data) {
                location.reload();
            }
        });
    });
});