function loop(img_count) {
    let imgPath = "./static/";
    setInterval(() => {
        
      let randomIndex = Math.floor(Math.random() * (img_count));
      console.log('kek')
      document
        .getElementById("loop")
        .setAttribute("src", `${imgPath}/${randomIndex}.png`);
    }, 2000);
  }
function lol() {
  let stuff = ['hi', 'hello', 'epic', 'kpop', 'jpop', 'poggers']
  setInterval(() => {
        
    let r = stuff[Math.floor(Math.random() * stuff.length)]
  
    document
      .getElementById("changingtext")
      .innerHTML = r
  }, 2000);
}

const submit = () => {
  console.log('xd')
  alert('Success!')
}
// document.getElementsByTagName('body')[0].addEventListener("load", submit);


  