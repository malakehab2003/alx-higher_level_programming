$(document).ready(function () {
        function translateHello() {
            const lc = $('#language_code').val();
    
            $.ajax({
                url: 'https://hellosalut.stefanbohacek.dev/?lang=' + lc,
                type: 'GET',
                success: function (da) {
                    $('#hello').text(da.hello);
                }
            });
        }

        $('#btn_translate, #language_code').on('click keypress', function (e) {
            if (e.type === 'click' || (e.type === 'keypress' && e.which === 13)) {
                translateHello();
            }
        });
    });
    