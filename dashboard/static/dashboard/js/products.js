// Kaimono shared product catalog — used by both the shop and the game detail page.
window.KAIMONO_PRODUCTS = [
  {
    id: 1, name: "NieR:Automata™ GOTY Edition", brand: "Square Enix", category: "games", type: "Action RPG", price: 19.99, originalPrice: 39.99, rating: 4.9, reviews: 2400, stock: "In stock · Ships in 24h", badges: ["-50%", "Summer"],
    image: "https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=400&q=80", popularity: 95, date: "2026-07-15",
    description: "The award-winning action RPG from PlatinumGames, now in its Game of the Year edition. Fight through a shattered world as android 2B in a breathtaking, melancholy story about machines, humanity and what it means to be alive.",
    releaseDate: "March 8, 2026", developer: "PlatinumGames", publisher: "Square Enix",
    tags: ["Action", "RPG", "Singleplayer", "Great Soundtrack", "Futuristic", "Cyberpunk"],
    media: [
      { type: "video", src: "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4", poster: "https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=1200&q=80",
      label: "Official Launch Trailer" },
    ],
    screenshots: [
      "https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=1200&q=80",
      "https://images.unsplash.com/photo-1563089145-599997674d42?auto=format&fit=crop&w=1200&q=80",
      "https://images.unsplash.com/photo-1547394765-185e1e68f34e?auto=format&fit=crop&w=1200&q=80",
      "https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=1200&q=80"
    ],
    friends: [
      { name: "shiro_kun", status: "owns", avatar: "https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=80&q=80" },
      { name: "hana_illustrator", status: "wants", avatar: "https://images.unsplash.com/photo-1547394765-185e1e68f34e?auto=format&fit=crop&w=80&q=80" },
      { name: "ren_dev", status: "owns", avatar: "https://images.unsplash.com/photo-1563089145-599997674d42?auto=format&fit=crop&w=80&q=80" }
    ],
    bundles: [
      { name: "Gameplay Bundle", price: 29.99, originalPrice: 49.99, includes: ["Base game", "Official OST — Chiptune Edition"], type: "bundle" },
      { name: "Collector's Edition", price: 79.99, originalPrice: 99.99, includes: ["GOTY Edition", "SteelBook case", "Artbook", "Acrylic pin"], type: "edition" },
      { name: "Automata DLC Pack", price: 9.99, originalPrice: 14.99, includes: ["DLC 3C3C1D119440927", "Costume pack"], type: "dlc" }
    ]
  },
  {
    id: 2, name: "Honkai: Star Rail Collector's Edition", brand: "HoYoverse", category: "games", type: "Turn-based RPG", price: 59.99, originalPrice: null, rating: 4.7, reviews: 1800, stock: "Pre-order · Ships Dec 2026", badges: ["New"],
    image: "https://images.unsplash.com/photo-1563089145-599997674d42?auto=format&fit=crop&w=400&q=80", popularity: 88, date: "2026-08-01",
    description: "Ride the Astral Express across the stars in HoYoverse's turn-based space fantasy. Collector's Edition ships with a full-color artbook, a pinned server soundtrack, and exclusive in-game redemption codes.",
    releaseDate: "December 15, 2026", developer: "HoYoverse", publisher: "HoYoverse",
    tags: ["Turn-based", "RPG", "Sci-Fi", "Fantasy", "Singleplayer"],
    media: [
      { type: "video", src: "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4", poster: "https://images.unsplash.com/photo-1563089145-599997674d42?auto=format&fit=crop&w=1200&q=80", label: "Star Rail — Launch Trailer" }
    ],
    screenshots: [
      "https://images.unsplash.com/photo-1563089145-599997674d42?auto=format&fit=crop&w=1200&q=80",
      "https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=1200&q=80",
      "https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=1200&q=80"
    ],
    friends: [
      { name: "hana_illustrator", status: "wants", avatar: "https://images.unsplash.com/photo-1547394765-185e1e68f34e?auto=format&fit=crop&w=80&q=80" },
      { name: "shiro_kun", status: "wants", avatar: "https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=80&q=80" }
    ],
    bundles: [
      { name: "Deluxe Edition", price: 79.99, originalPrice: null, includes: ["Collector's Edition", "Early access — 3 days early", "Digital artbook vol. 2"], type: "edition" }
    ]
  },
  {
    id: 3, name: "Genshin Impact 1/7 Scale PVC Figure", brand: "Anime Collectibles", category: "figures", type: "PVC Statue", price: 99.99, originalPrice: 129.99, rating: 4.9, reviews: 890, stock: "Release: Jan 2027", badges: ["Pre-Order"],
    image: "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?auto=format&fit=crop&w=400&q=80", popularity: 92, date: "2026-06-20",
    description: "A lovingly sculpted 1/7 scale PVC figure with a full display base. Pre-order ships worldwide in January 2027, wrapped in double-boxed collector-grade packaging with authenticity certificate.",
    releaseDate: "January 2027", developer: "HoYoverse", publisher: "Anime Collectibles",
    tags: ["Figure", "Pre-Order", "Collectible", "1/7 Scale"],
    media: [],
    screenshots: [
      "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?auto=format&fit=crop&w=1200&q=80",
      "https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=1200&q=80"
    ],
    friends: [
      { name: "shiro_kun", status: "wants", avatar: "https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=80&q=80" }
    ],
    bundles: []
  },
  {
    id: 4, name: "Persona 3 Reload Premium Hoodie", brand: "Official Apparel", category: "apparel", type: "Cotton Hoodie", price: 34.99, originalPrice: 49.99, rating: 4.6, reviews: 3100, stock: "In stock · 4 sizes", badges: ["-30%", "Bestseller"],
    image: "https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=400&q=80", popularity: 97, date: "2026-05-10",
    description: "Heavyweight cotton hoodie with the SEES emblem pressed on the chest. Official merchandise, machine-washable, available in S–XL.",
    releaseDate: "In stock now", developer: "ATLUS", publisher: "Official Apparel",
    tags: ["Apparel", "Unisex", "Cotton"],
    media: [],
    screenshots: [
      "https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=1200&q=80"
    ],
    friends: [],
    bundles: []
  },
  {
    id: 5, name: "Monster Hunter World: Iceborne Master", brand: "CAPCOM", category: "games", type: "Action", price: 9.89, originalPrice: 29.99, rating: 4.8, reviews: 5600, stock: "In stock · Ships in 24h", badges: ["-67%"],
    image: "https://images.unsplash.com/photo-1547394765-185e1e68f34e?auto=format&fit=crop&w=400&q=80", popularity: 85, date: "2025-12-01",
    description: "Master Edition bundles the base game and the massive Iceborne expansion. Hunt elder dragons in the Hoarfrost Reach with a full Master Rank campaign and new mounting mechanics.",
    releaseDate: "December 2025", developer: "CAPCOM", publisher: "CAPCOM",
    tags: ["Action", "Multiplayer", "Co-op", "Open World", "Hunting"],
    media: [
      { type: "video", src: "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/Sintel.mp4", poster: "https://images.unsplash.com/photo-1547394765-185e1e68f34e?auto=format&fit=crop&w=1200&q=80", label: "Iceborne Launch Trailer" }
    ],
    screenshots: [
      "https://images.unsplash.com/photo-1547394765-185e1e68f34e?auto=format&fit=crop&w=1200&q=80",
      "https://images.unsplash.com/photo-1563089145-599997674d42?auto=format&fit=crop&w=1200&q=80",
      "https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=1200&q=80"
    ],
    friends: [
      { name: "ren_dev", status: "owns", avatar: "https://images.unsplash.com/photo-1563089145-599997674d42?auto=format&fit=crop&w=80&q=80" },
      { name: "shiro_kun", status: "owns", avatar: "https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=80&q=80" },
      { name: "hana_illustrator", status: "wants", avatar: "https://images.unsplash.com/photo-1547394765-185e1e68f34e?auto=format&fit=crop&w=80&q=80" }
    ],
    bundles: [
      { name: "Iceborne Master Bundles", price: 9.89, originalPrice: 29.99, includes: ["Full Game", "Iceborne Expansion"], type: "bundle" },
      { name: "Mega Deluxe Kit", price: 24.99, originalPrice: 39.99, includes: ["Iceborne Master", "Handler Costume pack", "Samurai pose set"], type: "edition" }
    ]
  },
  {
    id: 6, name: "Hatsune Miku Nendoroid 15th Anniversary", brand: "Good Smile", category: "figures", type: "Nendoroid", price: 79.99, originalPrice: null, rating: 5.0, reviews: 4200, stock: "Only 12 left", badges: ["Limited"],
    image: "https://images.unsplash.com/photo-1563089145-599997674d42?auto=format&fit=crop&w=400&q=80", popularity: 99, date: "2026-04-15",
    description: "Celebrating 15 years of the world's most famous virtual singer with an anniversary nendoroid — three face plates, two buns, and a glow-scan hand-knitted scarf.",
    releaseDate: "April 15, 2026", developer: "Crypton Future Media", publisher: "Good Smile Company",
    tags: ["Nendoroid", "Limited", "Vocaloid", "Figure"],
    media: [],
    screenshots: [
      "https://images.unsplash.com/photo-1563089145-599997674d42?auto=format&fit=crop&w=1200&q=80",
      "https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=1200&q=80"
    ],
    friends: [
      { name: "hana_illustrator", status: "owns", avatar: "https://images.unsplash.com/photo-1547394765-185e1e68f34e?auto=format&fit=crop&w=80&q=80" },
      { name: "shiro_kun", status: "wants", avatar: "https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=80&q=80" }
    ],
    bundles: []
  },
  {
    id: 7, name: "Vintage Anime Art T-Shirt Collection", brand: "Official Apparel", category: "apparel", type: "Unisex Tee", price: 19.99, originalPrice: 24.99, rating: 4.4, reviews: 612, stock: "In stock · Unisex", badges: ["-20%"],
    image: "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?auto=format&fit=crop&w=400&q=80", popularity: 72, date: "2026-03-20",
    description: "A retro anime-print unisex crew neck in soft-washed cotton. This drop celebrates the hand-drawn era with three limited prints.",
    releaseDate: "In stock now", developer: "various", publisher: "Official Apparel",
    tags: ["Apparel", "Unisex", "Retro"],
    media: [],
    screenshots: [
      "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?auto=format&fit=crop&w=1200&q=80"
    ],
    friends: [],
    bundles: []
  },
  {
    id: 8, name: "Acrylic Keychain Collection Set (8 pcs)", brand: "Accessories", category: "accessories", type: "Acrylic", price: 12.99, originalPrice: null, rating: 4.9, reviews: 7800, stock: "In stock · Ships in 24h", badges: ["Bestseller"],
    image: "https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=400&q=80", popularity: 94, date: "2026-02-28",
    description: "Eight enamel-backed acrylic keychains of the full fictional idol lineup. A quick way to spell your favourite show in satchel flair.",
    releaseDate: "In stock now", developer: "SEGA", publisher: "Accessories",
    tags: ["Accessory", "Acrylic", "Set"],
    media: [],
    screenshots: [
      "https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=1200&q=80",
      "https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=1200&q=80"
    ],
    friends: [],
    bundles: []
  },
  {
    id: 9, name: "Project Sekai Colorful Stage! Soundtrack", brand: "Sega", category: "accessories", type: "CD + Booklet", price: 29.99, originalPrice: null, rating: 4.8, reviews: 1200, stock: "In stock", badges: ["New"],
    image: "https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=400&q=80", popularity: 80, date: "2026-07-01",
    description: "The piano-pressed Colorful Stage! original soundtrack with a full-color lyric booklet from the Secret Garden records garage.",
    releaseDate: "July 1, 2026", developer: "SEGA Colorful Palette", publisher: "Sega Music",
    tags: ["Soundtrack", "Music", "Collectible"],
    media: [],
    screenshots: [
      "https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=1200&q=80",
      "https://images.unsplash.com/photo-1547394765-185e1e68f34e?auto=format&fit=crop&w=1200&q=80"
    ],
    friends: [
      { name: "hana_illustrator", status: "owns", avatar: "https://images.unsplash.com/photo-1547394765-185e1e68f34e?auto=format&fit=crop&w=80&q=80" }
    ],
    bundles: []
  },
  {
    id: 10, name: "Chainsaw Man Power Scale Figure", brand: "Bandai", category: "figures", type: "1/8 Scale", price: 149.99, originalPrice: 179.99, rating: 4.9, reviews: 650, stock: "Pre-order · Feb 2027", badges: ["Pre-Order", "-17%"],
    image: "https://images.unsplash.com/photo-1547394765-185e1e68f34e?auto=format&fit=crop&w=400&q=80", popularity: 87, date: "2026-06-15",
    description: "A limited pre-order of Power in her chainsaw-fiend pose, 1/8 scale with swap, shirt and optional part pieces. Ships February 2027.",
    releaseDate: "February 2027", developer: "MAPPA", publisher: "Bandai Spirits",
    tags: ["Figure", "1/8 Scale", "Pre-Order", "Collectible"],
    media: [],
    screenshots: [
      "https://images.unsplash.com/photo-1547394765-185e1e68f34e?auto=format&fit=crop&w=1200&q=80",
      "https://images.unsplash.com/photo-1563089145-599997674d42?auto=format&fit=crop&w=1200&q=80"
    ],
    friends: [
      { name: "shiro_kun", status: "wants", avatar: "https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=80&q=80" },
      { name: "ren_dev", status: "owns", avatar: "https://images.unsplash.com/photo-1563089145-599997674d42?auto=format&fit=crop&w=80&q=80" }
    ],
    bundles: []
  },
  {
    id: 11, name: "Elden Ring Shadow of the Erdtree DLC", brand: "FromSoftware", category: "games", type: "Expansion", price: 39.99, originalPrice: null, rating: 4.8, reviews: 8900, stock: "In stock · Digital", badges: ["Hot"],
    image: "https://images.unsplash.com/photo-1563089145-599997674d42?auto=format&fit=crop&w=400&q=80", popularity: 96, date: "2026-05-20",
    description: "Explore the Land of Shadow in FromSoftware's acclaimed Elden Ring expansion, adding a colossal new region, 40+ weapons, and a host of terrifying bosses.",
    releaseDate: "May 2026", developer: "FromSoftware", publisher: "Bandai Namco",
    tags: ["Action RPG", "Soulslike", "Singleplayer", "Open World"],
    media: [
      { type: "video", src: "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/TearsOfSteel.mp4", poster: "https://images.unsplash.com/photo-1563089145-599997674d42?auto=format&fit=crop&w=1200&q=80", label: "Shadow Trailer" }
    ],
    screenshots: [
      "https://images.unsplash.com/photo-1563089145-599997674d42?auto=format&fit=crop&w=1200&q=80",
      "https://images.unsplash.com/photo-1547394765-185e1e68f34e?auto=format&fit=crop&w=1200&q=80",
      "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?auto=format&fit=crop&w=1200&q=80"
    ],
    friends: [
      { name: "ren_dev", status: "owns", avatar: "https://images.unsplash.com/photo-1563089145-599997674d42?auto=format&fit=crop&w=80&q=80" },
      { name: "shiro_kun", status: "owns", avatar: "https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=80&q=80" },
      { name: "hana_illustrator", status: "wants", avatar: "https://images.unsplash.com/photo-1547394765-185e1e68f34e?auto=format&fit=crop&w=80&q=80" }
    ],
    bundles: [
      { name: "Base Game Pack", price: 49.99, originalPrice: 59.99, includes: ["Elden Ring", "Shadow of the Erdtree DLC"], type: "edition" },
      { name: "Season Pass", price: 39.99, originalPrice: null, includes: ["Shadow of the Erdtree", "Future content drop"], type: "edition" }
    ]
  },
  {
    id: 12, name: "Jujutsu Kaisen Sukuna Hoodie Black", brand: "Crunchyroll", category: "apparel", type: "Premium Cotton", price: 54.99, originalPrice: 69.99, rating: 4.7, reviews: 2100, stock: "In stock · 5 sizes", badges: ["-21%"],
    image: "https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=400&q=80", popularity: 89, date: "2026-04-01",
    description: "A premium-cotton black hoodie with the King of Curses' domain-mark print and a ribbed kangaroo pocket.",
    releaseDate: "In stock now", developer: "MAPPA", publisher: "Crunchyroll",
    tags: ["Apparel", "Unisex", "Premium"],
    media: [],
    screenshots: [
      "https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=1200&q=80",
      "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?auto=format&fit=crop&w=1200&q=80"
    ],
    friends: [],
    bundles: []
  }
];

