function loop(img_count) {
    let imgPath = "./static/";
    setInterval(() => {
        
      let randomIndex = Math.floor(Math.random() * (img_count - 1));
      document
        .getElementById("loop")
        .setAttribute("src", `${imgPath}/${randomIndex}.png`);
    }, 250);
  }
  document.addEventListener("DOMContentLoaded", () => {
    loop()
  });