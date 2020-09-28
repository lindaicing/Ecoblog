$( document ).ready(function() {
    if($('#herobanner').attr("src")==''){
        $('#herobanner').attr('src', 'https://images.unsplash.com/photo-1473773508845-188df298d2d1?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2534&q=80');
        $('#herobanner').css({
            "opacity":"0.75"
        })
    }
});

// document.getElementById('herobanner').onerror = function() {
//     document.getElementById('herobanner').setAttribute('src', 'https://images.unsplash.com/photo-1473773508845-188df298d2d1?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2534&q=80');
// }
