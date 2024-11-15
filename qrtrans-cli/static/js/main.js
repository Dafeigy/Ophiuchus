console.log("Start ------------------>")

function displayData(responseData) {
    var transDiv = $('#trans');
    transDiv.empty(); // 清空 div 内容

    // 遍历 data 字段中的每个元素，并按行添加到 div 中
    $.each(responseData.data, function(index, line) {
        transDiv.append('<div>' + line + '</div>');
    });
}

function allInOne(){
    $.ajax({
        url:'/data',
        type:'get',
        success:function(data){
            // console.log(data)
            displayData(data)
            $
        }
    })
}

setInterval(allInOne, 500)