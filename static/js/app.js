document.getElementById("submit-form").addEventListener('click', function(event){
    event.preventDefault();

    var form_data = {"washing-stations": document.getElementById('washing-stations-entry').value,
                     "simulation-time": document.getElementById('simulation-time-entry').value,
                     "simulation-day": document.getElementById('sim-day').value,
                     "workers": document.getElementById('workers').value};
    $.ajax({
        type: "POST",
        url: "/get-form-data",
        dataType: "json",
        async: false,
        data: JSON.stringify(form_data),
        success: function(data, status){
            console.log(data);
            console.log(status);
        },
        contentType: 'application/json'
    });
});