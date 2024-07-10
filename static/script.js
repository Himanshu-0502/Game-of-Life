const gridElement = document.getElementById('grid');
let grid = [];
let interval;

// Fetch the grid from the server
async function fetchGrid(url) {
    const response = await fetch(url);
    return response.json();
}

// Initialize the grid
async function initializeGrid() {
    grid = await fetchGrid('/initialize');
    renderGrid();
}

// Render the grid
function renderGrid() {
    gridElement.innerHTML = '';
    for (let row of grid) {
        for (let cell of row) {
            const cellElement = document.createElement('div');
            cellElement.className = `cell ${cell ? 'alive' : ''}`;
            gridElement.appendChild(cellElement);
        }
    }
}

// Update the grid
async function updateGrid() {
    const response = await fetch('/update', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ grid: grid })
    });
    grid = await response.json();
    renderGrid();
}

// Start the game
function startGame() {
    if (!interval) {
        interval = setInterval(updateGrid, 1);
    }
}

// Stop the game
function stopGame() {
    clearInterval(interval);
    interval = null;
}

// Reset the game
function resetGame() {
    stopGame();
    initializeGrid();
}

initializeGrid();