// ============================================================================
// Stage 3 & 4 enrichment — consumed by game_detail.html only.
// Keyed by product id so the shop catalog above stays untouched.
// Fields: about, keyFeatures, features (Steam), dlc, requirements,
//         accolades, metacritic, reviewSummary, userReviews.
// ============================================================================
(function () {
  var A1 = "https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=80&q=80";
  var A2 = "https://images.unsplash.com/photo-1547394765-185e1e68f34e?auto=format&fit=crop&w=80&q=80";
  var A3 = "https://images.unsplash.com/photo-1563089145-599997674d42?auto=format&fit=crop&w=80&q=80";

  var EXTRA = {
    1: {
      about: [
        "In the year 11945, the alien-invaded Earth has been abandoned by humanity. Androids 2B, 9S and A2 are deployed to reclaim the planet from the machine lifeforms that now rule it — and to uncover the truth buried beneath the endless war.",
        "NieR:Automata blends PlatinumGames' signature fast-paced 3D combat with a deeply philosophical story told across 26 different endings. Every weapon, pod program and chip upgrade unlocks new ways to fight, while the haunting soundtrack by Keiichi Okabe carries you through the ruined cityscapes.",
        "This Game of the Year edition includes the full base game, the 3C3C1D119440927 DLC arenas, and every bonus costume from the original release — the definitive way to experience Yoko Taro's masterpiece."
      ],
      keyFeatures: [
        "Precision 3D action combat by PlatinumGames",
        "26 endings across a branching narrative",
        "Pod programs, chips and weapon upgrades",
        "Award-winning orchestral soundtrack",
        "Full GOTY content — DLC arenas included",
        "Multiple difficulty modes for every player"
      ],
      features: ["achievements", "cloud", "controller", "trading-cards", "singleplayer"],
      dlc: [
        { name: "3C3C1D119440927 — Secret Arena DLC", price: 9.99, originalPrice: 14.99, desc: "Three hidden arena challenges with exclusive boss fights and cosmetic rewards.", date: "Released" }
      ],
      requirements: {
        minimum: { os: "Windows 10 64-bit", cpu: "Intel Core i5-2400 / AMD FX-6300", ram: "6 GB RAM", gpu: "NVIDIA GeForce GTX 760 / AMD Radeon R9 270X", directx: "DirectX 11", storage: "50 GB available space" },
        recommended: { os: "Windows 10/11 64-bit", cpu: "Intel Core i7-3770 / AMD Ryzen 5 1600", ram: "8 GB RAM", gpu: "NVIDIA GeForce GTX 980 / AMD Radeon RX 480", directx: "DirectX 11", storage: "50 GB SSD" }
      },
      accolades: [
        { outlet: "Famitsu", score: "39/40", quote: "A masterpiece of action and storytelling that stays with you long after the credits roll." },
        { outlet: "IGN", score: "9.0", quote: "Brilliant combat wrapped around a story that keeps you thinking even when you're not playing." },
        { outlet: "GameSpot", score: "9/10", quote: "An unforgettable journey that earns every ounce of its praise." }
      ],
      metacritic: 91,
      reviewSummary: "Overwhelmingly Positive",
      userReviews: [
        { author: "shiro_kun", avatar: A1, date: "2026-08-16", hours: 92.4, lang: "en", positive: true, text: "Third playthrough and it still hits differently. Route B changing the perspective on everything is genius. The soundtrack is the best I've ever heard in a game.", helpful: 214 },
        { author: "hana_illustrator", avatar: A2, date: "2026-08-11", hours: 47.8, lang: "ja", positive: true, text: "ヨコオタロウの世界観に完全に心を掴まれました。エンディングまでの物語が美しく、泣きました。", helpful: 158 },
        { author: "ren_dev", avatar: A3, date: "2026-08-04", hours: 121.9, lang: "en", positive: true, text: "All 26 endings done. The combat is fluid, the hacking minigame is actually fun, and 2B is an all-time great protagonist. Runs flawlessly on my rig.", helpful: 96 },
        { author: "nina_v", avatar: A2, date: "2026-07-21", hours: 3.2, lang: "fr", positive: false, text: "Très beau jeu mais le port PC demande un correctif pour les textures. Attendez une mise à jour avant d'acheter.", helpful: 43 },
        { author: "kaito_gamer", avatar: A1, date: "2026-07-09", hours: 8.9, lang: "en", positive: true, text: "Got it on sale — worth every penny. The DLC arenas are brutal but rewarding. Don't skip the side quests, they matter.", helpful: 61 },
        { author: "sofia_plays", avatar: A3, date: "2026-06-27", hours: 55.3, lang: "es", positive: true, text: "La combinación de acción y filosofía es única. Las misiones secundarias amplían la historia de forma increíble.", helpful: 37 },
        { author: "max_hours", avatar: A1, date: "2026-06-14", hours: 210, lang: "de", positive: true, text: "Über 200 Stunden und immer noch neue Dialoge entdeckt. Ein Spiel, das man zweimal spielen MUSS.", helpful: 52 },
        { author: "lily_k", avatar: A2, date: "2026-06-02", hours: 0.7, lang: "zh", positive: false, text: "开场动画很美，但我的老显卡带不动，退款了。等升级配置后再来。", helpful: 12 }
      ]
    },
    2: {
      about: [
        "Step aboard the Astral Express and journey across a universe where gods, dreams and corporate warfare collide. Honkai: Star Rail is HoYoverse's turn-based space fantasy, where every planet holds its own civilization, crisis and cast of unforgettable Trailblazers.",
        "The Collector's Edition ships with a full-color artbook, a pinned server soundtrack and exclusive in-game redemption codes — the ultimate package for Trailblazers who want to own a piece of the journey before launch day."
      ],
      keyFeatures: [
        "Deep turn-based combat with elemental synergies",
        "Explore the worlds of Jarilo-VI, the Luofu and beyond",
        "Collector's Edition with exclusive redemption codes",
        "Full-color 120-page artbook included",
        "Pinned server soundtrack in collector packaging"
      ],
      features: ["achievements", "cloud", "controller", "multiplayer", "singleplayer"],
      dlc: [
        { name: "Digital Artbook Vol. 2", price: 4.99, originalPrice: null, desc: "Behind-the-scenes concept art for the Penacony arc.", date: "Pre-order bonus" },
        { name: "The Nameless — Official Soundtrack", price: 9.99, originalPrice: null, desc: "48-track digital soundtrack by HOYO-MiX.", date: "Available now" }
      ],
      requirements: {
        minimum: { os: "Windows 10 64-bit", cpu: "Intel Core i3 / AMD Ryzen 3", ram: "8 GB RAM", gpu: "Intel UHD Graphics 630 / GeForce GTX 650", directx: "DirectX 11", storage: "20 GB available space" },
        recommended: { os: "Windows 10/11 64-bit", cpu: "Intel Core i5 / AMD Ryzen 5", ram: "16 GB RAM", gpu: "NVIDIA GeForce GTX 1060 / AMD Radeon RX 580", directx: "DirectX 11", storage: "20 GB SSD" }
      },
      accolades: [
        { outlet: "IGN", score: "8.7", quote: "A gorgeous turn-based RPG with a surprising amount of heart hidden under its gacha surface." },
        { outlet: "PC Gamer", score: "88", quote: "Easily the most generous and polished space-fantasy of the year." },
        { outlet: "Eurogamer", score: "Essential", quote: "A collector's edition that actually respects the collector." }
      ],
      metacritic: 85,
      reviewSummary: "Very Positive",
      userReviews: [
        { author: "hana_illustrator", avatar: A2, date: "2026-08-15", hours: 31.2, lang: "ja", positive: true, text: "アートブックのクオリティが最高！ゲーム本編が待ちきれません。", helpful: 89 },
        { author: "stellar_rail", avatar: A3, date: "2026-08-09", hours: 12.4, lang: "en", positive: true, text: "The collector's packaging is gorgeous and the artbook is worth it alone. Codes redeemed without issues.", helpful: 64 },
        { author: "shiro_kun", avatar: A1, date: "2026-07-30", hours: 0, lang: "en", positive: true, text: "Pre-ordered the moment it went up. HoYoverse never misses with limited editions.", helpful: 77 },
        { author: "momo_k", avatar: A2, date: "2026-07-19", hours: 45.6, lang: "zh", positive: true, text: "限定版的做工很精致，OST 也很有收藏价值。", helpful: 33 },
        { author: "terra_x", avatar: A3, date: "2026-07-05", hours: 2.8, lang: "es", positive: false, text: "El envío tardó más de lo esperado, aunque el producto llegó en perfecto estado.", helpful: 8 },
        { author: "pixel_queen", avatar: A1, date: "2026-06-18", hours: 67, lang: "en", positive: true, text: "Beta tested the combat — it's addictive. This edition is a must for collectors.", helpful: 51 }
      ]
    },
    3: {
      about: [
        "A lovingly sculpted 1/7 scale figure with a full display base, capturing every detail of the character's iconic look.",
        "Pre-orders ship worldwide in January 2027, wrapped in double-boxed collector-grade packaging with an authenticity certificate."
      ],
      keyFeatures: [
        "1/7 scale with full display base",
        "Authenticity certificate included",
        "Double-boxed collector packaging",
        "Worldwide shipping from January 2027"
      ],
      reviewSummary: "Loved by Collectors",
      userReviews: [
        { author: "figure_otaku", avatar: A1, date: "2026-08-10", hours: null, lang: "en", positive: true, text: "Incredible sculpt quality, paintwork is flawless. Packing was double-boxed exactly as promised.", helpful: 91 },
        { author: "miku_fan_9", avatar: A2, date: "2026-07-22", hours: null, lang: "ja", positive: true, text: "細部の造形が美しい。写真より実物の方がいい。", helpful: 54 },
        { author: "kolektor_k", avatar: A3, date: "2026-06-15", hours: null, lang: "en", positive: false, text: "Base arrived slightly warped, but support sent a replacement within a week.", helpful: 17 }
      ]
    },
    4: {
      about: [
        "Heavyweight cotton hoodie with the SEES emblem pressed on the chest. Official merchandise, machine-washable and available in sizes S–XL.",
        "Printed and pressed in small batches to keep the emblem crisp wash after wash."
      ],
      keyFeatures: [
        "Official ATLUS merchandise",
        "Heavyweight cotton fleece",
        "Machine washable, print-safe",
        "Available in sizes S–XL"
      ],
      reviewSummary: "Highly Rated",
      userReviews: [
        { author: "sees_member", avatar: A1, date: "2026-08-06", hours: null, lang: "en", positive: true, text: "Heavyweight cotton, print is crisp. Fits true to size.", helpful: 132 },
        { author: "ryoji_tanaka", avatar: A2, date: "2026-07-14", hours: null, lang: "ja", positive: true, text: "生地が厚くて暖かい。プリントも剥がれにくそう。", helpful: 48 },
        { author: "lazy_days", avatar: A3, date: "2026-06-20", hours: null, lang: "en", positive: false, text: "Slightly smaller than expected — size up if you're between sizes.", helpful: 22 }
      ]
    },
    5: {
      about: [
        "The Master Edition bundles the critically acclaimed Monster Hunter: World with the massive Iceborne expansion. Travel to the Hoarfrost Reach, a frozen frontier of new monsters, Master Rank quests and the all-new clutch claw.",
        "Hunt alone or with up to three friends in seamless co-op. Every weapon gains new moves, every monster has a tempered variant, and the endgame Guiding Lands will keep hunters busy for hundreds of hours."
      ],
      keyFeatures: [
        "Full base game + Iceborne expansion",
        "New Hoarfrost Reach region and endemic life",
        "Master Rank quests and tempered monsters",
        "Clutch claw — new mounted combat mechanic",
        "Seamless 4-player online co-op"
      ],
      features: ["achievements", "cloud", "controller", "trading-cards", "multiplayer"],
      dlc: [
        { name: "Iceborne Deluxe Kit", price: 14.99, originalPrice: 19.99, desc: "Handler costume, Samurai pose set and exclusive weapon pendants.", date: "Available now" }
      ],
      requirements: {
        minimum: { os: "Windows 10 64-bit", cpu: "Intel Core i3-8350K / AMD Ryzen 3 2200G", ram: "8 GB RAM", gpu: "NVIDIA GeForce GTX 1060 6GB / AMD Radeon RX 570", directx: "DirectX 11", storage: "48 GB available space" },
        recommended: { os: "Windows 10 64-bit", cpu: "Intel Core i7-3770 / AMD Ryzen 5 1500X", ram: "16 GB RAM", gpu: "NVIDIA GeForce GTX 1660 / AMD Radeon RX 580", directx: "DirectX 11", storage: "48 GB SSD" }
      },
      accolades: [
        { outlet: "GameSpot", score: "9/10", quote: "Iceborne is everything a great expansion should be — bigger, bolder and endlessly replayable." },
        { outlet: "Eurogamer", score: "Essential", quote: "The co-op hunting loop remains one of gaming's greatest pleasures." },
        { outlet: "PC Gamer", score: "90", quote: "Hundreds of hours of content in a single, generous package." }
      ],
      metacritic: 90,
      reviewSummary: "Very Positive",
      userReviews: [
        { author: "ren_dev", avatar: A3, date: "2026-08-17", hours: 340.5, lang: "en", positive: true, text: "Iceborne doubles the game. The clutch claw took a while to learn but once it clicks, hunts feel amazing. 500 hours and counting.", helpful: 301 },
        { author: "shiro_kun", avatar: A1, date: "2026-08-12", hours: 88.9, lang: "en", positive: true, text: "Best value in the franchise. Base game plus expansion for this price is a steal.", helpful: 145 },
        { author: "hunter_anya", avatar: A2, date: "2026-08-03", hours: 26.4, lang: "ja", positive: true, text: "モンハン史上最高の拡張。新モンスターはどれも個性的で、装備集めが止まらない。", helpful: 88 },
        { author: "brutus_big", avatar: A1, date: "2026-07-24", hours: 152.7, lang: "de", positive: true, text: "Das Guiding-Lands-Endgame ist purer Zeitvertreib. Koop funktioniert einwandfrei.", helpful: 42 },
        { author: "yuki_snow", avatar: A3, date: "2026-07-11", hours: 6.1, lang: "zh", positive: false, text: "新手引导对没玩过系列的玩家不太友好，需要看很多教程视频。", helpful: 19 },
        { author: "carta_blanca", avatar: A2, date: "2026-06-30", hours: 74.2, lang: "es", positive: true, text: "El endgame es infinito. Perfecto para jugar con amigos.", helpful: 27 },
        { author: "leo_ko", avatar: A1, date: "2026-06-08", hours: 0.4, lang: "fr", positive: false, text: "Impossible de lancer sans modifier les fichiers de configuration sur mon ancien PC.", helpful: 11 }
      ]
    },
    6: {
      about: [
        "Celebrating 15 years of the world's most famous virtual singer, this anniversary nendoroid includes three face plates, two buns and a glow-scan hand-knitted scarf.",
        "An official Good Smile release with the usual impeccable paintwork and posing freedom."
      ],
      keyFeatures: [
        "15th anniversary exclusive",
        "3 interchangeable face plates",
        "Glow-scan knitted scarf accessory",
        "Official Good Smile release"
      ],
      reviewSummary: "Fan Favorite",
      userReviews: [
        { author: "chibi_collector", avatar: A2, date: "2026-08-12", hours: null, lang: "ja", positive: true, text: "15周年記念の出来がすごい。表情パーツが3つも付いて大満足。", helpful: 77 },
        { author: "vocaloid_ol", avatar: A1, date: "2026-07-25", hours: null, lang: "en", positive: true, text: "Anniversary edition worth every yen. The scarf accessory is adorable.", helpful: 63 },
        { author: "kai_zen", avatar: A3, date: "2026-06-28", hours: null, lang: "en", positive: true, text: "Box was slightly dented in transit but the figure itself is perfect.", helpful: 15 }
      ]
    },
    7: {
      about: [
        "A retro anime-print unisex crew neck in soft-washed cotton. This drop celebrates the hand-drawn era with three limited prints.",
        "Wash-safe print that holds up to everyday wear — a tribute piece for fans of classic animation."
      ],
      keyFeatures: [
        "Soft-washed cotton crew neck",
        "Three limited retro prints",
        "Unisex fit",
        "Wash-safe print"
      ],
      reviewSummary: "Mostly Positive",
      userReviews: [
        { author: "retro_lee", avatar: A3, date: "2026-08-02", hours: null, lang: "en", positive: true, text: "Print quality is amazing for the price. Washed twice, no fading.", helpful: 58 },
        { author: "maria_prints", avatar: A2, date: "2026-07-10", hours: null, lang: "en", positive: false, text: "Design is great but the fabric is thinner than expected.", helpful: 24 },
        { author: "otaku_dad", avatar: A1, date: "2026-06-19", hours: null, lang: "en", positive: true, text: "Bought for my son — he wears it every day. Good stuff.", helpful: 31 }
      ]
    },
    8: {
      about: [
        "Eight enamel-backed acrylic keychains of the full fictional idol lineup — a quick way to spell your favourite show in satchel flair.",
        "Scratch-resistant printing with sturdy metal clips, ready for backpacks, keys or display boards."
      ],
      keyFeatures: [
        "8-piece acrylic set",
        "Enamel-backed, scratch resistant",
        "Sturdy metal clips",
        "Great gift option"
      ],
      reviewSummary: "Overwhelmingly Positive",
      userReviews: [
        { author: "idol_fan_77", avatar: A2, date: "2026-08-08", hours: null, lang: "ja", positive: true, text: "8個セットでこの価格はお得。印刷も鮮明で文句なし。", helpful: 96 },
        { author: "satchel_sam", avatar: A1, date: "2026-07-17", hours: null, lang: "en", positive: true, text: "Great quality, sturdy clips. Bought a second set as gifts.", helpful: 44 },
        { author: "nemi_chan", avatar: A3, date: "2026-06-12", hours: null, lang: "en", positive: true, text: "Cute and well-made. Wish there were more characters though.", helpful: 29 }
      ]
    },
    9: {
      about: [
        "The piano-pressed Colorful Stage! original soundtrack with a full-color lyric booklet from the Secret Garden records garage.",
        "Each copy includes a digital download code so you can carry the set with you on the go."
      ],
      keyFeatures: [
        "Full original soundtrack",
        "Full-color lyric booklet",
        "Collector-grade packaging",
        "Digital download code included"
      ],
      reviewSummary: "Mostly Positive",
      userReviews: [
        { author: "piano_key", avatar: A1, date: "2026-08-14", hours: null, lang: "en", positive: true, text: "The booklet is gorgeous and the mastering is superb. A must for Colorful Stage fans.", helpful: 70 },
        { author: "sekai_hiro", avatar: A2, date: "2026-07-21", hours: null, lang: "ja", positive: true, text: "収録曲が豪華。歌詞ブックレットの紙質が最高。", helpful: 52 },
        { author: "vinyl_vic", avatar: A3, date: "2026-06-26", hours: null, lang: "en", positive: false, text: "Shipped in a thin envelope and the jewel case arrived cracked. The music itself is five stars.", helpful: 13 }
      ]
    },
    10: {
      about: [
        "A limited pre-order of Power in her chainsaw-fiend pose — 1/8 scale with swap, shirt and optional part pieces. Ships February 2027.",
        "A dynamic, shelf-commanding sculpt from Bandai Spirits for fans of the hit series."
      ],
      keyFeatures: [
        "1/8 scale, dynamic chainsaw-fiend pose",
        "Swap parts and optional pieces",
        "Limited pre-order run",
        "Ships February 2027"
      ],
      reviewSummary: "Very Positive",
      userReviews: [
        { author: "chainsaw_lover", avatar: A1, date: "2026-08-05", hours: null, lang: "en", positive: true, text: "Power looks incredible, the pose is dynamic. The pre-order wait was worth it.", helpful: 66 },
        { author: "akane_red", avatar: A2, date: "2026-07-13", hours: null, lang: "ja", positive: true, text: "塗装が繊細で、可動部分もスムーズ。限定品だけに早めの予約がおすすめ。", helpful: 41 },
        { author: "budget_bunta", avatar: A3, date: "2026-06-22", hours: null, lang: "en", positive: false, text: "Expensive, but you get what you pay for with Bandai scale figures.", helpful: 19 }
      ]
    },
    11: {
      about: [
        "Shadow of the Erdtree is the colossal expansion to FromSoftware's Game of the Year winner. Enter the Land of Shadow — a realm unseen in the base game — where the demigod Miquella and the fearsome Messmer the Impaler await.",
        "Explore a vast new region roughly the size of Limgrave, discover more than 40 new weapons and 10 terrifying bosses, and forge your own path through FromSoftware's most ambitious expansion to date."
      ],
      keyFeatures: [
        "Massive new region — the Land of Shadow",
        "10+ new bosses including Messmer the Impaler",
        "40+ new weapons, talismans and Ashes of War",
        "New summons and progression system",
        "Requires Elden Ring base game to play"
      ],
      features: ["achievements", "cloud", "controller", "multiplayer", "singleplayer"],
      dlc: [],
      requirements: {
        minimum: { os: "Windows 10 64-bit", cpu: "Intel Core i5-8400 / AMD Ryzen 3 3300X", ram: "12 GB RAM", gpu: "NVIDIA GeForce GTX 1060 3GB / AMD Radeon RX 580 4GB", directx: "DirectX 12", storage: "60 GB available space" },
        recommended: { os: "Windows 11 64-bit", cpu: "Intel Core i7-8700K / AMD Ryzen 5 3600X", ram: "16 GB RAM", gpu: "NVIDIA GeForce GTX 1070 8GB / AMD Radeon RX Vega 56", directx: "DirectX 12", storage: "60 GB SSD" }
      },
      accolades: [
        { outlet: "IGN", score: "10", quote: "A breathtaking expansion that stands shoulder-to-shoulder with the base game." },
        { outlet: "Famitsu", score: "38/40", quote: "The Land of Shadow is a masterclass in open-world design." },
        { outlet: "GameSpot", score: "9/10", quote: "FromSoftware at the absolute peak of their craft." }
      ],
      metacritic: 95,
      reviewSummary: "Very Positive",
      userReviews: [
        { author: "ren_dev", avatar: A3, date: "2026-08-15", hours: 96.7, lang: "en", positive: true, text: "Bigger than most full games. Messmer is the best boss FromSoft has ever made. The map density is insane.", helpful: 412 },
        { author: "shiro_kun", avatar: A1, date: "2026-08-08", hours: 61.3, lang: "en", positive: true, text: "If you finished the base game, this is mandatory. The Land of Shadow is a whole game's worth of content.", helpful: 233 },
        { author: "tarnished_7", avatar: A2, date: "2026-07-29", hours: 40.2, lang: "ja", positive: true, text: "難易度は高いが、探索の密度は本編を超えている。祝福の前で何度も死んだ。", helpful: 97 },
        { author: "golden_order", avatar: A3, date: "2026-07-18", hours: 15.9, lang: "de", positive: false, text: "Der Schwierigkeitsgrad ist selbst für Elden-Ring-Verhältnisse gnadenlos. Aber genau dafür lieben wir es.", helpful: 45 },
        { author: "moon_veil", avatar: A1, date: "2026-07-06", hours: 118.4, lang: "zh", positive: true, text: "DLC 的探索密度比本体还高，新武器新战灰玩法丰富，值回票价。", helpful: 76 },
        { author: "no_hit_run", avatar: A2, date: "2026-06-24", hours: 203.1, lang: "en", positive: true, text: "No-hit run completed. Peak gaming — FromSoft have outdone themselves again.", helpful: 184 },
        { author: "casual_rafa", avatar: A3, date: "2026-06-10", hours: 2.3, lang: "es", positive: false, text: "No me di cuenta de que requería el juego base y no lo tengo. Compren el pack completo.", helpful: 23 }
      ]
    },
    12: {
      about: [
        "A premium-cotton black hoodie with the King of Curses' domain-mark print and a ribbed kangaroo pocket.",
        "Cut roomy for comfort, with a heavyweight feel that holds its shape through the winter."
      ],
      keyFeatures: [
        "Premium heavyweight cotton",
        "Domain-mark print",
        "Ribbed kangaroo pocket",
        "Unisex sizing"
      ],
      reviewSummary: "Very Positive",
      userReviews: [
        { author: "domain_expansion", avatar: A1, date: "2026-08-07", hours: null, lang: "en", positive: true, text: "The domain print on the back is clean. Premium cotton feels great.", helpful: 83 },
        { author: "sukuna_fan_x", avatar: A2, date: "2026-07-16", hours: null, lang: "en", positive: true, text: "Best hoodie in my collection. Sizing runs a bit large, which I like.", helpful: 47 },
        { author: "winter_wolf", avatar: A3, date: "2026-06-23", hours: null, lang: "de", positive: true, text: "Sehr guter Stoff, der Druck hält auch nach mehreren Wäschen.", helpful: 26 }
      ]
    }
  };

  window.KAIMONO_PRODUCTS.forEach(function (p) {
    var extra = EXTRA[p.id];
    if (!extra) return;
    for (var k in extra) p[k] = extra[k];
  });
})();