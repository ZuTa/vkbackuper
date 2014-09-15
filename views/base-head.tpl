<head>
    <title>VK Backup</title>
    <link rel="shortcut icon" type="image/x-icon" href="{{ get_url('static', path='favicon.png') }}" />
    <link rel="stylesheet" type="text/css" href="{{ get_url('static', path='styles.css') }}"/>
    <script src="//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
    <script type="text/javascript" src="{{ get_url('static', path='main.js') }}"></script>
    <script type="text/javascript" src="{{ get_url('static', path='jquery.cookie.js') }}"></script>
    <script type="text/javascript" src="{{ get_url('static', path='spin.min.js') }}"></script>
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
