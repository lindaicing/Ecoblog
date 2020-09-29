$( document ).ready(function() {
    if($('#herobanner').attr("src")==''){
        $('#herobanner').attr('src', 'https://images.unsplash.com/photo-1473773508845-188df298d2d1?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2534&q=80');
        $('#herobanner').css({
            "opacity":"0.75"
        })
    }

    $("#confetti").click(function(){
        confetti.start(1000, 100);
    })

    sidebarChange();
    $(window).resize(function() {
        sidebarChange();
    })
    
    function sidebarChange(){
        if ($(window).width() > 768) {
            $("#sidebar, #beforeComments").removeClass("hiddenSidebar");
        } else {
            $("#sidebar, #beforeComments").addClass("hiddenSidebar");
        }
    }
});
