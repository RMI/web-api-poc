// Initialize organizations functionality when the DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    // Add event listener to the refresh button
    const refreshButton = document.getElementById('refresh-organizations');
    if (refreshButton) {
        refreshButton.addEventListener('click', loadOrganizations);
    }

    // Load organizations when navigating to the section
    document.getElementById('nav-organizations').addEventListener('click', loadOrganizations);
});

// Function to load organizations from the API
async function loadOrganizations() {
    const organizationsContainer = document.getElementById('organizations-container');
    organizationsContainer.innerHTML = '<p class="loading">Loading organizations...</p>';
    
    try {
        const organizations = await apiRequest('/organizations');
        
        if (organizations && organizations.length > 0) {
            let html = '<table class="data-table">';
            html += `
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Logo</th>
                        <th>Created</th>
                        <th>Updated</th>
                    </tr>
                </thead>
                <tbody>
            `;
            
            organizations.forEach(org => {
                const logoHtml = org.logo_url ? 
                    `<img src="${org.logo_url}" alt="Logo" style="max-height: 30px;">` : 
                    'N/A';
                
                html += `
                    <tr data-id="${org.id}">
                        <td>${org.id}</td>
                        <td>${org.name}</td>
                        <td>${logoHtml}</td>
                        <td>${formatDate(org.created_on)}</td>
                        <td>${formatDate(org.updated_on)}</td>
                    </tr>
                `;
            });
            
            html += '</tbody></table>';
            organizationsContainer.innerHTML = html;
            
            // Add event listener for row clicks
            document.querySelectorAll('#organizations-container tr[data-id]').forEach(row => {
                row.addEventListener('click', () => {
                    const orgId = row.getAttribute('data-id');
                    loadOrganizationDetails(orgId);
                });
            });
        } else {
            organizationsContainer.innerHTML = '<p class="no-results">No organizations found.</p>';
        }
    } catch (error) {
        organizationsContainer.innerHTML = `<p class="error">Error loading organizations: ${error.message}</p>`;
    }
}

// Function to load details for a specific organization
async function loadOrganizationDetails(id) {
    try {
        const organization = await apiRequest(`/organizations/${id}`);
        
        // Create modal or details view with the organization data
        alert(`Organization details for ID ${id}:\n\n${JSON.stringify(organization, null, 2)}`);
        
    } catch (error) {
        alert(`Error loading organization details: ${error.message}`);
    }
}
