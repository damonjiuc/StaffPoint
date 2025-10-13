const swiper = new Swiper('.nets-swiper', {
    slidesPerView: 4, // сколько видно за раз
    spaceBetween: 40, // отступ между логотипами
    loop: true,       // бесконечная прокрутка
    autoplay: {
        delay: 2000,    // пауза между слайдами
        disableOnInteraction: false,
    },
    speed: 1000,      // скорость перехода
    grabCursor: true,
    breakpoints: {
        1024: { slidesPerView: 5 },
        768: { slidesPerView: 4 },
        480: { slidesPerView: 1 },
    },
});