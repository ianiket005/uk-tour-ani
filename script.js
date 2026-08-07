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

const geminiForm = document.getElementById('gemini-form');
const geminiInput = document.getElementById('gemini-input');
const geminiOutput = document.getElementById('gemini-output');

if (geminiForm && geminiInput && geminiOutput) {
  geminiForm.addEventListener('submit', function (e) {
    e.preventDefault();
    const query = geminiInput.value.trim().toLowerCase();

    const responses = [
      {
        keywords: ['couple', 'romantic', 'honeymoon', 'partner'],
        message: 'Gemini suggests Mussoorie for couples: candlelit dinners, sunset views above the valley, and quiet walks through deodar forests.'
      },
      {
        keywords: ['family', 'kids', 'children', 'safe'],
        message: 'Gemini suggests Nainital and Jim Corbett for families: boat rides, zoo visits, easy trails, and wildlife safaris.'
      },
      {
        keywords: ['adventure', 'rafting', 'trek', 'camp', 'skiing'],
        message: 'Gemini recommends Rishikesh and Auli for high-energy adventure: river rafting, cliff jumping, trekking, and snow sports.'
      },
      {
        keywords: ['spiritual', 'meditation', 'yoga', 'temple', 'ashram'],
        message: 'Gemini recommends Rishikesh and Haridwar for a spiritual journey with yoga, temple ceremonies, and peaceful Ganges views.'
      },
      {
        keywords: ['hidden', 'secret', 'quiet', 'offbeat'],
        message: 'Gemini highlights Kausani and Kanatal for offbeat escapes, tea gardens, mountain sunrises, and secluded hill viewpoints.'
      },
      {
        keywords: ['history', 'culture', 'heritage'],
        message: 'Gemini suggests exploring the ancient temple towns of Badrinath and the historic trading routes around Almora for culture and history.'
      }
    ];

    const selected = responses.find((item) => item.keywords.some((keyword) => query.includes(keyword)));

    geminiOutput.textContent = selected
      ? selected.message
      : 'Gemini recommends exploring the Kumaon and Garhwal regions for a balanced trip with nature, food, and local culture. Try asking about adventure, relaxation, history, or hidden gems.';

    geminiInput.value = '';
  });
}

