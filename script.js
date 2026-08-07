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

// Weather + Crowd widget for destination pages
document.addEventListener('DOMContentLoaded', () => {
  try {
    const path = window.location.pathname.replace(/\\\\/g, '/');
    const parts = path.split('/');
    const file = parts[parts.length - 1];
    const mapping = {
      'mussoorie.html': { lat: 30.4599, lon: 78.0666, peak: [3,4,5,9,10,11] },
      'nainital.html': { lat: 29.3919, lon: 79.4542, peak: [3,4,5,10,11] },
      'rishikesh.html': { lat: 30.0869, lon: 78.2676, peak: [9,10,11,2,3,4] },
      'auli.html': { lat: 30.4138, lon: 79.5276, peak: [11,12,1,2,3] },
      'chopta.html': { lat: 30.2976, lon: 79.0950, peak: [3,4,5,9,10,11] },
      'jim-corbett.html': { lat: 29.3860, lon: 79.2173, peak: [11,12,1,2,3,4,5,6] },
      'kanatal.html': { lat: 30.4670, lon: 78.1964, peak: [3,4,5,9,10,11] },
      'lansdowne.html': { lat: 29.7870, lon: 78.6120, peak: [3,4,5,10,11] },
      'naukuchiatal.html': { lat: 29.3833, lon: 79.5020, peak: [3,4,5,9,10,11] },
      'kausani.html': { lat: 29.7527, lon: 79.5750, peak: [3,4,5,10,11] },
      'barkot.html': { lat: 31.0041, lon: 78.4629, peak: [4,5,9,10] },
      'munsiyari.html': { lat: 29.8751, lon: 80.1034, peak: [5,6,7,8,9] },
      'almora.html': { lat: 29.5878, lon: 79.6204, peak: [3,4,5,10,11] },
      'ranikhet.html': { lat: 29.6260, lon: 79.4197, peak: [3,4,5,9,10,11] },
      'mukteshwar.html': { lat: 29.5058, lon: 79.6355, peak: [3,4,5,9,10,11] },
      'champawat.html': { lat: 29.2746, lon: 80.2526, peak: [3,4,5,9,10,11] },
      'pithoragarh.html': { lat: 29.5810, lon: 80.2215, peak: [3,4,5,9,10,11] },
      'binsar.html': { lat: 29.7040, lon: 79.5230, peak: [3,4,5,9,10,11] },
      'devalsari.html': { lat: 29.6390, lon: 79.4670, peak: [4,5,9,10] },
      'chaukori.html': { lat: 29.9833, lon: 80.0630, peak: [3,4,5,9,10,11] }
    };

    const info = mapping[file];
    if (!info) return;

    const details = document.querySelector('.destination-details');
    if (!details) return;

    const widget = document.createElement('div');
    widget.className = 'detail-card';
    widget.id = 'weather-crowd-widget';
    widget.innerHTML = `<h3>Live Weather & Crowd</h3><p id='wc-loading'>Loading weather and crowd data…</p>`;

    details.insertBefore(widget, details.firstChild);

    const url = `https://api.open-meteo.com/v1/forecast?latitude=${info.lat}&longitude=${info.lon}&current_weather=true`;

    fetch(url)
      .then((res) => res.json())
      .then((data) => {
        const cw = data.current_weather;
        const temp = cw?.temperature ?? 'N/A';
        const wind = cw?.windspeed ?? 'N/A';
        const code = cw?.weathercode ?? -1;
        const desc = weatherCodeToText(code);

        // crowd estimator based on peak months + weekend factor
        const month = new Date().getMonth() + 1;
        const day = new Date().getDay();
        let crowd = 'Low';
        if (info.peak.includes(month)) crowd = 'High';
        else if (info.peak.includes((month % 12) + 1) || info.peak.includes((month + 10) % 12 + 1)) crowd = 'Medium';
        // weekend bump
        if (day === 0 || day === 6 && crowd === 'Medium') crowd = 'High';
        else if (day === 0 || day === 6 && crowd === 'Low') crowd = 'Medium';

        const html = `<div class='weather-box'>
            <p><strong>Temperature:</strong> ${temp}°C</p>
            <p><strong>Conditions:</strong> ${desc}</p>
            <p><strong>Wind:</strong> ${wind} km/h</p>
            <p><strong>Estimated Crowd:</strong> <span id='crowd-level'>${crowd}</span></p>
          </div>`;

        widget.innerHTML = `<h3>Live Weather & Crowd</h3>${html}`;
      })
      .catch((err) => {
        widget.innerHTML = `<h3>Live Weather & Crowd</h3><p>Unable to load weather data.</p>`;
        console.error('Weather fetch error', err);
      });

    function weatherCodeToText(code) {
      const map = {
        0: 'Clear sky',
        1: 'Mainly clear',
        2: 'Partly cloudy',
        3: 'Overcast',
        45: 'Fog',
        48: 'Depositing rime fog',
        51: 'Light drizzle',
        53: 'Moderate drizzle',
        55: 'Dense drizzle',
        61: 'Slight rain',
        63: 'Moderate rain',
        65: 'Heavy rain',
        80: 'Rain showers',
        95: 'Thunderstorm'
      };
      return map[code] || 'Light rain/unknown';
    }
  } catch (e) {
    console.error('Weather widget error', e);
  }
});

// 360 viewer modal
document.addEventListener('click', (e) => {
  const btn = e.target.closest('.view-360-btn');
  if (!btn) return;
  const card = btn.closest('.gallery-card');
  const img = card && card.querySelector('img');
  if (!img) return;

  // create modal
  const modal = document.createElement('div');
  modal.className = 'pv-modal';
  modal.innerHTML = `
    <div class='pv-backdrop'></div>
    <div class='pv-viewer' role='dialog' aria-modal='true'>
      <button class='pv-close' aria-label='Close 360 view'>✕</button>
      <div class='pv-sphere' style="background-image: url('${img.src}')"></div>
    </div>`;
  document.body.appendChild(modal);

  const backdrop = modal.querySelector('.pv-backdrop');
  const close = modal.querySelector('.pv-close');
  const sphere = modal.querySelector('.pv-sphere');

  let isDown = false;
  let startX = 0;
  let posX = 50; // percent

  function updateBg() {
    sphere.style.backgroundPosition = `${posX}% 50%`;
  }

  sphere.addEventListener('mousedown', (ev) => {
    isDown = true; startX = ev.clientX;
    sphere.style.cursor = 'grabbing';
  });
  window.addEventListener('mouseup', () => { isDown = false; sphere.style.cursor = 'grab'; });
  window.addEventListener('mousemove', (ev) => {
    if (!isDown) return;
    const dx = ev.clientX - startX;
    startX = ev.clientX;
    posX = (posX - dx / 5) % 100;
    if (posX < 0) posX += 100;
    updateBg();
  });

  // touch
  sphere.addEventListener('touchstart', (ev) => { isDown = true; startX = ev.touches[0].clientX; });
  window.addEventListener('touchend', () => { isDown = false; });
  window.addEventListener('touchmove', (ev) => {
    if (!isDown) return;
    const dx = ev.touches[0].clientX - startX;
    startX = ev.touches[0].clientX;
    posX = (posX - dx / 5) % 100;
    if (posX < 0) posX += 100;
    updateBg();
  });

  backdrop.addEventListener('click', closeModal);
  close.addEventListener('click', closeModal);

  function closeModal() {
    document.body.removeChild(modal);
    // cleanup listeners (simpler approach: reload handlers removed with element)
  }

  // initial styles
  sphere.style.cursor = 'grab';
  sphere.style.backgroundPosition = '50% 50%';
});



