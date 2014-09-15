<html>
    <head>
        % include('base-head.tpl', title='VK Authentication')

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
            $(function() {
                setTimeout(function() {
                    var val = $.cookie("vk-authorize");
                    if (val) {
                        window.close();
                    }
                }, 1000);
            });
        </script>
    </body>
</html>