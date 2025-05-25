// Mobile nav toggle
const menuBtn = document.getElementById('mobileMenuBtn');
const navLinks = document.getElementById('navLinks');
const header = document.querySelector('.header'); // Get the header element

// Scroll-to-top functionality
const scrollBtn = document.getElementById('scrollToTopBtn');

window.addEventListener('scroll', () => {
  const currentScrollTop = window.pageYOffset || document.documentElement.scrollTop;

  // Show/hide scroll-to-top button
  if (currentScrollTop > 300) { // If scrolled down more than 300px
    scrollBtn.classList.add('visible'); // Show the scroll-to-top button
  } else {
    scrollBtn.classList.remove('visible'); // Hide the scroll-to-top button
  }

  // Logic for showing/hiding the header on scroll
  const scrollThreshold = 150; // Distance to scroll down before header appears

  if (currentScrollTop > scrollThreshold) { // If scrolled past the threshold
    header.classList.add('visible-on-scroll'); // Add the class to make the header visible and keep it visible
  } else {
    header.classList.remove('visible-on-scroll'); // If at the top of the page (below threshold), hide the header
  }
});

menuBtn.addEventListener('click', () => { // Event listener for mobile menu button
  navLinks.classList.toggle('active'); // Toggles 'active' class on navigation links
});

scrollBtn.addEventListener('click', () => { // Event listener for scroll-to-top button
  window.scrollTo({ top: 0, behavior: 'smooth' }); // Scrolls smoothly to the top of the page
});