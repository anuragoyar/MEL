# Manual Test Cases for Logout Functionality (MEL-004)

## Test Case 1: Successful Logout
**Description:** Verify that a user can successfully log out of the system.

**Steps:**
1. Login to the system with valid credentials
2. Navigate to the dashboard
3. Click the "Logout" button in the header
4. Observe the redirection and any messages

**Expected Results:**
- User should be redirected to the login page
- A success message should appear indicating successful logout
- The session should be cleared
- Attempting to go back to the dashboard should redirect to login page

## Test Case 2: CSRF Protection
**Description:** Verify that the logout functionality is protected against CSRF attacks.

**Steps:**
1. Login to the system
2. Using browser developer tools, inspect the logout form
3. Verify the presence of CSRF token in the form
4. Try to submit the form after removing the CSRF token

**Expected Results:**
- The logout form should contain a CSRF token
- Attempting to submit the form without the CSRF token should fail
- An error message should be displayed

## Test Case 3: Browser Back Button After Logout
**Description:** Verify that using the browser's back button after logout doesn't expose sensitive information.

**Steps:**
1. Login to the system
2. Navigate to different pages in the dashboard
3. Logout
4. Use the browser's back button multiple times

**Expected Results:**
- User should not be able to access protected pages
- Each attempt should redirect to the login page
- No sensitive information should be displayed

## Test Case 4: Multiple Browser Tabs
**Description:** Verify that logging out affects all open tabs of the application.

**Steps:**
1. Login to the system
2. Open the dashboard in multiple browser tabs
3. Perform logout in one tab
4. Try to perform actions in other tabs

**Expected Results:**
- After logout, attempting any action in other tabs should redirect to login
- No unauthorized access should be possible in any tab

## Test Case 5: Logout Button UI
**Description:** Verify that the logout button is properly styled and accessible.

**Steps:**
1. Login to the system
2. Navigate to the dashboard
3. Inspect the logout button in different screen sizes
4. Test keyboard navigation to the logout button

**Expected Results:**
- Logout button should be clearly visible in the header
- Button should be properly styled with an icon
- Button should be accessible via keyboard navigation
- Button should be responsive and visible on mobile devices

## Test Case 6: Session Timeout
**Description:** Verify that after logout, any stored session data is properly cleared.

**Steps:**
1. Login to the system
2. Perform some actions that store session data
3. Logout
4. Login again

**Expected Results:**
- After logging back in, no data from the previous session should persist
- A fresh session should be created
- No cached sensitive information should be accessible 