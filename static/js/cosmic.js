/**
 * cosmic.js — Starfield and Meteor Shower Background
 * High-performance 60fps HTML5 Canvas background effect.
 * Renders twinkling dark-space stars and realistic shooting meteor streaks.
 */

(function () {
    // 1. Create or bind canvas element
    let canvas = document.getElementById('cosmic-canvas');
    if (!canvas) {
        canvas = document.createElement('canvas');
        canvas.id = 'cosmic-canvas';
        document.body.prepend(canvas);
    }

    const ctx = canvas.getContext('2d');
    let width = (canvas.width = window.innerWidth);
    let height = (canvas.height = window.innerHeight);

    // 2. Starfield Setup
    const STAR_COUNT = Math.min(Math.floor((width * height) / 6000), 220);
    const stars = [];

    const starColors = [
        'rgba(255, 255, 255, ',    // Crisp white
        'rgba(185, 245, 107, ',    // Brand lime/emerald
        'rgba(167, 243, 208, ',    // Mint green
        'rgba(224, 231, 255, ',    // Pale star blue
        'rgba(253, 230, 138, '     // Warm star yellow
    ];

    function createStar() {
        return {
            x: Math.random() * width,
            y: Math.random() * height,
            radius: Math.random() < 0.85 ? Math.random() * 1.2 + 0.4 : Math.random() * 1.8 + 1.2,
            baseAlpha: Math.random() * 0.6 + 0.25,
            alpha: 0.5,
            twinkleSpeed: Math.random() * 0.025 + 0.008,
            twinklePhase: Math.random() * Math.PI * 2,
            colorPrefix: starColors[Math.floor(Math.random() * starColors.length)],
            hasGlow: Math.random() < 0.12 // Some prominent stars have a soft glow
        };
    }

    for (let i = 0; i < STAR_COUNT; i++) {
        stars.push(createStar());
    }

    // 3. Meteor Shower Setup
    const meteors = [];
    let lastMeteorSpawn = 0;
    let nextMeteorDelay = 800; // Time in ms until next meteor

    class Meteor {
        constructor() {
            this.reset();
        }

        reset() {
            // Trajectory angle: ~35-42 degrees diagonally downwards to the left
            this.angle = (Math.PI * 0.72) + (Math.random() * 0.15 - 0.075);
            
            // Spawn from upper or right boundary
            if (Math.random() < 0.55) {
                // Top boundary
                this.x = Math.random() * (width * 1.1) + (width * 0.1);
                this.y = -40;
            } else {
                // Right boundary
                this.x = width + 40;
                this.y = Math.random() * (height * 0.5);
            }

            this.speed = Math.random() * 9 + 11; // 11 to 20 px/frame
            this.length = Math.random() * 120 + 90; // 90 to 210 px tail length
            this.thickness = Math.random() * 1.6 + 1.2;

            // Velocity vectors
            this.vx = Math.cos(this.angle) * this.speed;
            this.vy = Math.sin(this.angle) * this.speed;

            // Lifecycle
            this.life = 0;
            this.maxLife = Math.random() * 65 + 45; // Frames to survive
            this.alive = true;
            this.opacity = 0;

            // Star dust particles trailing behind
            this.sparks = [];
        }

        update() {
            this.life++;
            this.x += this.vx;
            this.y += this.vy;

            // Fade in smoothly, then fade out
            const progress = this.life / this.maxLife;
            if (progress < 0.2) {
                this.opacity = progress / 0.2;
            } else {
                this.opacity = Math.max(0, 1 - (progress - 0.2) / 0.8);
            }

            // Occasionally emit tiny glowing spark particle
            if (Math.random() < 0.35 && this.opacity > 0.3) {
                this.sparks.push({
                    x: this.x + (Math.random() * 4 - 2),
                    y: this.y + (Math.random() * 4 - 2),
                    alpha: this.opacity * 0.8,
                    size: Math.random() * 1.4 + 0.6,
                    decay: Math.random() * 0.04 + 0.02
                });
            }

            // Update trailing sparks
            for (let i = this.sparks.length - 1; i >= 0; i--) {
                const s = this.sparks[i];
                s.alpha -= s.decay;
                if (s.alpha <= 0) {
                    this.sparks.splice(i, 1);
                }
            }

            if (this.life >= this.maxLife || this.x < -150 || this.y > height + 150) {
                this.alive = false;
            }
        }

        draw(ctx) {
            if (!this.alive) return;

            // 1. Draw sparks
            for (const s of this.sparks) {
                ctx.fillStyle = `rgba(185, 245, 107, ${s.alpha})`;
                ctx.beginPath();
                ctx.arc(s.x, s.y, s.size, 0, Math.PI * 2);
                ctx.fill();
            }

            // 2. Draw meteor tail streak
            const tailX = this.x - Math.cos(this.angle) * this.length;
            const tailY = this.y - Math.sin(this.angle) * this.length;

            const gradient = ctx.createLinearGradient(tailX, tailY, this.x, this.y);
            gradient.addColorStop(0, 'rgba(185, 245, 107, 0)');
            gradient.addColorStop(0.65, `rgba(185, 245, 107, ${this.opacity * 0.45})`);
            gradient.addColorStop(0.9, `rgba(220, 252, 175, ${this.opacity * 0.8})`);
            gradient.addColorStop(1, `rgba(255, 255, 255, ${this.opacity})`);

            ctx.save();
            ctx.strokeStyle = gradient;
            ctx.lineWidth = this.thickness;
            ctx.lineCap = 'round';
            ctx.shadowColor = '#b9f56b';
            ctx.shadowBlur = 10 * this.opacity;

            ctx.beginPath();
            ctx.moveTo(tailX, tailY);
            ctx.lineTo(this.x, this.y);
            ctx.stroke();

            // 3. Glowing head
            ctx.fillStyle = `rgba(255, 255, 255, ${this.opacity})`;
            ctx.shadowColor = '#ffffff';
            ctx.shadowBlur = 8;
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.thickness * 1.1, 0, Math.PI * 2);
            ctx.fill();

            ctx.restore();
        }
    }

    // 4. Handle Window Resize
    function onResize() {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;

        // Re-scatter any out of bound stars
        for (const s of stars) {
            if (s.x > width) s.x = Math.random() * width;
            if (s.y > height) s.y = Math.random() * height;
        }
    }
    window.addEventListener('resize', onResize);

    // 5. Main Animation Loop
    let lastTime = performance.now();
    let isVisible = true;

    document.addEventListener('visibilitychange', () => {
        isVisible = !document.hidden;
        if (isVisible) lastTime = performance.now();
    });

    function animate(currentTime) {
        requestAnimationFrame(animate);

        if (!isVisible) return;

        const delta = currentTime - lastTime;
        lastTime = currentTime;

        // Clear canvas with deep dark space base
        ctx.clearRect(0, 0, width, height);

        // A. Draw Subtle Space Glow / Vignette
        const radialBg = ctx.createRadialGradient(
            width * 0.5, height * 0.35, 100,
            width * 0.5, height * 0.5, Math.max(width, height)
        );
        radialBg.addColorStop(0, 'rgba(12, 22, 17, 0.45)'); // Subtle deep emerald-tinted center
        radialBg.addColorStop(0.7, 'rgba(8, 13, 11, 0.7)');
        radialBg.addColorStop(1, 'rgba(4, 7, 6, 0.9)');
        ctx.fillStyle = radialBg;
        ctx.fillRect(0, 0, width, height);

        // B. Render Stars
        for (let i = 0; i < stars.length; i++) {
            const s = stars[i];
            s.twinklePhase += s.twinkleSpeed;
            const twinkle = Math.sin(s.twinklePhase) * 0.35;
            const currentAlpha = Math.max(0.12, Math.min(1.0, s.baseAlpha + twinkle));

            // Soft glow for prominent stars
            if (s.hasGlow && currentAlpha > 0.5) {
                ctx.save();
                ctx.shadowColor = '#b9f56b';
                ctx.shadowBlur = 5;
                ctx.fillStyle = `${s.colorPrefix}${currentAlpha * 0.8})`;
                ctx.beginPath();
                ctx.arc(s.x, s.y, s.radius * 1.3, 0, Math.PI * 2);
                ctx.fill();
                ctx.restore();
            } else {
                ctx.fillStyle = `${s.colorPrefix}${currentAlpha})`;
                ctx.beginPath();
                ctx.arc(s.x, s.y, s.radius, 0, Math.PI * 2);
                ctx.fill();
            }
        }

        // C. Spawn & Update Meteor Shower
        if (currentTime - lastMeteorSpawn > nextMeteorDelay) {
            lastMeteorSpawn = currentTime;
            // Random delay between 1.2s and 3.2s
            nextMeteorDelay = Math.random() * 2000 + 1200;

            // Add new meteor
            meteors.push(new Meteor());

            // 20% chance of a double meteor (meteor shower burst)
            if (Math.random() < 0.22) {
                setTimeout(() => {
                    meteors.push(new Meteor());
                }, Math.random() * 300 + 150);
            }
        }

        // Update and draw active meteors
        for (let i = meteors.length - 1; i >= 0; i--) {
            const m = meteors[i];
            m.update();
            m.draw(ctx);
            if (!m.alive) {
                meteors.splice(i, 1);
            }
        }
    }

    requestAnimationFrame(animate);
})();
