const galleryElement = document.getElementById("gallery");
const filterElement = document.getElementById("filters");
const lightboxElement = document.getElementById("lightbox");
const lightboxStageElement = document.getElementById("stage");
const lightboxCaptionElement = document.getElementById("caption");

const KIND_LABELS = { image: "Image", lottie: "Lottie" };
const MANIFEST_URL = "results/manifest.json";

let lightboxAnimation = null;

function loadGallery() {
  fetch(MANIFEST_URL, { cache: "no-store" })
    .then(response => response.json())
    .then(({ categories }) => {
      renderCategoryFilters(categories);
      renderGallery(categories, null);
    })
    .catch(() => {
      galleryElement.innerHTML = '<p class="empty">Could not load the manifest.</p>';
    });

  document.getElementById("close").addEventListener("click", closeLightbox);
  lightboxElement.addEventListener("click", event => {
    if (event.target === lightboxElement) closeLightbox();
  });
  document.addEventListener("keydown", event => {
    if (event.key === "Escape" && !lightboxElement.hidden) closeLightbox();
  });
}

function renderCategoryFilters(categories) {
  const options = [{ id: null, title: "All" }, ...categories];
  let selectedId = null;

  filterElement.replaceChildren(...options.map(option => {
    const chip = document.createElement("button");
    chip.className = "chip";
    chip.textContent = option.title;
    chip.setAttribute("aria-pressed", String(option.id === selectedId));

    chip.addEventListener("click", () => {
      selectedId = option.id;
      filterElement.querySelectorAll(".chip").forEach((otherChip, index) => {
        otherChip.setAttribute("aria-pressed", String(options[index].id === selectedId));
      });
      renderGallery(categories, selectedId);
    });

    return chip;
  }));
}

function renderGallery(categories, selectedCategoryId) {
  galleryElement.replaceChildren();
  const visibleCategories = categories.filter(
    category => !selectedCategoryId || category.id === selectedCategoryId
  );

  if (!visibleCategories.length) {
    galleryElement.innerHTML = '<p class="empty">No content yet.</p>';
    return;
  }

  for (const category of visibleCategories) {
    const section = document.createElement("section");
    section.className = "category";
    section.innerHTML = '<h2></h2><div class="grid"></div>';
    section.querySelector("h2").textContent = category.title;
    section.querySelector(".grid").append(...category.items.map(createCard));
    galleryElement.append(section);
  }
}

function createCard(item) {
  const card = document.createElement("button");
  card.className = "card";
  card.innerHTML = `<div class="preview"></div>
    <div class="meta"><span class="title"></span><span class="badge"></span></div>`;
  card.querySelector(".title").textContent = item.title;
  card.querySelector(".badge").textContent = KIND_LABELS[item.kind] ?? item.kind;

  mountMedia(card.querySelector(".preview"), item);
  card.addEventListener("click", () => openLightbox(item));

  return card;
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

function openLightbox(item) {
  lightboxAnimation = mountMedia(lightboxStageElement, item);
  lightboxCaptionElement.textContent = `${item.title} · ${KIND_LABELS[item.kind] ?? item.kind}`;
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
