// Initialize scenarios functionality when the DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    // Add event listener to the refresh button
    const refreshButton = document.getElementById('refresh-scenarios');
    if (refreshButton) {
        refreshButton.addEventListener('click', loadScenarios);
    }

    // Load scenarios when navigating to the section
    document.getElementById('nav-scenarios').addEventListener('click', loadScenarios);
});

// Function to load scenarios from the API
async function loadScenarios() {
    const scenariosContainer = document.getElementById('scenarios-container');
    scenariosContainer.innerHTML = '<p class="loading">Loading scenarios...</p>';
    
    try {
        const scenarios = await apiRequest('/scenarios');
        
        if (scenarios && scenarios.length > 0) {
            let html = '<table class="data-table">';
            html += `
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Description</th>
                        <th>Time Horizon</th>
                        <th>Source</th>
                        <th>Organization</th>
                        <th>Created</th>
                    </tr>
                </thead>
                <tbody>
            `;
            
            scenarios.forEach(scenario => {
                html += `
                    <tr data-id="${scenario.id}">
                        <td>${scenario.id}</td>
                        <td>${scenario.name}</td>
                        <td>${scenario.description || 'N/A'}</td>
                        <td>${scenario.time_horizon || 'N/A'}</td>
                        <td>${scenario.source || 'N/A'}</td>
                        <td>${scenario.organization_id || 'N/A'}</td>
                        <td>${formatDate(scenario.created_on)}</td>
                    </tr>
                `;
            });
            
            html += '</tbody></table>';
            scenariosContainer.innerHTML = html;
            
            // Add event listener for row clicks
            document.querySelectorAll('#scenarios-container tr[data-id]').forEach(row => {
                row.addEventListener('click', () => {
                    const scenarioId = row.getAttribute('data-id');
                    loadScenarioDetails(scenarioId);
                });
            });
        } else {
            scenariosContainer.innerHTML = '<p class="no-results">No scenarios found.</p>';
        }
    } catch (error) {
        scenariosContainer.innerHTML = `<p class="error">Error loading scenarios: ${error.message}</p>`;
    }
}

// Function to load details for a specific scenario
async function loadScenarioDetails(id) {
    try {
        const scenario = await apiRequest(`/scenarios/${id}`);
        
        // Create modal or details view with the scenario data
        alert(`Scenario details for ID ${id}:\n\n${JSON.stringify(scenario, null, 2)}`);
        
    } catch (error) {
        alert(`Error loading scenario details: ${error.message}`);
    }
}
