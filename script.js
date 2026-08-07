const menuBtn = document.querySelector('.menu-btn');
const navLinks = document.querySelector('.nav-links');
const form = document.getElementById('trip-form');
const formMessage = document.getElementById('form-message');
const plannerForm = document.getElementById('planner-form');
const plannerOutput = document.getElementById('planner-output');
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

if (plannerForm && plannerOutput) {
  plannerForm.addEventListener('submit', function (e) {
    e.preventDefault();
    const interest = document.getElementById('interest').value;

    const suggestions = {
      adventure: 'Try Rishikesh and Auli for rafting, trekking, and exciting snow adventures.',
      peace: 'Choose Nainital or Mussoorie for calm lakes, scenic views, and cozy stays.',
      family: 'A family-friendly trip to Jim Corbett and Nainital will be perfect for wildlife and easy sightseeing.',
      spiritual: 'Visit Rishikesh and Haridwar for temples, yoga, and peaceful spiritual experiences.'
    };

    plannerOutput.textContent = suggestions[interest] || 'Pick an option to see your perfect destination.';
  });
}

