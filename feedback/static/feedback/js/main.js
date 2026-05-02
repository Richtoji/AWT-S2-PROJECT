document.addEventListener("DOMContentLoaded", function () {
    // Custom Cursor logic
    const dot = document.querySelector('.cursor-dot');
    const outline = document.querySelector('.cursor-outline');

    if (dot && outline) {
        window.addEventListener('mousemove', function (e) {
            const posX = e.clientX;
            const posY = e.clientY;

            dot.style.left = `${posX}px`;
            dot.style.top = `${posY}px`;

            // Trailing effect using Web Animations API
            outline.animate({
                left: `${posX}px`,
                top: `${posY}px`
            }, { duration: 500, fill: "forwards" });

            // Active state detection
            const target = e.target;
            if (target.closest('a, button, .cursor-hover, input, select, textarea')) {
                dot.classList.add('active');
                outline.style.borderColor = 'rgba(255, 255, 255, 0.8)';
            } else {
                dot.classList.remove('active');
                outline.style.borderColor = 'rgba(74, 222, 128, 0.5)';
            }
        });
    }

    // Interactive Parallax background meshes based on mouse movement
    const mesh = document.querySelector('.bg-mesh');
    window.addEventListener('mousemove', (e) => {
        const x = e.clientX / window.innerWidth;
        const y = e.clientY / window.innerHeight;

        if (mesh) {
            // Shift the background radically smooth
            mesh.style.transform = `translate(-${x * 40}px, -${y * 40}px)`;
        }
    });

    // Initialize AOS (Animate On Scroll) library
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 800,
            once: true,
            offset: 50,
            easing: 'ease-out-cubic'
        });
    }

    // Initialize VanillaTilt for 3D interactive cards
    if (typeof VanillaTilt !== 'undefined') {
        VanillaTilt.init(document.querySelectorAll(".glass-panel"), {
            max: 5,
            speed: 400,
            glare: true,
            "max-glare": 0.1,
            scale: 1.02
        });
    }

    // Ripple effect for custom buttons
    const buttons = document.querySelectorAll('.btn-primary-custom, .btn-glass');
    buttons.forEach(btn => {
        btn.addEventListener('click', function (e) {
            let x = e.clientX - e.target.getBoundingClientRect().left;
            let y = e.clientY - e.target.getBoundingClientRect().top;

            let ripples = document.createElement('span');
            ripples.className = 'ripple-span';
            ripples.style.left = x + 'px';
            ripples.style.top = y + 'px';
            this.appendChild(ripples);

            setTimeout(() => {
                ripples.remove();
            }, 600);
        });
    });

    // Generate floating dust particles for the background
    const body = document.querySelector('body');
    for (let i = 0; i < 30; i++) {
        let span = document.createElement('span');
        span.className = 'dust-particle';

        let size = Math.random() * 3 + 1;
        span.style.width = size + 'px';
        span.style.height = size + 'px';

        span.style.left = Math.random() * innerWidth + 'px';
        span.style.top = (Math.random() * innerHeight + innerHeight) + 'px'; // Start slightly below screen

        let duration = Math.random() * 10 + 10;
        span.style.animationDuration = duration + 's';

        let delay = Math.random() * 10;
        span.style.animationDelay = delay + 's';

        body.appendChild(span);
    }

    // Live Clock functionality
    function updateClock() {
        const clockElement = document.getElementById('live-clock');
        if (clockElement) {
            const now = new Date();
            let hours = now.getHours();
            let minutes = now.getMinutes();
            let seconds = now.getSeconds();
            const ampm = hours >= 12 ? 'PM' : 'AM';
            
            hours = hours % 12;
            hours = hours ? hours : 12; // 0 hour should be 12
            
            const hoursStr = hours.toString().padStart(2, '0');
            const minutesStr = minutes.toString().padStart(2, '0');
            const secondsStr = seconds.toString().padStart(2, '0');
            
            clockElement.textContent = `${hoursStr}:${minutesStr}:${secondsStr} ${ampm}`;
        }
    }
    
    updateClock();
    setInterval(updateClock, 1000);

    // Navbar scroll effect
    const nav = document.getElementById('main-nav');
    if (nav) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 20) {
                nav.classList.add('scrolled');
            } else {
                nav.classList.remove('scrolled');
            }
        });
    }

    // Top Loading Progress Bar logic
    const progressBar = document.getElementById('topProgressBar');
    if (progressBar) {
        // Initial load simulation
        progressBar.style.width = '30%';
        
        window.addEventListener('load', () => {
            progressBar.style.width = '100%';
            setTimeout(() => {
                progressBar.style.opacity = '0';
                setTimeout(() => {
                    progressBar.style.width = '0';
                    progressBar.style.opacity = '1';
                }, 400);
            }, 500);
        });

        // Intercepting link clicks for progress bar feedback (Natural Feel)
        document.querySelectorAll('a').forEach(link => {
            if (link.hostname === window.location.hostname && !link.hash && link.target !== '_blank') {
                link.addEventListener('click', () => {
                    progressBar.style.width = '70%';
                });
            }
        });
    }

    // Synchronize pseudonyms for like forms
    const loggedInUser = localStorage.getItem('loggedInUser');
    if (loggedInUser) {
        document.querySelectorAll('.user-pseudonym-input').forEach(input => {
            input.value = loggedInUser;
        });
        
        // Also pre-fill upload form pseudonyms
        const uploadPseudonym = document.getElementById('pseudonymInput');
        if (uploadPseudonym) uploadPseudonym.value = loggedInUser;
    }
});

// Skeleton screens logic for perceived performance
window.addEventListener('load', () => {
    // Give a minimal delay (e.g. 500ms) to allow the shimmer effect to be perceived nicely
    const skeletons = document.querySelectorAll('.skeleton');
    setTimeout(() => {
        skeletons.forEach(el => el.classList.remove('skeleton'));
        
        // Refresh plugins that rely on element heights
        if (typeof AOS !== 'undefined') AOS.refresh();
        if (typeof Masonry !== 'undefined') {
            const msnryGrids = document.querySelectorAll('[data-masonry]');
            msnryGrids.forEach(grid => {
                const msnry = Masonry.data(grid);
                if (msnry) msnry.layout();
            });
        }
    }, 600);
});
