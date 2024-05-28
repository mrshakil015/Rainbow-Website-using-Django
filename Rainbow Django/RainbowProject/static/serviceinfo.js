document.addEventListener('DOMContentLoaded', function () {
    fetch('/servicedata')
        .then(response => response.json())
        .then(data => {
            const servicecardsContainer = document.getElementById('service-cards-container');
            data.forEach(service_details => {
                const servicecard = document.createElement('div');
                servicecard.classList.add('col-lg-4');
                servicecard.classList.add('col-md-6');
                servicecard.innerHTML = `
                <div class="card card-item">
                    <div class="card-body">
                        <div class="rounded">
                        <img class="colored-box text-center h3" src="../static/images/icons/serviceicon.png" alt="Service Icon" width="30" height="30">
                            <h3 class="mb-3">${service_details.servicename}</h3>
                            <p>${service_details.aboutservice}</p>
                        </div>                        
                    </div>
                </div>
            `;
                servicecardsContainer.appendChild(servicecard);
            });
        })
        .catch(error => console.error('Error fetching data:', error));
});
