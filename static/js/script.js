import * as THREE from
    "https://cdn.jsdelivr.net/npm/three@0.180.0/build/three.module.js";

const container = document.getElementById("skillmap-globe");

if (container && !container.dataset.initialized) {
    container.dataset.initialized = "true";

    // -------------------------------
    // SCENE SETUP
    // -------------------------------

    const scene = new THREE.Scene();

    const camera = new THREE.PerspectiveCamera(
        40,
        1,
        0.1,
        100
    );

    camera.position.z = 5.2;

    const renderer = new THREE.WebGLRenderer({
        alpha: true,
        antialias: true
    });

    renderer.setPixelRatio(
        Math.min(window.devicePixelRatio, 2)
    );

    renderer.setSize(
        container.clientWidth,
        container.clientHeight
    );

    container.appendChild(renderer.domElement);

    // All globe elements rotate together.
    const globe = new THREE.Group();

    scene.add(globe);

    const RADIUS = 1.65;

    // -------------------------------
    // LATITUDE/LONGITUDE TO 3D
    // -------------------------------

    function getPosition(lat, lon, radius = RADIUS) {
        const phi = (90 - lat) * Math.PI / 180;
        const theta = (lon + 180) * Math.PI / 180;

        return new THREE.Vector3(
            -radius * Math.sin(phi) * Math.cos(theta),
            radius * Math.cos(phi),
            radius * Math.sin(phi) * Math.sin(theta)
        );
    }

    // -------------------------------
    // APPROXIMATE CONTINENT SHAPES
    // -------------------------------

    // These simplified outlines are used to generate
    // dotted landmasses. They are illustrative, not
    // accurate geographic boundary data.

    const continents = [
        // North America
        [
            [-168, 72], [-140, 70], [-125, 55],
            [-130, 45], [-112, 30], [-97, 16],
            [-82, 24], [-65, 45], [-80, 60],
            [-100, 73], [-135, 75]
        ],

        // South America
        [
            [-81, 12], [-60, 10], [-48, -5],
            [-35, -15], [-50, -35], [-68, -56],
            [-77, -35], [-81, -5]
        ],

        // Europe and Asia
        [
            [-10, 36], [5, 58], [30, 72],
            [65, 75], [105, 65], [145, 55],
            [160, 42], [125, 20], [105, 5],
            [80, 8], [65, 25], [45, 35],
            [35, 20], [15, 30]
        ],

        // Africa
        [
            [-18, 35], [10, 37], [35, 25],
            [48, 5], [35, -15], [20, -35],
            [5, -35], [-10, -10], [-18, 15]
        ],

        // Australia
        [
            [112, -12], [132, -10], [153, -25],
            [145, -40], [120, -35], [112, -20]
        ],

        // Greenland
        [
            [-55, 60], [-30, 70], [-42, 82],
            [-60, 78]
        ],

        // Japan and nearby island region
        [
            [130, 32], [145, 35], [145, 45],
            [137, 42]
        ],

        // Madagascar
        [
            [45, -12], [50, -15], [48, -26],
            [44, -20]
        ]
    ];

    // Ray-casting point-in-polygon test.
    function isInsidePolygon(lon, lat, polygon) {
        let inside = false;

        for (
            let i = 0, j = polygon.length - 1;
            i < polygon.length;
            j = i++
        ) {
            const [xi, yi] = polygon[i];
            const [xj, yj] = polygon[j];

            const crosses =
                (yi > lat) !== (yj > lat) &&
                lon <
                    ((xj - xi) * (lat - yi)) /
                    ((yj - yi) || 0.000001) + xi;

            if (crosses) {
                inside = !inside;
            }
        }

        return inside;
    }

    function isLand(lat, lon) {
        // Avoid ambiguous wraparound at the map edges.
        if (Math.abs(lon) > 175) {
            return false;
        }

        return continents.some(
            polygon => isInsidePolygon(lon, lat, polygon)
        );
    }

    // -------------------------------
    // DOTTED EARTH
    // -------------------------------

    const landPositions = [];
    const landColors = [];

    const landColor = new THREE.Color("#42d9ff");

    for (let lat = -58; lat <= 82; lat += 2.8) {
        for (let lon = -177; lon <= 177; lon += 2.8) {
            if (!isLand(lat, lon)) continue;

            const position = getPosition(lat, lon, RADIUS);

            landPositions.push(
                position.x,
                position.y,
                position.z
            );

            landColors.push(
                landColor.r,
                landColor.g,
                landColor.b
            );
        }
    }

    const landGeometry = new THREE.BufferGeometry();

    landGeometry.setAttribute(
        "position",
        new THREE.Float32BufferAttribute(landPositions, 3)
    );

    landGeometry.setAttribute(
        "color",
        new THREE.Float32BufferAttribute(landColors, 3)
    );

    const landMaterial = new THREE.PointsMaterial({
        size: 0.027,
        vertexColors: true,
        transparent: true,
        opacity: 0.9,
        sizeAttenuation: true
    });

    const landDots = new THREE.Points(
        landGeometry,
        landMaterial
    );

    globe.add(landDots);

    // -------------------------------
    // SUBTLE SPHERE OUTLINE
    // -------------------------------

    const sphereGeometry = new THREE.SphereGeometry(
        RADIUS,
        48,
        48
    );

    const sphereMaterial = new THREE.MeshBasicMaterial({
        color: 0x1673a6,
        wireframe: true,
        transparent: true,
        opacity: 0.055
    });

    const sphereOutline = new THREE.Mesh(
        sphereGeometry,
        sphereMaterial
    );

    globe.add(sphereOutline);

    // -------------------------------
    // GLOWING CONNECTION ARCS
    // -------------------------------

    const connections = [
        // North America to Europe
        { from: [40, -100], to: [51, 0] },

        // Europe to India
        { from: [51, 0], to: [19, 73] },

        // India to East Asia
        { from: [19, 73], to: [35, 139] },

        // Europe to Africa
        { from: [51, 0], to: [-1, 37] },

        // India to Australia
        { from: [19, 73], to: [-25, 133] },

        // North America to South America
        { from: [40, -100], to: [-15, -60] },

        // North America to East Asia
        { from: [40, -100], to: [35, 139] }
    ];

    const arcMaterial = new THREE.LineBasicMaterial({
        color: 0x3ce9ff,
        transparent: true,
        opacity: 0.8
    });

    function createArc(start, end) {
        const points = [];

        const startPoint = getPosition(
            start[0],
            start[1],
            RADIUS + 0.025
        );

        const endPoint = getPosition(
            end[0],
            end[1],
            RADIUS + 0.025
        );

        const middle = startPoint.clone().add(endPoint).multiplyScalar(0.5);

        middle.setLength(RADIUS + 0.45);

        const curve = new THREE.QuadraticBezierCurve3(
            startPoint,
            middle,
            endPoint
        );

        for (let i = 0; i <= 50; i++) {
            points.push(curve.getPoint(i / 50));
        }

        const geometry = new THREE.BufferGeometry().setFromPoints(
            points
        );

        const line = new THREE.Line(geometry, arcMaterial);

        globe.add(line);
    }

    connections.forEach(connection => {
        createArc(connection.from, connection.to);
    });

    // -------------------------------
    // CAREER NETWORK MARKERS
    // -------------------------------

    const locations = [
        { name: "North America", lat: 40, lon: -100 },
        { name: "Europe", lat: 51, lon: 0 },
        { name: "India", lat: 19, lon: 73 },
        { name: "East Asia", lat: 35, lon: 139 },
        { name: "Africa", lat: -1, lon: 37 },
        { name: "Australia", lat: -25, lon: 133 },
        { name: "South America", lat: -15, lon: -60 }
    ];

    const markerMaterial = new THREE.MeshBasicMaterial({
        color: 0x72ffcf
    });

    locations.forEach(location => {
        const marker = new THREE.Mesh(
            new THREE.SphereGeometry(0.035, 12, 12),
            markerMaterial
        );

        marker.position.copy(
            getPosition(
                location.lat,
                location.lon,
                RADIUS + 0.045
            )
        );

        globe.add(marker);

        // Soft halo around each network point.
        const halo = new THREE.Mesh(
            new THREE.SphereGeometry(0.075, 12, 12),
            new THREE.MeshBasicMaterial({
                color: 0x24e8c5,
                transparent: true,
                opacity: 0.15
            })
        );

        halo.position.copy(marker.position);

        globe.add(halo);
    });

    // Tilt the Earth slightly for a more interesting view.
    globe.rotation.z = -0.12;
    globe.rotation.x = 0.12;

    // -------------------------------
    // MOUSE DRAG ROTATION
    // -------------------------------

    let dragging = false;
    let previousX = 0;
    let previousY = 0;

    let velocityX = 0;
    let velocityY = 0;

    container.addEventListener("pointerdown", event => {
        dragging = true;

        previousX = event.clientX;
        previousY = event.clientY;

        container.setPointerCapture(event.pointerId);
    });

    container.addEventListener("pointermove", event => {
        if (!dragging) return;

        const deltaX = event.clientX - previousX;
        const deltaY = event.clientY - previousY;

        velocityY = deltaX * 0.005;
        velocityX = deltaY * 0.005;

        globe.rotation.y += velocityY;
        globe.rotation.x += velocityX;

        // Keep the globe from flipping upside down.
        globe.rotation.x = Math.max(
            -1.35,
            Math.min(1.35, globe.rotation.x)
        );

        previousX = event.clientX;
        previousY = event.clientY;
    });

    function stopDragging() {
        dragging = false;
    }

    container.addEventListener("pointerup", stopDragging);
    container.addEventListener("pointercancel", stopDragging);

    // -------------------------------
    // SCROLL TO ZOOM
    // -------------------------------

    container.addEventListener(
        "wheel",
        event => {
            event.preventDefault();

            camera.position.z += event.deltaY * 0.003;

            camera.position.z = Math.max(
                3.3,
                Math.min(7, camera.position.z)
            );
        },
        { passive: false }
    );

    // -------------------------------
    // RESPONSIVE SIZE
    // -------------------------------

    function resizeGlobe() {
        const width = container.clientWidth;
        const height = container.clientHeight;

        if (!width || !height) return;

        camera.aspect = width / height;
        camera.updateProjectionMatrix();

        renderer.setSize(width, height);
    }

    const resizeObserver = new ResizeObserver(resizeGlobe);

    resizeObserver.observe(container);

    // -------------------------------
    // ANIMATION LOOP
    // -------------------------------

    const reducedMotion = window.matchMedia(
        "(prefers-reduced-motion: reduce)"
    ).matches;

    function animate() {
        requestAnimationFrame(animate);

        if (!dragging && !reducedMotion) {
            // Automatic rotation.
            globe.rotation.y += 0.0018;

            // Gentle momentum after dragging.
            globe.rotation.y += velocityY * 0.12;
            globe.rotation.x += velocityX * 0.12;

            velocityX *= 0.92;
            velocityY *= 0.92;
        }

        renderer.render(scene, camera);
    }

    resizeGlobe();
    animate();
}