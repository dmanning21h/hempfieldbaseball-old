const navSlide = () => {
  const burger = document.querySelector('.burger');
  const nav = document.querySelector('.nav-links');
  const navLinks = document.querySelectorAll('.nav-links li');

  burger.addEventListener('click', () => {
    // Burger Animation
    burger.classList.toggle('toggle');

    // Nav Slide In
    nav.classList.toggle('nav-active');

    // Animate Links
    navLinks.forEach((link, index) => {
      if (link.style.animation) {
        link.style.animation = '';
      }
      else {
        link.style.animation = `navLinkFade 0.2s ease forwards ${(index / 8) + 0.05}s`
      }
    });
  });
}

navSlide();