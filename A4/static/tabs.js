//code form chatgpt for navigation tab functionality
function openTab(event, tabName) {
    // Hide all tab contents
    let tabContents = document.getElementsByClassName("tab-content");
    for (let i = 0; i < tabContents.length; i++) {
        tabContents[i].style.display = "none";
    }

    // Remove the 'active' class from all tab buttons
    let tabButtons = document.getElementsByClassName("tab-button");
    for (let i = 0; i < tabButtons.length; i++) {
        tabButtons[i].classList.remove("active");
    }

    // Show the selected tab and add the 'active' class to the clicked button
    document.getElementById(tabName).style.display = "block";
    event.currentTarget.classList.add("active");
}
