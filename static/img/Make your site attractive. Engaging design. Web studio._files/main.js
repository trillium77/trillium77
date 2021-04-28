//Scroll Button
    //Click
    $(function() {
      $('.scrollup').click(function() {
        // переместиться в верхнюю часть страницы
        $("html, body").animate({
          scrollTop:0
        },1000);
      })
    })
    //Visible
    $(window).scroll(function() {
      if ($(this).scrollTop()>200) {
        $('.scrollup').fadeIn();
      }
      else {
        $('.scrollup').fadeOut();
      }
    });

