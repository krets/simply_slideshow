var index = 0

function cacheAdjacent(){
    var size=2
    for(var i=index-size; i<index+size; i++){
        $.get("/image", {index:i}).done(function(data){preload(data, i);})
    }
}
function preload(src, i){
    $('<img />')[0].src = src;
}

function loadNext(){
    index = index + 1;
    loadImage(index);
}
function loadPrevious(){
    index = index - 1;
    loadImage(index);
}
function loadImage(i){
    $.get("/image", {index:i}).done(function(data){$('.container img')[0].src=data;})
}
$(function() {
    $('a.nav.right').attr('href', '#');
    $('a.nav.right').click(loadNext);
    $('a.nav.left').attr('href', '#');
    $('a.nav.left').click(loadPrevious);
});
