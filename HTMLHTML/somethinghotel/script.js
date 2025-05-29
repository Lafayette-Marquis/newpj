let text = '{ "employees" : [' +
'{ "firstName":"Alexander" , "lastName":"Rejunski", "jobtitle":"Host"},' +
'{ "firstName":"Charlotte" , "lastName":"Smith", "jobtitle":"Barista"},' +
'{ "firstName":"Peter" , "lastName":"Parker", "jobtitle":"Housekeeper manager"},' + 
'{ "firstName":"Javier" , "lastName":"Javier", "jobtitle":"Housekeeper"},' +
'{ "firstName":"Malachi", "lastName":"Anderson", "jobtitle":"Kitchen Staff Manager"} ]}';
const obj = JSON.parse(text);/*list of the employees to be typed*/

const toggleButton = document.getElementById('toggle-button');
const link = document.getElementById('Link')
const body = document.body;

toggleButton.addEventListener('click', () => {
    body.classList.toggle('dark-mode');

    // Change button text based on mode
    if (body.classList.contains('dark-mode')) {
        toggleButton.textContent = 'Switch to Light Mode';
    } else {
        toggleButton.textContent = 'Switch to Dark Mode';
    }
});
document.getElementById("employees").innerHTML =
        obj.employees[0].firstName + " " + obj.employees[0].lastName + ", who is the " + obj.employees[0].jobtitle + ", " +
        obj.employees[1].firstName + " " + obj.employees[1].lastName + ", who is the " + obj.employees[1].jobtitle + ", " +
        obj.employees[2].firstName + " " + obj.employees[2].lastName + ", who is the " + obj.employees[2].jobtitle + ", " +
        obj.employees[3].firstName + " " + obj.employees[3].lastName + ", who is the " + obj.employees[3].jobtitle + ", " +
        obj.employees[4].firstName + " " + obj.employees[4].lastName + ", who is the " + obj.employees[4].jobtitle + ".";