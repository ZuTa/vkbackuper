<html>
<head>
    <title>VK Backup</title>
    <link rel="shortcut icon" type="image/x-icon" href="/static/favicon.png" />
    <script src="//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
</head>

<body>
    <img src="{{profile_photo_src}}" />

    <p>
        Hi, {{user_name}}!
        Welcome to VK Backpup!
    </p>

    <div>
        You have {{photos_count}} photos and {{photo_albums_count}} albums. Do you want to get it all on your local computer?
        <button id="retrieve-photos-button" type="button">Retrieve my photos</button>
        <span id="waiting-text" style="display:none;">retrieving...</span>
        <a id="download-photos-link" style="display:none;">Download</a>
    </div>


    <script>
        $(function() {
            $("#retrieve-photos-button").click(function() {
                $(this).prop('disabled', true);
                $("#waiting-text").toggle();

                $.get("download-photos",
                    function(arc) {
                        $("#waiting-text").toggle();
                        $("#download-photos-link").attr("href", arc);
                        $("#download-photos-link").toggle();
                    }
                );
            });
        });
    </script>
</body>

</html>
