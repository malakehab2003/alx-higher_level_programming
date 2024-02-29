$(document).ready(function () {
        $('#btn_translate').click(function () {
                const lc = $('#language_code').val();

                $.ajax({
                        url:'https://hellosalut.stefanbohacek.dev/?',
                        type: 'GET',
                        data: { lang: lc },
                        success: function (da) {
                                $('#hello').text(da.hello);
                        }

                });
        });
});