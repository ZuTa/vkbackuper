<html>
    <head>
        % include('base-head.tpl')

        <style>
            p.text {
                margin: 20px;
            }
        </style>
    </head>
    <body>
        <p class="text">
            Authenticating...
        </p>

        <script>
            var COOKIE = "{{cookie_name}}";

            $(function() {
                setTimeout(function() {
                    var val = $.cookie(COOKIE);
                    if (val) {
                        window.close();
                    }
                }, 1000);
            });
        </script>
    </body>
</html>