
document.addEventListener('DOMContentLoaded', function() {
    // Successful Students Pagination
    const studentItemsPerPage = 4;
    const studentCards = document.querySelectorAll('.student-card-item');
    const studentTotalItems = studentCards.length;
    const studentTotalPages = Math.ceil(studentTotalItems / studentItemsPerPage);
    let studentCurrentPage = 1;

    function showStudentPage(page) {
        const start = (page - 1) * studentItemsPerPage;
        const end = start + studentItemsPerPage;
        studentCards.forEach((item, index) => {
            item.style.display = (index >= start && index < end) ? 'block' : 'none';
        });
        updateStudentPaginationControls();
    }

    function updateStudentPaginationControls() {
        const paginationContainer = document.getElementById('student-pagination-controls');
        paginationContainer.innerHTML = '';
        const ul = document.createElement('ul');
        ul.classList.add('pagination', 'justify-content-center');
        
        for (let i = 1; i <= studentTotalPages; i++) {
            const li = document.createElement('li');
            li.classList.add('page-item');
            if (i === studentCurrentPage) {
                li.classList.add('active');
            }
            const button = document.createElement('button');
            button.textContent = i;
            button.classList.add('page-link');
            button.addEventListener('click', () => {
                studentCurrentPage = i;
                showStudentPage(studentCurrentPage);
            });
            li.appendChild(button);
            ul.appendChild(li);
        }
        
        paginationContainer.appendChild(ul);
    }

    showStudentPage(studentCurrentPage);

    // Gallery Pagination
    const galleryItemsPerPage = 3;
    const galleryItems = document.querySelectorAll('.gallery-item');
    const galleryTotalItems = galleryItems.length;
    const galleryTotalPages = Math.ceil(galleryTotalItems / galleryItemsPerPage);
    let galleryCurrentPage = 1;

    function showGalleryPage(page) {
        const start = (page - 1) * galleryItemsPerPage;
        const end = start + galleryItemsPerPage;
        galleryItems.forEach((item, index) => {
            item.style.display = (index >= start && index < end) ? 'block' : 'none';
        });
        updateGalleryPaginationControls();
    }

    function updateGalleryPaginationControls() {
        const paginationContainer = document.getElementById('gallery-pagination-controls');
        paginationContainer.innerHTML = '';
        const ul = document.createElement('ul');
        ul.classList.add('pagination', 'justify-content-center');
        
        for (let i = 1; i <= galleryTotalPages; i++) {
            const li = document.createElement('li');
            li.classList.add('page-item');
            if (i === galleryCurrentPage) {
                li.classList.add('active');
            }
            const button = document.createElement('button');
            button.textContent = i;
            button.classList.add('page-link');
            button.addEventListener('click', () => {
                galleryCurrentPage = i;
                showGalleryPage(galleryCurrentPage);
            });
            li.appendChild(button);
            ul.appendChild(li);
        }
        
        paginationContainer.appendChild(ul);
    }

    showGalleryPage(galleryCurrentPage);
});


document.addEventListener('DOMContentLoaded', function() {
    // Services Pagination
    const serviceItemsPerPage = 3;
    const serviceCards = document.querySelectorAll('.service-card-item');
    const serviceTotalItems = serviceCards.length;
    const serviceTotalPages = Math.ceil(serviceTotalItems / serviceItemsPerPage);
    let serviceCurrentPage = 1;

    function showServicePage(page) {
        const start = (page - 1) * serviceItemsPerPage;
        const end = start + serviceItemsPerPage;
        serviceCards.forEach((item, index) => {
            item.style.display = (index >= start && index < end) ? 'block' : 'none';
        });
        updateServicePaginationControls();
    }

    function updateServicePaginationControls() {
        const paginationContainer = document.getElementById('service-pagination-controls');
        paginationContainer.innerHTML = '';
        const ul = document.createElement('ul');
        ul.classList.add('pagination', 'justify-content-center');
        
        for (let i = 1; i <= serviceTotalPages; i++) {
            const li = document.createElement('li');
            li.classList.add('page-item');
            if (i === serviceCurrentPage) {
                li.classList.add('active');
            }
            const button = document.createElement('button');
            button.textContent = i;
            button.classList.add('page-link');
            button.addEventListener('click', () => {
                serviceCurrentPage = i;
                showServicePage(serviceCurrentPage);
            });
            li.appendChild(button);
            ul.appendChild(li);
        }
        
        paginationContainer.appendChild(ul);
    }

    showServicePage(serviceCurrentPage);

    // Courses Pagination
    const courseItemsPerPage = 3;
    const courseCards = document.querySelectorAll('.course-card-item');
    const courseTotalItems = courseCards.length;
    const courseTotalPages = Math.ceil(courseTotalItems / courseItemsPerPage);
    let courseCurrentPage = 1;

    function showCoursePage(page) {
        const start = (page - 1) * courseItemsPerPage;
        const end = start + courseItemsPerPage;
        courseCards.forEach((item, index) => {
            item.style.display = (index >= start && index < end) ? 'block' : 'none';
        });
        updateCoursePaginationControls();
    }

    function updateCoursePaginationControls() {
        const paginationContainer = document.getElementById('course-pagination-controls');
        paginationContainer.innerHTML = '';
        const ul = document.createElement('ul');
        ul.classList.add('pagination', 'justify-content-center');
        
        for (let i = 1; i <= courseTotalPages; i++) {
            const li = document.createElement('li');
            li.classList.add('page-item');
            if (i === courseCurrentPage) {
                li.classList.add('active');
            }
            const button = document.createElement('button');
            button.textContent = i;
            button.classList.add('page-link');
            button.addEventListener('click', () => {
                courseCurrentPage = i;
                showCoursePage(courseCurrentPage);
            });
            li.appendChild(button);
            ul.appendChild(li);
        }
        
        paginationContainer.appendChild(ul);
    }

    showCoursePage(courseCurrentPage);
});

