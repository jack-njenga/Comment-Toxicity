

let menuIcon = document.getElementById("menu-icon");
let menuContainer = document.getElementById("menu-container");
let menuNav = document.getElementById("menu-nav");

function toggleMenu() {
  menuContainer.classList.toggle("active");
}
document.addEventListener("click", function (event) {
  if (!menuIcon.contains(event.target) &&
    menuContainer.contains(event.target) &&
    !menuNav.contains(event.target)
  ) {
    event.stopPropagation();
    menuContainer.classList.remove("active");
  }
});