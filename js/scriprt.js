// Navbar Background Change on Scroll
window.addEventListener('scroll', function () {
    const navbar = document.getElementById('navbar');
    if (window.scrollY > 100) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Toggle Navigation Links on Mobile
const hamburger = document.getElementById('hamburger');
const closeBtn = document.getElementById("close");
const navLinks = document.getElementById('nav-links');

hamburger.addEventListener('click', function() {
    navLinks.classList.toggle('active');
    navLinks.style.width ='none';
    //hamburger.style.display = "none";
    //closeBtn.style.display = "block";
});

// Toggle between hamburger and close icon on click
closeBtn.addEventListener("click", () => {
    closeBtn.style.display = "none";
    hamburger.style.display = "block";
});
window.addEventListener('click', function(event) {
    if (!programsButton.contains(event.target) && !programList.contains(event.target)) {
        programList.classList.remove('active');
    }
});
let currentIndex = 0;
const slides = document.querySelectorAll('.slide');
const totalSlides = slides.length;
const slidesToShow = window.innerWidth <= 768 ? 2 : 3;

function updateSliderPosition() {
    const slideWidth = slides[0].clientWidth;
    const offset = -(currentIndex * slideWidth);
    document.getElementById('slider').style.transform = `translateX(${offset}px)`;
}

function moveSlide(direction) {
    currentIndex += direction;
    if (currentIndex < 0) {
        currentIndex = totalSlides - slidesToShow;
    } else if (currentIndex > totalSlides - slidesToShow) {
        currentIndex = 0;
    }
    updateSliderPosition();
}
//go to top
// Select the button
const goTopButton = document.getElementById('goTop');
const helpButton = document.getElementById('help');
const helpinButton = document.getElementById('helpin');
const closehelp = document.getElementById('clos');



// Show the button when scrolling down
window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
        goTopButton.style.display = 'block';
        helpButton.style.display = 'block';
    } else {
        goTopButton.style.display = 'none';
        helpButton.style.display = 'none';
        helpinButton.style.display = 'none';
    }
    }

);
goTopButton.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});

helpButton.addEventListener('click', () => {
    helpinButton.style.display = 'block';
});

closehelp.addEventListener('click', () => {
    helpinButton.style.display = 'none';
});

// Automatic Slide Change every 5 seconds
let slideInterval = setInterval(() => {
    moveSlide(1);
}, 5000);

// Stop sliding on button click and reset interval
document.querySelector('.prev').onclick = () => {
    moveSlide(-1);
    resetSlideInterval();
};

document.querySelector('.next').onclick = () => {
    moveSlide(1);
    resetSlideInterval();
};

// Reset interval on manual slide change
function resetSlideInterval() {
    clearInterval(slideInterval);
    slideInterval = setInterval(() => {
        moveSlide(1);
    }, 5000);
}

// Adjust slide width on resize
window.addEventListener('resize', () => {
    currentIndex = 0;
    updateSliderPosition();
});

//youtube video
const videoContainer = document.querySelector('.video-container');
const youtubeVideo = document.getElementById('youtube-video');

// Video ID from the URL
const videoId = 'B6yrwO0y-6c';

// Construct the YouTube iframe URL
const youtubeUrl = `https://www.youtube.com/embed/${videoId}?autoplay=1&controls=1&showinfo=0`;

// Set the iframe source
youtubeVideo.src = youtubeUrl;

//inner html
// Get the element
const element = document.getElementById('email');

// Change the innerHTML
element.innerHTML = 'New content';



