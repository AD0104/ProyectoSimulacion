document.getElementById("submit-form").addEventListener('click', function(event){
    event.preventDefault();

    var form_data = {"washing-stations": document.getElementById('washing-stations-entry').value,
                     "simulation-time": document.getElementById('simulation-time-entry').value,
                     "simulation-day": document.getElementById('sim-day').value};
    $.post("/get-form-data",form_data, function(data, status){
        if(status != "success"){
            alert('Algo salio mal: '+data+"\nStatus: "+status)
        }
    });
});
var simulation_form = document.getElementById("sim-form");
// simulation_form.addEventListener('submit', function(event){
//     event.preventDefault();
//     console.log('test');
// })