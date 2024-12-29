let renderer, camera, scene;
    let city, smoke, town;
    const uSpeed = 0.001;
    let mouse = new THREE.Vector2();

    // Initialize the scene
    function init() {
      setupRenderer();
      setupCamera();
      setupScene();
      createCity();
      setupLighting();
      createSmoke();
      generateLines();
      addEventListeners();
      animate();
    }

    // Setup the WebGL renderer
    function setupRenderer() {
      renderer = new THREE.WebGLRenderer({ antialias: true });
      renderer.setSize(window.innerWidth, window.innerHeight);
      
      if (window.innerWidth > 800) {
        renderer.shadowMap.enabled = false;
        renderer.shadowMap.type = THREE.PCFSoftShadowMap;
      }
      
      document.getElementById('threejs-background').appendChild(renderer.domElement);
    }

    // Setup the camera
    function setupCamera() {
      camera = new THREE.PerspectiveCamera(20, window.innerWidth / window.innerHeight, 1, 500);
      camera.position.set(6, 6, 15);
    }

    // Setup the main scene
    function setupScene() {
      scene = new THREE.Scene();
      city = new THREE.Object3D();
      smoke = new THREE.Object3D();
      town = new THREE.Object3D();

      const setcolor = 0xF02050;
      scene.background = new THREE.Color(setcolor);
      scene.fog = new THREE.Fog(setcolor, 10, 16);

      scene.add(city);
      city.add(smoke);
      city.add(town);

      // Add grid helper
      const gridHelper = new THREE.GridHelper(60, 120, 0xFF0000, 0x000000);
      city.add(gridHelper);
    }

    // Create the buildings
    function createCity() {
      const segments = 1;
      
      for (let i = 1; i < 80; i++) {
        const geometry = new THREE.BoxGeometry(1, 1, 1, segments, segments, segments);
        const material = new THREE.MeshStandardMaterial({
          color: 0x000000,
          wireframe: false,
          side: THREE.DoubleSide,
          roughness: 0.3,
          metalness: 0.8
        });

        // Create building
        const building = new THREE.Mesh(geometry, material);
        building.castShadow = true;
        building.receiveShadow = true;
        building.scale.y = 0.1 + Math.abs(mathRandom(8));
        building.scale.x = building.scale.z = 0.9 + mathRandom(0.1);
        building.position.x = Math.round(mathRandom());
        building.position.z = Math.round(mathRandom());
        building.position.y = building.scale.y / 2;

        // Create floor
        const floor = building.clone();
        floor.scale.y = 0.05;
        floor.position.y = 0;

        town.add(building);
        town.add(floor);
      }
    }

    // Setup scene lighting
    function setupLighting() {
      const ambientLight = new THREE.AmbientLight(0xFFFFFF, 3);
      const lightFront = new THREE.SpotLight(0xFFFFFF, 20, 10);
      const lightBack = new THREE.PointLight(0xFFFFFF, 0.5);

      lightFront.rotation.x = 45 * Math.PI / 180;
      lightFront.rotation.z = -45 * Math.PI / 180;
      lightFront.position.set(5, 5, 5);
      lightFront.castShadow = true;
      lightFront.shadow.mapSize.width = 6000;
      lightFront.shadow.mapSize.height = lightFront.shadow.mapSize.width;
      lightFront.penumbra = 0.1;

      lightBack.position.set(0, 6, 0);

      scene.add(ambientLight);
      city.add(lightFront);
      scene.add(lightBack);
    }

    // Create smoke particles
    function createSmoke() {
      const particleMaterial = new THREE.MeshToonMaterial({
        color: 0xFFFF00,
        side: THREE.DoubleSide
      });
      
      const particleGeometry = new THREE.CircleGeometry(0.01, 3);
      
      for (let i = 0; i < 150; i++) {
        const particle = new THREE.Mesh(particleGeometry, particleMaterial);
        particle.position.set(
          mathRandom(5),
          mathRandom(5),
          mathRandom(5)
        );
        particle.rotation.set(
          mathRandom(),
          mathRandom(),
          mathRandom()
        );
        smoke.add(particle);
      }
      
      smoke.position.y = 2;
    }

    // Generate moving lines/cars
    function generateLines() {
      for (let i = 0; i < 40; i++) {
        createCar(0.1, 20);
      }
    }

    // Create a single car
    function createCar(scale = 0.1, position = 20) {
      const carMaterial = new THREE.MeshToonMaterial({
        color: 0xFFFF00,
        side: THREE.DoubleSide
      });
      
      const carGeometry = new THREE.BoxGeometry(1, scale/40, scale/40);
      const car = new THREE.Mesh(carGeometry, carMaterial);
      
      car.position.x = -position;
      car.position.z = mathRandom(3);
      car.position.y = Math.abs(mathRandom(5));
      
      car.castShadow = true;
      car.receiveShadow = true;
      
      city.add(car);
      
      TweenMax.to(car.position, 3, {
        x: position,
        repeat: -1,
        yoyo: true,
        delay: mathRandom(3)
      });
    }

    // Utility function for random numbers
    function mathRandom(num = 8) {
      return -Math.random() * num + Math.random() * num;
    }

    // Handle window resize
    function onWindowResize() {
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
    }

    // Handle mouse movement
    function onMouseMove(event) {
      mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
      mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;
    }

    // Handle touch events
    function onTouchMove(event) {
      if (event.touches.length === 1) {
        event.preventDefault();
        mouse.x = (event.touches[0].pageX / window.innerWidth) * 2 - 1;
        mouse.y = -(event.touches[0].pageY / window.innerHeight) * 2 + 1;
      }
    }

    // Add event listeners
    function addEventListeners() {
      window.addEventListener('resize', onWindowResize, false);
      window.addEventListener('mousemove', onMouseMove, false);
      window.addEventListener('touchmove', onTouchMove, false);
    }

    // Animation loop
    function animate() {
      requestAnimationFrame(animate);
      
      // Rotate city based on mouse position
      city.rotation.y -= ((mouse.x * 8) - camera.rotation.y) * uSpeed;
      city.rotation.x -= (-(mouse.y * 2) - camera.rotation.x) * uSpeed;
      
      // Clamp rotation
      city.rotation.x = Math.max(-0.05, Math.min(city.rotation.x, 1));
      
      // Rotate smoke
      smoke.rotation.y += 0.01;
      smoke.rotation.x += 0.01;

      camera.lookAt(city.position);
      renderer.render(scene, camera);
    }

    // Start the application
    document.addEventListener("DOMContentLoaded", function() {
      init();
  });
  
  // ... (kode lainnya tetap sama)