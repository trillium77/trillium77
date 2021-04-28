
$(function() {
  $('.myscrollup').click(function() {
    $("html, body").animate({
      scrollTop:0
    },1000);
  })
})
$(window).scroll(function() {
  if ($(this).scrollTop()>500) {
    $('.myscrollup').fadeIn();
  }

  else {
    $('.myscrollup').fadeOut();
  }
});
