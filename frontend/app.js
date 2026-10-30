const sectionsElement = document.getElementById("sections");
const statsElement = document.getElementById("stats");
const navElement = document.getElementById("category-nav");
const searchElement = document.getElementById("search");
const lightboxElement = document.getElementById("lightbox");
const lightboxStageElement = document.getElementById("stage");
const lightboxCaptionElement = document.getElementById("caption");
const lightboxDownloadElement = document.getElementById("lightbox-download");
const themeToggleElement = document.getElementById("theme-toggle");

const KIND_LABELS = { image: "Image", lottie: "Lottie" };
const MANIFEST_URL = "results/manifest.json";
const CATEGORY_ORDER = ["streak", "rating", "food", "verbs"];   // Categories not listed here come last
const KEY_ENTER = "Enter";
const KEY_SPACE = " ";
const KEY_ESCAPE = "Escape";
const KEY_SEARCH_FOCUS = "/";
const THEME_STORAGE_KEY = "theme";   // Same key as in the script in index.html
const THEME_LIGHT = "light";
const THEME_DARK = "dark";
const ACTIVE_SECTION_OFFSET = 140;   // Pixels below the top where a section counts as "current"

const ICON_MOON = '<svg viewBox="0 0 24 24"><path d="M21 12.8A9 9 0 1111.2 3a7 7 0 009.8 9.8z"/></svg>';
const ICON_SUN = '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>';
const ICON_DOWNLOAD = '<svg viewBox="0 0 24 24"><path d="M12 4v11M7 11l5 5 5-5M5 20h14"/></svg>';
const ICON_GRID = '<svg viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7" rx="2"/><rect x="14" y="3" width="7" height="7" rx="2"/><rect x="3" y="14" width="7" height="7" rx="2"/><rect x="14" y="14" width="7" height="7" rx="2"/></svg>';
const ICON_IMAGE = '<svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="16" rx="3"/><circle cx="9" cy="10" r="2"/><path d="M21 16l-5-5-9 9"/></svg>';
const ICON_PLAY = '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M10 8.5l5 3.5-5 3.5z"/></svg>';
const ICON_FOLDER = '<svg viewBox="0 0 24 24"><path d="M3 7a2 2 0 012-2h4l2 2h8a2 2 0 012 2v8a2 2 0 01-2 2H5a2 2 0 01-2-2z"/></svg>';
const CATEGORY_ICONS = {
  streak: '<svg viewBox="0 0 24 24"><path d="M12 22c4 0 7-2.8 7-7 0-3-1.8-5-3.5-7-.4 1.5-1.2 2.5-2.5 3 0-3-1.5-5.5-4-8-.5 3-4 5.5-4 11 0 4.2 3 8 7 8z"/></svg>',
  rating: '<svg viewBox="0 0 24 24"><path d="M12 3l2.7 5.6 6.1.8-4.5 4.2 1.1 6.1L12 16.8l-5.4 2.9 1.1-6.1L3.2 9.4l6.1-.8z"/></svg>',
  food: '<svg viewBox="0 0 24 24"><path d="M7 3v8a2 2 0 002 2v8M11 3v8a2 2 0 01-2 2M17 21V3c-2.5 1.5-3 5-3 8h3"/></svg>',
};

let allCategories = [];
let lightboxAnimation = null;

function loadGallery() {
  fetch(MANIFEST_URL, { cache: "no-store" })
    .then(response => response.json())
    .then(({ categories }) => {
      allCategories = sortCategories(categories);
      renderStats(allCategories);
      renderNavigation(allCategories);
      renderGallery();
    })
    .catch(() => renderEmptyMessage("Could not load the manifest."));

  registerSearchListeners();
  registerScrollListener();
  registerLightboxListeners();
  registerThemeToggle();
}

function sortCategories(categories) {
  return [...categories].sort((first, second) => getCategoryRank(first) - getCategoryRank(second));
}

function getCategoryRank(category) {
  const index = CATEGORY_ORDER.indexOf(category.id);
  return index === -1 ? CATEGORY_ORDER.length : index;
}

function registerThemeToggle() {
  updateThemeToggle();
  themeToggleElement.addEventListener("click", toggleTheme);
}

