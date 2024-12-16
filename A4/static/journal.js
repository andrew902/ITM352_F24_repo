//code from chatgpt for running journal functionality
document.addEventListener("DOMContentLoaded", () => {
    const saveButton = document.getElementById('save-entry');
    const journalEntry = document.getElementById('journal-entry');
    const savedEntriesContainer = document.getElementById('saved-entries');

    // Load saved journal entries when the page is loaded
    loadJournalEntries();

    // Save new journal entry
    saveButton.addEventListener('click', () => {
        const entryText = journalEntry.value.trim();
        if (entryText !== '') {
            const entryDate = new Date().toLocaleDateString();
            const newEntry = {
                date: entryDate,
                text: entryText
            };
            saveJournalEntry(newEntry);
            journalEntry.value = '';  // Clear the textarea
        }
    });

    // Save journal entry to localStorage
    function saveJournalEntry(entry) {
        let entries = JSON.parse(localStorage.getItem('journalEntries')) || [];
        entries.push(entry);
        localStorage.setItem('journalEntries', JSON.stringify(entries));
        loadJournalEntries();  // Reload the entries to display the new one
    }

    // Load journal entries from localStorage
    function loadJournalEntries() {
        savedEntriesContainer.innerHTML = '';  // Clear the previous entries
        const entries = JSON.parse(localStorage.getItem('journalEntries')) || [];
        entries.forEach((entry, index) => {
            const entryDiv = document.createElement('div');
            entryDiv.classList.add('entry');
            entryDiv.innerHTML = `
                <h4>${entry.date}</h4>
                <p>${entry.text}</p>
                <button class="delete-button" data-index="${index}">×</button>
            `;
            savedEntriesContainer.appendChild(entryDiv);
        });

        // Add event listeners to the delete buttons
        const deleteButtons = document.querySelectorAll('.delete-button');
        deleteButtons.forEach(button => {
            button.addEventListener('click', (event) => {
                const index = event.target.getAttribute('data-index');
                deleteJournalEntry(index);
            });
        });
    }

    // Delete a journal entry from localStorage and update the display
    function deleteJournalEntry(index) {
        let entries = JSON.parse(localStorage.getItem('journalEntries')) || [];
        entries.splice(index, 1);  // Remove the entry from the array
        localStorage.setItem('journalEntries', JSON.stringify(entries));
        loadJournalEntries();  // Reload the entries to reflect the deletion
    }
});
