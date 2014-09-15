$(function() {
    $('.vk-authorize').click(function() {
        signinWin = window.open("/vk-authorize", "Sign-in to VK", "width=780,height=410,toolbar=0,scrollbars=0,status=0,resizable=0,location=0,menuBar=0,left=" + 800 + ",top=" + 500);
        setTimeout(CheckLoginStatus, 2000);
        signinWin.focus();

        return false;
    });

    function CheckLoginStatus() {
        if (signinWin.closed) {
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
        else setTimeout(CheckLoginStatus, 1000);
    }
});