document.addEventListener('DOMContentLoaded', function () {
    const imagesPerPage = 4;
    let currentPage = 1;
    let autoScrollInterval;

    fetch('/successfulstudentdata')
        .then(response => response.json())
        .then(data => {
            const successfulstudentcardsContainer = document.getElementById('successfulstudent-cards-container');
            const totalImages = data.length;
            const totalPages = Math.ceil(totalImages / imagesPerPage);

            // Function to display images for the current page
            const displayImages = () => {
                // Clear existing content
                successfulstudentcardsContainer.innerHTML = '';

                // Calculate start and end index of images for the current page
                const startIndex = (currentPage - 1) * imagesPerPage;
                const endIndex = Math.min(startIndex + imagesPerPage, totalImages);

                // Loop through images for the current page and create image elements
                for (let i = startIndex; i < endIndex; i++) {
                    const successfulstudent_details = data[i];
                    const successfulstudentcard = document.createElement('div');
                    successfulstudentcard.classList.add('col-lg-3');
                    successfulstudentcard.classList.add('col-md-6');
                    console.log(successfulstudent_details.image_name);
                    successfulstudentcard.innerHTML = `
                    <div class="card card-item">
                    <div class="view view-cascade overlay text-center">
                    <img src="../static/images/successfulstudent/${successfulstudent_details.image_name}" class="card-img-top" alt="profile image">
                    </div>
                    <div class="card-body">
                      <h4 class="card-title"><strong>${successfulstudent_details.studentname}</strong>
                      </h4>
                      <p class="designation">${successfulstudent_details.studentdesignation}</p>
                      <p class="institute">${successfulstudent_details.studentinstitute}</p>
                    </div>
                  </div>
                    `;
                    successfulstudentcardsContainer.appendChild(successfulstudentcard);
                }

                // Update pagination links
                updatePagination();
            };

            // Function to update pagination links
            const updatePagination = () => {
                const paginationContainer = document.getElementById('successfulpagination');
                paginationContainer.innerHTML = '';

                // Add Previous button
                if (currentPage > 1) {
                    paginationContainer.innerHTML += `
                        <li class="page-item">
                            <button class="page-link" onclick="changePage(${currentPage - 1})" aria-label="Previous">
                                <span aria-hidden="true">&laquo;</span>
                                <span class="visually-hidden">Previous</span>
                            </button>
                        </li>
                    `;
                }

                // Add numbered pages
                for (let i = 1; i <= totalPages; i++) {
                    paginationContainer.innerHTML += `
                        <li class="page-item${currentPage === i ? ' active' : ''}">
                            <button class="page-link" onclick="changePage(${i})">${i}</button>
                        </li>
                    `;
                }

                // Add Next button
                if (currentPage < totalPages) {
                    paginationContainer.innerHTML += `
                        <li class="page-item">
                            <button class="page-link" onclick="changePage(${currentPage + 1})" aria-label="Next">
                                <span aria-hidden="true">&raquo;</span>
                                <span class="visually-hidden">Next</span>
                            </button>
                        </li>
                    `;
                }
            };

            // Initial display
            displayImages();

            // Function to handle pagination
            window.changePage = (page) => {
                currentPage = page;
                displayImages();
            };

            // Auto scroll pagination function
            const autoScrollPagination = () => {
                autoScrollInterval = setInterval(() => {
                    if (currentPage < totalPages) {
                        currentPage++;
                    } else {
                        currentPage = 1;
                    }
                    displayImages();
                }, 5000); // Change 5000 to desired milliseconds for auto scroll interval
            };

            // Start auto scrolling
            autoScrollPagination();

            // Stop auto scrolling on hover
            document.getElementById('successfulpagination').addEventListener('mouseenter', () => {
                clearInterval(autoScrollInterval);
            });

            // Resume auto scrolling on mouse leave
            document.getElementById('successfulpagination').addEventListener('mouseleave', () => {
                autoScrollPagination();
            });
        })
        .catch(error => console.error('Error fetching data:', error));
});
