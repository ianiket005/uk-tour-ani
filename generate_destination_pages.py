from pathlib import Path

pages = [
    {
        'file': 'mussoorie.html',
        'title': 'Mussoorie',
        'image': 'https://images.unsplash.com/photo-1501785888041-af3ef285b470?auto=format&fit=crop&w=1600&q=80',
        'intro': 'A charming hill station with colonial charm, cool weather, and scenic mountain views.',
        'about': 'Mussoorie is a classic Uttarakhand destination known for its panoramic hills, winding trails, and vibrant Mall Road. Visitors enjoy viewpoints like Cloud’s End, Gun Hill, and Lal Tibba, along with cozy cafes and local handicrafts.',
        'highlights': 'Mall Road promenade, Gun Hill cable car, Lal Tibba sunrise, Company Garden, Camel’s Back Road.',
        'best_time': 'March to June and September to November for pleasant weather and clear skies.',
        'reach': 'Drive from Dehradun (65 km) or travel by road from Rishikesh and Haridwar.',
        'attractions': ['Lal Tibba sunrise viewpoint', 'Cable car ride to Gun Hill', 'Walk along Camel’s Back Road', 'Company Garden and boating', 'Shop local handicrafts on Mall Road'],
        'tips': ['Book hill-facing rooms for sunrise views.', 'Carry light woolens even in summer evenings.', 'Start early for popular viewpoints to avoid crowds.', 'Try local snacks like roasted corn and baked apples.'],
        'gallery': [
            {'image': 'https://images.unsplash.com/photo-1520697222861-a3a51f3b11b4?auto=format&fit=crop&w=1200&q=80', 'caption': 'Sunrise over Lal Tibba'},
            {'image': 'https://images.unsplash.com/photo-1500856056008-859079534e9e?auto=format&fit=crop&w=1200&q=80', 'caption': 'Mall Road evening stroll'},
            {'image': 'https://images.unsplash.com/photo-1483683804023-6ccdb62f86ef?auto=format&fit=crop&w=1200&q=80', 'caption': 'Cafes and crisp mountain air'}
        ]
    },
    {
        'file': 'nainital.html',
        'title': 'Nainital',
        'image': 'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1600&q=80',
        'intro': 'A serene lake town famous for its emerald Naini Lake and lively hill-side markets.',
        'about': 'Nainital sits beside a picturesque lake surrounded by forested hills. The town blends natural beauty with charming attractions like Snow View Point, Nainital Zoo, and cozy boat rides on the water.',
        'highlights': 'Naini Lake boating, Snow View Point, Tiffin Top, Naina Devi Temple, Mall Road.',
        'best_time': 'March to June and October to November when the weather is cool and dry.',
        'reach': 'Accessible via Kathgodam railway station, then a 1.5-hour drive or taxi to Nainital.',
        'attractions': ['Boat ride on Naini Lake', 'Panoramic view from Snow View Point', 'Visit Nainital Zoo', 'Sunset at Tiffin Top', 'Shop fresh fruits and handicrafts on Mall Road'],
        'tips': ['Take an early morning boat ride for peaceful lake views.', 'Carry warm clothing at night during winter months.', 'Use shared taxis to reach nearby viewpoints affordably.'],
        'gallery': [
            {'image': 'https://images.unsplash.com/photo-1524510182-6cc5792f2186?auto=format&fit=crop&w=1200&q=80', 'caption': 'Boating on Naini Lake'},
            {'image': 'https://images.unsplash.com/photo-1500534314209-a26d8f7e5a0d?auto=format&fit=crop&w=1200&q=80', 'caption': 'Snow View Point panorama'},
            {'image': 'https://images.unsplash.com/photo-1483683804023-6ccdb62f86ef?auto=format&fit=crop&w=1200&q=80', 'caption': 'Colorful market street'}
        ]
    },
    {
        'file': 'rishikesh.html',
        'title': 'Rishikesh',
        'image': 'https://images.unsplash.com/photo-1500375592092-40eb2168fd21?auto=format&fit=crop&w=1600&q=80',
        'intro': 'The yoga capital of the world and adventure hub on the banks of the Ganges.',
        'about': 'Rishikesh blends spirituality and adventure, offering river rafting, yoga schools, ashrams, and serene riverside cafés. The town’s iconic bridges and temples draw pilgrims and globetrotters alike.',
        'highlights': 'Laxman Jhula, Ram Jhula, Ganga Aarti, rafting on the Ganges, Beatles Ashram.',
        'best_time': 'September to November and February to April are ideal for river activities and sightseeing.',
        'reach': 'Train service to Haridwar then a 25-minute road transfer, or direct road access from Delhi and Dehradun.',
        'attractions': ['Attend evening Ganga Aarti at Triveni Ghat', 'Cross the crowd-free Ram Jhula', 'Explore Beatles Ashram ruins', 'Try river rafting on the Ganges', 'Practice yoga at a riverside ashram'],
        'tips': ['Book river rafting in advance during peak season.', 'Respect the spiritual atmosphere around temples and ghats.', 'Sample local chai and street food near the riverfront.'],
        'gallery': [
            {'image': 'https://images.unsplash.com/photo-1517821099609-1d8500d20b64?auto=format&fit=crop&w=1200&q=80', 'caption': 'Laxman Jhula by sunset'},
            {'image': 'https://images.unsplash.com/photo-1469924470255-d00c5b450d21?auto=format&fit=crop&w=1200&q=80', 'caption': 'Rafting on the Ganges'},
            {'image': 'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1200&q=80', 'caption': 'Riverside yoga session'}
        ]
    },
    {
        'file': 'auli.html',
        'title': 'Auli',
        'image': 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1600&q=80',
        'intro': 'A snow-clad ski destination with dramatic alpine meadows and mountain peaks.',
        'about': 'Auli is renowned for its skiing slopes, cable cars, and majestic views of Nanda Devi. It’s a winter sports paradise and a beautiful summer retreat for scenic walks.',
        'highlights': 'Auli ski slopes, ropeway ride, Nanda Devi views, Gurso Bugyal meadows, Kuri Village.',
        'best_time': 'November to February for skiing; April to June for pleasant weather and wildflowers.',
        'reach': 'Drive from Joshimath (16 km) after reaching Rishikesh or Haridwar by road.',
        'attractions': ['Ski on Auli slopes', 'Ride the cable car to Joshimath', 'Hike through Gurso Bugyal meadows', 'View sunrise over Nanda Devi', 'Visit the peaceful Kuri Village'],
        'tips': ['Carry warm, layered clothing during winter months.', 'Book ski equipment and instructors in advance.', 'Acclimatize gradually after arriving at higher altitude.'],
        'gallery': [
            {'image': 'https://images.unsplash.com/photo-1515817007009-6b7ac17e0a7c?auto=format&fit=crop&w=1200&q=80', 'caption': 'Ski slopes in Auli'},
            {'image': 'https://images.unsplash.com/photo-1516382799247-182fc6f46215?auto=format&fit=crop&w=1200&q=80', 'caption': 'Cable car view'},
            {'image': 'https://images.unsplash.com/photo-1500534314209-a26d8f7e5a0d?auto=format&fit=crop&w=1200&q=80', 'caption': 'Mountain sunrise at Auli'}
        ]
    },
    {
        'file': 'chopta.html',
        'title': 'Chopta',
        'image': 'https://images.unsplash.com/photo-1501785888041-af3ef285b470?auto=format&fit=crop&w=1600&q=80',
        'intro': 'A tranquil alpine meadow area known as the Mini Switzerland of India.',
        'about': 'Chopta is a quiet retreat surrounded by pine forests and snow-capped peaks. It serves as the base for the popular Tungnath temple trek and offers beautiful mountain scenery year-round.',
        'highlights': 'Tungnath and Chandrashila treks, Deoria Tal, panoramic Himalayan views, wildflower meadows.',
        'best_time': 'March to June and September to November for clear skies and pleasant hikes.',
        'reach': 'Road access from Rishikesh via Rudraprayag and Ukhimath; the last stretch is through hilly roads.',
        'attractions': ['Trek to Tungnath temple', 'Climb to Chandrashila summit', 'Visit Deoria Tal lake', 'Relax in pine forest cottages', 'Enjoy wildflower meadows during summer'],
        'tips': ['Start treks early to avoid afternoon weather changes.', 'Carry water and light snacks for the Chandrashila climb.', 'Book simple forest stays to enjoy the natural silence.'],
        'gallery': [
            {'image': 'https://images.unsplash.com/photo-1519125323398-675f0ddb6308?auto=format&fit=crop&w=1200&q=80', 'caption': 'Pine forest trails in Chopta'},
            {'image': 'https://images.unsplash.com/photo-1470770841072-f978cf4d019e?auto=format&fit=crop&w=1200&q=80', 'caption': 'Tungnath trek views'},
            {'image': 'https://images.unsplash.com/photo-1439396087961-98bc12c21176?auto=format&fit=crop&w=1200&q=80', 'caption': 'Deoria Tal reflections'}
        ]
    },
    {
        'file': 'jim-corbett.html',
        'title': 'Jim Corbett',
        'image': 'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1600&q=80',
        'intro': 'India’s oldest national park, famous for tigers, safaris, and wilderness escapes.',
        'about': 'Jim Corbett National Park stretches across forested valleys and grasslands, offering wildlife safaris and nature stays. It’s ideal for spotting tigers, elephants, deer, and bird species.',
        'highlights': 'Jeep safaris, elephant rides, birdwatching, Corbett Museum, Garjiya Devi Temple.',
        'best_time': 'November to June when the park is open and wildlife sightings are best.',
        'reach': 'Nearest railhead is Ramnagar, followed by a short taxi ride into the park.',
        'attractions': ['Morning jeep safari for tigers', 'Visit Dhikala or Bijrani zones', 'Go birdwatching at sunrise', 'Explore the Corbett Museum', 'Walk to the scenic Garjiya Devi Temple'],
        'tips': ['Book safari permits early in peak season.', 'Carry binoculars and insect repellent.', 'Respect park rules and keep noise to a minimum.'],
        'gallery': [
            {'image': 'https://images.unsplash.com/photo-1486308510493-aa64833637c7?auto=format&fit=crop&w=1200&q=80', 'caption': 'Jeep safari in the jungle'},
            {'image': 'https://images.unsplash.com/photo-1499395237500-9176d2ce008a?auto=format&fit=crop&w=1200&q=80', 'caption': 'Wildlife watching at sunrise'},
            {'image': 'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1200&q=80', 'caption': 'Lush forest trails'}
        ]
    },
    {
        'file': 'kanatal.html',
        'title': 'Kanatal',
        'image': 'https://images.unsplash.com/photo-1520722357030-ae4cc914e202?auto=format&fit=crop&w=1600&q=80',
        'intro': 'A peaceful hill station perfect for quiet mountain views and apple orchards.',
        'about': 'Kanatal offers solitude and scenic beauty above Mussoorie, with pine forests, apple orchards, and a relaxed village feel. It is ideal for nature walks and small group retreats.',
        'highlights': 'Surkanda Devi trek, Tehri Lake views, jungle stays, quiet forest trails.',
        'best_time': 'March to June and September to November for crisp weather and clear skies.',
        'reach': 'Accessible by road from Dehradun via Mussoorie and Dhanaulti.',
        'attractions': ['Hike to Surkanda Devi temple', 'Stroll through apple orchards', 'Watch the sunset over Tehri Lake', 'Stay in a forest cottage', 'Explore nearby Dhanaulti attractions'],
        'tips': ['Use a local guide for safe forest walks.', 'Bring sunscreen and warm layers for mornings.', 'Enjoy local Kumaoni cuisine at small eateries.'],
        'gallery': [
            {'image': 'https://images.unsplash.com/photo-1517487881594-2787fef5ebf7?auto=format&fit=crop&w=1200&q=80', 'caption': 'Quiet forest cottage at Kanatal'},
            {'image': 'https://images.unsplash.com/photo-1514996937319-344454492b37?auto=format&fit=crop&w=1200&q=80', 'caption': 'Apple orchard pathways'},
            {'image': 'https://images.unsplash.com/photo-1517777170478-778e5e2624b3?auto=format&fit=crop&w=1200&q=80', 'caption': 'Golden hour over the hills'}
        ]
    },
    {
        'file': 'lansdowne.html',
        'title': 'Lansdowne',
        'image': 'https://images.unsplash.com/photo-1501425359018-03a3900cbd6a?auto=format&fit=crop&w=1600&q=80',
        'intro': 'A serene cantonment town surrounded by oak and pine forests.',
        'about': 'Lansdowne is a quiet British-era hill station with walking trails, ancient churches, and a slow-paced atmosphere. It’s perfect for travelers seeking calm away from the busy tourist spots.',
        'highlights': 'Bhulla Tal lake, Tip-in-Top viewpoint, St. Mary’s Church, trekking trails.',
        'best_time': 'March to June and October to November for the best hill weather.',
        'reach': 'Drive from Kotdwar or take a train to Kotdwar and then a short road journey.',
        'attractions': ['Boating at Bhulla Tal', 'Hike to Tip-in-Top viewpoint', 'Visit St. Mary’s Church', 'Watch birdlife in the forest', 'Relax at the quiet cantonment walkways'],
        'tips': ['Carry rain protection during monsoon.', 'Book a stay near Bhulla Tal for easier access to walks.', 'Keep the pace slow to enjoy the calm ambiance.'],
        'gallery': [
            {'image': 'https://images.unsplash.com/photo-1493244040629-496f6d136cc3?auto=format&fit=crop&w=1200&q=80', 'caption': 'Boat ride on Bhulla Tal'},
            {'image': 'https://images.unsplash.com/photo-1494526585095-c41746248156?auto=format&fit=crop&w=1200&q=80', 'caption': 'Forest trail in Lansdowne'},
            {'image': 'https://images.unsplash.com/photo-1517865445835-95fb86cdf35f?auto=format&fit=crop&w=1200&q=80', 'caption': 'Tip-in-Top viewpoint'}
        ]
    },
    {
        'file': 'naukuchiatal.html',
        'title': 'Naukuchiatal',
        'image': 'https://images.unsplash.com/photo-1500534314209-a26d8f7e5a0d?auto=format&fit=crop&w=1600&q=80',
        'intro': 'A calm lake destination known for birdwatching, boating, and lakeside peace.',
        'about': 'Naukuchiatal is a lesser-known lake town with a beautifully shaped nine-cornered lake. It offers a quiet alternative to nearby Nainital, with birdwatching and serene waters.',
        'highlights': 'Boating, birdwatching, paragliding, lakeside walks, nature photography.',
        'best_time': 'March to June and September to November for mild weather and bird activity.',
        'reach': 'It is about 35 km from Kathgodam, followed by a short drive through hill roads.',
        'attractions': ['Boat ride around the nine-cornered lake', 'Birdwatching on the lakeshore', 'Try paragliding over the valley', 'Take a nature walk at sunrise', 'Capture reflections on calm waters'],
        'tips': ['Stay in a lakeside cottage for the best views.', 'Bring binoculars for the birds at dawn.', 'Combine Naukuchiatal with a visit to nearby Bhimtal.'],
        'gallery': [
            {'image': 'https://images.unsplash.com/photo-1493558103817-58b2924bce98?auto=format&fit=crop&w=1200&q=80', 'caption': 'Lakeside morning in Naukuchiatal'},
            {'image': 'https://images.unsplash.com/photo-1517821099609-1d8500d20b64?auto=format&fit=crop&w=1200&q=80', 'caption': 'Birdwatching by the shore'},
            {'image': 'https://images.unsplash.com/photo-1493558103817-0a04f2f2dc02?auto=format&fit=crop&w=1200&q=80', 'caption': 'Peaceful water reflections'}
        ]
    },
    {
        'file': 'kausani.html',
        'title': 'Kausani',
        'image': 'https://images.unsplash.com/photo-1557804506-669a67965ba0?auto=format&fit=crop&w=1600&q=80',
        'intro': 'A quiet tea town famous for panoramic Himalayan sunrise views.',
        'about': 'Kausani is known for its terraced tea gardens and spectacular vistas of Trisul and Nanda Devi. It is a peaceful spot for mountaintop walks and calm evenings.',
        'highlights': 'Sunrise point, tea garden tours, Anasakti Ashram, Baijnath Temple.',
        'best_time': 'March to June and October to November for clear mountain views.',
        'reach': 'Accessible by road from Ranikhet and Almora, or by train to Kathgodam then by taxi.',
        'attractions': ['Watch sunrise over the Himalayas', 'Walk through tea gardens', 'Visit Anasakti Ashram', 'Explore ancient Baijnath Temple', 'Relax at panoramic viewpoints'],
        'tips': ['Wake early for the sunrise panorama.', 'Pack layers for chilly hill mornings.', 'Enjoy locally grown tea at a garden estate.'],
        'gallery': [
            {'image': 'https://images.unsplash.com/photo-1445820138746-1f1b423f7a31?auto=format&fit=crop&w=1200&q=80', 'caption': 'Tea terraces in Kausani'},
            {'image': 'https://images.unsplash.com/photo-1500534314209-a26d8f7e5a0d?auto=format&fit=crop&w=1200&q=80', 'caption': 'Himalayan panoramic view'},
            {'image': 'https://images.unsplash.com/photo-1494526585095-c41746248156?auto=format&fit=crop&w=1200&q=80', 'caption': 'Sunset behind mountain ridges'}
        ]
    },
    {
        'file': 'barkot.html',
        'title': 'Barkot',
        'image': 'https://images.unsplash.com/photo-1497806509691-f7bfc40b73ec?auto=format&fit=crop&w=1600&q=80',
        'intro': 'A scenic valley town serving as the gateway to Yamunotri.',
        'about': 'Barkot sits on the banks of the Yamuna River with lush orchards and mountain views. It is a good staging point for pilgrimage routes and forest walks.',
        'highlights': 'Yamunotri gateway, apple orchards, river beaches, local markets.',
        'best_time': 'April to June and September to November for pleasant weather.',
        'reach': 'Reachable by road from Dehradun via Mussoorie and Uttarkashi.',
        'attractions': ['Walk along the Yamuna River', 'Explore apple orchards', 'Visit local temples and markets', 'Use Barkot as a base for Yamunotri pilgrimage'],
        'tips': ['Choose a riverside hotel for calm views.', 'Carry comfortable shoes for local walks.', 'Plan early travel for the mountain route to Yamunotri.'],
        'gallery': [
            {'image': 'https://images.unsplash.com/photo-1500534314209-a26d8f7e5a0d?auto=format&fit=crop&w=1200&q=80', 'caption': 'Yamuna river valley views'},
            {'image': 'https://images.unsplash.com/photo-1494526585095-c41746248156?auto=format&fit=crop&w=1200&q=80', 'caption': 'Riverside orchard walk'},
            {'image': 'https://images.unsplash.com/photo-1445820138746-1f1b423f7a31?auto=format&fit=crop&w=1200&q=80', 'caption': 'Evening valley glow'}
        ]
    },
    {
        'file': 'munsiyari.html',
        'title': 'Munsiyari',
        'image': 'https://images.unsplash.com/photo-1500534623283-312aade485b7?auto=format&fit=crop&w=1600&q=80',
        'intro': 'A remote village offering access to high Himalayan treks and snow vistas.',
        'about': 'Munsiyari is a base for treks toward Milam Glacier and Nanda Devi, with spectacular alpine meadows and mountain views. It is ideal for travelers seeking nature, hiking, and offbeat mountain culture.',
        'highlights': 'Pangarchulla trek, Thamri Kund, glacier views, local Kumaoni cuisine.',
        'best_time': 'May to October, avoiding heavy monsoon months.',
        'reach': 'Reachable by road from Kathgodam via Almora and Bageshwar.',
        'attractions': ['Watch the sunrise over Nanda Devi peaks', 'Trek to Thamri Kund', 'Visit local villages and markets', 'Explore alpine meadows and glaciers'],
        'tips': ['Acclimatize properly before high-altitude treks.', 'Hire local guides for glacier routes.', 'Pack warm layers and sturdy trekking shoes.'],
        'gallery': [
            {'image': 'https://images.unsplash.com/photo-1483683804023-6ccdb62f86ef?auto=format&fit=crop&w=1200&q=80', 'caption': 'Mountain village at dawn'},
            {'image': 'https://images.unsplash.com/photo-1470770841072-f978cf4d019e?auto=format&fit=crop&w=1200&q=80', 'caption': 'Hiking trail in the Himalayas'},
            {'image': 'https://images.unsplash.com/photo-1494526585095-c41746248156?auto=format&fit=crop&w=1200&q=80', 'caption': 'Snow-capped peak views'}
        ]
    },
    {
        'file': 'almora.html',
        'title': 'Almora',
        'image': 'https://images.unsplash.com/photo-1516483638261-f4dbaf036963?auto=format&fit=crop&w=1600&q=80',
        'intro': 'A cultural town with ancient temples, arts, and countryside views.',
        'about': 'Almora is a lively Kumaoni town famous for its handicrafts, sunset points, and old-world charm. Its markets and temples reflect a rich hill culture and scenic mountain scenery.',
        'highlights': 'Bright End Corner, Katarmal Sun Temple, local crafts, quiet walking lanes.',
        'best_time': 'March to June and October to November for clear views and cool weather.',
        'reach': 'By road from Ranikhet, Nainital, or Kathgodam.',
        'attractions': ['Watch sunset from Bright End Corner', 'Visit Katarmal Sun Temple', 'Shop handmade shawls and pottery', 'Explore quiet lanes and local cafés'],
        'tips': ['Carry a camera for sunset viewpoints.', 'Taste local Kumaoni dishes such as bhatt ki churkani.', 'Stay near the Mall Road area for easy access to attractions.'],
        'gallery': [
            {'image': 'https://images.unsplash.com/photo-1497806509691-f7bfc40b73ec?auto=format&fit=crop&w=1200&q=80', 'caption': 'Almora valley viewpoint'},
            {'image': 'https://images.unsplash.com/photo-1516483638261-f4dbaf036963?auto=format&fit=crop&w=1200&q=80', 'caption': 'Traditional Kumaoni streets'},
            {'image': 'https://images.unsplash.com/photo-1514996937319-344454492b37?auto=format&fit=crop&w=1200&q=80', 'caption': 'Sunset over the hills'}
        ]
    },
    {
        'file': 'ranikhet.html',
        'title': 'Ranikhet',
        'image': 'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1600&q=80',
        'intro': 'A peaceful pine town with hill walks and scenic viewpoints.',
        'about': 'Ranikhet offers a gentle hill experience with forests, temples, and colonial-era charm. Its quiet roads and mountain views make it ideal for a relaxed getaway.',
        'highlights': 'Golf Course, Jhoola Devi Temple, Chaubatia Gardens, Pine Hills.',
        'best_time': 'March to June and September to November for cool, pleasant weather.',
        'reach': 'Road access from Kathgodam, Haldwani, or Almora.',
        'attractions': ['Visit the Ranikhet Golf Course', 'Walk through Chaubatia Gardens', 'Explore Jhoola Devi Temple', 'Enjoy forest walks and viewpoints'],
        'tips': ['Carry comfortable walking shoes for trails.', 'Keep a rain jacket handy during shoulder season.', 'Book a stay close to the main market for convenience.'],
        'gallery': [
            {'image': 'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1200&q=80', 'caption': 'Pine hill walk in Ranikhet'},
            {'image': 'https://images.unsplash.com/photo-1501425359018-03a3900cbd6a?auto=format&fit=crop&w=1200&q=80', 'caption': 'Chaubatia Gardens greenery'},
            {'image': 'https://images.unsplash.com/photo-1494526585095-c41746248156?auto=format&fit=crop&w=1200&q=80', 'caption': 'Sunset over the cantonment town'}
        ]
    },
    {
        'file': 'mukteshwar.html',
        'title': 'Mukteshwar',
        'image': 'https://images.unsplash.com/photo-1546018100-0479d147f465?auto=format&fit=crop&w=1600&q=80',
        'intro': 'A clifftop destination for stunning Himalayan sunrise and quiet treks.',
        'about': 'Mukteshwar sits on a cliff overlooking the Kumaon Himalayas. It is famous for long walks, birdwatching, and relaxed forest stays.',
        'highlights': 'Mukteshwar Temple, Chauli Ki Jali, local orchards, nature trails.',
        'best_time': 'March to June and September to November for the best skies and weather.',
        'reach': 'Drive from Nainital, Almora, or Kathgodam via hill roads.',
        'attractions': ['See panoramic views from Chauli Ki Jali', 'Visit the old Mukteshwar Temple', 'Explore organic orchards', 'Walk along forest trails at sunrise'],
        'tips': ['Stay in a cliffside cottage for dramatic views.', 'Bring binoculars for birdwatching.', 'Avoid trekking after dark on narrow paths.'],
        'gallery': [
            {'image': 'https://images.unsplash.com/photo-1470770841072-f978cf4d019e?auto=format&fit=crop&w=1200&q=80', 'caption': 'Cliffside sunrise view'},
            {'image': 'https://images.unsplash.com/photo-1500534314209-a26d8f7e5a0d?auto=format&fit=crop&w=1200&q=80', 'caption': 'Forest path near Mukteshwar'},
            {'image': 'https://images.unsplash.com/photo-1494526585095-c41746248156?auto=format&fit=crop&w=1200&q=80', 'caption': 'Quiet hill outlook'}
        ]
    },
    {
        'file': 'champawat.html',
        'title': 'Champawat',
        'image': 'https://images.unsplash.com/photo-1500534314209-a26d8f7e5a0d?auto=format&fit=crop&w=1600&q=80',
        'intro': 'A historic hill town with temples, terraced farms, and calm mountain life.',
        'about': 'Champawat is an ancient town with archaeological sites, historic temples, and lovely valley scenery. It is a peaceful stop for those exploring eastern Kumaon.',
        'highlights': 'Baleshwar Temple, Anand Acharya Ashram, terraced fields, rugged hill trails.',
        'best_time': 'March to June and September to November for clear weather.',
        'reach': 'Accessible by road from Pithoragarh or Almora.',
        'attractions': ['Visit Baleshwar Temple', 'Explore the old market', 'Walk the terraced fields', 'Relax at local ashrams and viewpoints'],
        'tips': ['Hire a local guide for temple history tours.', 'Carry water and sun protection for hill walks.', 'Enjoy simple local foods in the town market.'],
        'gallery': [
            {'image': 'https://images.unsplash.com/photo-1500534314209-a26d8f7e5a0d?auto=format&fit=crop&w=1200&q=80', 'caption': 'Terraced farming valleys'},
            {'image': 'https://images.unsplash.com/photo-1494526585095-c41746248156?auto=format&fit=crop&w=1200&q=80', 'caption': 'Historic temple steps'},
            {'image': 'https://images.unsplash.com/photo-1445820138746-1f1b423f7a31?auto=format&fit=crop&w=1200&q=80', 'caption': 'Peaceful hill village'}
        ]
    },
    {
        'file': 'pithoragarh.html',
        'title': 'Pithoragarh',
        'image': 'https://images.unsplash.com/photo-1501004318641-b39e6451bec6?auto=format&fit=crop&w=1600&q=80',
        'intro': 'A scenic border town with Himalayan views and trekking access.',
        'about': 'Pithoragarh provides dramatic vistas of the eastern Himalayas and access to remote valleys. It is known for its historic fort and vibrant local markets.',
        'highlights': 'Pithoragarh Fort, Kali River valley, Askot wildlife sanctuary, panoramic viewpoints.',
        'best_time': 'March to June and September to November for bright mountain views.',
        'reach': 'Road access from Almora, Tanakpur, and Kathgodam.',
        'attractions': ['Visit the historic Pithoragarh Fort', 'Walk the Kali River valley', 'Shop in the lively town market', 'Use Pithoragarh as a base for Askot wildlife trips'],
        'tips': ['Allow time to acclimatize after the road journey.', 'Explore local cuisine at tea shops near the market.', 'Carry camera gear for dramatic Himalayan vistas.'],
        'gallery': [
            {'image': 'https://images.unsplash.com/photo-1455390582262-044cdead277a?auto=format&fit=crop&w=1200&q=80', 'caption': 'View from a mountain fort'},
            {'image': 'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1200&q=80', 'caption': 'River valley landscape'},
            {'image': 'https://images.unsplash.com/photo-1494526585095-c41746248156?auto=format&fit=crop&w=1200&q=80', 'caption': 'Market street ambience'}
        ]
    },
    {
        'file': 'binsar.html',
        'title': 'Binsar',
        'image': 'https://images.unsplash.com/photo-1518176258769-f227c798150e?auto=format&fit=crop&w=1600&q=80',
        'intro': 'An oak forest sanctuary with birds, wildlife, and sweeping peak views.',
        'about': 'Binsar is a wildlife sanctuary known for its ancient oak forests and panoramic views of the Himalayas. It is a quiet place for nature walks, birdwatching, and mountain serenity.',
        'highlights': 'Binsar Zero Point, Binsar Wildlife Sanctuary, forest trails, birdwatching, sunset viewpoints.',
        'best_time': 'March to June and September to November for ideal trekking and wildlife watching.',
        'reach': 'Drive from Almora or Ranikhet through forest roads.',
        'attractions': ['Take a sunrise hike to Zero Point', 'Spot birds and small wildlife on forest trails', 'Visit Binsar Wildlife Sanctuary', 'Relax at the sanctuary viewpoint for mountain views'],
        'tips': ['Hire a local guide for the sanctuary trails.', 'Bring binoculars and a field guide for bird species.', 'Book a wildlife lodge for early-morning access.'],
        'gallery': [
            {'image': 'https://images.unsplash.com/photo-1518176258769-f227c798150e?auto=format&fit=crop&w=1200&q=80', 'caption': 'Oak forest trail'},
            {'image': 'https://images.unsplash.com/photo-1494526585095-c41746248156?auto=format&fit=crop&w=1200&q=80', 'caption': 'Sunrise over the sanctuary'},
            {'image': 'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1200&q=80', 'caption': 'Mountain viewpoint in Binsar'}
        ]
    },
    {
        'file': 'devalsari.html',
        'title': 'Devalsari',
        'image': 'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1600&q=80',
        'intro': 'A peaceful meadow village ideal for camping and forest walks.',
        'about': 'Devalsari is a calm glade surrounded by pine forests, offering a remote nature experience. It is perfect for camping, birdwatching, and forest exploration.',
        'highlights': 'Camping, Devalsari lake, forest trails, quiet mountain views.',
        'best_time': 'April to June and September to November for the best hiking weather.',
        'reach': 'Road access from Ranikhet or Almora with a short hill drive.',
        'attractions': ['Camp near Devalsari lake', 'Walk through cedar and pine forests', 'Enjoy valley views at sunrise', 'Spot birds and seasonal flowers'],
        'tips': ['Reserve a camping site ahead of the season.', 'Carry a warm sleeping bag for chilly nights.', 'Respect the natural surroundings and keep the area clean.'],
        'gallery': [
            {'image': 'https://images.unsplash.com/photo-1494526585095-c41746248156?auto=format&fit=crop&w=1200&q=80', 'caption': 'Camping in Devalsari'},
            {'image': 'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1200&q=80', 'caption': 'Forest trail path'},
            {'image': 'https://images.unsplash.com/photo-1445820138746-1f1b423f7a31?auto=format&fit=crop&w=1200&q=80', 'caption': 'Dawn light through pines'}
        ]
    },
    {
        'file': 'chaukori.html',
        'title': 'Chaukori',
        'image': 'https://images.unsplash.com/photo-1518105779142-d975f22f1b0d?auto=format&fit=crop&w=1600&q=80',
        'intro': 'A quiet tea town with dramatic sunrise views over snow-capped peaks.',
        'about': 'Chaukori is famous for tea gardens and sunrise viewpoints overlooking the Panchachuli peaks. It is a lesser-known destination for travelers seeking calm and mountain charm.',
        'highlights': 'Tea gardens, sunrise points, trekking, panoramic Himalayan views.',
        'best_time': 'March to June and September to November for clear mountain vistas.',
        'reach': 'Road access from Pithoragarh or Almora via quiet hill roads.',
        'attractions': ['Watch sunrise over Panchachuli peaks', 'Walk through tea plantations', 'Visit quiet hamlets and viewpoints', 'Enjoy local Kumaoni tea and snacks'],
        'tips': ['Wake early for the sunrise viewpoint.', 'Carry a light jacket for cool mornings.', 'Book homestays close to the tea gardens.'],
        'gallery': [
            {'image': 'https://images.unsplash.com/photo-1494526585095-c41746248156?auto=format&fit=crop&w=1200&q=80', 'caption': 'Tea garden terraces'},
            {'image': 'https://images.unsplash.com/photo-1470770841072-f978cf4d019e?auto=format&fit=crop&w=1200&q=80', 'caption': 'Morning mountain view'},
            {'image': 'https://images.unsplash.com/photo-1445820138746-1f1b423f7a31?auto=format&fit=crop&w=1200&q=80', 'caption': 'Quiet hill road'}
        ]
    }
]

