#To integrate this code into a website, you can make an AJAX request to the /checkPwStrength endpoint whenever a user enters a password.

#Example using jQuery

$(#password_input').on('input', function() {
    $.ajax({
        type: 'POST',
        url: '/checkPwStrength',
        data: {'password': $('#password_input').val()},
        dataType: 'json',
        success: function(data) {
            $('#password_strength').text(data.password_strength);
        }
    });
});
