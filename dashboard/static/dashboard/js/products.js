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