root = Path('c:/Users/Aniket Patel/Desktop/uk tour 2')
dest_dir = root / 'destinations'
dest_dir.mkdir(parents=True, exist_ok=True)

for page in pages:
    gallery_html = '\n'.join(
        f"          <div class='gallery-card'>\n            <img src='{item['image']}' alt='{item['caption']}' />\n            <h4>{item['caption']}</h4>\n          </div>"
        for item in page['gallery']
    )
    attractions_html = '\n'.join(f"<li>{item}</li>" for item in page['attractions'])
    tips_html = '\n'.join(f"<li>{item}</li>" for item in page['tips'])

    file_path = dest_dir / page['file']
    page_html = f"""<!DOCTYPE html>
<html lang='en'>
  <head>
    <meta charset='UTF-8' />
    <meta name='viewport' content='width=device-width, initial-scale=1.0' />
    <title>{page['title']} - Uttarakhand Tourism</title>
    <link rel='stylesheet' href='../styles.css' />
  </head>
  <body>
    <header class='hero' style='background-image: linear-gradient(180deg, rgba(15, 23, 42, 0.72), rgba(15, 23, 42, 0.22)), url("{page['image']}"); background-position: center; background-size: cover;'>
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
        <h1>{page['title']}</h1>
        <p>{page['intro']}</p>
        <a href='../index.html' class='btn'>Back to Home</a>
      </div>
    </header>
    <main>
      <section class='section alt-section'>
        <div class='card'>
          <h2>About {page['title']}</h2>
          <p>{page['about']}</p>
        </div>
      </section>

      <section class='section'>
        <div class='destination-details'>
          <div class='detail-card'>
            <h3>Highlights</h3>
            <p>{page['highlights']}</p>
          </div>
          <div class='detail-card'>
            <h3>Best Time to Visit</h3>
            <p>{page['best_time']}</p>
          </div>
          <div class='detail-card'>
            <h3>How to Reach</h3>
            <p>{page['reach']}</p>
          </div>
          <div class='detail-card'>
            <h3>Top Attractions</h3>
            <ul>{attractions_html}</ul>
          </div>
          <div class='detail-card'>
            <h3>Travel Tips</h3>
            <ul>{tips_html}</ul>
          </div>
        </div>
      </section>

      <section class='section alt-section destination-gallery'>
        <h2>Photo Gallery</h2>
        <div class='gallery-grid'>
{gallery_html}
        </div>
      </section>
    </main>

    <footer>
      <p>© <span id='year'></span> Uttarakhand Tourism. All rights reserved.</p>
      <p>Web Developer: Aniket Patel</p>
    </footer>
    <script src='../script.js'></script>
  </body>
</html>"""

    file_path.write_text(page_html, encoding='utf-8')

print('Generated', len(pages), 'destination pages in', dest_dir)
