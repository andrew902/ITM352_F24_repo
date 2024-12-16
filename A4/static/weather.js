//code from chatgpt for open weather api functionality
document.addEventListener("DOMContentLoaded", () => {
    const apiKey = "b74e844c4803cdb071a54d67b274fe2c";
    const city = "Honolulu";
    const url = `https://api.openweathermap.org/data/2.5/forecast?q=${city}&appid=${apiKey}&units=imperial`;

    fetch(url)
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById("weather-container");
            const weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
            const currentDayIndex = new Date().getDay(); // Get the current day of the week
            let dayCounter = currentDayIndex; // Start from today
            let daysProcessed = new Set(); // Track which days have been processed

            // Loop through the forecast data, which is every 3 hours
            data.list.forEach(forecast => {
                const forecastDate = new Date(forecast.dt * 1000); // Convert timestamp to Date object
                const weekday = weekdays[forecastDate.getDay()]; // Get the weekday name

                // Check if we already added the weather for this weekday, and that we haven't reached 7 days yet
                if (!daysProcessed.has(weekday) && daysProcessed.size < 7) {
                    daysProcessed.add(weekday);

                    // Check the weather info
                    const weather = forecast.weather[0].description;
                    const temp = forecast.main.temp;
                    const rain = forecast.rain ? "🌧️" : "☀️";

                    // Add the weather data for the day
                    container.innerHTML += `
                        <div class="weather-day">
                            <h3>${weekday}</h3>
                            <p><strong>Weather:</strong> ${weather} ${rain}</p>
                            <p><strong>Temperature:</strong> ${temp}°F</p>
                        </div>
                    `;
                }
            });
        })
        .catch(err => console.error("Error fetching weather data:", err));
});
