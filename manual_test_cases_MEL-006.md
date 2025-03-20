# Manual Test Cases for MEL-006: Profile Page Implementation

## Test Case 1: Profile Navigation from Dashboard
**Description**: Verify that users can navigate to the profile page from the dashboard.
**Steps**:
1. Log in to the application
2. Navigate to the dashboard
3. Click on the "Profile" button in the header

**Expected Results**:
- User is redirected to the profile page
- URL should change to /profile/
- Profile page should load without errors

## Test Case 2: Profile Page Content Display
**Description**: Verify that all user information is displayed correctly on the profile page.
**Steps**:
1. Log in to the application
2. Navigate to the profile page
3. Check all displayed user information

**Expected Results**:
- Full Name is displayed (or "Not provided" if not set)
- Email Address is displayed correctly
- Date Joined is displayed in the format "Month DD, YYYY"
- All information matches the user's actual data

## Test Case 3: Profile Page Layout and Styling
**Description**: Verify that the profile page layout and styling are correct.
**Steps**:
1. Log in to the application
2. Navigate to the profile page
3. Check the page layout and styling elements

**Expected Results**:
- Page follows the same layout structure as the dashboard
- Profile card is properly styled with shadow and rounded corners
- Font Awesome icons are displayed correctly
- Responsive design works on different screen sizes

## Test Case 4: Authentication Protection
**Description**: Verify that the profile page is protected from unauthorized access.
**Steps**:
1. Open a new browser window (not logged in)
2. Try to access the profile page directly via URL (/profile/)

**Expected Results**:
- User is redirected to the login page
- After successful login, user is redirected back to the profile page

## Test Case 5: Navigation Back to Dashboard
**Description**: Verify that users can navigate back to the dashboard from the profile page.
**Steps**:
1. Log in to the application
2. Navigate to the profile page
3. Click on the "Dashboard" button in the header

**Expected Results**:
- User is redirected to the dashboard page
- URL should change to /dashboard/
- Dashboard page should load without errors

## Test Case 6: Sidebar Navigation
**Description**: Verify that the sidebar navigation works correctly on the profile page.
**Steps**:
1. Log in to the application
2. Navigate to the profile page
3. Check the sidebar navigation items

**Expected Results**:
- "Profile" item in the sidebar is highlighted as active
- Other navigation items are visible but not highlighted
- Sidebar maintains consistent styling with the dashboard

## Test Case 7: Logout from Profile Page
**Description**: Verify that users can log out from the profile page.
**Steps**:
1. Log in to the application
2. Navigate to the profile page
3. Click the "Logout" button

**Expected Results**:
- User is successfully logged out
- User is redirected to the login page
- Session is terminated

## Edge Cases

### Test Case 8: Missing User Information
**Description**: Verify proper handling of missing user information.
**Steps**:
1. Log in with a user account that has minimal information (e.g., only email)
2. Navigate to the profile page

**Expected Results**:
- Full Name shows "Not provided" when name is not set
- Other fields display available information correctly
- No errors or layout issues due to missing data

### Test Case 9: Long Text Handling
**Description**: Verify proper handling of long text in user information fields.
**Steps**:
1. Log in with a user account that has very long values for name or email
2. Navigate to the profile page

**Expected Results**:
- Long text is properly contained within the layout
- No text overflow issues
- Layout remains consistent and visually appealing 