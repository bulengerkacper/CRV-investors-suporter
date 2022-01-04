$.get('/avg/3',  // url
    function (data, textStatus, jqXHR) {  // success callback
        // alert('status: ' + textStatus + ', data:' + data);
        $('result_of_avg_3').append("3 DAYS: " + data + "</br>");
    });
$.get('/avg/5',  // url
    function (data, textStatus, jqXHR) {  // success callback
    // alert('status: ' + textStatus + ', data:' + data);
    $('result_of_avg_5').append("5 DAYS: " + data + "</br>");
});
$.get('/avg/31',  // url
    function (data, textStatus, jqXHR) {  // success callback
    // alert('status: ' + textStatus + ', data:' + data);
    $('result_of_avg_31').append("31 DAYS: " + data + "</br>");
});
$.get('/avg/180',  // url
    function (data, textStatus, jqXHR) {  // success callback
    // alert('status: ' + textStatus + ', data:' + data);
    $('result_of_avg_180').append("180 DAYS: " + data + "</br>");
});

$.get('/avg_from_last_15min',  // url
    function (data, textStatus, jqXHR) {  // success callback
    // alert('status: ' + textStatus + ', data:' + data);
    $('result_of_avg_15min').append("15 min: " + data + "</br>");
});
$.get('/compare_15min_to_days/3',  // url
    function (data, textStatus, jqXHR) {  // success callback
    // alert('status: ' + textStatus + ', data:' + data);
    $('compare_to_3').append(data);
});
$.get('/compare_15min_to_days/5',  // url
    function (data, textStatus, jqXHR) {  // success callback
    // alert('status: ' + textStatus + ', data:' + data);
    $('compare_to_5').append(data);
});
$.get('/compare_15min_to_days/31',  // url
    function (data, textStatus, jqXHR) {  // success callback
    // alert('status: ' + textStatus + ', data:' + data);
    $('compare_to_31').append(data);
});
$.get('/compare_15min_to_days/180',  // url
    function (data, textStatus, jqXHR) {  // success callback
    // alert('status: ' + textStatus + ', data:' + data);
    $('compare_to_180').append(data);
    });

$.get('/get_current_value',  // url
    function (data, textStatus, jqXHR) {  // success callback
    // alert('status: ' + textStatus + ', data:' + data);
    $('cur_val').append(data);
});

$.get('/yesterday_to_today',  // url
    function (data, textStatus, jqXHR) {  // success callback
    // take wrong value after refresh
    $('yesterday_to_today').append(data);
});

$.get('/rsi/14', 
    function (data, textStatus, jqXHR) {  // success callback
    // take wrong value after refresh
    $('rsi_14').append(data);
});
function myFunction() {
    coin_type=document.getElementById("success_select").value;
    $.ajax({
    type: 'POST',
    contentType: 'application/json',
    url: '/coinswitcher',
    dataType: 'json',
    data: JSON.stringify({ "value": coin_type }),
    success: function (result) {
    },
    error: function (error) { console.error(error) }
    });
    location.reload();
}
