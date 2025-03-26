# Manual Test Cases - KAN-2: Logout Confirmation Dialog

## Overview
These test cases validate the implementation of a custom confirmation dialog that appears when a user attempts to log out. The dialog should provide options to confirm or cancel the logout process.

## Test Environment
- **Browser(s)**: Chrome, Firefox, Safari, Edge
- **Screen Size(s)**: Desktop, Tablet, Mobile
- **Operating System(s)**: Windows, macOS, iOS, Android

## Prerequisites
- A valid user account
- User is logged in and on the dashboard page

## Test Cases

### TC-1: Basic Logout Modal Display
**Description**: Verify that the confirmation modal appears when clicking the logout button.

**Steps**:
1. Navigate to the dashboard
2. Click the "Logout" button
3. Observe the modal dialog

**Expected Result**:
- A modal dialog appears in the center of the screen
- The background is dimmed (overlay effect)
- The modal contains a header with "Logout Confirmation" title
- The modal contains a message "Are you sure you want to log out?"
- The modal contains two buttons: "Yes, Logout" and "Cancel"
- Modal appears with a smooth animation

### TC-2: Modal Cancellation
**Description**: Verify that canceling the logout modal keeps the user on the current page.

**Steps**:
1. Navigate to the dashboard
2. Click the "Logout" button
3. When the modal appears, click the "Cancel" button

**Expected Result**:
- The modal disappears with a smooth animation
- The user remains on the dashboard page
- All dashboard functionality remains accessible
- No session data is cleared

### TC-3: Logout Confirmation
**Description**: Verify that confirming logout properly logs the user out.

**Steps**:
1. Navigate to the dashboard
2. Click the "Logout" button
3. When the modal appears, click the "Yes, Logout" button

**Expected Result**:
- The modal closes
- The user is logged out
- The user is redirected to the login page
- Attempting to go back in the browser doesn't bypass the logout

### TC-4: Modal Dismissal by Clicking Outside
**Description**: Verify that clicking outside the modal dismisses it (cancel behavior).

**Steps**:
1. Navigate to the dashboard
2. Click the "Logout" button
3. When the modal appears, click anywhere outside the modal (on the backdrop)

**Expected Result**:
- The modal disappears with a smooth animation
- The user remains on the dashboard page
- All dashboard functionality remains accessible
- No session data is cleared

### TC-5: Modal Dismissal by Keyboard (ESC)
**Description**: Verify that pressing the ESC key dismisses the modal (cancel behavior).

**Steps**:
1. Navigate to the dashboard
2. Click the "Logout" button
3. When the modal appears, press the ESC key on the keyboard

**Expected Result**:
- The modal disappears with a smooth animation
- The user remains on the dashboard page
- All dashboard functionality remains accessible
- No session data is cleared

### TC-6: Keyboard Navigation and Accessibility
**Description**: Verify that the modal is accessible via keyboard navigation.

**Steps**:
1. Navigate to the dashboard
2. Press Tab key to navigate to the Logout button
3. Press Enter to click the button
4. When the modal appears, use Tab key to navigate between buttons
5. Use Enter key to activate buttons

**Expected Result**:
- Focus is properly trapped within the modal
- Tab order follows a logical sequence (Cancel button, then Yes Logout button)
- Pressing Enter activates the focused button
- All interactive elements have visible focus indicators

### TC-7: Mobile Responsiveness
**Description**: Verify that the modal is responsive on mobile devices.

**Steps**:
1. Access the dashboard on a mobile device or using responsive mode in browser dev tools
2. Click the "Logout" button
3. Observe the modal display

**Expected Result**:
- Modal is properly centered on the screen
- Modal width adapts to the screen size
- Text and buttons are legible and appropriately sized
- Buttons are large enough for touch interaction
- No horizontal scrolling is required

## Edge Cases

### TC-8: Multiple Logout Attempts
**Description**: Verify proper behavior when clicking logout multiple times quickly.

**Steps**:
1. Navigate to the dashboard
2. Click the "Logout" button multiple times in rapid succession

**Expected Result**:
- Only one modal dialog appears
- No duplicate modals are created
- The modal functions correctly

### TC-9: Session Timeout During Confirmation
**Description**: Verify behavior when session times out while the logout modal is open.

**Steps**:
1. Configure a short session timeout (if possible)
2. Login and wait until just before timeout
3. Click the "Logout" button
4. Let the session timeout while the modal is open
5. Click "Cancel" button

**Expected Result**:
- User is redirected to the login page
- A session timeout message is displayed
- No errors occur 