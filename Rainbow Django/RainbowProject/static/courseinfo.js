document.addEventListener('DOMContentLoaded', function () {
    fetch('/coursedata')
        .then(response => response.json())
        .then(data => {
            const cardsContainer = document.getElementById('cards-container');
            data.forEach(course_details => {
                const card = document.createElement('div');
                console.log("This is course details: ", course_details);
                console.log("Course id: ", course_details.courseid);
                card.classList.add('col-lg-4');
                card.classList.add('col-md-6');
                card.innerHTML = `
                <div class="card card-item">
                    <div class="card-header view view-cascade overlay text-center">
                        <img src="../static/images/${course_details.image_name}" class="card-img-top" alt="profile image">
                    </div>
                    <div class="card-body">
                    <hr>
                        <h4 class="card-title"><strong>${course_details.course_name}</strong></h4>
                        <div class="card-info">
                            <button class="btn btn-outline-primary">${course_details.month_duration} মাস</button>
                            <button class="btn btn-outline-primary">সপ্তাহে ${course_details.weekly} দিন</button>
                            <button class="btn btn-outline-primary">${course_details.duration_hour} ঘন্টা ${course_details.duration_minute} মিনিট</button>
                            <p class="price">৳  ${course_details.amount}/-</p>
                            <hr>
                            <div class="course-footer">
                                <button class="btn btn-outline-primary" onclick="redirectToCourseInfo(${course_details.courseid})">বিস্তারিত দেখুন</button>
                            </div>
                        </div>
                    </div>
                </div>
            `;
                cardsContainer.appendChild(card);
            });
        })
        .catch(error => console.error('Error fetching data:', error));
});

function redirectToCourseInfo(courseid) {
    window.location.href = `/courseinfo/${courseid}`;
}
