$(document).ready(function() {
    CollapsibleLists.apply();
    $('#popup').click(togglePopup);

    // Region-clicking and loading icon logic
    let loader = $('#popup .loader');
    let iframe = $('#popup iframe');
    $('.regions a').click(function(e) {
        e.preventDefault();
        iframe.attr("src", e.target.href);
        loader.css("display", "block");
        togglePopup();
    });
    iframe.on("load", function() {
        loader.css("display", "none");
    });
});

function togglePopup() {
    let popup = $('#popup');
    if (popup.css("display") === "none") {
        $('body').css("overflow", "hidden");
        popup.css("display", "block");
    } else {
        $('body').css("overflow", "auto");
        popup.css("display", "none");

        // Need to unload iframe upon exit, otherwise it will
        // persist when clicking the next region
        $('#popup iframe').attr("src", "about:blank");
    }
}