function toggleTheme() {
  const nextTheme = getCurrentTheme() === THEME_LIGHT ? THEME_DARK : THEME_LIGHT;

  document.documentElement.dataset.theme = nextTheme;
  saveTheme(nextTheme);
  updateThemeToggle();
}

function getCurrentTheme() {
  return document.documentElement.dataset.theme === THEME_LIGHT ? THEME_LIGHT : THEME_DARK;
}

function saveTheme(theme) {
  try {
    localStorage.setItem(THEME_STORAGE_KEY, theme);
  } catch (error) {
    // Storage can be blocked. The theme then only lasts until the page is closed.
  }
}

function updateThemeToggle() {
  const isLight = getCurrentTheme() === THEME_LIGHT;
  const label = isLight ? "Switch to dark mode" : "Switch to light mode";

  themeToggleElement.innerHTML = isLight ? ICON_MOON : ICON_SUN;   // The icon shows the theme you switch to
  themeToggleElement.setAttribute("aria-label", label);
  themeToggleElement.title = label;
}

function registerSearchListeners() {
  searchElement.addEventListener("input", renderGallery);

  document.addEventListener("keydown", event => {
    const isTyping = document.activeElement.tagName === "INPUT";

    if (event.key === KEY_SEARCH_FOCUS && !isTyping) {
      event.preventDefault();
      searchElement.focus();
    }
  });
}

function registerScrollListener() {
  window.addEventListener("scroll", markActiveNavLink, { passive: true });
}

function renderStats(categories) {
  const items = categories.flatMap(category => category.items);
  const imageCount = items.filter(item => item.kind === "image").length;

  const stats = [
    { icon: ICON_GRID, value: items.length, label: "Total assets" },
    { icon: ICON_FOLDER, value: categories.length, label: "Categories" },
    { icon: ICON_IMAGE, value: imageCount, label: "Images" },
    { icon: ICON_PLAY, value: items.length - imageCount, label: "Animations" },
  ];

  statsElement.replaceChildren(...stats.map(createStat));
}

function createStat({ icon, value, label }) {
  const stat = document.createElement("div");
  stat.className = "stat";
  stat.innerHTML = `<span class="stat-icon">${icon}</span>
    <div><span class="stat-value"></span><span class="stat-label"></span></div>`;

  stat.querySelector(".stat-value").textContent = value;
  stat.querySelector(".stat-label").textContent = label;
  return stat;
}

function renderNavigation(categories) {
  navElement.replaceChildren(...categories.map(createNavLink));
  markActiveNavLink();
}

function createNavLink(category) {
  const link = document.createElement("button");
  link.className = "nav-link";
  link.dataset.categoryId = category.id;
  link.innerHTML = `${CATEGORY_ICONS[category.id] ?? ICON_FOLDER}
    <span class="nav-title"></span><span class="nav-count"></span>`;

  link.querySelector(".nav-title").textContent = category.title;
  link.querySelector(".nav-count").textContent = category.items.length;
  link.addEventListener("click", () => jumpToCategory(category.id));
  return link;
}

function jumpToCategory(categoryId) {
  // A search could have hidden the section, so the search is cleared first.
  if (searchElement.value) {
    searchElement.value = "";
    renderGallery();
  }

  document.getElementById(`category-${categoryId}`)?.scrollIntoView();
}

function markActiveNavLink() {
  const sections = [...sectionsElement.querySelectorAll(".category")];
  const passedSections = sections.filter(section => section.getBoundingClientRect().top <= ACTIVE_SECTION_OFFSET);
  const currentSection = passedSections.pop() ?? sections[0];

  for (const link of navElement.children) {
    link.setAttribute("aria-current", String(link.dataset.categoryId === currentSection?.dataset.categoryId));
  }
}

function renderGallery() {
  const visibleCategories = filterCategories({ categories: allCategories, query: searchElement.value });

  if (!visibleCategories.length) {
    renderEmptyMessage(allCategories.length ? "Nothing matches your search." : "No content yet.");
    return;
  }

  sectionsElement.replaceChildren(...visibleCategories.map(createCategorySection));
  markActiveNavLink();
}

