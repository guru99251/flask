document.addEventListener("DOMContentLoaded", () => {
    // Select the result title and table rows
    const resultTitle = document.querySelector(".result-title");
    const tableRows = document.querySelectorAll(".result-table tbody tr");

    // Use requestAnimationFrame to synchronize animations
    requestAnimationFrame(() => {
        if (resultTitle) {
            resultTitle.classList.add("animate-title");
        }

        tableRows.forEach((row) => {
            row.classList.add("animate-row");
        });
    });

    // Debug: log rows for visibility
    console.debug("Result title and table rows animations synchronized.", { resultTitle, tableRows });
});

// Optional: Add an event listener to highlight hovered rows with a slight animation
const table = document.querySelector(".result-table tbody");
if (table) {
    table.addEventListener("mouseover", (event) => {
        const target = event.target.closest("tr");
        if (target) {
            target.style.transition = "transform 0.2s ease";
            target.style.transform = "scale(1.02)";
        }
    });

    table.addEventListener("mouseout", (event) => {
        const target = event.target.closest("tr");
        if (target) {
            target.style.transform = "scale(1)";
        }
    });
}

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const inputs = form.querySelectorAll("input[type='number']");
    const warningMessage = document.createElement("p");
    warningMessage.textContent = "최소 하나의 사용자에게 값을 입력해야 합니다.";
    warningMessage.style.color = "red";
    warningMessage.style.display = "none";
    form.insertBefore(warningMessage, form.querySelector("button"));

    form.addEventListener("submit", (event) => {
        let hasValue = false;
        inputs.forEach(input => {
            if (input.value.trim() !== "") {
                hasValue = true;
            }
        });

        if (!hasValue) {
            event.preventDefault();
            warningMessage.style.display = "block";
        } else {
            warningMessage.style.display = "none";
        }
    });
});

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const inputs = form.querySelectorAll("input[type='number']");
    const warningMessage = document.createElement("p");
    warningMessage.style.color = "red";
    warningMessage.style.display = "none";
    form.insertBefore(warningMessage, form.querySelector("button"));

    form.addEventListener("submit", (event) => {
        let isValid = true;
        warningMessage.textContent = ""; // Clear any previous warnings

        // Reset all card borders
        const cards = form.querySelectorAll(".card");

        inputs.forEach(input => {
            const name = input.name;
            const value = parseFloat(input.value);
            const card = input.closest(".card"); // Find the card for this input

            if (!isNaN(value)) {
                if (
                    (name.startsWith("grade") && value > 4.3) ||
                    (name.startsWith("ibt") && value > 120) ||
                    (name.startsWith("itp") && value > 677) ||
                    (name.startsWith("ielts") && value > 9)
                ) {
                    isValid = false;
                    card.style.border = "4px solid red"; // Highlight invalid card
                }
            }
        });

        if (!isValid) {
            event.preventDefault();
            warningMessage.textContent = "잘못 입력된 값이 있습니다.";
            warningMessage.style.display = "block";
        } else {
            warningMessage.style.display = "none";
        }
    });
});

