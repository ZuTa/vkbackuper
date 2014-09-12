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

    <div>
        Google Drive. <button id="authorize-button" style="visibility: hidden">Authorize</button> <span id="gd-linked" style="display: none; color:red;"> Linked </span>
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

    <script>
        var clientId = '670624754813-bqnjav9r2qitrf6tfcdiagnt4gjvsdq2.apps.googleusercontent.com';
        var scopes = 'https://www.googleapis.com/auth/drive';

        // Use a button to handle authentication the first time.
        function handleClientLoad() {
            window.setTimeout(checkAuth, 1);
        }

        function checkAuth() {
            gapi.auth.authorize({client_id: clientId, scope: scopes, immediate: true}, handleAuthResult);
        }

        function handleAuthResult(authResult) {
            var authorizeButton = document.getElementById('authorize-button');

            if (authResult && !authResult.error) {
                authorizeButton.style.visibility = 'hidden';
                console.log("Logged to GDrive");
                document.getElementById("gd-linked").style.display = 'inline';
                // do something here
            } else {
                authorizeButton.style.visibility = '';
                authorizeButton.onclick = handleAuthClick;
            }
        }

        function handleAuthClick(event) {
            gapi.auth.authorize({client_id: clientId, scope: scopes, immediate: false}, handleAuthResult);
            return false;
        }
    </script>
    <script src="https://apis.google.com/js/client.js?onload=handleClientLoad"></script>
</body>

</html>
