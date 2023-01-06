function toggle() {
   if (document.documentElement.style.getPropertyValue("--bg") == "white") { 
    document.documentElement.style.setProperty("--bg", "black");
    document.documentElement.style.setProperty("--clr", "white");
  } else {
    document.documentElement.style.setProperty("--bg", "white");
    document.documentElement.style.setProperty("--clr", "black");
  }
}
window.addEventListener("DOMContentLoaded", function () {
    eel.speak("Welcome to Page replacement algorithm visualizer")();
});