function showHide(element) {
    var x = document.getElementById(element);
    if (x.style.display === 'none') {
        x.style.display = 'block';
    } else {
        x.style.display = 'none';
    }
}

$( document ).ready(function() {
    $('#chevron-btn').click(function(){

        var the_id = $(this).attr("href");

        $('html, body').animate({
            scrollTop:$(the_id).offset().top
        }, 'slow');

        return false;
    });
});


