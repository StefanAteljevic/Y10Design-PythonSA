// Slideshow script

let slideIndex = 0;

function showSlides() {
  const slides = document.getElementsByClassName("mySlides");
  const dots = document.getElementsByClassName("dot");

  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }

  for (let i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }

  if (slideIndex >= slides.length) {
    slideIndex = 0;
  }

  slides[slideIndex].style.display = "block";  
  dots[slideIndex].className += " active";
  slideIndex++;

  setTimeout(showSlides, 10000);
}

showSlides();

// Script that allows multiple reviews to be taken from firebase and placed on the page

function search() {
  const query = document.getElementById("stefan").value;
  firebase.database().ref("/Reviews/").once("value").then(reviews => {
    let gameFound = false;
    let i = 0;
    reviews.forEach(_review => {
      const review = _review.val();
      console.log(review.game, query);

      // if(review.review == review) {
      //   window.location.replace(`review.html?review=${review.review}`);
      // }
      if(review.game == query) {
        console.log(review.name);
        gameFound = true;
        window.location.replace(`results.html?game=${review.game}`);
      }

      if(!gameFound && i == reviews.numChildren() - 1) {
        window.location.replace("/notfound.html");
      }
      i++;
    });
  })
}



function keypressed(e) {
  if(e.key === "Enter") {
    search();
  }
}


