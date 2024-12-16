//code from chatgpt to have database of quotes that get randomly cycled through
document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.getElementById('toggle-quote');
    const quoteText = document.getElementById('motivational-quote');
    const quotes = [
        "\"Don't stop when you're tired, stop when you're done.\"",
        "\"If you can get through things that you hate to do, on the other side is greatness.\"",
        "\"The most important conversations you'll ever have are the ones you'll have with yourself.\"",
        "\"Suffering is a test. That's all it is. Suffering is the true test of life.",
        "\"You have to be willing to go to war with yourself and create a whole new identity.\"" ,
        "\"We're either getting better or we're getting worse.",
        "\"We don't rise to the level of our expectations, we fall to the level of our training.\""
    ];

    toggleButton.addEventListener('click', () => {
        if (quoteText.style.display === 'none') {
            const randomQuote = quotes[Math.floor(Math.random() * quotes.length)];
            quoteText.textContent = randomQuote;
            quoteText.style.display = 'block';
            toggleButton.textContent = "Hide Motivation";
        } else {
            quoteText.style.display = 'none';
            toggleButton.textContent = "Click For New Motivation";
        }
    });
});
