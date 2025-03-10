document.addEventListener('DOMContentLoaded', function () {
    function setActiveLink() {
        const currentPath = window.location.pathname;
        const currentHash = window.location.hash;
        const navLinks = document.querySelectorAll('.navbar-nav .nav-link');

        navLinks.forEach(function (navLink) {
            const linkPath = new URL(navLink.href).pathname;
            const linkHash = new URL(navLink.href).hash;

            if (linkPath === currentPath && linkHash === currentHash) {
                navLink.classList.add('active');
            } else {
                navLink.classList.remove('active');
            }
        });
    }

    function scrollToHash() {
        const hash = window.location.hash;
        if (hash) {
            const targetElement = document.querySelector(hash);
            if (targetElement) {
                const headerHeight = document.querySelector('.navbar').offsetHeight;
                window.scrollTo({
                    top: targetElement.offsetTop - headerHeight,
                    behavior: 'smooth'
                });
            }
        }
    }

    // Initial setup
    setActiveLink();
    scrollToHash();

    // Update on hash change
    window.addEventListener('hashchange', function () {
        setActiveLink();
        scrollToHash();
    });

    // Ensure smooth scrolling with offset when clicking on anchor links
    document.querySelectorAll('a.nav-link').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            // Check if the link is an internal link with a hash fragment
            if (this.getAttribute('href').startsWith('#')) {
                e.preventDefault();
                const targetElement = document.querySelector(this.getAttribute('href'));
                if (targetElement) {
                    const headerHeight = document.querySelector('.navbar').offsetHeight;
                    window.scrollTo({
                        top: targetElement.offsetTop - headerHeight,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });
});