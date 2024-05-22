 <script>

   let slideIndex = 1;
   showIntroSlides(slideIndex);

   function plusIntroSlides(n) {
     showIntroSlides(slideIndex += n);
   }

   function currentIntroSlide(n) {
     showIntroSlides(slideIndex = n);
   }
   
    let slideIndex = 0;
    showIntroSlides();

    function showIntroSlides() {
      let i;
      let slides = document.getElementsByClassName("myInroSlides");
      let dots = document.getElementsByClassName("dotIntro");
      for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";  
      }
      slideIndex++;
      if (slideIndex > slides.length) {slideIndex = 1}    
      for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
      }
      slides[slideIndex-1].style.display = "block";  
      dots[slideIndex-1].className += " active";
      setTimeout(showIntroSlides, 2000); // Change image every 2 seconds
    }
 </script>
