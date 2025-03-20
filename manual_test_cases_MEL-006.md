# Manual Test Cases for Profile Page (MEL-006)

## Test Case 1: Profile Navigation
**Description**: Verify that clicking the profile button navigates to the profile page  
**Prerequisites**: User is logged in and on the dashboard page  
**Steps**:
1. Click on the profile button in the sidebar
2. Observe the URL change and page navigation

**Expected Results**:
- URL should change to `/profile/`
- Profile page should load with user information
- Sidebar should show "Profile" as active

## Test Case 2: Profile Information Display
**Description**: Verify that all user information is displayed correctly  
**Prerequisites**: User is logged in and on the profile page  
**Steps**:
1. Observe the profile card section
2. Check the full name display
3. Check the email address display
4. Check the date joined display

**Expected Results**:
- Full name should be displayed (or "Not provided" if not set)
- Email address should match the logged-in user's email
- Date joined should be in the format "Month DD, YYYY"
- All information should be correctly formatted and styled

## Test Case 3: Authentication Check
**Description**: Verify that the profile page is only accessible to authenticated users  
**Prerequisites**: User is not logged in  
**Steps**:
1. Try to access the profile page directly via URL (/profile/)
2. Observe the system response

**Expected Results**:
- User should be redirected to the login page
- After successful login, user should be redirected back to the profile page

## Test Case 4: Profile Page Layout and Responsiveness
**Description**: Verify that the profile page layout is correct and responsive  
**Prerequisites**: User is logged in and on the profile page  
**Steps**:
1. View the page on a desktop browser
2. Resize the browser window to tablet size
3. Resize the browser window to mobile size
4. Check all elements' visibility and alignment

**Expected Results**:
- All elements should be properly aligned and spaced
- Profile card should be centered and properly formatted
- Sidebar should collapse/adjust based on screen size
- Text should be readable at all screen sizes
- No horizontal scrolling should be required

## Test Case 5: Navigation Links
**Description**: Verify that all navigation links on the profile page work correctly  
**Prerequisites**: User is logged in and on the profile page  
**Steps**:
1. Click the Dashboard link in the header
2. Return to profile page
3. Click the Logout button
4. Try to access profile page after logout

**Expected Results**:
- Dashboard link should navigate to dashboard page
- Logout button should successfully log out the user
- After logout, attempting to access profile should redirect to login page

## Edge Cases

### Test Case 6: Long Text Handling
**Description**: Verify that the page handles long text values appropriately  
**Prerequisites**: User account with very long name/email  
**Steps**:
1. Log in with a test account that has a very long name
2. Navigate to the profile page
3. Observe how long text is displayed

**Expected Results**:
- Long text should be properly truncated or wrapped
- Page layout should not break
- All information should remain readable

### Test Case 7: Special Characters
**Description**: Verify that the page handles special characters correctly  
**Prerequisites**: User account with special characters in name  
**Steps**:
1. Log in with a test account that has special characters in the name
2. Navigate to the profile page
3. Observe how special characters are displayed

**Expected Results**:
- Special characters should be displayed correctly
- No encoding issues should be visible
- Page layout should remain intact 