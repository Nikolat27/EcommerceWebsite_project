//========= start home slider =========///
var swiper = new Swiper("#homeSlider", {
  spaceBetween: 30,
  centeredSlides: true,
  loop: true,
  autoplay: {
    delay: 3000,
    disableOnInteraction: false,
  },
  effect: "fade",
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});

///=============end home slider ============/

//============= sugget moment =============//

var swiperSugget = new Swiper("#suggetMoment", {
  slidesPerView: 1,
  spaceBetween: 30,
  loop: true,
  autoplay: {
    delay: 3000,
    disableOnInteraction: false,
  },
  speed: 500,
  on: {
    init: function () {
      $(".swiper-progress-bar").removeClass("animate");
      $(".swiper-progress-bar").removeClass("active");
      $(".swiper-progress-bar").eq(0).addClass("animate");
      $(".swiper-progress-bar").eq(0).addClass("active");
    },
    slideChangeTransitionStart: function () {
      $(".swiper-progress-bar").removeClass("animate");
      $(".swiper-progress-bar").removeClass("active");
      $(".swiper-progress-bar").eq(0).addClass("active");
    },
    slideChangeTransitionEnd: function () {
      $(".swiper-progress-bar").eq(0).addClass("animate");
    }
  }
});

//============= end sugget moment =============//

//============= start amazing =============//

///offer
///offer gallery
var swiper = new Swiper(".amazing-slider-link", {
  spaceBetween: 10,
  slidesPerView: 4,
  freeMode: true,
  watchSlidesProgress: true,
  allowTouchMove: false,
});
var swiper2 = new Swiper(".amazing-slider-slider", {
  effect: "fade",
  speed: 1000,
  loop: true,
  autoplay: {
    delay: 5000,
    disableOnInteraction: false,
  },
  spaceBetween: 10,
  thumbs: {
    swiper: swiper,
  },
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
});


//============= end amazing =============//

//========= start product box ==============/

var swiper = new Swiper("#product-slider", {
  slidesPerView: 5,
  spaceBetween: 10,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  breakpoints: {
    100: {
      slidesPerView: 1,
      spaceBetween: 20,
    },
    576: {
      slidesPerView: 2,
      spaceBetween: 20,
    },
    768: {
      slidesPerView: 2,
      spaceBetween: 20,
    },
    1024: {
      slidesPerView: 3,
      spaceBetween: 20,
    },
    1200: {
      slidesPerView: 4,
      spaceBetween: 20,
    },
    1400: {
      slidesPerView: 5,
      spaceBetween: 20,
    }},
});

//========= end product box ==============/


//=========== product gallery ===================//

var proSwiper = new Swiper(".product-gallery-thumb", {
  spaceBetween: 10,
  slidesPerView: 4,
  freeMode: true,
  watchSlidesProgress: true,
  breakpoints: {
    // when window width is >= 320px
    320: {
      slidesPerView: 3,
      spaceBetween: 10
    },
    // when window width is >= 480px
    400: {
      slidesPerView: 4,
      spaceBetween: 10
    },
  },
});
var proThumbswiper = new Swiper(".product-gallery", {
  spaceBetween: 10,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  zoom: {
    maxRatio: 3,
    minRation: 1
  },
  thumbs: {
    swiper: proSwiper,
  },
});

//=========== end product gallery ===================//

//========= start new category ==============/
var swiper = new Swiper(".free-mode", {
  slidesPerView: "auto",
  spaceBetween: 10,
  freeMode: true,
});
//========= end new category ==============/