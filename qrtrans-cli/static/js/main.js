// console.log("Start ------------------>")

streamingReadyFlag = false
isStreamFlag = false

function displayData(responseData) {
    var transDiv = $('#trans');
    transDiv.empty(); // 清空 div 内容

    // 遍历 data 字段中的每个元素，并按行添加到 div 中
    $.each(responseData.data, function(index, line) {
        transDiv.append('<pre>' + line + '</pre>');
    });
}

function updateQRcode(){
    if (isStreamFlag && streamingReadyFlag){
        $.ajax({
            url:'/data',
            type:'get',
            success:function(data){
                displayData(data)
            }
        })
    }
    else{
        return
    }
}

setInterval(updateQRcode, 40)

$(document).ready(function() {
    $('#file-select').on('change', function() {
        var formData = new FormData();
        var file = $(this)[0].files[0];
        if (!file) {
            alert('Please select a file');
            return;
        }
        
        formData.append('file', file);

        $.ajax({
            url: '/upload',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                console.log(file)
                $('#status').html(
                    `File: <span class="green">${file.name}</span> Size: <span class="green">${file.size}</span> Bytes. ↓ Click <span class="green">[Stream!)</span> Button!`
                );
                if (file.size != 0){
                    streamingReadyFlag = true
                    $('#streaming-button').addClass('green');
                }
                else{
                    streamingReadyFlag = false
                    $('#streaming-button').removeClass('green');
                    $('#streaming-button').removeClass('red');
                    $('#status').html(
                        "No file selected yet..."
                    );
                    alert("Empty File. Re-select!")
                }
                
            },
            error: function() {
                // $('#status').html('Error uploading file');
                alert(`File: ${file.name} Size: ${file.size} Bytes uploaded Failed!`)
            }
        });
    });
    $('#streaming-button').click(function(){
        isStreamFlag = !isStreamFlag; // 取反变量值
        if (isStreamFlag){
            $('#streaming-button').removeClass('green');
            $('#streaming-button').addClass('red');
            $('#streaming-button').text("Pause")
        }
        else{
            $('#streaming-button').removeClass('red');
            $('#streaming-button').addClass('green');
            $('#streaming-button').text("Continue")
        }
    });
});


