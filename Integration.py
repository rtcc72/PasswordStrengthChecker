'''$(#password_input').on('input', function() {
    $.ajax({
        type: 'POST',
        url: '/check_password_strength',
        data: {'password': $('#password_input').val()},
        dataType: 'json',
        success: function(data) {
            $('#password_strength').text(data.password_strength);
        }
    });
});'''
