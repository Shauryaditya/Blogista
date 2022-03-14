const headline = document.querySelector(".headline");


const tl = new TimelineMax();

tl.fromTo(hero,1, {height: "0%"}, {height: "80%", ease: Power2.easeInOut});
tl.fromTo(hero,1.2, {width: '100%'}, {width: '80%',ease: Power2.easeInOut});
tl.fromTo(slider,1.2, {x: "-100%"}, {x: '0%', ease: Power2.easeInOut}); 