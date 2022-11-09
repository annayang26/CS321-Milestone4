$('.live-search-list li').each(function(){
    $(this).attr('data-search-term', $(this).text().toLowerCase());
});
    
$('.live-search-box').on('keyup', function(){
    
var searchTerm = $(this).val().toLowerCase();
    
    $('.live-search-list li').each(function(){
    
        if (searchTerm.length == 0) {
            $(this).show();
        } else if ($(this).filter('[data-search-term *= ' + searchTerm + ']').length > 0 || searchTerm.length < 1) {
            $(this).show();
        } else {
            $(this).hide();
        }
    
    });
    
});