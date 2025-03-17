/**
 * Dashboard JavaScript
 * Handles interactive functionality for the dashboard
 */

document.addEventListener('DOMContentLoaded', function() {
    console.log('Dashboard loaded');
    
    // Initialize widgets
    initializeWidgets();
    
    // Set up event listeners
    setupEventListeners();
});

/**
 * Initialize dashboard widgets
 */
function initializeWidgets() {
    // This is a placeholder for future widget initialization
    console.log('Widgets initialized');
    
    // Example: Update timestamp
    const timestampElements = document.querySelectorAll('.timestamp');
    timestampElements.forEach(element => {
        const timestamp = element.getAttribute('data-timestamp');
        if (timestamp) {
            const date = new Date(parseInt(timestamp) * 1000);
            element.textContent = formatDate(date);
        }
    });
}

/**
 * Set up event listeners for dashboard elements
 */
function setupEventListeners() {
    // Navigation toggle for mobile
    const navToggle = document.querySelector('.nav-toggle');
    if (navToggle) {
        navToggle.addEventListener('click', function() {
            const sidebar = document.querySelector('.sidebar');
            sidebar.classList.toggle('active');
        });
    }
    
    // Widget refresh buttons
    const refreshButtons = document.querySelectorAll('.widget-refresh');
    refreshButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const widgetId = this.closest('.widget').getAttribute('id');
            refreshWidget(widgetId);
        });
    });
}

/**
 * Refresh a specific widget
 * @param {string} widgetId - The ID of the widget to refresh
 */
function refreshWidget(widgetId) {
    console.log(`Refreshing widget: ${widgetId}`);
    // This is a placeholder for actual widget refresh logic
    
    // Show loading indicator
    const widget = document.getElementById(widgetId);
    if (widget) {
        const content = widget.querySelector('.widget-content');
        if (content) {
            content.innerHTML = '<div class="loading">Loading...</div>';
            
            // Simulate loading delay
            setTimeout(() => {
                content.innerHTML = '<p>Widget refreshed at ' + formatDate(new Date()) + '</p>';
            }, 1000);
        }
    }
}

/**
 * Format a date object to a readable string
 * @param {Date} date - The date to format
 * @returns {string} Formatted date string
 */
function formatDate(date) {
    return date.toLocaleString();
} 