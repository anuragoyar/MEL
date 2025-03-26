/**
 * Modal Component JavaScript
 * Handles functionality for custom modal dialogs
 */

class Modal {
    constructor(options = {}) {
        this.id = options.id || 'modal-' + Date.now();
        this.title = options.title || 'Confirmation';
        this.content = options.content || '';
        this.confirmText = options.confirmText || 'Confirm';
        this.cancelText = options.cancelText || 'Cancel';
        this.confirmClass = options.confirmClass || 'button-primary';
        this.cancelClass = options.cancelClass || 'button-secondary';
        this.onConfirm = options.onConfirm || function() {};
        this.onCancel = options.onCancel || function() {};
        this.onClose = options.onClose || function() {};
        this.backdrop = null;
        this.element = null;
        this.confirmButton = null;
        this.cancelButton = null;
        
        // Bind methods
        this.open = this.open.bind(this);
        this.close = this.close.bind(this);
        this.confirm = this.confirm.bind(this);
        this.cancel = this.cancel.bind(this);
        this.handleKeyDown = this.handleKeyDown.bind(this);
        
        // Create modal element
        this.create();
    }
    
    /**
     * Create the modal DOM element
     */
    create() {
        // Create backdrop
        this.backdrop = document.createElement('div');
        this.backdrop.className = 'modal-backdrop';
        this.backdrop.id = this.id + '-backdrop';
        
        // Create modal
        this.element = document.createElement('div');
        this.element.className = 'modal';
        this.element.setAttribute('role', 'dialog');
        this.element.setAttribute('aria-labelledby', this.id + '-title');
        this.element.setAttribute('aria-modal', 'true');
        
        // Create modal header
        const header = document.createElement('div');
        header.className = 'modal-header';
        
        const title = document.createElement('h3');
        title.className = 'modal-title';
        title.id = this.id + '-title';
        title.textContent = this.title;
        
        header.appendChild(title);
        
        // Create modal body
        const body = document.createElement('div');
        body.className = 'modal-body';
        
        if (typeof this.content === 'string') {
            body.innerHTML = this.content;
        } else if (this.content instanceof Node) {
            body.appendChild(this.content);
        }
        
        // Create modal footer
        const footer = document.createElement('div');
        footer.className = 'modal-footer';
        
        this.cancelButton = document.createElement('button');
        this.cancelButton.type = 'button';
        this.cancelButton.className = this.cancelClass;
        this.cancelButton.textContent = this.cancelText;
        this.cancelButton.addEventListener('click', this.cancel);
        
        this.confirmButton = document.createElement('button');
        this.confirmButton.type = 'button';
        this.confirmButton.className = this.confirmClass;
        this.confirmButton.textContent = this.confirmText;
        this.confirmButton.addEventListener('click', this.confirm);
        
        footer.appendChild(this.cancelButton);
        footer.appendChild(this.confirmButton);
        
        // Assemble modal
        this.element.appendChild(header);
        this.element.appendChild(body);
        this.element.appendChild(footer);
        
        // Add modal to backdrop
        this.backdrop.appendChild(this.element);
        
        // Add backdrop click handler
        this.backdrop.addEventListener('click', (e) => {
            if (e.target === this.backdrop) {
                this.cancel();
            }
        });
    }
    
    /**
     * Open the modal
     */
    open() {
        // Append to body
        document.body.appendChild(this.backdrop);
        
        // Force reflow
        this.backdrop.offsetWidth;
        
        // Add active class
        this.backdrop.classList.add('active');
        
        // Focus the cancel button by default
        this.cancelButton.focus();
        
        // Add key event listener
        document.addEventListener('keydown', this.handleKeyDown);
    }
    
    /**
     * Close the modal
     */
    close() {
        // Remove active class
        this.backdrop.classList.remove('active');
        
        // Remove modal after animation
        setTimeout(() => {
            if (this.backdrop.parentNode) {
                this.backdrop.parentNode.removeChild(this.backdrop);
            }
        }, 300);
        
        // Remove key event listener
        document.removeEventListener('keydown', this.handleKeyDown);
        
        // Call onClose callback
        this.onClose();
    }
    
    /**
     * Handle confirm button click
     */
    confirm() {
        this.onConfirm();
        this.close();
    }
    
    /**
     * Handle cancel button click
     */
    cancel() {
        this.onCancel();
        this.close();
    }
    
    /**
     * Handle keyboard events
     * @param {KeyboardEvent} e - The keyboard event
     */
    handleKeyDown(e) {
        // Close on escape key
        if (e.key === 'Escape') {
            this.cancel();
        }
        
        // Confirm on enter key
        if (e.key === 'Enter') {
            this.confirm();
        }
        
        // Trap focus within modal
        if (e.key === 'Tab') {
            const focusableElements = this.element.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])');
            const firstElement = focusableElements[0];
            const lastElement = focusableElements[focusableElements.length - 1];
            
            if (e.shiftKey && document.activeElement === firstElement) {
                e.preventDefault();
                lastElement.focus();
            } else if (!e.shiftKey && document.activeElement === lastElement) {
                e.preventDefault();
                firstElement.focus();
            }
        }
    }
} 