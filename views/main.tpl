<html>

    % include('base-head.tpl')

    <body>
        <header>
            <h1><a class="main-link" href="/">VK BACKUP</a></h1>
            <p>backup your valuable data</p>
        </header>

        <article>
            To backup your data from <a class="regular-link" href="http://vk.com">VK</a> you need to go through four simple steps:

            <ol type="1">
                <li>
                    Provide access to your VK profile.
                    <a href="#" class="vk-authorize">Authorize</a>

                    <span class="vk-authorized-text">
                        (Authorized as <span class="vk-user"></span>)
                    </span>

                    <span class="vk-authorization-error">
                        Not authorized!
                    </span>
                </li>
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
                ZuTa &copy; 2014
            </span>
        </footer>
    </body>
</html>
