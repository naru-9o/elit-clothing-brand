function loco() {
    gsap.registerPlugin(ScrollTrigger);
  
    // Using Locomotive Scroll from Locomotive https://github.com/locomotivemtl/locomotive-scroll
  
    const locoScroll = new LocomotiveScroll({
      el: document.querySelector("#main"),
      smooth: true,
    });
    // each time Locomotive Scroll updates, tell ScrollTrigger to update too (sync positioning)
    locoScroll.on("scroll", ScrollTrigger.update);
  
    // tell ScrollTrigger to use these proxy methods for the "#main" element since Locomotive Scroll is hijacking things
    ScrollTrigger.scrollerProxy("#main", {
      scrollTop(value) {
        return arguments.length
          ? locoScroll.scrollTo(value, 0, 0)
          : locoScroll.scroll.instance.scroll.y;
      }, // we don't have to define a scrollLeft because we're only scrolling vertically.
      getBoundingClientRect() {
        return {
          top: 0,
          left: 0,
          width: window.innerWidth,
          height: window.innerHeight,
        };
      },
      // LocomotiveScroll handles things completely differently on mobile devices - it doesn't even transform the container at all! So to get the correct behavior and avoid jitters, we should pin things with position: fixed on mobile. We sense it by checking to see if there's a transform applied to the container (the LocomotiveScroll-controlled element).
      pinType: document.querySelector("#main").style.transform
        ? "transform"
        : "fixed",
    });
  
    // each time the window updates, we should refresh ScrollTrigger and then update LocomotiveScroll.
    ScrollTrigger.addEventListener("refresh", () => locoScroll.update());
  
    ScrollTrigger.refresh();
}
  
loco();
  
function navScroll() {

  gsap.to("#nav-left img", {
    transform: "translateY(-100%)",
    opacity: 0,
    scrollTrigger: {
    trigger: "#page1",
    scroller: "#main",
    start: "top 0",
    end: "top -5%",
    scrub: true,
    },
});

  gsap.to("#nav-right #nav-icons", {
    transform: "translateY(-100%)",
    opacity: 0,
    scrollTrigger: {
      trigger: "#page1",
      scroller: "#main",
      start: "top 0",
      end: "top -5%",
      scrub: true,
    },
  });

    document.addEventListener('DOMContentLoaded', function() {
      const menuToggle = document.getElementById('menu-toggle');
      const sidebar = document.getElementById('sidebar');
      const closeBtn = document.getElementById('close-btn');
  
      // Open the sidebar when the menu toggle is clicked
      menuToggle.addEventListener('click', function(event) {
          event.preventDefault();
          sidebar.classList.toggle('show');
      });
  
      // Close the sidebar when the close button is clicked
      closeBtn.addEventListener('click', function() {
          sidebar.classList.remove('show');
      });
  });
}
  
navScroll();
  



// ADD TO CART FUNCTIONALITY 

document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".add-to-cart").forEach((button) => {
    button.addEventListener("click", function () {
      const productContainer =
        this.closest("#page5") ||
        this.closest("#page4") ||
        this.closest("#page2") ||
        this.closest("#page1");

      const productName =
        productContainer.querySelector(".product-name").innerText; // Unique product name
      const productPrice =
        productContainer.querySelector(".product-price").innerText;
      const productImage = productContainer.querySelector(
        ".image, .product-image"
      ).src;

      // Add a unique identifier like name
      fetch("/add-to-cart", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name: productName, // Unique identifier
          price: productPrice,
          image: productImage,
        }),
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.success) {
            console.log("Product added to cart:", data.cart);

            // Display success notification
            const notification = document.querySelector(".notification");
            notification.style.display = "block";
            setTimeout(() => {
              notification.style.opacity = "1";
              notification.style.transform = "translateY(0)";
            }, 10);

            setTimeout(() => {
              notification.style.opacity = "0";
              notification.style.transform = "translateY(-20px)";
              setTimeout(() => {
                notification.style.display = "none";
              }, 500);
            }, 2000);
          } else {
            console.error("Failed to add product to cart:", data.message);
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    });
  });
});


  

function scrol() {
  document.querySelectorAll('[id^="rightDiv"]').forEach((element, index) => {
    ScrollTrigger.create({
        trigger: element,
        pin: true,
        scroller: `#main`,
        start: `top top`,
        end: `210% top`,
    });
});
   
}
  
scrol();