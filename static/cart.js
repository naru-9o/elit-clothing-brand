function loco() {
    gsap.registerPlugin(ScrollTrigger);

// Using Locomotive Scroll from Locomotive https://github.com/locomotivemtl/locomotive-scroll

const locoScroll = new LocomotiveScroll({
  el: document.querySelector("#main"),
  smooth: true
});
// each time Locomotive Scroll updates, tell ScrollTrigger to update too (sync positioning)
locoScroll.on("scroll", ScrollTrigger.update);

// tell ScrollTrigger to use these proxy methods for the "#main" element since Locomotive Scroll is hijacking things
ScrollTrigger.scrollerProxy("#main", {
  scrollTop(value) {
    return arguments.length ? locoScroll.scrollTo(value, 0, 0) : locoScroll.scroll.instance.scroll.y;
  }, // we don't have to define a scrollLeft because we're only scrolling vertically.
  getBoundingClientRect() {
    return {top: 0, left: 0, width: window.innerWidth, height: window.innerHeight};
  },
  // LocomotiveScroll handles things completely differently on mobile devices - it doesn't even transform the container at all! So to get the correct behavior and avoid jitters, we should pin things with position: fixed on mobile. We sense it by checking to see if there's a transform applied to the container (the LocomotiveScroll-controlled element).
  pinType: document.querySelector("#main").style.transform ? "transform" : "fixed"
});

// each time the window updates, we should refresh ScrollTrigger and then update LocomotiveScroll. 
ScrollTrigger.addEventListener("refresh", () => locoScroll.update());

ScrollTrigger.refresh();

}

loco()


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
            scrub: true
        }
    })

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

navScroll()


function remove(){
    
document.getElementById('cart-items').addEventListener('click', function(event) {

    if (event.target.classList.contains('remove-from-cart')) {
        const itemIndex = event.target.getAttribute('data-index');

        // Send a request to remove the item from the cart
        fetch(`/remove-from-cart/${itemIndex}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Reload the page or update the cart items without refreshing
                window.location.reload();  // For simplicity, just reload the page
            } else {
                console.error('Failed to remove item from cart');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
});


}

remove()



