let app = document.getElementById('typewriter');

let typewriter = new Typewriter(app, {
  loop: true,
  delay: 75,
});
 
typewriter
  .pauseFor(2500)
  .typeString('<span style= "color: #405d27"; >La música es el verdadero lenguaje universal</span>')
  .pauseFor(200)
  .deleteChars(10)
  .start();
