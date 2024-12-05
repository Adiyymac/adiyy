// Add text to the "about-footer" section
const aboutFooter = document.querySelector('.about-footer');
aboutFooter.textContent = 'About Us: Malharul Uloom Arabic College is dedicated to providing quality education in Arabic studies and Islamic culture.';

// Update the "address" section with additional details
const address = document.querySelector('.adress-footer');
address.innerHTML = `
    <p><i class="fa-solid fa-location-dot"></i> Palamthodu, Kerala, India</p>
    <p><i class="fa-solid fa-phone"></i> +91 9876543210</p>
    <p><i class="fa-regular fa-envelope"></i> info@malharulcollege.edu</p>
`;

// Add links to the "goto" section
const goto = document.querySelector('.goto');
goto.innerHTML = `
    <a href="#about">About Us</a> | 
    <a href="#courses">Courses</a> | 
    <a href="#contact">Contact</a>

    <br>
    <div class="icon-footr">
        <i class="fa-brands fa-instagram"></i>
        <i class="fa-brands fa-facebook"></i>
        <i class="fa-brands fa-youtube"></i>
        <i class="fa-brands fa-pinterest"></i>
        <i class="fa-brands fa-twitter"></i>
        <i class="fa-brands fa-linkedin"></i>
    </div>

`
;

// Add a list of recent posts in the "recentpost" section
const recentPosts = document.querySelector('.recentpost');
recentPosts.innerHTML = `
    <h4>Recent Posts</h4>
    <ul>
        <li><a href="#">Arabic Studies - A Journey</a></li>
        <li><a href="#">Upcoming Events 2024</a></li>
        <li><a href="#">Islamic Scholarship Opportunities</a></li>
    </ul>
`;

// Update the footer copyright dynamically
//const footerParagraph = document.querySelector('footer p');
//footerParagraph.textContent = `© ${new Date().getFullYear()} Malharul Uloom Arabic College. All rights reserved.`;


//chnage lastest event
// Get the elements
const eventsContainer = document.querySelector('.events');
const eventItems = document.querySelectorAll('.event');

// Define the new data
const eventData = [
  {
    date: 'Jan 10',
    description: 'iniyumurulum malhar arts fest x'
  },
  {
    date: 'Jan 15',
    description: 'New event description 2'
  },
  {
    date: 'Jan 20',
    description: 'New event description 3'
  },
  {
    date: 'Jan 25',
    description: 'New event description 4'
  }
];

// Loop through the event items and update the innerHTML
eventItems.forEach((item, index) => {
  const dateElement = item.querySelector('.date');
  const descriptionElement = item.querySelector('.eventcote');
  
  dateElement.innerHTML = eventData[index].date;
  descriptionElement.innerHTML = eventData[index].description;
});