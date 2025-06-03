// API base URL and key from config (with defaults if not set)
const API_BASE_URL = window.APP_CONFIG.API_BASE_URL.startsWith('{{') ? 
  'http://localhost:8000' : window.APP_CONFIG.API_BASE_URL;

const API_KEY = window.APP_CONFIG.API_KEY.startsWith('{{') ? 
  'abc123' : window.APP_CONFIG.API_KEY;

// Main navigation functionality
document.addEventListener('DOMContentLoaded', () => {
    // Navigation handling
    const navLinks = document.querySelectorAll('nav a');
    const sections = document.querySelectorAll('.section');

    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            
            // Remove active class from all links and sections
            navLinks.forEach(l => l.classList.remove('active'));
            sections.forEach(s => s.classList.remove('active'));
            
            // Add active class to clicked link
            link.classList.add('active');
            
            // Show corresponding section
            const targetId = link.id.replace('nav-', '') + '-section';
            document.getElementById(targetId).classList.add('active');
        });
    });

    // Initial data loading for the home page
    checkApiHealth();
    loadTables();
});

// Function to check API health
async function checkApiHealth() {
    const healthStatus = document.getElementById('health-status');
    
    try {
        const response = await fetch(`${API_BASE_URL}/health`, {
            headers: {
                'X-API-Key': API_KEY
            }
        });
        
        if (response.ok) {
            const data = await response.json();
            healthStatus.innerHTML = `<span class="status-indicator healthy">✓ API is healthy: ${data.status}</span>`;
            healthStatus.classList.add('healthy');
        } else {
            healthStatus.innerHTML = `<span class="status-indicator unhealthy">✗ API is unhealthy: ${response.status}</span>`;
            healthStatus.classList.add('unhealthy');
        }
    } catch (error) {
        healthStatus.innerHTML = `<span class="status-indicator unhealthy">✗ Cannot connect to API: ${error.message}</span>`;
        healthStatus.classList.add('unhealthy');
    }
}

// Function to load database tables
async function loadTables() {
    const tablesList = document.getElementById('tables-list');
    
    try {
        const response = await fetch(`${API_BASE_URL}/tables`, {
            headers: {
                'X-API-Key': API_KEY
            }
        });
        
        if (response.ok) {
            const data = await response.json();
            
            if (data.tables && data.tables.length > 0) {
                let html = '<ul class="table-list">';
                data.tables.forEach(table => {
                    html += `<li>${table}</li>`;
                });
                html += '</ul>';
                tablesList.innerHTML = html;
            } else {
                tablesList.innerHTML = '<p>No tables found in the database.</p>';
            }
        } else {
            tablesList.innerHTML = `<p class="error">Error loading tables: ${response.status}</p>`;
        }
    } catch (error) {
        tablesList.innerHTML = `<p class="error">Cannot load tables: ${error.message}</p>`;
    }
}

// Helper function for making API requests
async function apiRequest(endpoint, method = 'GET', body = null) {
    const options = {
        method,
        headers: {
            'X-API-Key': API_KEY,
            'Content-Type': 'application/json'
        }
    };
    
    if (body) {
        options.body = JSON.stringify(body);
    }
    
    try {
        const response = await fetch(`${API_BASE_URL}${endpoint}`, options);
        
        if (!response.ok) {
            throw new Error(`API error: ${response.status}`);
        }
        
        return await response.json();
    } catch (error) {
        console.error('API request failed:', error);
        throw error;
    }
}

// Format a date string for display
function formatDate(dateString) {
    if (!dateString) return 'N/A';
    
    const date = new Date(dateString);
    return date.toLocaleDateString() + ' ' + date.toLocaleTimeString();
}
