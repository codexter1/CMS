$( document ).ready(function() {
    $(".dropdown-trigger").dropdown();
    console.log( "ready!" );
});

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.carousel');
    var instances = M.Carousel.init(elems, options);
  });

  
