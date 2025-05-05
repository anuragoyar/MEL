/**
 * Logout Confirmation Dialog
 * Handles the confirmation dialog before logging out
 */

document.addEventListener('DOMContentLoaded', function() {
    // Find all logout forms
    const logoutForms = document.querySelectorAll('form[action*="logout"]');
    
    logoutForms.forEach(form => {
        form.addEventListener('submit', function(event) {
            event.preventDefault();
            
            // Create and show the confirmation dialog
            const confirmDialog = document.createElement('div');
            confirmDialog.className = 'logout-dialog-overlay';
            confirmDialog.innerHTML = `
                <div class="logout-dialog">
                    <h3>Confirm Logout</h3>
                    <p>Are you sure you want to logout?</p>
                    <div class="logout-dialog-buttons">
                        <button type="button" class="btn btn-outline" id="cancel-logout">Cancel</button>
                        <button type="button" class="btn btn-primary" id="confirm-logout">Yes, Logout</button>
                    </div>
                </div>
            `;
            
            document.body.appendChild(confirmDialog);
            
            // Handle dialog buttons
            document.getElementById('cancel-logout').addEventListener('click', function() {
                confirmDialog.remove();
            });
            
            document.getElementById('confirm-logout').addEventListener('click', function() {
                form.submit();
            });
            
            // Close dialog when clicking outside
            confirmDialog.addEventListener('click', function(e) {
                if (e.target === confirmDialog) {
                    confirmDialog.remove();
                }
            });
            
            // Handle escape key
            document.addEventListener('keydown', function(e) {
                if (e.key === 'Escape' && document.body.contains(confirmDialog)) {
                    confirmDialog.remove();
                }
            });
        });
    });
}); 