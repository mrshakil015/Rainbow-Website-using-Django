document.addEventListener('DOMContentLoaded', function () {
    const galleryimagesPerPage = 2;
    let gallerycurrentPage = 1;
    let galleryAutoScrollInterval;

    fetch('/galleryimagedata')
        .then(response => response.json())
        .then(data => {
            const galleryimagecardsContainer = document.getElementById('galleryimage-cards-container');
            const gallerytotalImages = data.length;
            const gallerytotalPages = Math.ceil(gallerytotalImages / galleryimagesPerPage);

            // Function to display images for the current page
            const gallerydisplayImages = () => {
                // Clear existing content
                galleryimagecardsContainer.innerHTML = '';

                // Calculate start and end index of images for the current page
                const gallerystartIndex = (gallerycurrentPage - 1) * galleryimagesPerPage;
                const galleryendIndex = Math.min(gallerystartIndex + galleryimagesPerPage, gallerytotalImages);

                // Loop through images for the current page and create image elements
                for (let i = gallerystartIndex; i < galleryendIndex; i++) {
                    const galleryimage_details = data[i];
                    const galleryimagecard = document.createElement('div');
                    galleryimagecard.classList.add('col-lg-6');
                    galleryimagecard.classList.add('col-md-6');
                    galleryimagecard.innerHTML = `
                        <div class="img-card" style="height: 300px; padding-top:20px;">
                            <img src="../static/images/${galleryimage_details.imagename}" class="card-img-top" alt="profile image" style="width: 100%; height: 100%; object-fit: cover; border-radius: 20px;">
                        </div>
                    `;
                    galleryimagecardsContainer.appendChild(galleryimagecard);
                }

                // Update gallerypagination links
                updategallerypagination();
            };

            // Function to update gallerypagination links
            const updategallerypagination = () => {
                const gallerypaginationContainer = document.getElementById('gallerypagination');
                gallerypaginationContainer.innerHTML = '';

                // Add Previous button
                if (gallerycurrentPage > 1) {
                    gallerypaginationContainer.innerHTML += `
                        <li class="page-item">
                            <button class="page-link" onclick="gallerychangePage(${gallerycurrentPage - 1})" aria-label="Previous">
                                <span aria-hidden="true">&laquo;</span>
                                <span class="visually-hidden">Previous</span>
                            </button>
                        </li>
                    `;
                }

                // Add numbered pages
                for (let i = 1; i <= gallerytotalPages; i++) {
                    gallerypaginationContainer.innerHTML += `
                        <li class="page-item${gallerycurrentPage === i ? ' active' : ''}">
                            <button class="page-link" onclick="gallerychangePage(${i})">${i}</button>
                        </li>
                    `;
                }

                // Add Next button
                if (gallerycurrentPage < gallerytotalPages) {
                    gallerypaginationContainer.innerHTML += `
                        <li class="page-item">
                            <button class="page-link" onclick="gallerychangePage(${gallerycurrentPage + 1})" aria-label="Next">
                                <span aria-hidden="true">&raquo;</span>
                                <span class="visually-hidden">Next</span>
                            </button>
                        </li>
                    `;
                }
            };

            // Initial display
            gallerydisplayImages();

            // Function to handle gallerypagination
            window.gallerychangePage = (page) => {
                gallerycurrentPage = page;
                gallerydisplayImages();
            };

            // Auto scroll pagination function
            const galleryautoScrollPagination = () => {
                galleryAutoScrollInterval = setInterval(() => {
                    if (gallerycurrentPage < gallerytotalPages) {
                        gallerycurrentPage++;
                    } else {
                        gallerycurrentPage = 1;
                    }
                    gallerydisplayImages();
                }, 5000); // Change 5000 to desired milliseconds for auto scroll interval
            };

            // Start auto scrolling
            galleryautoScrollPagination();

            // Stop auto scrolling on hover
            document.getElementById('gallerypagination').addEventListener('mouseenter', () => {
                clearInterval(galleryAutoScrollInterval);
            });

            // Resume auto scrolling on mouse leave
            document.getElementById('gallerypagination').addEventListener('mouseleave', () => {
                galleryautoScrollPagination();
            });
        })
        .catch(error => console.error('Error fetching data:', error));
});
