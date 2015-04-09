$(document).ready(function(){
$("#one").click(function(){
    $("#pa").hide();
});
$("#btn").click(function(e){

        e.preventDefault();
        var adddata = $("#formid");
        var ajaxType = adddata.attr('method');
        var ajaxUrl = adddata.attr('action');
        var ajaxData = adddata.serialize();
        var ajaxDataType = "json";
        var ajaxSuccessFunction = function(data){
            console.log(data);
        }


        $.ajax({
            url: ajaxUrl,
            dataType : 'json',
            type: ajaxType,
            data : ajaxData,
            beforeSend: function(){
                console.log("inside ajax");
            },
            success: ajaxSuccessFunction,
        });

    });
});

