# UI Design & Architecture Specification: Kaimono Game Store Dashboard

Dokumen ini adalah panduan teknis implementasi UI untuk agen AI (OpenCode). Implementasikan setiap komponen secara modular sesuai instruksi di bawah ini.

---

## 🎨 Global Design System & Theme

- **Aesthetic**: Soft Anime / Minimalist Japanese Tech UI (Inspired by Project Sekai).
- **Base Background**: `#EBF0F5` (Soft pastel blue-gray).
- **Primary Cards**: `#FFFFFF` with `border-radius: 18px` (`rounded-2xl`).
- **Top Bar**: `#1E1E28` (Dark Slate / Charcoal).
- **Accent Colors**: 
  - Indigo / Lavender: `#6366F1` / `#818CF8`
  - Text Primary: `#1E293B` (`slate-800`)
  - Text Muted: `#94A3B8` (`slate-400`)
- **Typography**: `Plus Jakarta Sans` or `Inter`, clean sans-serif.
- **Layout Constraint**: Ultra-compact, zero-scroll fit-to-screen desktop app (`h-screen`, `overflow-hidden`).

---

## 🧩 Component Breakdown & Tasks

### Step 1: Top Bar Header (`/components/Header.html`)
- **Container**: Full-width fixed height (`py-2 px-6`), dark background `#1E1E28`, flex-row space-between.
- **Left Content**: 
  - Logo/Username: `@KAIMONO` (Bold White).
  - Separator: `|`.
  - Subtitle: `STORE DASHBOARD // GAMING PLATFORM` (Slate muted).
- **Right Content**:
  - Server Indicator: Green pulsing dot + `STEAM SERVER: ONLINE`.
  - User Badge: `GamerTag_99` with list icon.

### Step 2: Floating Sidebar (`/components/Sidebar.html`)
- **Container**: Vertical floating bar (`w-14`, white background `#FFFFFF`, `rounded-2xl`, border-slate-100, shadow-sm).
- **Top Section**:
  - Circular User Avatar with indigo border (`w-9 h-9`).
- **Middle Section (Navigation Icons)**:
  - Vertical flex column with icons: `Home` (Active - Dark background), `Gamepad2`, `ShoppingBag`, `Heart`, `Trophy`, `Settings`.
- **Bottom Section**:
  - `LogOut` icon with subtle red hover state (`hover:text-rose-500`).

### Step 3: Sub-Header & Search Bar (`/components/SubHeader.html`)
- **Breadcrumb & Title**: 
  - Small uppercase text: `DASHBOARD / HOSHINO ICHIKA` (Indigo accent).
  - Main Heading: `Featured Store` (Bold, `text-xl`).
  - Date Badge (Right): Calendar icon + Current Date (`20 September, 2026`).
- **Search Bar**: 
  - Input container (`rounded-2xl`, full width, white background).
  - Magnifying glass icon pinned left (`slate-400`).
  - Placeholder: `Search games, genres, or publishers...`.

### Step 4: Hero Spotlight Banner (`/components/HeroBanner.html`)
- **Container**: Horizontal card with gradient background (`from-slate-900 via-indigo-950 to-purple-900`), `rounded-2xl`, overflow-hidden.
- **Left Overlay**:
  - Tag pill: `Project Sekai` (`bg-white/10`, backdrop-blur).
  - Headline: `Welcome! to our game store Kaimono!!!`.
  - Call To Action: White pill button `Play Now` with play icon.
- **Right Content**:
  - Semi-transparent anime character/game illustration overlay (`opacity-50`).

### Step 5: New Releases / Trending Grid (`/components/NewReleases.html`)
- **Section Header**: Title `New Releases` + `view all` text button.
- **Grid Container**: 3-column equal width grid (`grid-cols-3 gap-2.5`).
- **Item Cards**:
  - Soft white background, `rounded-2xl`, padding 2.5.
  - Icon Badge (Left): Light pastel background (`bg-indigo-50`, `bg-emerald-50`, `bg-amber-50`).
  - Item Info (Right): Title (`Songwriting`, `Stage Performance`, `Recording`), Rating/Duration subtitle.

### Step 6: Activity & Playtime Bar (`/components/PlaytimeBar.html`)
- **Container**: White card (`rounded-2xl`, padding 3.5).
- **Label**: `Game Activity` / `Weekly Playtime Goal`.
- **Status Row**: `Total hours played` (Left) | `65%` (Right, bold).
- **Progress Track**: Slate-100 background, Slate-700 active fill (`w-[65%]`).

### Step 7: Right Side Panel (`/components/RightPanel.html`)
- **Sub-component 1 (Collection Cards)**:
  - Header: `Collection Card` + `view all`.
  - Card Item 1: `Birthday Card` + Thumbnail image.
  - Card Item 2: `World Link` + Thumbnail image.
- **Sub-component 2 (Notifications Panel)**:
  - Header: `Notifications` + Bell Icon.
  - Item List: Clock icon + `Band practice starts in 30 minutes`, Music icon + `Lyrics finalized`.
- **Sub-component 3 (Featured Media Cover)**:
  - Full-width image card with dark gradient overlay bottom-to-top.
  - Caption: `The Beginning of Something New` (Most Popular Video).

---

## 🛠 Execution Order for OpenCode

1. **Phase 1**: Setup CSS System (Tailwind CDN / Config + Plus Jakarta Sans Font).
2. **Phase 2**: Build Layout Shell (`Header`, `Sidebar`, `Main Area Container`).
3. **Phase 3**: Implement Main Area Components (`SubHeader`, `Search`, `HeroBanner`, `NewReleases`, `PlaytimeBar`).
4. **Phase 4**: Implement Right Panel (`CollectionCards`, `Notifications`, `FeaturedMediaCover`).
5. **Phase 5**: Pixel-perfection check against reference image & responsiveness test.


https://opncd.ai/share/uB2tZyTG