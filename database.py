# database.py - Comprehensive Multi-Disciplinary Career & Education Catalogue for SkillMap
# Supports diverse educational backgrounds: Arts & Humanities (BA), Commerce (B.Com/BBA), 
# Science (B.Sc), Computer Applications (BCA), and Engineering (B.Tech).

CAREERS_DATABASE = [
    # ----------------------------------------------------
    # ARTS, HUMANITIES & MEDIA PATHWAYS (BA / MA / Mass Comm)
    # ----------------------------------------------------
    {
        "id": "content-strategist",
        "title": "Content Strategist & Copywriter",
        "category": "Media, Arts & Communications",
        "stream": "Arts & Humanities",
        "eligible_degrees": ["BA", "B.Sc", "BBA", "B.Com", "Diploma"],
        "symbol": "✎",
        "level": "Entry to Intermediate",
        "description": "Craft brand narratives, plan multimedia digital publications, and manage communications across global digital channels.",
        "skills": ["Creative Writing", "SEO & Keyword Research", "Brand Storytelling", "Editing & Proofreading", "Social Media Strategy"],
        "education": {
            "diploma": ["Diploma in Creative Writing", "Diploma in Digital Media & PR"],
            "bachelors": ["BA in English / Literature", "BA in Journalism & Mass Communication", "BA in Media Studies", "BBA in Marketing"],
            "masters": ["MA in English / Mass Communication", "Master in Digital Marketing & Media", "MBA in Communications"]
        },
        "roadmap": [
            "Build writing fundamentals and study audience engagement psychology",
            "Learn SEO tools (Semrush, Google Search Console, Ahrefs)",
            "Create a personal portfolio of published articles, case studies, or blog posts",
            "Master content management systems (WordPress, Webflow)",
            "Progress to editorial planning, brand voice direction, and cross-channel strategy"
        ],
        "salary_range": "$52,000 - $88,000 / yr",
        "growth": "High (16% growth in digital media)",
        "prerequisites": "Expressive writing abilities, curiosity, research skills"
    },
    {
        "id": "policy-analyst",
        "title": "Public Policy & Research Analyst",
        "category": "Public Sector, Law & Governance",
        "stream": "Social Sciences & Humanities",
        "eligible_degrees": ["BA", "MA", "B.Sc"],
        "symbol": "⚖",
        "level": "Intermediate",
        "description": "Analyze government policies, conduct qualitative & demographic research, and advise think tanks, NGOs, or public institutions.",
        "skills": ["Qualitative Research", "Policy Evaluation", "Report Writing", "Critical Thinking", "Data Interpretation"],
        "education": {
            "diploma": ["Diploma in Public Administration", "Diploma in Human Rights & Law"],
            "bachelors": ["BA in Political Science", "BA in Economics", "BA in Sociology / Public Administration", "BA in History"],
            "masters": ["Master of Public Policy (MPP)", "MA in International Relations", "MA in Development Studies"]
        },
        "roadmap": [
            "Understand legislative frameworks, constitutional law, and socio-economic systems",
            "Develop qualitative research methodology (interviews, focus groups, surveys)",
            "Learn basic statistical software (SPSS, R, Excel)",
            "Publish policy briefs, white papers, and academic critiques",
            "Advise NGOs, government bodies, or legislative advocacy groups"
        ],
        "salary_range": "$62,000 - $105,000 / yr",
        "growth": "Steady (11% growth)",
        "prerequisites": "Critical thinking, strong research ethics, public affairs interest"
    },
    {
        "id": "hr-specialist",
        "title": "Human Resources (HR) & Talent Specialist",
        "category": "People, Organization & Management",
        "stream": "Humanities, Commerce & Management",
        "eligible_degrees": ["BA", "BBA", "B.Com", "B.Sc"],
        "symbol": "👥",
        "level": "Entry to Intermediate",
        "description": "Spearhead talent acquisition, cultivate workplace culture, oversee employee relations, and design leadership development programs.",
        "skills": ["Talent Sourcing", "Interviewing & Assessment", "Conflict Resolution", "Workplace Psychology", "HR Systems (HRIS)"],
        "education": {
            "diploma": ["Diploma in Human Resource Management (DHRM)"],
            "bachelors": ["BA in Psychology", "BBA in Human Resource Management", "BA in Sociology", "B.Com in General Management"],
            "masters": ["MBA in Human Resources", "MA in Organizational Psychology", "M.Sc in Human Capital Development"]
        },
        "roadmap": [
            "Understand labor laws, compliance, and employee lifecycle management",
            "Learn sourcing on LinkedIn Recruiter and Applicant Tracking Systems (ATS)",
            "Conduct structured interviews and behavioral assessments",
            "Design compensation, benefits, and wellness packages",
            "Drive organizational culture, diversity initiatives, and executive coaching"
        ],
        "salary_range": "$58,000 - $96,000 / yr",
        "growth": "High (12% growth)",
        "prerequisites": "Interpersonal empathy, active listening, organizational skills"
    },

    # ----------------------------------------------------
    # COMMERCE, BUSINESS & FINANCE PATHWAYS (B.Com / BBA / CA / Finance)
    # ----------------------------------------------------
    {
        "id": "financial-analyst",
        "title": "Financial Analyst & Wealth Planner",
        "category": "Banking, Finance & Commerce",
        "stream": "Commerce & Economics",
        "eligible_degrees": ["B.Com", "BBA", "BA", "B.Sc"],
        "symbol": "₹",
        "level": "Entry to Intermediate",
        "description": "Analyze corporate financial statements, build valuation models, assess investment portfolios, and forecast market performance.",
        "skills": ["Financial Modeling", "Corporate Accounting", "Advanced Excel", "Valuation Analysis", "Risk Assessment"],
        "education": {
            "diploma": ["Diploma in Banking & Financial Management", "Diploma in Taxation (DIT)"],
            "bachelors": ["B.Com in Accounting & Finance", "BBA in Finance", "BA in Economics", "B.Sc in Actuarial Science"],
            "masters": ["Master of Finance (M.Fin)", "MBA in Finance", "M.Com in Banking & Financial Markets"]
        },
        "roadmap": [
            "Master balance sheet, P&L statement, and cash flow analysis",
            "Build three-statement DCF (Discounted Cash Flow) financial models in Excel",
            "Study capital markets, asset management, and corporate valuation",
            "Prepare for professional designations (CFA, CFP, or CA/ACCA)",
            "Advise investment banks, equity research firms, or corporate treasury units"
        ],
        "salary_range": "$72,000 - $118,000 / yr",
        "growth": "High (15% growth)",
        "prerequisites": "Quantitative aptitude, attention to detail, economic interest"
    },
    {
        "id": "digital-marketer",
        "title": "Digital Growth & Performance Marketer",
        "category": "Marketing, Sales & Advertising",
        "stream": "Commerce, Media & Arts",
        "eligible_degrees": ["BBA", "BA", "B.Com", "BCA", "Diploma"],
        "symbol": "↗",
        "level": "Entry to Intermediate",
        "description": "Run performance ad campaigns (Google/Meta), optimize sales funnels, and scale customer acquisition for modern businesses.",
        "skills": ["Performance Marketing (Ads)", "Google Analytics 4", "Email Automation", "Conversion Rate Optimization (CRO)", "Copywriting"],
        "education": {
            "diploma": ["Diploma in Digital Marketing & E-Commerce"],
            "bachelors": ["BBA in Digital Marketing", "BA in Mass Media / Advertising", "B.Com in E-Commerce & Marketing"],
            "masters": ["MBA in Marketing Management", "M.Sc in Strategic Marketing"]
        },
        "roadmap": [
            "Learn digital consumer journey fundamentals and paid marketing platforms",
            "Set up tracking pixels, conversion tags, and Google Analytics",
            "Manage paid ad spend on Google Search, YouTube, and Meta",
            "Build email nurture sequences and automated sales funnels",
            "Optimize customer acquisition costs (CAC) and lifetime value (LTV)"
        ],
        "salary_range": "$55,000 - $98,000 / yr",
        "growth": "Very High (19% growth)",
        "prerequisites": "Analytical thinking, creative experimentation, commercial instinct"
    },

    # ----------------------------------------------------
    # DESIGN & CREATIVE PATHWAYS (B.Des / BFA / Multimedia)
    # ----------------------------------------------------
    {
        "id": "ui-ux-designer",
        "title": "UI/UX & Product Designer",
        "category": "Design & User Experience",
        "stream": "Design & Fine Arts",
        "eligible_degrees": ["B.Des", "BA", "BFA", "BCA", "B.Tech", "Diploma"],
        "symbol": "✳",
        "level": "Entry to Intermediate",
        "description": "Design clean, intuitive digital products, mobile apps, and interactive experiences by understanding user needs and behaviors.",
        "skills": ["Figma", "User Research", "Wireframing & Prototyping", "Design Systems", "Usability Testing"],
        "education": {
            "diploma": ["Diploma in UI/UX Design", "Diploma in Graphic Design & Animation"],
            "bachelors": ["B.Des (Bachelor of Design) in Interaction Design", "BA in Fine Arts (BFA)", "BA in Visual Media", "BCA / B.Sc in Multimedia"],
            "masters": ["M.Des in Human-Computer Interaction (HCI)", "Master of Interaction Design"]
        },
        "roadmap": [
            "Learn user experience fundamentals: empathy mapping, personas, user flows",
            "Master Figma for component libraries, auto-layout, and clickable prototypes",
            "Conduct usability testing and iterate based on real feedback",
            "Understand design system tokens, typography scales, and accessibility",
            "Assemble a case-study portfolio showcasing end-to-end design solutions"
        ],
        "salary_range": "$68,000 - $115,000 / yr",
        "growth": "High (16% growth)",
        "prerequisites": "Visual empathy, problem-solving, aesthetic sense"
    },

    # ----------------------------------------------------
    # DATA & COMPUTATIONAL SCIENCES (B.Sc / BCA / B.Tech)
    # ----------------------------------------------------
    {
        "id": "data-analyst",
        "title": "Data Analyst & Business Intelligence Specialist",
        "category": "Data & Analytics",
        "stream": "Mathematics, Statistics & IT",
        "eligible_degrees": ["B.Sc", "B.Com", "BCA", "BBA", "B.Tech"],
        "symbol": "▥",
        "level": "Entry to Intermediate",
        "description": "Transform business records into strategic clarity through SQL database queries, statistical modeling, and interactive dashboards.",
        "skills": ["SQL", "Excel", "Python for Data", "PowerBI / Tableau", "Foundational Statistics"],
        "education": {
            "diploma": ["Diploma in Data Analytics", "Diploma in Business Intelligence"],
            "bachelors": ["B.Sc in Statistics / Mathematics / Economics", "BCA (Bachelor of Computer Applications)", "B.Com in Business Analytics", "B.Tech in Any Branch"],
            "masters": ["M.Sc in Applied Statistics / Data Science", "MBA in Business Analytics", "MCA in Data Analytics"]
        },
        "roadmap": [
            "Master business data manipulation in Excel and relational querying in SQL",
            "Learn Python for data analysis using Pandas and NumPy",
            "Create clear visual dashboards using Tableau or PowerBI",
            "Understand foundational statistics and hypothesis testing",
            "Build real-world exploratory data analysis (EDA) portfolio projects"
        ],
        "salary_range": "$65,000 - $105,000 / yr",
        "growth": "Very High (23% growth)",
        "prerequisites": "Analytical curiosity, numeracy, pattern recognition"
    },

    # ----------------------------------------------------
    # SOFTWARE & COMPUTER SCIENCE PATHWAYS (BCA / B.Tech / B.Sc CS)
    # ----------------------------------------------------
    {
        "id": "python-developer",
        "title": "Python Software Developer",
        "category": "Software & Web Engineering",
        "stream": "Computer Science & Applications",
        "eligible_degrees": ["BCA", "B.Tech", "B.Sc", "Diploma"],
        "symbol": "⌘",
        "level": "Entry to Intermediate",
        "description": "Engineer scalable software systems, automate complex business workflows, and build server-side web APIs using Python.",
        "skills": ["Python", "Flask / Django", "SQL Databases", "Git & GitHub", "REST APIs", "Problem Solving"],
        "education": {
            "diploma": ["Diploma in Computer Engineering", "Diploma in Software Development"],
            "bachelors": ["BCA (Bachelor of Computer Applications)", "B.Tech in Computer Science / IT", "B.Sc in Computer Science / IT"],
            "masters": ["MCA (Master of Computer Applications)", "M.Tech in Computer Science", "M.Sc in Information Technology"]
        },
        "roadmap": [
            "Learn Python fundamentals: data types, loops, functions, and OOP",
            "Master working with databases using SQL and ORMs",
            "Build web backends and REST APIs using Flask or Django",
            "Learn version control with Git and GitHub",
            "Deploy applications to cloud platforms and write unit tests"
        ],
        "salary_range": "$75,000 - $125,000 / yr",
        "growth": "High (22% over next 10 years)",
        "prerequisites": "Logical reasoning, computer science fundamentals"
    },
    {
        "id": "cybersecurity-analyst",
        "title": "Cybersecurity & Network Defender",
        "category": "Information Security & Networks",
        "stream": "Computer Science & IT",
        "eligible_degrees": ["BCA", "B.Tech", "B.Sc", "Diploma"],
        "symbol": "◇",
        "level": "Intermediate",
        "description": "Safeguard enterprise infrastructure, detect cyber threats, inspect security breaches, and defend networks.",
        "skills": ["Computer Networks (TCP/IP)", "Linux Administration", "Python Scripting", "Ethical Hacking", "Security Standards"],
        "education": {
            "diploma": ["Diploma in Cyber Security", "Diploma in Computer Networking & Hardware"],
            "bachelors": ["BCA with Cybersecurity", "B.Tech in Cyber Security / IT", "B.Sc in Cyber Forensics / Computer Science"],
            "masters": ["M.Tech in Information Security", "M.Sc in Cyber Forensics", "MCA with Security Specialization"]
        },
        "roadmap": [
            "Learn computer networking protocols: TCP/IP, DNS, VPNs, and firewalls",
            "Master Linux operating system navigation and command-line tools",
            "Write Python scripts for automated security scanning and log analysis",
            "Study vulnerability assessment, threat intelligence, and penetration testing",
            "Pursue recognized industry certifications (CompTIA Security+, CEH)"
        ],
        "salary_range": "$80,000 - $130,000 / yr",
        "growth": "High (32% growth)",
        "prerequisites": "Understanding of computers, operating systems, and networks"
    },
    {
        "id": "machine-learning-engineer",
        "title": "Machine Learning & AI Engineer",
        "category": "Artificial Intelligence",
        "stream": "Computer Science & Mathematics",
        "eligible_degrees": ["B.Tech", "B.Sc", "BCA", "Masters"],
        "symbol": "✧",
        "level": "Intermediate to Advanced",
        "description": "Develop algorithmic systems and deep neural networks that learn patterns from vast data repositories.",
        "skills": ["Python", "Linear Algebra", "Machine Learning", "TensorFlow/PyTorch", "SQL", "Data Pipelines"],
        "education": {
            "diploma": ["Post-Graduate Diploma in AI & Machine Learning"],
            "bachelors": ["B.Tech in Artificial Intelligence & ML / CSE", "B.Sc in Mathematics / Statistics / Data Science", "BCA with AI Specialization"],
            "masters": ["M.Tech / M.S in AI & Machine Learning", "M.Sc in Data Science", "Ph.D in AI & Machine Learning"]
        },
        "roadmap": [
            "Solidify Python programming and linear algebra/calculus fundamentals",
            "Master classical ML algorithms with Scikit-Learn (regression, clustering, trees)",
            "Explore Deep Learning frameworks such as PyTorch or TensorFlow",
            "Learn data engineering fundamentals and model evaluation techniques",
            "Deploy models as live inference APIs with Docker and cloud servers"
        ],
        "salary_range": "$110,000 - $165,000 / yr",
        "growth": "Extremely High (30%+ growth)",
        "prerequisites": "Strong Python knowledge and mathematical foundations"
    }
]

