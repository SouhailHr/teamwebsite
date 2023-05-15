

var navMenu= document.getElementById('nav-menu'),
      navToggle = document.getElementById('nav-toggle'),
      navClose = document.getElementById('nav-close')

/*------ Menu Show button  - small devices ------ */
if(navToggle){
    navToggle.addEventListener('click', () =>{
        navMenu.classList.add('show-menu')
    })
}
/*------ Menu Remove button  - small devices ------ */

if (navClose){
    navClose.addEventListener('click', () =>{
        navMenu.classList.remove('show-menu')
    })
}

/*------ Menu  Mobile ------ */
var navLink= document.querySelectorAll('.nav__link')

function linkAction(){
    var navMenu= document.getElementById('nav-menu')
    // when u click a link , the menu is removed
    navMenu.classList.remove('show-menu')
}

for (var i = 0; i < navLink.length; i++) {
    navLink[i].addEventListener('click', linkAction);
}

/*------- Skills Menu  --------------*/

var skillsContent = document.getElementsByClassName('skills__content'),
    skillsHeader = document.querySelectorAll('.skills__header')

function toggleSkills() {
    var itemClass = this.parentNode.className

    for (i = 0; i < skillsContent.length; i++) {
        skillsContent[i].className = 'skills__content skills__close'
    }
    if (itemClass === 'skills__content skills__close') {
        this.parentNode.className = 'skills__content skills__open'
    }
}

for (var i = 0; i < skillsHeader.length; i++) {
    skillsHeader[i].addEventListener('click', toggleSkills);
}



/*------- Qualifications Tree --------------*/

var tabs = document.querySelectorAll(".tab-js"),
    tabcontents = document.querySelectorAll(".content-js")


tabs.forEach(tab =>{
    tab.addEventListener('click', () => {
        var target = document.querySelector(tab.dataset.target);
        console.log(target);
        console.log(tab.dataset.target);

        /* Remove the content outputed */
        tabcontents.forEach(tabContent => {
            tabContent.classList.remove('qualification__active');
        })
        /* show the content targeted */
        target.classList.add('qualification__active');

        /* Remove the light from  the actual tab  */
        tabs.forEach(tab => {
            tab.classList.remove('qualification__active');
        })
        /* add the light to the new tab */
        tab.classList.add('qualification__active');
    })

})


/* ===================== Dark Light Theme ========================*/

var themeButton = document.querySelector('.change-theme')
var darkTheme = 'dark-theme';
var iconTheme = 'uil-sun';


// Select Previous theme and icon used by the user
var selectedTheme = localStorage.getItem('selected-theme');
var selectedIcon = localStorage.getItem('selected-icon');

//  we store the-theme and the icon in variables after validation of the dark-theme class

var getCurrentTheme = () => document.body.classList.contains(darkTheme) ? 'dark' : 'light';
var getCurrentIcon = () => document.body.classList.contains(iconTheme) ? 'uil-moon' : 'uil-sun';

//  Check if the user chose a topic

if (selectedTheme) {
    // if valid . we check the activated theme
    document.body.classList[selectedTheme === 'dark' ? 'add' : 'remove'](darkTheme);
    themeButton.classList[selectedIcon === 'uil-moon' ? 'add' : 'remove'](iconTheme);
}

themeButton.addEventListener('click', () => {
    // add or remove the dark/icon ,  theme when click
    document.body.classList.toggle(darkTheme);
    themeButton.classList.toggle(iconTheme);

    // we save the current icon and theme
    localStorage.setItem('selected-theme', getCurrentTheme);
    localStorage.setItem('selected-icon', getCurrentIcon);
})