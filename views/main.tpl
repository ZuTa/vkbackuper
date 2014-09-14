<html>
    <head>
        <title>VK Backup</title>
        <link rel="shortcut icon" type="image/x-icon" href="{{ get_url('static', path='favicon.png') }}" />
        <link rel="stylesheet" type="text/css" href="{{ get_url('static', path='styles.css') }}"/>
        <script src="//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
        <script type="text/javascript" src="{{ get_url('static', path='main.js') }}"></script>
        <style>
            @font-face {
                font-family: 'attackofthecucumbers';
                src: url('{{ get_url('static', path='attackofthecucumbers.ttf') }}');
            }
            body {
                background-image: url("{{ get_url('static', path='bg.jpg') }}");
                -moz-background-size: cover;
                -webkit-background-size: cover;
                background-size: cover;
                background-position: top center !important;
                background-repeat: no-repeat !important;
                background-attachment: fixed;
            }
        </style>
    </head>

    <body>
        <header>
            <h1><a class="main-link" href="/">VK BACKUP</a></h1>
            <p>backup your valuable data</p>
        </header>

        <article>
            To backup your data from <a class="regular-link" href="http://vk.com">VK</a> you need to go through four simple steps:

            <ol type="1">
                <li>Provide access to your VK profile. <a href="#" class="vk-authorize">Authorize</a> </li>
                <li>Provide access to your Google Drive. <a href="#" class="google-drive-authorize">Authorize</a> </li>
                <li>Choose what you would like to backup: <br/>
                    <div class="backup-items">
                        <input name="photos" type="checkbox" checked/> <label for="photos">Photos</label> <br/>
                        <input name="audio" type="checkbox" checked/> <label for="audio">Audio</label> <br/>
                    </div>
                </li>
                <li>Press <a href="#" class="backup-button" >Backup</a> to start </li>
            </ol>
            </p>
        </article>
        <footer>
            <span>
                &copy; ZuTa, 2014
            </span>
        </footer>
    </body>
</html>
