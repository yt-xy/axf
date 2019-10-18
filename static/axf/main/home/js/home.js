$(function () {
    initWheel();
    initMustBuy();
});


function initWheel(){
    var mySwiper = new Swiper('#topSwiper',
                                {
                                    loop:true,
                                    autoplay:3000,
                                    pagination:'.swiper-pagination',
                                    autoplayDisableOnInteraction:false,
                                })
}

function initMustBuy(){
    var mySwiper1 = new Swiper('#swiperMenu',
        {
            slidesPerView:3,
        })
}