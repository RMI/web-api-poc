// Initialize search functionality when the DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    const searchButton = document.getElementById('search-button');
    const searchInput = document.getElementById('search-input');
    
    if (searchButton && searchInput) {
        // Search when button is clicked
        searchButton.addEventListener('click', () => {
            performSearch(searchInput.value);
        });
        
        // Search when Enter key is pressed
        searchInput.addEventListener('keyup', (e) => {
            if (e.key === 'Enter') {
                performSearch(searchInput.value);
            }
        });
    }
});

// Function to perform search
async function performSearch(query) {
    if (!query || query.trim() === '') {
        document.getElementById('search-results').innerHTML = 
            '<p>Please enter a search term.</p>';
        return;
    }
    
    const resultsContainer = document.getElementById('search-results');
    resultsContainer.innerHTML = '<p class="loading">Searching...</p>';
    
    try {
        const results = await apiRequest(`/search?q=${encodeURIComponent(query)}`);
        
        if (results.items && results.items.length > 0) {
            let html = `<p>Found ${results.total_count} results for "${query}":</p>`;
            html += '<div class="search-results-list">';
            
            results.items.forEach(item => {
                html += `
                    <div class="search-result-item">
                        <h4>${item.name}</h4>
                        <p>ID: ${item.id}</p>
                    </div>
                `;
            });
            
            html += '</div>';
            resultsContainer.innerHTML = html;
        } else {
            resultsContainer.innerHTML = `<p class="no-results">No results found for "${query}".</p>`;
        }
    } catch (error) {
        resultsContainer.innerHTML = `<p class="error">Error performing search: ${error.message}</p>`;
    }
}
