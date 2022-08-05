const navSlide = () => {
  const burger = document.querySelector('.burger');
  const nav = document.querySelector('.nav__list');
  const navLinks = document.querySelectorAll('.nav__link');

  burger.addEventListener('click', () => {
    // Burger Animation
    burger.classList.toggle('burger--toggle');

    // Nav Slide In
    nav.classList.toggle('nav__list--active');

    // Animate Links
    navLinks.forEach((link, index) => {
      if (link.style.animation) {
        link.style.animation = '';
      }
      else {
        link.style.animation = `navLinkFade 0.35s ease forwards ${(index / 8) + 0.05}s`
      }
    });
  });
}

navSlide();