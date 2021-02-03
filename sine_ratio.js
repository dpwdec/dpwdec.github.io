let input, button, greeting, slider;

function setup() {
  // create canvas
  let canvas = createCanvas(600, 150);
  canvas.parent('sine_ratio')
  slider = createSlider();
  slider.position(0, 150)
  slider.parent('sine_ratio')
}

function draw() {
  background(255);

  line(20, 40, 400, 40);
  line(20, 100, 400, 100);

  _
    .range(11)
    .map(x => x * 380/10)
    .forEach(x => {
      line(20 + x, 35, 20 + x, 45);
      line(20 + x, 95, 20 + x, 105);
    });

  let deltaX = slider.value() / 1000.0;

  let deltaXSin = Math.sin(deltaX);

  textSize(15)
  text(`Delta x: ${deltaX}`, 20, 20)
  text(`Sin(Delta x): ${deltaXSin}`, 20, 80)

  circle(20 + (3800 * deltaX), 40, 20, 20)

  circle(20 + (3800 * (deltaXSin)), 100, 20, 20)
}