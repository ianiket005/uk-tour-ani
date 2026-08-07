const menuBtn = document.querySelector('.menu-btn');
const navLinks = document.querySelector('.nav-links');
const form = document.getElementById('trip-form');
const formMessage = document.getElementById('form-message');
const yearSpan = document.getElementById('year');

if (yearSpan) {
  yearSpan.textContent = new Date().getFullYear();
}

if (menuBtn && navLinks) {
  menuBtn.addEventListener('click', () => {
    navLinks.classList.toggle('active');
  });
}

if (form) {
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    formMessage.textContent = 'Thank you! We will contact you soon.';
    form.reset();
  });
}
