var myCarousel = document.querySelector('#carouselExampleIndicators')
var carousel = new bootstrap.Carousel(carouselExampleIndicators, {
  interval: 10000,
  wrap: true
})

var prevButton = document.querySelector('.carousel-control-prev')
var nextButton = document.querySelector('.carousel-control-next')

prevButton.addEventListener('click', function() {
  carousel.prev()
})

nextButton.addEventListener('click', function() {
  carousel.next()
})
