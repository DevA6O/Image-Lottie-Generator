const galleryElement = document.getElementById("gallery");
const filterElement = document.getElementById("filters");
const lightboxElement = document.getElementById("lightbox");
const lightboxStageElement = document.getElementById("stage");
const lightboxCaptionElement = document.getElementById("caption");
const lightboxDownloadElement = document.getElementById("lightbox-download");

const KIND_LABELS = { image: "Image", lottie: "Lottie" };
const MANIFEST_URL = "results/manifest.json";
const ALL_CATEGORIES_ID = null;
const KEY_ENTER = "Enter";
const KEY_SPACE = " ";
const KEY_ESCAPE = "Escape";

let lightboxAnimation = null;

function loadGallery() {
  fetch(MANIFEST_URL, { cache: "no-store" })
    .then(response => response.json())
    .then(({ categories }) => {
      renderCategoryFilters(categories);
      renderGallery({ categories, selectedCategoryId: ALL_CATEGORIES_ID });
    })
    .catch(() => renderEmptyMessage("Could not load the manifest."));

  registerLightboxListeners();
}

function renderCategoryFilters(categories) {
  const filterOptions = [{ id: ALL_CATEGORIES_ID, title: "All" }, ...categories];

  const chips = filterOptions.map(filterOption => {
    const chip = createChip(filterOption.title);

    chip.addEventListener("click", () => {
      markSelectedChip({ chips, selectedChip: chip });
      renderGallery({ categories, selectedCategoryId: filterOption.id });
    });

    return chip;
  });

  markSelectedChip({ chips, selectedChip: chips[0] });
  filterElement.replaceChildren(...chips);
}

function createChip(title) {
  const chip = document.createElement("button");
  chip.className = "chip";
  chip.textContent = title;
  return chip;
}

function markSelectedChip({ chips, selectedChip }) {
  for (const chip of chips) {
    chip.setAttribute("aria-pressed", String(chip === selectedChip));
  }
}

function renderGallery({ categories, selectedCategoryId }) {
  const visibleCategories = categories.filter(
    category => selectedCategoryId === ALL_CATEGORIES_ID || category.id === selectedCategoryId
  );

  if (!visibleCategories.length) {
    renderEmptyMessage("No content yet.");
    return;
  }

  galleryElement.replaceChildren(...visibleCategories.map(createCategorySection));
}

function renderEmptyMessage(message) {
  const messageElement = document.createElement("p");
  messageElement.className = "empty";
  messageElement.textContent = message;
  galleryElement.replaceChildren(messageElement);
}

function createCategorySection(category) {
  const section = document.createElement("section");
  section.className = "category";
  section.innerHTML = '<h2></h2><div class="grid"></div>';
  section.querySelector("h2").textContent = category.title;
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
      <a class="card-download" aria-label="Download">&#8681;</a>
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
