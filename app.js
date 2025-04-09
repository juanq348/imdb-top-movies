// Esperar a que el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', function() {
    // Funcionalidad para las pestañas de visualización
    const tabs = document.querySelectorAll('.viz-tab');
    
    tabs.forEach(tab => {
        tab.addEventListener('click', function() {
            // Desactivar todas las pestañas
            tabs.forEach(t => t.classList.remove('active'));
            
            // Desactivar todos los contenidos
            document.querySelectorAll('.viz-content').forEach(content => {
                content.classList.remove('active');
            });
            
            // Activar la pestaña actual
            this.classList.add('active');
            
            // Activar el contenido correspondiente
            const tabId = this.getAttribute('data-tab');
            document.getElementById(tabId).classList.add('active');
        });
    });

    // Funcionalidad para hacer las tarjetas clickeables si es necesario
    const vizItems = document.querySelectorAll('.viz-item');
    
    vizItems.forEach(item => {
        item.addEventListener('click', function() {
            // Aquí puedes agregar funcionalidad para mostrar una versión ampliada del gráfico
            // Por ejemplo, abrir un modal con la imagen a tamaño completo
            const imgSrc = this.querySelector('img').src;
            const title = this.querySelector('h3').textContent;
            
            // Ejemplo: console.log(`Imagen ${title} clickeada: ${imgSrc}`);
            // Aquí puedes implementar un modal o lightbox
        });
    });

    // Animación de scroll suave para los enlaces internos
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
});

// Función opcional para animar elementos cuando aparecen en el viewport
function animateOnScroll() {
    const elements = document.querySelectorAll('.method-card, .viz-item, .finding-card');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1
    });
    
    elements.forEach(element => {
        observer.observe(element);
    });
}

// Descomentar la siguiente línea para activar animaciones al hacer scroll
// animateOnScroll();