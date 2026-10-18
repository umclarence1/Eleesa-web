from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

# Create document
doc = Document()

# Add title
title = doc.add_heading('Department Website Development Proposal', 0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

# Add Executive Summary
doc.add_heading('Executive Summary', level=1)
doc.add_paragraph('This document outlines the features, pricing, and implementation timeline for a professional department website similar to the ACSES website model.')

# Section 1: Website Features
doc.add_heading('1. WEBSITE FEATURES', level=1)

doc.add_heading('Core Pages', level=2)
core_pages = [
    'Home Page - Professional landing page with multiple sections',
    'About Section - Department overview and mission',
    'Programs/Services - Showcase of offerings and initiatives',
    'Team Directory - Executives and staff profiles',
    'Gallery - Image portfolio and projects',
    'Events Calendar - Upcoming events and announcements',
    'News/Updates - Latest department news',
    'Contact Page - Contact information and inquiry forms'
]
for page in core_pages:
    doc.add_paragraph(page, style='List Bullet')

doc.add_heading('Technical Features', level=2)
tech_features = [
    'Fully Responsive Design - Optimized for mobile, tablet, and desktop',
    'Professional Animations - Smooth transitions and modern UI',
    'SEO Optimization - Improved search engine visibility',
    'Progressive Web App (PWA) - Works offline',
    'Social Media Integration - Share buttons and social links',
    'Contact Forms - Email notifications for inquiries',
    'Performance Optimization - Fast load times',
    'Security - SSL/HTTPS encryption'
]
for feature in tech_features:
    doc.add_paragraph(feature, style='List Bullet')

# Section 2: Technology Stack
doc.add_heading('2. TECHNOLOGY STACK', level=1)
tech_stack = [
    'Frontend Framework - React 18',
    'Build Tool - Vite',
    'Styling - Tailwind CSS',
    'Routing - React Router',
    'Animations - Framer Motion',
    'Icons - Heroicons, FontAwesome',
    'Analytics - Vercel Analytics',
    'Backend - Node.js + Express.js',
    'Database - PostgreSQL (via Supabase)'
]
for tech in tech_stack:
    doc.add_paragraph(tech, style='List Bullet')

# Section 3: Pricing Breakdown
doc.add_heading('3. PRICING BREAKDOWN', level=1)
doc.add_heading('A. Development/Workmanship Costs', level=2)

# Basic Package
doc.add_heading('Basic Package (Static Content)', level=3)
doc.add_heading('Frontend Development Setup:', level=4)
basic_frontend = [
    'Setup and configuration: GHS 800 - 1,200',
    'Home page design & development: GHS 1,000 - 1,500',
    'Additional pages (4-5 pages): GHS 1,200 - 1,800',
    'Gallery functionality: GHS 600 - 1,000',
    'Contact form setup: GHS 400 - 700'
]
for item in basic_frontend:
    doc.add_paragraph(item, style='List Bullet')
doc.add_paragraph('Frontend Subtotal: GHS 4,000 - 6,200', style='List Bullet')

doc.add_heading('Backend Development Setup:', level=4)
doc.add_paragraph('Not included in Basic Package', style='List Bullet')

doc.add_heading('Database Setup:', level=4)
doc.add_paragraph('Not included in Basic Package', style='List Bullet')

p = doc.add_paragraph()
p.add_run('Basic Package Total: GHS 4,000 - 6,200').bold = True

# Standard Package
doc.add_heading('Standard Package (Recommended)', level=3)

doc.add_heading('Frontend Development Setup:', level=4)
for item in basic_frontend:
    doc.add_paragraph(item, style='List Bullet')
doc.add_paragraph('Frontend Subtotal: GHS 4,000 - 6,200', style='List Bullet')

doc.add_heading('Backend Development Setup:', level=4)
backend_items = [
    'Backend API for content management: GHS 1,200 - 2,000',
    'Admin panel for managing content: GHS 1,200 - 1,600',
    'Email notification system: GHS 400 - 800',
    'Search functionality: GHS 600 - 1,000'
]
for item in backend_items:
    doc.add_paragraph(item, style='List Bullet')
doc.add_paragraph('Backend Subtotal: GHS 3,400 - 5,400', style='List Bullet')

doc.add_heading('Database Setup:', level=4)
doc.add_paragraph('Database setup: GHS 600 - 1,000', style='List Bullet')
doc.add_paragraph('Database Subtotal: GHS 600 - 1,000', style='List Bullet')

p = doc.add_paragraph()
p.add_run('Standard Package Total: GHS 8,000 - 12,600').bold = True

# Hosting Costs
doc.add_heading('B. Hosting & Infrastructure Costs (Annual)', level=2)

table = doc.add_table(rows=9, cols=3)
table.style = 'Light Grid Accent 1'
hdr_cells = table.rows[0].cells
hdr_cells[0].text = 'Service'
hdr_cells[1].text = 'Cost'
hdr_cells[2].text = 'Details'

hosting_data = [
    ('Web Hosting', 'FREE - GHS 864/year', 'Netlify Free or $9-20/month paid; Vercel Free or $20/month'),
    ('Domain Name', 'GHS 120 - 240/year', '.com.gh, .com, .online (~GHS 10-20/month)'),
    ('SSL Certificate', 'FREE', 'Included with all modern hosting'),
    ('Email Hosting', 'GHS 400 - 800/year', 'Optional (Porkbun: ~GHS 36/month per inbox)'),
    ('CDN/Cache', 'FREE', 'Included with Netlify/Vercel'),
    ('Backup Services', 'FREE', 'Automatic with hosting providers'),
    ('Analytics & Monitoring', 'FREE', 'Built into Netlify/Vercel (free tier)'),
    ('Database Hosting', 'FREE - GHS 1,200/year', 'Free tier available (Firebase, Supabase free)')
]

for i, (service, cost, details) in enumerate(hosting_data, 1):
    row_cells = table.rows[i].cells
    row_cells[0].text = service
    row_cells[1].text = cost
    row_cells[2].text = details

# Total Annual
total_row = table.add_row().cells
total_row[0].text = 'Total Annual'
total_row[1].text = 'GHS 520 - 2,140/year'
total_row[2].text = '~GHS 44 - 178/month'

# Section 4: Implementation Timeline
doc.add_heading('4. IMPLEMENTATION TIMELINE', level=1)

timeline_table = doc.add_table(rows=7, cols=3)
timeline_table.style = 'Light Grid Accent 1'
hdr_cells = timeline_table.rows[0].cells
hdr_cells[0].text = 'Phase'
hdr_cells[1].text = 'Duration'
hdr_cells[2].text = 'Deliverables'

timeline_data = [
    ('Planning & Design', '1-2 weeks', 'Wireframes, design mockups, requirements'),
    ('Development', '3-6 weeks', 'Frontend & backend development, testing'),
    ('Content Migration', '1-2 weeks', 'Transfer existing content, setup management'),
    ('Testing & QA', '1 week', 'Bug fixes, performance testing'),
    ('Deployment', '1 week', 'Hosting setup, domain configuration'),
    ('Training', '1-2 days', 'Admin panel training, maintenance guide')
]

for i, (phase, duration, deliverables) in enumerate(timeline_data, 1):
    row_cells = timeline_table.rows[i].cells
    row_cells[0].text = phase
    row_cells[1].text = duration
    row_cells[2].text = deliverables

total_row = timeline_table.add_row().cells
total_row[0].text = 'Total'
total_row[1].text = '8-15 weeks'
total_row[2].text = 'Full project completion'

# Section 5: Project Summary
doc.add_heading('5. PROJECT SUMMARY', level=1)
doc.add_heading('What You Get:', level=2)

benefits = [
    'Professional, modern website',
    'Mobile-responsive design',
    'Content management system',
    'Email inquiries & notifications',
    'Analytics & performance tracking',
    'SSL security',
    'Professional hosting',
    'Search functionality',
    'Admin dashboard'
]
for benefit in benefits:
    doc.add_paragraph(benefit, style='List Bullet')

# Section 6: Payment Terms
doc.add_heading('6. PAYMENT TERMS & CONDITIONS', level=1)
doc.add_heading('Suggested Payment Structure:', level=2)

payment = [
    '30% upfront (project kickoff)',
    '40% at midpoint (after design approval)',
    '30% at completion (after testing & deployment)'
]
for item in payment:
    doc.add_paragraph(item, style='List Bullet')

doc.add_heading('Support After Launch:', level=2)
support = [
    '30 days free support included',
    'Ongoing support packages available monthly',
    'Emergency support available 24/7'
]
for item in support:
    doc.add_paragraph(item, style='List Bullet')

# Section 7: Next Steps
doc.add_heading('7. NEXT STEPS', level=1)
next_steps = [
    'Clarify specific requirements and preferences',
    'Finalize package selection (Basic/Standard)',
    'Customize content and branding',
    'Set up domain and hosting',
    'Begin development phase',
    'Regular progress updates and reviews'
]
for i, step in enumerate(next_steps, 1):
    doc.add_paragraph(step, style='List Number')

# Section 8: Contact
doc.add_heading('CONTACT & QUESTIONS', level=1)
doc.add_paragraph('Feel free to discuss:')
contact_items = [
    'Budget adjustments',
    'Feature modifications',
    'Timeline acceleration/extension',
    'Additional customizations'
]
for item in contact_items:
    doc.add_paragraph(item, style='List Bullet')

# Footer
doc.add_paragraph()
footer_p = doc.add_paragraph('Document prepared for department website proposal')
footer_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
footer_p = doc.add_paragraph('Prepared: May 14, 2026')
footer_p.alignment = WD_ALIGN_PARAGRAPH.CENTER

# Save document
docx_path = r'c:\Users\Clarence\eleesa-website\PROPOSAL_DOCUMENT.docx'
doc.save(docx_path)
print(f"SUCCESS: DOCX created at {docx_path}")