# Quick filter degrees popular across India & global colleges
# Course & Degree Cards Catalogue
POPULAR_DEGREES = [
    {
        "code": "BCA",
        "name": "Bachelor of Computer Applications",
        "icon": "💻",
        "tagline": "Software, Web Development & IT",
        "stream": "Computer Applications",
        "duration": "3 Years",
        "color": "#b9f56b"
    },
    {
        "code": "B.Tech",
        "name": "Bachelor of Technology / Engineering",
        "icon": "⚙️",
        "tagline": "Computer Science, AI & Engineering",
        "stream": "Engineering",
        "duration": "4 Years",
        "color": "#42f5c5"
    },
    {
        "code": "BA",
        "name": "Bachelor of Arts",
        "icon": "📚",
        "tagline": "Media, Content, Policy, HR & Psychology",
        "stream": "Arts & Humanities",
        "duration": "3 Years",
        "color": "#fcd34d"
    },
    {
        "code": "B.Com",
        "name": "Bachelor of Commerce",
        "icon": "📊",
        "tagline": "Accounting, Finance, Analytics & Banking",
        "stream": "Commerce & Finance",
        "duration": "3 Years",
        "color": "#60a5fa"
    },
    {
        "code": "BBA",
        "name": "Bachelor of Business Administration",
        "icon": "💼",
        "tagline": "Marketing, Business Growth & Operations",
        "stream": "Management & Business",
        "duration": "3 Years",
        "color": "#f472b6"
    },
    {
        "code": "B.Sc",
        "name": "Bachelor of Science",
        "icon": "🔬",
        "tagline": "Statistics, Math, Data Science & Research",
        "stream": "Sciences & Statistics",
        "duration": "3 Years",
        "color": "#34d399"
    },
    {
        "code": "B.Des",
        "name": "Bachelor of Design",
        "icon": "🎨",
        "tagline": "UI/UX, Product Design & Interaction",
        "stream": "Design & Fine Arts",
        "duration": "4 Years",
        "color": "#c084fc"
    },
    {
        "code": "Diploma",
        "name": "Polytechnic & Professional Diploma",
        "icon": "📜",
        "tagline": "Applied Technical & Vocational Diplomas",
        "stream": "Technical & Vocational",
        "duration": "1 - 3 Years",
        "color": "#94a3b8"
    }
]

# Master lists for search & filters
ALL_AVAILABLE_SKILLS = sorted(
    list({skill for career in CAREERS_DATABASE for skill in career["skills"]})
)

ALL_CATEGORIES = sorted(
    list({career["category"] for career in CAREERS_DATABASE})
)

ALL_STREAMS = sorted(
    list({career["stream"] for career in CAREERS_DATABASE})
)
