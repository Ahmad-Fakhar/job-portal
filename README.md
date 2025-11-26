# Job Portal Management System

A comprehensive Django-based job portal management system with three user roles: Admin, Company, and Job Seeker.

## Features

### For Job Seekers
- User registration and profile management
- Browse and search jobs with advanced filters
- Apply for jobs with resume upload and cover letter
- Save/bookmark favorite jobs
- Track application status
- View job details with company information

### For Companies
- Company registration (pending admin approval)
- Company profile management
- Post and manage job listings
- View and manage job applications
- Update application status (Applied → Under Review → Shortlisted → Interview Scheduled → Accepted/Rejected)
- Dashboard with statistics

### For Admins
- Approve/reject company registrations
- Manage all users, companies, and jobs
- View detailed statistics and analytics
- Moderate job postings

## Technology Stack

- **Backend**: Django 4.2.7
- **Frontend**: Bootstrap 5, Font Awesome, Custom CSS
- **Database**: SQLite (Development) / PostgreSQL (Production via Supabase)
- **Forms**: Django Crispy Forms with Bootstrap 5
- **Authentication**: Custom user model with role-based access control

## Installation

### Prerequisites
- Python 3.8+
- pip
- Virtual environment

### Setup Steps

1. **Navigate to project directory**
   ```bash
   cd "F:\Mini Projects\Tayyab\Job-Portal-Management-System"
   ```

2. **Activate virtual environment**
   ```bash
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create admin user**
   ```bash
   python manage.py create_admin
   ```
   Default credentials: `admin` / `admin123`

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Project Structure

```
Job-Portal-Management-System/
├── accounts/          # User authentication and job seeker profiles
├── companies/         # Company management and job postings
├── jobs/              # Job listings and applications
├── admin_panel/       # Admin dashboard and management
├── notifications/     # System notifications
├── job_portal/        # Main project settings
├── templates/         # HTML templates
├── static/            # CSS, JavaScript, images
│   ├── css/
│   ├── js/
│   └── images/
└── media/             # User uploaded files
```

## User Roles & Permissions

### Job Seeker
- Can register and create profile
- Can browse and search jobs
- Can apply to jobs
- Can save jobs
- Can view application status

### Company
- Can register company (pending approval)
- Can edit company profile
- Can post jobs (after approval)
- Can manage applications
- Can view dashboard statistics

### Admin
- Can approve/reject companies
- Can manage all users
- Can delete/activate jobs
- Can view analytics

## Database Models

### User (Custom)
- UUID primary key
- User types: admin, company, jobseeker
- Profile information

### JobSeeker
- One-to-one with User
- Resume upload
- Skills, education, experience

### Company
- One-to-one with User
- Status: pending, approved, rejected
- Company details and logo

### Job
- Foreign key to Company
- Job details, salary, location
- Active/published status
- View count

### Application
- Foreign key to Job and User
- Status tracking
- Resume and cover letter
- One application per user per job

## Key Features Implementation

### Role-Based Access Control
Custom decorators ensure proper access:
- `@admin_required`
- `@company_required`
- `@company_approved_required`
- `@jobseeker_required`
- `@profile_complete_required`

### Job Search & Filtering
- Keyword search across title, description, company
- Location filtering
- Job type, category, experience filters
- Sort by date, title
- Pagination (20 jobs per page)

### Application Status Workflow
1. Applied → 2. Under Review → 3. Shortlisted → 4. Interview Scheduled → 5. Accepted/Rejected

### Notifications System
- Company approval/rejection
- New application alerts
- Application status updates

## Recent Improvements

### UI/UX Enhancements
- ✅ Modern, responsive design with Bootstrap 5
- ✅ Custom CSS with smooth animations
- ✅ Mobile-friendly layout
- ✅ Professional color scheme and typography
- ✅ Interactive job cards with hover effects
- ✅ Improved forms with better styling

### Bug Fixes
- ✅ Fixed company profile template field references
- ✅ Fixed application status badge colors
- ✅ Improved template structure

### Frontend Features
- ✅ AJAX for job saving
- ✅ Auto-hiding alerts
- ✅ Image preview for uploads
- ✅ Character counters for forms
- ✅ Loading states for buttons
- ✅ Smooth scrolling

## Usage Examples

### Register as Job Seeker
1. Click "Register" on homepage
2. Fill in username, email, password
3. Complete profile with resume
4. Start applying for jobs

### Register as Company
1. Click "For Employers"
2. Fill in company details
3. Wait for admin approval
4. After approval, post jobs

### Apply for Job
1. Browse jobs or search
2. Click "View Details"
3. Click "Apply Now"
4. Upload resume and write cover letter
5. Submit application

## Development Commands

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run tests
python manage.py test

# Collect static files
python manage.py collectstatic
```

## Configuration

### Database
By default, the project uses SQLite. For PostgreSQL:
1. Set `USE_POSTGRES=True` in environment variables
2. Configure database credentials in `.env`

### Environment Variables
Create a `.env` file with:
```
SECRET_KEY=your-secret-key
DEBUG=True
USE_POSTGRES=False
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=your-host
```

## Security Features

- CSRF protection
- SQL injection prevention
- XSS protection
- Secure password validation
- File upload validation
- Role-based access control

## Contributing

This is a private project. For any issues or improvements, please contact the repository owner.

## License

This project is proprietary and confidential.

## Contact

For support or questions, please refer to the project documentation or contact the development team.
