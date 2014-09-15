$(function() {
    var popupOptions = "width=780,height=410,toolbar=0,scrollbars=0,status=0,resizable=0,location=0,menuBar=0,left=800,top=500";

    var vkSigninWin = null;
    $('.vk-authorize').click(function() {
        vkSigninWin = window.open("/vk-authorize", "Sign-in to VK", popupOptions);
        setTimeout(CheckVKLoginStatus, 2000);
        vkSigninWin.focus();

        return false;
    });

    function CheckVKLoginStatus() {
        if (vkSigninWin.closed) {
            if ($.cookie("vk-authorize") == "1") {
                $.getJSON("/vk-user", function(data) {
                    if (data["result"] === "OK") {
                        $(".vk-user").text(data["user"]);
                        $(".vk-authorized-text").show();
                        $(".vk-authorization-error").hide();
                    }
                    else {
                        $(".vk-authorized-text").hide();
                        $(".vk-authorization-error").show();
                    }
                });
            }
        }
        else setTimeout(CheckVKLoginStatus, 1000);
    }

    var gdSigninWin = null;
    $('.google-drive-authorize').click(function() {
        gdSigninWin = window.open("/gd-authorize", "Sign-in to Google Drive", popupOptions);
        setTimeout(CheckGDLoginStatus, 2000);
        gdSigninWin.focus();

        return false;
    });

    function CheckGDLoginStatus() {
        if (gdSigninWin.closed) {
            if ($.cookie("gd-authorize") == "1") {
                $(".gd-authorized-text").show();
            }
        }
        else setTimeout(CheckGDLoginStatus, 1000);
    }
});