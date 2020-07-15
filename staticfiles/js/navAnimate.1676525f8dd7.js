//MOBILE VIEW NAV SLIDE IN
const slider = () => {
    const hamburger=document.querySelector('.hamburger');
    const navSlide=document.querySelector('.slider-main');
    hamburger.addEventListener('click', () => {
        navSlide.classList.toggle('active');
        scrollDisable();
    });
}
const sliderOut = () =>{
    const arrow=document.querySelector('.arrow');
    const navSlide=document.querySelector('.slider-main');
    arrow.addEventListener('touchend', () => {
        navSlide.classList.toggle('active');
        scrollActive();
    });
}
function scrollDisable(){
    document.querySelector('html').style.position='fixed';
}
function scrollActive(){
    document.querySelector('html').style.position='static';
}
function sliderOutOnBodyTouch(){
    const doc=document.querySelector('#Opac-slider');
    const navSlide=document.querySelector('.slider-main');
    doc.addEventListener('touchend', () => {
        if(navSlide.classList.contains('active')){
            navSlide.classList.remove('active');
            scrollActive();
        }
    });
}
slider();
sliderOut();
sliderOutOnBodyTouch();
//END MOBILE VIEW NAV SLIDE IN