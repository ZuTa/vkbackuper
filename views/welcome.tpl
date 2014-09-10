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
        You have {{photos_count}} photos and {{photo_albums_count}} albums. Would you like to have them on your local computer?
        <button id="retrieve-photos-button" type="button">Load my photos</button>
        <span id="waiting-photo-text" style="display:none;">loading...</span>
        <a id="download-photos-link" style="display:none;">Download</a>
    </div>

    <br/>

    <div>
        You have {{audio_count}} audio tracks. Would you like to have them on your local computer?
        <button id="retrieve-audio-button" type="button">Load my audio</button>
        <span id="waiting-audio-text" style="display:none;">loading...</span>
        <a id="download-audio-link" style="display:none;">Download</a>
    </div>


    <script>
        $(function() {
            var retrieve = function(btn, waitElement, linkElement, url) {
                btn.click(function() {
                    $(this).prop('disabled', true);
                    waitElement.toggle();

                    $.get(url,
                        function(arc) {
                            waitElement.toggle();
                            linkElement.attr("href", arc);
                            linkElement.toggle();
                        }
                    );
                });
            }

            retrieve($("#retrieve-photos-button"), $("#waiting-photo-text"), $("#download-photos-link"), "pack-photos");

            retrieve($("#retrieve-audio-button"), $("#waiting-audio-text"), $("#download-audio-link"), "pack-audio");
        });
    </script>
</body>

</html>
