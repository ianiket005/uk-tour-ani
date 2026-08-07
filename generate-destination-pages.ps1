$pages = @(
    @{File='mussoorie.html'; Title='Mussoorie'; Image='https://images.unsplash.com/photo-1501785888041-af3ef285b470?auto=format&fit=crop&w=1600&q=80'; Intro='A charming hill station with colonial charm, cool weather, and scenic mountain views.'; About='Mussoorie is a classic Uttarakhand destination known for its panoramic hills, winding trails, and vibrant Mall Road. Visitors enjoy viewpoints like Cloud’s End, Gun Hill, and Lal Tibba, along with cozy cafes and local handicrafts.'; Highlights='Mall Road promenade, Gun Hill cable car, Lal Tibba sunrise, Company Garden, Camel’s Back Road.'; BestTime='March to June and September to November for pleasant weather and clear skies.'; Reach='Drive from Dehradun (65 km) or travel by road from Rishikesh and Haridwar.'};
    @{File='nainital.html'; Title='Nainital'; Image='https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1600&q=80'; Intro='A serene lake town famous for its emerald Naini Lake and lively hill-side markets.'; About='Nainital sits beside a picturesque lake surrounded by forested hills. The town blends natural beauty with charming attractions like Snow View Point, Nainital Zoo, and cozy boat rides on the water.'; Highlights='Naini Lake boating, Snow View Point, Tiffin Top, Naina Devi Temple, Mall Road.'; BestTime='March to June and October to November when the weather is cool and dry.'; Reach='Accessible via Kathgodam railway station, then a 1.5-hour drive or taxi to Nainital.'};
    @{File='rishikesh.html'; Title='Rishikesh'; Image='https://images.unsplash.com/photo-1500375592092-40eb2168fd21?auto=format&fit=crop&w=1600&q=80'; Intro='The yoga capital of the world and adventure hub on the banks of the Ganges.'; About='Rishikesh blends spirituality and adventure, offering river rafting, yoga schools, ashrams, and serene riverside cafés. The town’s iconic bridges and temples draw pilgrims and globetrotters alike.'; Highlights='Laxman Jhula, Ram Jhula, Ganga Aarti, rafting on the Ganges, Beatles Ashram.'; BestTime='September to November and February to April are ideal for river activities and sightseeing.'; Reach='Train service to Haridwar then a 25-minute road transfer, or direct road access from Delhi and Dehradun.'};
    @{File='auli.html'; Title='Auli'; Image='https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1600&q=80'; Intro='A snow-clad ski destination with dramatic alpine meadows and mountain peaks.'; About='Auli is renowned for its skiing slopes, cable cars, and majestic views of Nanda Devi. It’s a winter sports paradise and a beautiful summer retreat for scenic walks.'; Highlights='Auli ski slopes, ropeway ride, Nanda Devi views, Gurso Bugyal meadows, Kuri Village.'; BestTime='November to February for skiing; April to June for pleasant weather and wildflowers.'; Reach='Drive from Joshimath (16 km) after reaching Rishikesh or Haridwar by road.'};
    @{File='chopta.html'; Title='Chopta'; Image='https://images.unsplash.com/photo-1501785888041-af3ef285b470?auto=format&fit=crop&w=1600&q=80'; Intro='A tranquil alpine meadow area known as the Mini Switzerland of India.'; About='Chopta is a quiet retreat surrounded by pine forests and snow-capped peaks. It serves as the base for the popular Tungnath temple trek and offers beautiful mountain scenery year-round.'; Highlights='Tungnath and Chandrashila treks, Deoria Tal, panoramic Himalayan views, wildflower meadows.'; BestTime='March to June and September to November for clear skies and pleasant hikes.'; Reach='Road access from Rishikesh via Rudraprayag and Ukhimath; the last stretch is through hilly roads.'};
    @{File='jim-corbett.html'; Title='Jim Corbett'; Image='https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1600&q=80'; Intro='India’s oldest national park, famous for tigers, safaris, and wilderness escapes.'; About='Jim Corbett National Park stretches across forested valleys and grasslands, offering wildlife safaris and nature stays. It’s ideal for spotting tigers, elephants, deer, and bird species.'; Highlights='Jeep safaris, elephant rides, birdwatching, Corbett Museum, Garjiya Devi Temple.'; BestTime='November to June when the park is open and wildlife sightings are best.'; Reach='Nearest railhead is Ramnagar, followed by a short taxi ride into the park.'};
    @{File='kanatal.html'; Title='Kanatal'; Image='https://images.unsplash.com/photo-1520722357030-ae4cc914e202?auto=format&fit=crop&w=1600&q=80'; Intro='A peaceful hill station perfect for quiet mountain views and apple orchards.'; About='Kanatal offers solitude and scenic beauty above Mussoorie, with pine forests, apple orchards, and a relaxed village feel. It is ideal for nature walks and small group retreats.'; Highlights='Surkanda Devi trek, Tehri Lake views, jungle stays, quiet forest trails.'; BestTime='March to June and September to November for crisp weather and clear skies.'; Reach='Accessible by road from Dehradun via Mussoorie and Dhanaulti.'};
    @{File='lansdowne.html'; Title='Lansdowne'; Image='https://images.unsplash.com/photo-1501425359018-03a3900cbd6a?auto=format&fit=crop&w=1600&q=80'; Intro='A serene cantonment town surrounded by oak and pine forests.'; About='Lansdowne is a quiet British-era hill station with walking trails, ancient churches, and a slow-paced atmosphere. It’s perfect for travelers seeking calm away from the busy tourist spots.'; Highlights='Bhulla Tal lake, Tip-in-Top viewpoint, St. Mary’s Church, trekking trails.'; BestTime='March to June and October to November for the best hill weather.'; Reach='Drive from Kotdwar or take a train to Kotdwar and then a short road journey.'};
    @{File='naukuchiatal.html'; Title='Naukuchiatal'; Image='https://images.unsplash.com/photo-1500534314209-a26d8f7e5a0d?auto=format&fit=crop&w=1600&q=80'; Intro='A calm lake destination known for birdwatching, boating, and lakeside peace.'; About='Naukuchiatal is a lesser-known lake town with a beautifully shaped nine-cornered lake. It offers a quiet alternative to nearby Nainital, with birdwatching and serene waters.'; Highlights='Boating, birdwatching, paragliding, lakeside walks, nature photography.'; BestTime='March to June and September to November for mild weather and bird activity.'; Reach='It is about 35 km from Kathgodam, followed by a short drive through hill roads.'};
    @{File='kausani.html'; Title='Kausani'; Image='https://images.unsplash.com/photo-1557804506-669a67965ba0?auto=format&fit=crop&w=1600&q=80'; Intro='A quiet tea town famous for panoramic Himalayan sunrise views.'; About='Kausani is known for its terraced tea gardens and spectacular vistas of Trisul and Nanda Devi. It is a peaceful spot for mountaintop walks and calm evenings.'; Highlights='Sunrise point, tea garden tours, Anasakti Ashram, Baijnath Temple.'; BestTime='March to June and October to November for clear mountain views.'; Reach='Accessible by road from Ranikhet and Almora, or by train to Kathgodam then by taxi.'};
    @{File='barkot.html'; Title='Barkot'; Image='https://images.unsplash.com/photo-1497806509691-f7bfc40b73ec?auto=format&fit=crop&w=1600&q=80'; Intro='A scenic valley town serving as the gateway to Yamunotri.'; About='Barkot sits on the banks of the Yamuna River with lush orchards and mountain views. It is a good staging point for pilgrimage routes and forest walks.'; Highlights='Yamunotri gateway, apple orchards, river beaches, local markets.'; BestTime='April to June and September to November for pleasant weather.'; Reach='Reachable by road from Dehradun via Mussoorie and Uttarkashi.'};
    @{File='munsiyari.html'; Title='Munsiyari'; Image='https://images.unsplash.com/photo-1500534623283-312aade485b7?auto=format&fit=crop&w=1600&q=80'; Intro='A remote village offering access to high Himalayan treks and snow vistas.'; About='Munsiyari is a base for treks toward Milam Glacier and Nanda Devi, with spectacular alpine meadows and mountain views. It is ideal for travelers seeking nature, hiking, and offbeat mountain culture.'; Highlights='Pangarchulla trek, Thamri Kund, birth place of glaciers, snow-capped peaks, local Kumaoni cuisine.'; BestTime='May to October, avoiding heavy monsoon months.'; Reach='Reachable by road from Kathgodam via Almora and Bageshwar.'};
    @{File='almora.html'; Title='Almora'; Image='https://images.unsplash.com/photo-1516483638261-f4dbaf036963?auto=format&fit=crop&w=1600&q=80'; Intro='A cultural town with ancient temples, arts, and countryside views.'; About='Almora is a lively Kumaoni town famous for its handicrafts, sunset points, and old-world charm. Its markets and temples reflect a rich hill culture and scenic mountain scenery.'; Highlights='Bright End Corner, Katarmal Sun Temple, local crafts, quiet walking lanes.'; BestTime='March to June and October to November for clear views and cool weather.'; Reach='By road from Ranikhet, Nainital, or Kathgodam.'};
    @{File='ranikhet.html'; Title='Ranikhet'; Image='https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1600&q=80'; Intro='A peaceful pine town with hill walks and scenic viewpoints.'; About='Ranikhet offers a gentle hill experience with forests, temples, and colonial-era charm. Its quiet roads and mountain views make it ideal for a relaxed getaway.'; Highlights='Golf Course, Jhoola Devi Temple, Chaubatia Gardens, Pine Hills.'; BestTime='March to June and September to November for cool, pleasant weather.'; Reach='Road access from Kathgodam, Haldwani, or Almora.'};
    @{File='mukteshwar.html'; Title='Mukteshwar'; Image='https://images.unsplash.com/photo-1546018100-0479d147f465?auto=format&fit=crop&w=1600&q=80'; Intro='A clifftop destination for stunning Himalayan sunrise and quiet treks.'; About='Mukteshwar sits on a cliff overlooking the Kumaon Himalayas. It is famous for long walks, birdwatching, and relaxed forest stays.'; Highlights='Mukteshwar Temple, Chauli Ki Jali, local orchards, nature trails.'; BestTime='March to June and September to November for the best skies and weather.'; Reach='Drive from Nainital, Almora, or Kathgodam via hill roads.'};
    @{File='champawat.html'; Title='Champawat'; Image='https://images.unsplash.com/photo-1500534314209-a26d8f7e5a0d?auto=format&fit=crop&w=1600&q=80'; Intro='A historic hill town with temples, terraced farms, and calm mountain life.'; About='Champawat is an ancient town with archaeological sites, historic temples, and lovely valley scenery. It is a peaceful stop for those exploring eastern Kumaon.'; Highlights='Baleshwar Temple, Anand Acharya Ashram, terraced fields, rugged hill trails.'; BestTime='March to June and September to November for clear weather.'; Reach='Accessible by road from Pithoragarh or Almora.'};
    @{File='pithoragarh.html'; Title='Pithoragarh'; Image='https://images.unsplash.com/photo-1501004318641-b39e6451bec6?auto=format&fit=crop&w=1600&q=80'; Intro='A scenic border town with Himalayan views and trekking access.'; About='Pithoragarh provides dramatic vistas of the eastern Himalayas and access to remote valleys. It is known for its historic fort and vibrant local markets.'; Highlights='Pithoragarh Fort, Kali River valley, Askot wildlife sanctuary, panoramic viewpoints.'; BestTime='March to June and September to November for bright mountain views.'; Reach='Road access from Almora, Tanakpur, and Kathgodam.'};
    @{File='binsar.html'; Title='Binsar'; Image='https://images.unsplash.com/photo-1518176258769-f227c798150e?auto=format&fit=crop&w=1600&q=80'; Intro='An oak forest sanctuary with birds, wildlife, and sweeping peak views.'; About='Binsar is a wildlife sanctuary known for its ancient oak forests and panoramic views of the Himalayas. It is a quiet place for nature walks, birdwatching, and mountain serenity.'; Highlights='Binsar Zero Point, Binsar Wildlife Sanctuary, forest trails, birdwatching, sunset viewpoints.'; BestTime='March to June and September to November for ideal trekking and wildlife watching.'; Reach='Drive from Almora or Ranikhet through forest roads.'};
    @{File='devalsari.html'; Title='Devalsari'; Image='https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1600&q=80'; Intro='A peaceful meadow village ideal for camping and forest walks.'; About='Devalsari is a calm glade surrounded by pine forests, offering a remote nature experience. It is perfect for camping, birdwatching, and forest exploration.'; Highlights='Camping, Devalsari lake, forest trails, quiet mountain views.'; BestTime='April to June and September to November for the best hiking weather.'; Reach='Road access from Ranikhet or Almora with a short hill drive.'};
    @{File='chaukori.html'; Title='Chaukori'; Image='https://images.unsplash.com/photo-1518105779142-d975f22f1b0d?auto=format&fit=crop&w=1600&q=80'; Intro='A quiet tea town with dramatic sunrise views over snow-capped peaks.'; About='Chaukori is famous for tea gardens and sunrise viewpoints overlooking the Panchachuli peaks. It is a lesser-known destination for travelers seeking calm and mountain charm.'; Highlights='Tea gardens, sunrise points, trekking, panoramic Himalayan views.'; BestTime='March to June and September to November for clear mountain vistas.'; Reach='Road access from Pithoragarh or Almora via quiet hill roads.'}
)

