const sidebarProfileExpander = document.querySelector(
  "#sidebar-bottom-expander-icon"
);
const sidebarExpandable = document.querySelector("#sidebar-expandable");
const cancelMenu = document.querySelector("#cancel-menu");
const menu = document.querySelector("#menu-icon");
const sidebar = document.querySelector("#sidebar");
const createChannel = document.querySelector("#add-channel");
const modal = document.querySelector("#modal");
const cancelModal = document.querySelector("#cancel-modal");

sidebarProfileExpander.addEventListener("click", (event) => {
  if (sidebarExpandable.style.display === "none") {
    sidebarExpandable.style.display = "flex";
  } else {
    sidebarExpandable.style.display = "none";
  }
});
cancelMenu.addEventListener("click", (event) => {
  sidebar.style.display = "none";
});
menu.addEventListener("click", (event) => {
  sidebar.style.display = "flex";
});
createChannel.addEventListener("click", (event) => {
  modal.style.display = "flex";
});
cancelModal.addEventListener("click", (event) => {
  modal.style.display = "none";
});

