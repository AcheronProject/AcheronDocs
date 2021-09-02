document.addEventListener("DOMContentLoaded", function() {
    show_toc_left();
});

function show_toc_left(){
    document.querySelectorAll('.md-nav .md-nav--secondary')[0].setAttribute("style", "display: block; overflow: visible; color: #7d7f8e9c")
    document.querySelectorAll('.md-nav .md-nav--secondary label')[0].remove()
}
