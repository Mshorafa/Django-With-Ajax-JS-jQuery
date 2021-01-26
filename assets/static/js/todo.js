$(document).ready(function (){
    var csrf =$('input[name=csrfmiddlewaretoken]').val();

    $('#createdButton').click(function (){

        var SerialzedData = $('#createdTaskForm').serialize()


        $.ajax({
            url:$('#createdTaskForm').data('url'),
            data:SerialzedData,
            type:'post',
            success:function(response){

                $('#taskList').append(`<div class="card mb-1" id="taskCard" data-id=${response.task.id}>
                <div class="card-body">
                    ${response.task.title}
                    <button type="button" class="close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
            </div>`)
            }
        })
        $('#createdTaskForm')[0].reset()
    });

    $('#taskCard').on('click','.card',function (){
        var CardID = $(this).data('id');
        console.log($('#taskCard').data('id'));
        $.ajax({
            // url: $(this).data('url'),
            url: `/tasks/${CardID}/completed/`,
            data: {
                csrfmiddlewaretoken:csrf,
                id:CardID
            },
            type:'post',
            success:function (){
                console.log(CardID)
                var cardItme = $(`#taskCard[data-id=${CardID}]`)
                cardItme.css('text-decoration','line-through')
                $('#taskList').append(cardItme);

            }
        });
    }).on('click','button.close',function (event) {
        event.stopPropagation();
        var CardID = $(this).parent().parent().data('id')
        $.ajax({
            // uri:$(this).data('url'),
            url: `/tasks/${CardID}/removeTask/`,
            data:{
                csrfmiddlewaretoken:csrf,
                id:CardID
            },
            type:'post',
            success:function (){
                $(`#taskCard[data-id=${CardID}]`).remove()
            }
        })

    })

});