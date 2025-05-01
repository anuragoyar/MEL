/**
 * Logout Confirmation JavaScript
 * Implements the logout confirmation modal functionality
 */

document.addEventListener('DOMContentLoaded', function() {
    // Find all logout forms
    const logoutForms = document.querySelectorAll('form[action*="logout"]');
    
    // Add event listener to each logout form
    logoutForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            // Prevent the default form submission
            e.preventDefault();
            
            // Create and open the confirmation modal
            const logoutModal = new Modal({
                title: 'Logout Confirmation',
                content: '<p>Are you sure you want to log out?</p>',
                confirmText: 'Yes, Logout',
                cancelText: 'Cancel',
                confirmClass: 'button-primary',
                cancelClass: 'button-secondary',
                onConfirm: () => {
                    // Submit the form when confirmed
                    form.submit();
                },
                onCancel: () => {
                    console.log('Logout cancelled');
                }
            });
            
            // Open the modal
            logoutModal.open();
        });
    });
}); 