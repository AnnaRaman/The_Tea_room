let countrySelected = $('#id_deafault_country').val();
if(!countrySelected) {
    $('#id_deafault_country').css('color', '#aab7c4')
};
$('#id_deafault_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#aab7c4')
    } else {
        $(this).css('color', '#000')
    }
});