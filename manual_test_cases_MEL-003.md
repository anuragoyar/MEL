# Manual Test Cases for Dashboard Implementation (MEL-003)

## Test Case 1: Dashboard Access After Login
**Description:** Verify that the dashboard is accessible after successful login.

**Steps:**
1. Navigate to the login page (root URL: `/`).
2. Enter valid credentials (email and password).
3. Click the "Login" button.
4. Observe the redirection.

**Expected Results:**
- User should be redirected to the dashboard page (`/dashboard/`).
- Dashboard should load without errors.
- User's name or email should be displayed in the welcome message.

## Test Case 2: Dashboard Access Without Login
**Description:** Verify that the dashboard is not accessible without authentication.

**Steps:**
1. Open a new browser session (or clear cookies).
2. Try to access the dashboard directly by navigating to `/dashboard/`.

**Expected Results:**
- User should be redirected to the login page.
- An appropriate message should indicate that authentication is required.

## Test Case 3: Dashboard UI Elements
**Description:** Verify that all UI elements are properly displayed on the dashboard.

**Steps:**
1. Login with valid credentials.
2. Navigate to the dashboard.
3. Inspect the header, sidebar, main content, and footer.

**Expected Results:**
- Header should display the logo and user information.
- Sidebar should display navigation menu items with icons.
- Main content should display widgets (Summary, Notifications, Recent Activity).
- Footer should be visible at the bottom of the page.

## Test Case 4: Static Asset Loading
**Description:** Verify that all static assets (CSS, JavaScript, and FontAwesome icons) load correctly.

**Steps:**
1. Login with valid credentials.
2. Navigate to the dashboard.
3. Open browser developer tools (F12).
4. Go to the Network tab.
5. Refresh the page.

**Expected Results:**
- All CSS files should load without errors (main.css, dashboard.css).
- All JavaScript files should load without errors (main.js, dashboard.js).
- FontAwesome icons should be visible in the navigation menu and widget headers.
- No 404 errors should be present for static assets.

## Test Case 5: Responsive Design
**Description:** Verify that the dashboard is responsive and adapts to different screen sizes.

**Steps:**
1. Login with valid credentials.
2. Navigate to the dashboard.
3. Use browser developer tools to simulate different device sizes:
   - Desktop (1920x1080)
   - Tablet (768x1024)
   - Mobile (375x667)

**Expected Results:**
- On desktop: Full layout with sidebar visible.
- On tablet: Layout should adjust, possibly with a collapsed sidebar.
- On mobile: Layout should be optimized for small screens, with stacked elements.
- All content should be readable and accessible on all device sizes.

## Test Case 6: Browser Compatibility
**Description:** Verify that the dashboard works correctly on different browsers.

**Steps:**
1. Login with valid credentials.
2. Navigate to the dashboard.
3. Test on the following browsers:
   - Chrome (latest version)
   - Firefox (latest version)
   - Safari (latest version)
   - Edge (latest version)

**Expected Results:**
- Dashboard should display correctly on all tested browsers.
- All functionality should work as expected on all tested browsers.
- No visual glitches or layout issues should be present.

## Test Case 7: Session Management
**Description:** Verify that the dashboard session is maintained correctly.

**Steps:**
1. Login with valid credentials.
2. Navigate to the dashboard.
3. Leave the page idle for 5 minutes.
4. Interact with the dashboard again.

**Expected Results:**
- User should remain logged in.
- Dashboard should still be accessible without requiring re-authentication.
- No session timeout errors should occur (unless session timeout is configured for less than 5 minutes). 