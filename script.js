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

const mapContainer = document.getElementById('map');
const legendContainer = document.querySelector('.map-legend');

if (mapContainer && window.L) {
  const map = L.map('map', { scrollWheelZoom: false }).setView([30.0668, 79.0193], 8);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
  }).addTo(map);

  const destinations = [
    {
      name: 'Mussoorie',
      coords: [30.4590, 77.9680],
      description: 'Hill station with colonial charm and scenic viewpoints.'
    },
    {
      name: 'Nainital',
      coords: [29.3852, 79.4542],
      description: 'Famous lake town offering boat rides, gardens, and quiet walks.'
    },
    {
      name: 'Rishikesh',
      coords: [30.0869, 78.2676],
      description: 'Adventure, yoga, and spiritual vibes on the banks of the Ganges.'
    },
    {
      name: 'Auli',
      coords: [30.5785, 79.6410],
      description: 'Snowy slopes and alpine views for skiing and trekking.'
    },
    {
      name: 'Chopta',
      coords: [30.3751, 79.1293],
      description: 'Lush meadows and mountain trails in the Mini Switzerland of Uttarakhand.'
    },
    {
      name: 'Jim Corbett',
      coords: [29.5304, 78.7747],
      description: 'Wildlife sanctuary perfect for safari adventure and nature photography.'
    }
  ];

  const markers = {};

  destinations.forEach((destination) => {
    const marker = L.marker(destination.coords).addTo(map);
    marker.bindPopup(`<strong>${destination.name}</strong><br>${destination.description}`);
    markers[destination.name.toLowerCase()] = marker;

    if (legendContainer) {
      const button = document.createElement('button');
      button.type = 'button';
      button.textContent = destination.name;
      button.addEventListener('click', () => {
        map.setView(destination.coords, 11, { animate: true });
        marker.openPopup();
      });
      legendContainer.appendChild(button);
    }
  });
}
