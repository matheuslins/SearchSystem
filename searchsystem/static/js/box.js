/*
*
* Function to get a cookie stored on browser
*
*/
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
/*
*
* Function to delete a box
*
*/
function delete_box(url, box, message, return_url) {
    alertify.confirm(message, function(){
        var csrftoken = getCookie('csrftoken');

        $.ajax({
            method: 'post',
            beforeSend: function (request) {
                request.setRequestHeader('X-CSRFToken', csrftoken);
            },
            url: url,
            success: function(data) {
                alertify.alert('Remove Box', 'Box removed successfully!', function(){
                    window.location.href = return_url;
                });
            }
        });
    });
}