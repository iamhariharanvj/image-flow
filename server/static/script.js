document.addEventListener("DOMContentLoaded", function () {
    setInterval(() => {
        nextSlide();
    }, 5000); // Change interval to 5000 milliseconds (5 seconds)
});

function nextSlide() {
    const slider = document.querySelector('.slider');
    const firstSlide = slider.firstElementChild;

    slider.appendChild(firstSlide.cloneNode(true));

    firstSlide.remove();

    slider.style.transform = 'translateX(0)';
}