function filterCategories({ categories, query }) {
  const normalizedQuery = query.trim().toLowerCase();

  return categories
    .map(category => ({
      ...category,
      items: category.items.filter(item => matchesQuery({ item, category, normalizedQuery })),
    }))
    .filter(category => category.items.length);
}

function matchesQuery({ item, category, normalizedQuery }) {
  const searchableText = `${item.title} ${category.title} ${getKindLabel(item)}`.toLowerCase();
  return searchableText.includes(normalizedQuery);
}

function renderEmptyMessage(message) {
  const messageElement = document.createElement("p");
  messageElement.className = "empty";
  messageElement.textContent = message;
  sectionsElement.replaceChildren(messageElement);
}

function createCategorySection(category) {
  const section = document.createElement("section");
  section.className = "category";
  section.id = `category-${category.id}`;
  section.dataset.categoryId = category.id;
  section.innerHTML = `<div class="category-header"><h2></h2><span class="category-count"></span></div>
    <div class="grid"></div>`;

  section.querySelector("h2").textContent = category.title;
  section.querySelector(".category-count").textContent = category.items.length;
  section.querySelector(".grid").append(...category.items.map(createCard));
  return section;
}

function createCard(item) {
  // A div, because a download link inside a button is invalid HTML.
  const card = document.createElement("div");
  card.className = "card";
  card.tabIndex = 0;
  card.setAttribute("role", "button");
  card.innerHTML = `<div class="preview"></div>
    <div class="meta">
      <span class="title"></span>
      <span class="badge"></span>
      <a class="card-download" aria-label="Download">${ICON_DOWNLOAD}</a>
    </div>`;

  card.querySelector(".title").textContent = item.title;
  card.querySelector(".badge").textContent = getKindLabel(item);
  mountMedia(card.querySelector(".preview"), item);
  prepareCardDownload(card, item);
  registerCardListeners(card, item);

  return card;
}

function getKindLabel(item) {
  return KIND_LABELS[item.kind] ?? item.kind;
}

function prepareCardDownload(card, item) {
  const downloadLink = card.querySelector(".card-download");
  setDownloadTarget(downloadLink, item);

  // Downloading must not also open the lightbox.
  downloadLink.addEventListener("click", event => event.stopPropagation());
}

function setDownloadTarget(linkElement, item) {
  linkElement.href = item.file;
  linkElement.download = item.file.split("/").pop();
  linkElement.title = `Download ${linkElement.download}`;
}

function registerCardListeners(card, item) {
  card.addEventListener("click", () => openLightbox(item));

  card.addEventListener("keydown", event => {
    const isCardFocused = event.target === card;
    const isOpenKey = event.key === KEY_ENTER || event.key === KEY_SPACE;

    if (isCardFocused && isOpenKey) {
      event.preventDefault();
      openLightbox(item);
    }
  });
}

/** Fills the element with the image or a running Lottie animation. Returns the animation, if any. */
function mountMedia(element, item) {
  element.replaceChildren();

  if (item.kind === "image") {
    const image = new Image();
    image.src = item.file;
    image.alt = item.title;
    image.loading = "lazy";
    element.append(image);
    return null;
  }

  const animationContainer = document.createElement("div");
  element.append(animationContainer);

  return lottie.loadAnimation({
    container: animationContainer,
    renderer: "svg",
    loop: true,
    autoplay: true,
    path: item.file,
  });
}

function registerLightboxListeners() {
  document.getElementById("close").addEventListener("click", closeLightbox);

  lightboxElement.addEventListener("click", event => {
    if (event.target === lightboxElement) closeLightbox();
  });

  document.addEventListener("keydown", event => {
    if (event.key === KEY_ESCAPE && !lightboxElement.hidden) closeLightbox();
  });
}

function openLightbox(item) {
  lightboxAnimation = mountMedia(lightboxStageElement, item);
  lightboxCaptionElement.textContent = `${item.title} · ${getKindLabel(item)}`;
  setDownloadTarget(lightboxDownloadElement, item);

  lightboxElement.hidden = false;
  document.body.style.overflow = "hidden";
}

function closeLightbox() {
  lightboxAnimation?.destroy();
  lightboxAnimation = null;
  lightboxStageElement.replaceChildren();

  lightboxElement.hidden = true;
  document.body.style.overflow = "";
}

loadGallery();