foreach ($page in $pages) {
    $content = @"
<!DOCTYPE html>
<html lang='en'>
  <head>
    <meta charset='UTF-8' />
    <meta name='viewport' content='width=device-width, initial-scale=1.0' />
    <title>$($page.Title) - Uttarakhand Tourism</title>
    <link rel='stylesheet' href='../styles.css' />
  </head>
  <body>
    <header class='hero' style='background-image: linear-gradient(180deg, rgba(15, 23, 42, 0.72), rgba(15, 23, 42, 0.22)), url("$($page.Image)"); background-position: center; background-size: cover;'>
      <nav class='navbar'>
        <a href='../index.html' class='logo'>Uttarakhand</a>
        <button class='menu-btn' aria-label='Toggle menu'>☰</button>
        <ul class='nav-links'>
          <li><a href='../index.html#destinations'>Destinations</a></li>
          <li><a href='../index.html#hidden-gems'>Hidden Gems</a></li>
          <li><a href='../index.html#ai-planner'>AI Planner</a></li>
          <li><a href='../index.html#contact'>Contact</a></li>
        </ul>
      </nav>

      <div class='hero-content'>
        <h1>$($page.Title)</h1>
        <p>$($page.Intro)</p>
        <a href='../index.html' class='btn'>Back to Home</a>
      </div>
    </header>

    <main>
      <section class='section alt-section'>
        <div class='card'>
          <h2>About $($page.Title)</h2>
          <p>$($page.About)</p>
        </div>
      </section>

      <section class='section'>
        <div class='feature-grid'>
          <div class='feature-card'>
            <h3>Highlights</h3>
            <p>$($page.Highlights)</p>
          </div>
          <div class='feature-card'>
            <h3>Best Time to Visit</h3>
            <p>$($page.BestTime)</p>
          </div>
          <div class='feature-card'>
            <h3>How to Reach</h3>
            <p>$($page.Reach)</p>
          </div>
        </div>
      </section>
    </main>

    <footer>
      <p>© <span id='year'></span> Uttarakhand Tourism. All rights reserved.</p>
      <p>Web Developer: Aniket Patel</p>
    </footer>

    <script src='../script.js'></script>
  </body>
</html>
"@
    Set-Content -Path (Join-Path $PWD 'destinations' $page.File) -Value $content -Encoding UTF8
}
