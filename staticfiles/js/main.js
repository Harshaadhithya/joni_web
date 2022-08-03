// add more stylings to navbar while scrolling 
let nav = document.querySelector(".navbar");
window.onscroll = function () {
    if(document.documentElement.scrollTop > 40){
        nav.classList.add("navbar-moved");
    }
    else{
        nav.classList.remove("navbar-moved");
    }
}


//hide navbar if a link is clicked(mobile view)
let navbar_links=document.querySelectorAll(".nav-link");
let navCollapse=document.getElementById("navbarNav");
for(link of navbar_links){
    link.addEventListener('click',function(){
        navCollapse.classList.remove("show");
    })
}


// $(document).ready(function() {
//     $(".owl").owlCarousel({
//         items: 4,
//         loop: true,
//         nav: false,
//         autoplay: true,
//         autoplayTimeout: 2000,
//         autoplayHoverPause: true,
//         responsiveClass: true,
//         responsive: {
//             0: {
//                 items: 2
//             },
//             600: {
//                 items: 3
//             },
//             1000: {
//                 items: 6
//             }
//         }
//     });
// });

$('.owl-carousel').owlCarousel({
    loop:true,
    margin:10,
    nav:false,
    autoplay:true,
    autoplayTimeout: 2000,
    autoplayHoverPause: true,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:1
        },
        1000:{
            items:1
        }
    }
})


$(".step").click( function() {
	$(this).addClass("active").prevAll().addClass("active");
	$(this).nextAll().removeClass("active");
});

$(".step01").click( function() {
	$("#line-progress").css("width", "3%");
	$(".discovery").addClass("active").siblings().removeClass("active");
});

$(".step02").click( function() {
	$("#line-progress").css("width", "33%");
	$(".strategy").addClass("active").siblings().removeClass("active");
});

$(".step03").click( function() {
	$("#line-progress").css("width", "66.5%");
	$(".creative").addClass("active").siblings().removeClass("active");
});

$(".step04").click( function() {
	$("#line-progress").css("width", "100%");
	$(".production").addClass("active").siblings().removeClass("active");
});

// $(".step05").click( function() {
// 	$("#line-progress").css("width", "100%");
// 	$(".analysis").addClass("active").siblings().removeClass("active");
// });


