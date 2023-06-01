
$(document).ready(function() {
    $('#myForm').submit(async function(event) {
        event.preventDefault();
        const BaseUrl = '/getdepid/';
        const Depart =  $('#Department').val();
        const Url = BaseUrl+Depart;
        var formData = {
            Name: $('#inputName4').val(),
            Surname: $('#inputSurName4').val(),
            Staff_number: $('#inputStaffNo4').val(),
            ID_number: $('#inputID').val(),
            Specialization: $('#inputSpecialization').val(),
            City: $('#inputCity').val(),
            Department: await fetchIDFromAPI(Url),
            Average_Rate: 0.0
        };
        try {
            $.ajax({
                type: 'POST',
                url: '/enterdoctor/',
                data: formData,
                success: function(response) {
                    console.log('Record created successfully!');
                    console.log(response);
                },
                error: function(xhr, textStatus, errorThrown) {
                    console.log('Error creating record:', errorThrown);
                    console.log('Error txt status:', textStatus);
                    console.log('Error xhr:', xhr);
                }
            });
        }catch(error)
        {
            console.error('Error:', error);
        }
        
    });
});
function fetchIDFromAPI(url) {
    return new Promise(function(resolve, reject) {
        $.ajax({
            type: 'GET',
            url: url,
            success: function(apiResponse) {
                var resp = apiResponse.id;
                resolve(resp); 
            },
            error: function(xhr, textStatus, errorThrown) {
                console.log('Error retrieving API value:', errorThrown);
                reject(errorThrown);
            }
        });
    });
  }
  
  
