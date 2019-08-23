$(document).ready((function(_this) {
    return function() {
        var bt;
        bt = $('#back_to_top');
        if ($(document).width() > 480) {
            $(window).scroll(function() {
                var st;
              
                st = $(window).scrollTop();
                if (st > 400) {
                    return bt.css('display', 'block');
                } else {
                    return bt.css('display', 'none');
                }
            });
            return bt.click(function() {
                $('body,html').animate({
                    scrollTop: 0
                },
                800);
                return false;
            });
        }
    };
})(this));