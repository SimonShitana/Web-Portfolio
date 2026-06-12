import os
import flet as ft

def main(page: ft.Page):

    # =========================================================
    # PAGE SETTINGS (Optimized for Fixed Header Layout)
    # =========================================================
    page.title = "Simon Shitana - Mechanical Engineering Portfolio"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.spacing = 0
    page.bgcolor = "#fff5eb"
    page.scroll = None

    # =========================================================
    # PREMIUM MECHANICAL ENGINEERING ORANGE PALETTE
    # =========================================================
    PRIMARY_ORANGE = "#c45100"
    ACCENT_ORANGE = "#e8650a"
    DEEP_ORANGE = "#a04000"
    LIGHT_BG = "#fff5eb"
    SECTION_ORANGE = "#ffede0"
    SECTION_DEEP = "#ffe0cc"
    BG_WHITE = "#ffffff"
    TEXT_GREY = "#4a3b2e"
    AVATAR_BG = "#ffede0"
    SUBTEXT_GREY = "#7a6b5e"
    CARD_BG = "#fefaf7"
    BORDER_COLOR = "#f0dcc8"
    
    DARK_CARD_BG = "#a04000"        
    DARK_TEXT_WHITE = "#ffffff"

    def open_certificate_zoom(title: str, image_file: str):
        zoom_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text(title, color=PRIMARY_ORANGE, weight=ft.FontWeight.BOLD),
            content=ft.Container(
                width=900,
                height=620,
                bgcolor=BG_WHITE,
                padding=10,
                border_radius=8,
                content=ft.Image(src=f"/images/{image_file}", fit="contain"),
            ),
            actions=[
                ft.TextButton("Close", on_click=lambda e: close_certificate_zoom(zoom_dialog)),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        page.show_dialog(zoom_dialog)

    def close_certificate_zoom(dialog):
        page.pop_dialog()

    def get_uniform_border(width: int, color: str):
        return ft.Border(
            top=ft.BorderSide(width, color),
            bottom=ft.BorderSide(width, color),
            left=ft.BorderSide(width, color),
            right=ft.BorderSide(width, color),
        )

    def create_section_header(title: str, subtitle: str):
        return ft.Column(
            spacing=8,
            controls=[
                ft.Text(
                    title, 
                    size=28, 
                    weight=ft.FontWeight.BOLD, 
                    color=PRIMARY_ORANGE, 
                    style=ft.TextStyle(letter_spacing=1.2)
                ),
                ft.Text(subtitle, size=15, color=TEXT_GREY),
                ft.Container(height=4, width=60, bgcolor=ACCENT_ORANGE, border_radius=2),
                ft.Container(height=15)
            ]
        )

    def create_skill_chip(label: str, level: float):
        return ft.Container(
            bgcolor=BG_WHITE,
            padding=ft.Padding(16, 12, 16, 12),
            border_radius=8,
            border=get_uniform_border(1, BORDER_COLOR),
            content=ft.Column([
                ft.Row([
                    ft.Text(label, weight=ft.FontWeight.W_600, color=DEEP_ORANGE, size=14),
                    ft.Text(f"{int(level*100)}%", weight=ft.FontWeight.BOLD, color=PRIMARY_ORANGE, size=12)
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Container(height=6),
                ft.Stack([
                    ft.Container(height=4, bgcolor="#f0e0d0", border_radius=2, expand=True),
                    ft.Container(height=4, bgcolor=PRIMARY_ORANGE, border_radius=2, width=120 * level)
                ])
            ])
        )

    def create_info_card(title: str, body: str, icon=ft.Icons.CHECK_CIRCLE):
        return ft.Container(
            bgcolor=BG_WHITE,
            padding=20,
            border_radius=8,
            border=get_uniform_border(1, BORDER_COLOR),
            content=ft.Column(
                spacing=10,
                controls=[
                    ft.Row([
                        ft.Icon(icon, color=PRIMARY_ORANGE, size=24),
                        ft.Text(title, size=16, weight=ft.FontWeight.BOLD, color=DEEP_ORANGE),
                    ]),
                    ft.Text(body, color=TEXT_GREY, size=13),
                ],
            ),
        )

    current_page_key = {"value": "overview"}
    nav_buttons = {}

    def build_page_view(section_control, page_key):
        return ft.Column(
            key=f"page-{page_key}",
            expand=True,
            scroll=ft.ScrollMode.ALWAYS,
            spacing=0,
            controls=[section_control],
        )

    def navigate_to(page_key):
        current_page_key["value"] = page_key
        page_switcher.content = build_page_view(portfolio_pages[page_key], page_key)
        for key, button in nav_buttons.items():
            button.style = ft.ButtonStyle(
                color=BG_WHITE if key == page_key else "#f0c8a8",
                overlay_color="#e8650a",
            )
        page.update()

    # =========================================================
    # SECTION 1: OVERVIEW SECTION
    # =========================================================
    hero_section = ft.Container(
        key="overview",
        bgcolor=LIGHT_BG,
        padding=ft.Padding(60, 80, 60, 80),
        content=ft.ResponsiveRow(
            spacing=50,
            controls=[
                ft.Column(
                    col={"sm": 12, "md": 12},
                    spacing=25,
                    controls=[
                        ft.Container(
                            bgcolor=SECTION_ORANGE,
                            padding=ft.Padding(16, 8, 16, 8),
                            border_radius=30,
                            width=200,
                            content=ft.Text(
                                "✨ ASPIRING MECHANICAL ENGINEER",
                                size=12,
                                weight=ft.FontWeight.W_600,
                                color=ACCENT_ORANGE,
                                text_align=ft.TextAlign.CENTER,
                            ),
                        ),
                        ft.Text(
                            "Driving Innovation in",
                            size=36,
                            weight=ft.FontWeight.W_500,
                            color=TEXT_GREY,
                        ),
                        ft.Text(
                            "Mechanical & Mining Engineering",
                            size=48,
                            weight=ft.FontWeight.BOLD,
                            color=PRIMARY_ORANGE,
                            style=ft.TextStyle(height=1.2, letter_spacing=1),
                        ),
                        ft.Text(
                            "through Technology",
                            size=36,
                            weight=ft.FontWeight.W_500,
                            color=TEXT_GREY,
                        ),
                        ft.Text(
                            "Passionate about leveraging engineering principles and modern technology to solve real-world challenges in mining safety, thermal systems, and sustainable manufacturing.",
                            size=16,
                            color=TEXT_GREY,
                            style=ft.TextStyle(height=1.5),
                        ),
                        ft.Row(
                            spacing=40,
                            controls=[
                                ft.Column(
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                        ft.Text("3+", size=38, weight=ft.FontWeight.BOLD, color=PRIMARY_ORANGE),
                                        ft.Text("Years Academic", size=12, color=SUBTEXT_GREY),
                                    ],
                                ),
                                ft.VerticalDivider(color=BORDER_COLOR),
                                ft.Column(
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                        ft.Text("10+", size=38, weight=ft.FontWeight.BOLD, color=PRIMARY_ORANGE),
                                        ft.Text("Projects", size=12, color=SUBTEXT_GREY),
                                    ],
                                ),
                                ft.VerticalDivider(color=BORDER_COLOR),
                                ft.Column(
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                        ft.Text("6", size=38, weight=ft.FontWeight.BOLD, color=PRIMARY_ORANGE),
                                        ft.Text("Certifications", size=12, color=SUBTEXT_GREY),
                                    ],
                                ),
                            ],
                        ),
                        ft.Row(
                            spacing=15,
                            controls=[
                                ft.ElevatedButton(
                                    "Explore My Work",
                                    icon=ft.Icons.WORK_OUTLINE,
                                    bgcolor=PRIMARY_ORANGE,
                                    color=BG_WHITE,
                                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8), padding=ft.Padding(25, 12, 25, 12)),
                                    on_click=lambda e: navigate_to("projects"),
                                ),
                                ft.OutlinedButton(
                                    "Download CV",
                                    icon=ft.Icons.DOWNLOAD,
                                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8), side=ft.BorderSide(2, PRIMARY_ORANGE), padding=ft.Padding(25, 12, 25, 12)),
                                    url="/CV_2026.pdf.pdf",
                                ),
                            ],
                        ),
                        ft.Row(
                            spacing=20,
                            controls=[
                                ft.Row(spacing=8, controls=[
                                    ft.Icon(ft.Icons.EMAIL, color=ACCENT_ORANGE, size=18),
                                    ft.Text("simonshitana21@gmail.com", size=13, color=TEXT_GREY),
                                ]),
                                ft.Row(spacing=8, controls=[
                                    ft.Icon(ft.Icons.PHONE, color=ACCENT_ORANGE, size=18),
                                    ft.Text("+264 81 768 7816", size=13, color=TEXT_GREY),
                                ]),
                            ],
                        ),
                    ],
                ),
            ],
        ),
    )

    # =========================================================
    # SECTION 2: ABOUT ME SECTION
    # =========================================================
    about_section = ft.Container(
        key="about",
        bgcolor=BG_WHITE,
        padding=ft.Padding(60, 80, 60, 80),
        content=ft.ResponsiveRow(
            spacing=50,
            controls=[
                ft.Column(
                    col={"sm": 12, "md": 5},
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            width=320,
                            height=320,
                            border_radius=160,
                            bgcolor=AVATAR_BG,
                            alignment=ft.Alignment(0, 0),
                            border=get_uniform_border(4, PRIMARY_ORANGE),
                            shadow=ft.BoxShadow(blur_radius=25, color="#d4a07a", spread_radius=3, offset=ft.Offset(0, 10)),
                            content=ft.Image(src="/images/profile.jpg", width=316, height=316, border_radius=158, fit="cover"),
                        ),
                        ft.Container(height=30),
                        ft.ElevatedButton(
                            "🔗 Open LinkedIn",
                            bgcolor=PRIMARY_ORANGE,
                            color=BG_WHITE,
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8), padding=ft.Padding(30, 12, 30, 12)),
                            url="https://www.linkedin.com/in/simon-shitana-a960b730b/",
                        ),
                    ],
                ),
                ft.Column(
                    col={"sm": 12, "md": 7},
                    spacing=20,
                    controls=[
                        ft.Text("About Me", size=32, weight=ft.FontWeight.BOLD, color=PRIMARY_ORANGE),
                        ft.Container(height=4, width=60, bgcolor=ACCENT_ORANGE, border_radius=2),
                        ft.Container(height=10),
                        ft.Text("I began my engineering journey with a strong focus on mechanical systems, thermodynamics, and fluid mechanics. My passion for innovation led me to integrate modern technology into traditional engineering practices.", size=15, color=TEXT_GREY, style=ft.TextStyle(height=1.6)),
                        ft.Text("Through my academic career at UNAM, I've developed expertise in mechanical design, thermal system analysis, and manufacturing processes. I've complemented my engineering education with MATLAB certifications and data analytics skills.", size=15, color=TEXT_GREY, style=ft.TextStyle(height=1.6)),
                        ft.Text("I am particularly passionate about applying engineering principles to solve real-world challenges in mining safety and industrial operations. My work on the Mineshield project demonstrates my commitment to leveraging technology for practical safety solutions.", size=15, color=TEXT_GREY, style=ft.TextStyle(height=1.6)),
                        ft.Text("Currently, I'm fascinated by the intersection of mechanical engineering and data science, exploring how predictive analytics can optimize thermal systems and manufacturing processes.", size=15, color=TEXT_GREY, style=ft.TextStyle(height=1.6)),
                        ft.Divider(color=BORDER_COLOR),
                        ft.Row(spacing=15, controls=[
                            ft.ElevatedButton("Contact Me", icon=ft.Icons.EMAIL, bgcolor=PRIMARY_ORANGE, color=BG_WHITE, on_click=lambda e: navigate_to("contact")),
                            ft.OutlinedButton("View Projects", icon=ft.Icons.FOLDER_OPEN, style=ft.ButtonStyle(side=ft.BorderSide(2, PRIMARY_ORANGE)), on_click=lambda e: navigate_to("projects")),
                        ]),
                    ],
                ),
            ],
        ),
    )

    # 3. Skills Section
    skills_section = ft.Container(
        key="skills",
        bgcolor=SECTION_ORANGE,
        padding=40,
        content=ft.Column([
            create_section_header("CORE MECHANICAL & TECHNICAL MATRIX", "Integrated expertise across thermodynamics, fluid mechanics, and digital engineering solutions."),
            ft.ResponsiveRow([
                ft.Column(col={"sm": 12, "md": 4}, spacing=10, controls=[
                    ft.Text("Thermo-Fluid Systems", weight=ft.FontWeight.BOLD, color=ACCENT_ORANGE, size=16),
                    create_skill_chip("Thermodynamics Analysis", 0.88),
                    create_skill_chip("Fluid Mechanics", 0.85),
                    create_skill_chip("Heat Transfer", 0.82),
                ]),
                ft.Column(col={"sm": 12, "md": 4}, spacing=10, controls=[
                    ft.Text("Mechanical Design & CAD", weight=ft.FontWeight.BOLD, color=ACCENT_ORANGE, size=16),
                    create_skill_chip("SolidWorks/AutoCAD", 0.80),
                    create_skill_chip("FEA Analysis", 0.75),
                    create_skill_chip("MATLAB/Simulink", 0.85),
                ]),
                ft.Column(col={"sm": 12, "md": 4}, spacing=10, controls=[
                    ft.Text("Data & Digital Integration", weight=ft.FontWeight.BOLD, color=ACCENT_ORANGE, size=16),
                    create_skill_chip("Python Engineering Analytics", 0.82),
                    create_skill_chip("CFD Simulation", 0.78),
                    create_skill_chip("Power BI Dashboards", 0.80),
                ]),
            ], spacing=20)
        ])
    )

    # 4. Individual Portfolio Reflection Section
    contribution_section = ft.Container(
        key="contribution",
        bgcolor=LIGHT_BG,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("INDIVIDUAL CONTRIBUTION PORTFOLIO", "Reflection, evidence, lessons learned, challenges, and showcase material."),
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        ft.Container(col={"sm": 12, "md": 6}, content=create_info_card("Semester Project Contribution", "I contributed to the engineering logic, documentation, and portfolio evidence for the Mineshield app, with emphasis on making technical work traceable for the Mechanical, Mining, and Manufacturing engineering modules.", ft.Icons.ENGINEERING)),
                        ft.Container(col={"sm": 12, "md": 6}, content=create_info_card("Evidence of Work", "This portfolio includes MATLAB certificates, implementation notes, code snippets, design/documentation placeholders, GitHub logs, and technical explanations that can be verified during assessment.", ft.Icons.FACT_CHECK)),
                        ft.Container(col={"sm": 12, "md": 6}, content=create_info_card("What I Learned", "I strengthened my ability to translate engineering calculations into software requirements, document individual progress in a large 19-member team, and present mathematical concepts clearly with proper notation.", ft.Icons.LIGHTBULB)),
                        ft.Container(col={"sm": 12, "md": 6}, content=create_info_card("Challenges Addressed", "The main challenge was proving individual contribution inside a 19-member project. I addressed it by organizing weekly logs, GitHub evidence, screenshots, and a concise impact narrative.", ft.Icons.TROUBLESHOOT)),
                    ],
                ),
                ft.Container(
                    bgcolor=LIGHT_BG,
                    padding=20,
                    border_radius=8,
                    border=get_uniform_border(1, BORDER_COLOR),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Column([
                                ft.Text("Individual Contribution Video", size=18, weight=ft.FontWeight.BOLD, color=DEEP_ORANGE),
                                ft.Text("Watch the final showcase recording of my individual contribution to the Mineshield project.", color=TEXT_GREY, size=13),
                            ]),
                            ft.TextButton("Watch Video", icon=ft.Icons.VIDEO_LIBRARY, url="https://drive.google.com/drive/folders/1m2OSdE8WwZKpmWNR-2WS2pAwwpySQRk1?usp=sharing", style=ft.ButtonStyle(color=ACCENT_ORANGE)),
                        ],
                    ),
                ),
            ],
        ),
    )

    # 5. Project Timeline Section
    timeline_section = ft.Container(
        key="timeline",
        bgcolor=LIGHT_BG,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("PROJECT WORKLOAD TIMELINE", "Weekly log of my specific contributions to the semester group project."),
                ft.Container(
                    bgcolor=BG_WHITE,
                    padding=25,
                    border_radius=10,
                    border=get_uniform_border(1, BORDER_COLOR),
                    content=ft.Column(
                        spacing=15,
                        controls=[
                            ft.Text("Week 1-2: Role assignment, initial meetings, project charter", size=16, weight=ft.FontWeight.BOLD, color=ACCENT_ORANGE),
                            ft.Text("Assigned specific engineering roles within the group, participated in kickoff meetings, and contributed to drafting the project charter document for Mineshield.", color=TEXT_GREY),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Text("Week 3-4: SRS coordination, pitch preparation, client communication", size=16, weight=ft.FontWeight.BOLD, color=ACCENT_ORANGE),
                            ft.Text("Coordinated Software Requirements Specification documentation, prepared project pitch materials, and maintained regular client communication channels.", color=TEXT_GREY),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Text("Week 5-6: Daily standups, team coordination, Phase 2 progress tracking", size=16, weight=ft.FontWeight.BOLD, color=ACCENT_ORANGE),
                            ft.Text("Led daily standup meetings, coordinated team activities across modules, and tracked Phase 2 deliverables and milestones.", color=TEXT_GREY),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Text("Week 7-8: Mid-term review, resource allocation", size=16, weight=ft.FontWeight.BOLD, color=ACCENT_ORANGE),
                            ft.Text("Prepared mid-term review documentation, managed resource allocation across team members, and ensured proper distribution of tasks.", color=TEXT_GREY),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Text("Week 9-10: Phase 3 kickoff, final deliverable planning, Q&A preparation", size=16, weight=ft.FontWeight.BOLD, color=ACCENT_ORANGE),
                            ft.Text("Kicked off Phase 3 activities, planned final deliverables, and prepared Q&A responses for the final presentation.", color=TEXT_GREY),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Text("Final Week: Daily standups (Fri/Sat/Sun 9AM), management report, Q&A moderation, final submission sign-off", size=16, weight=ft.FontWeight.BOLD, color=ACCENT_ORANGE),
                            ft.Text("Conducted final daily standup meetings, compiled management report, moderated Q&A sessions, and completed final submission sign-off process.", color=TEXT_GREY),
                        ],
                    ),
                ),
            ],
        ),
    )

    # 6. Projects Section - ALL PROJECTS
    project_section = ft.Container(
        key="projects",
        bgcolor=BG_WHITE,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("MY ENGINEERING PROJECTS", "Showcasing my mechanical, software, and educational work"),
                
                # MINESHIELD APP (Phone format images)
                ft.Container(
                    bgcolor=CARD_BG,
                    padding=25,
                    border_radius=10,
                    border=get_uniform_border(1, BORDER_COLOR),
                    content=ft.Column(
                        spacing=12,
                        controls=[
                            ft.Row([
                                ft.Icon(ft.Icons.SHIELD, color=PRIMARY_ORANGE, size=32),
                                ft.Text("Mineshield Safety App", size=22, weight=ft.FontWeight.BOLD, color=ACCENT_ORANGE),
                                ft.Container(bgcolor=PRIMARY_ORANGE, padding=ft.Padding(8, 4, 8, 4), border_radius=4, content=ft.Text("Main Project", size=10, color=BG_WHITE, weight=ft.FontWeight.BOLD)),
                            ]),
                            ft.Text("Mobile safety monitoring system for hazardous workplaces using smartphone sensors.", size=14, color=TEXT_GREY),
                            ft.Container(bgcolor=LIGHT_BG, padding=12, border_radius=6, content=ft.Column([
                                ft.Text("KEY FEATURES:", size=12, weight=ft.FontWeight.BOLD, color=DEEP_ORANGE),
                                ft.Text("• Fall detection using accelerometer sensors", size=12, font_family="monospace", color=ACCENT_ORANGE),
                                ft.Text("• Excessive noise monitoring via microphone", size=12, font_family="monospace", color=ACCENT_ORANGE),
                                ft.Text("• Last known location tracking (underground GPS alternative)", size=12, font_family="monospace", color=ACCENT_ORANGE),
                                ft.Text("• Real-time cloud dashboards for supervisors", size=12, font_family="monospace", color=ACCENT_ORANGE),
                            ])),
                            ft.Row([
                                ft.Container(content=ft.Text("JavaScript", size=11, color=BG_WHITE), bgcolor=PRIMARY_ORANGE, padding=5, border_radius=4),
                                ft.Container(content=ft.Text("React Native", size=11, color=DEEP_ORANGE), bgcolor=LIGHT_BG, padding=5, border_radius=4),
                                ft.Container(content=ft.Text("Firebase", size=11, color=DEEP_ORANGE), bgcolor=LIGHT_BG, padding=5, border_radius=4),
                            ]),
                            
                            # 3 Image placeholders for Mineshield (Phone format - vertical/portrait)
                            ft.Text("Project Screenshots", size=14, weight=ft.FontWeight.BOLD, color=DEEP_ORANGE),
                            ft.ResponsiveRow(
                                spacing=15,
                                run_spacing=15,
                                controls=[
                                    ft.Container(
                                        col={"sm": 12, "md": 4},
                                        height=400,
                                        bgcolor=BG_WHITE,
                                        border_radius=8,
                                        border=get_uniform_border(1, BORDER_COLOR),
                                        alignment=ft.Alignment(0, 0),
                                        content=ft.Column(
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                            spacing=10,
                                            controls=[
                                                ft.Icon(ft.Icons.PHOTO, color=PRIMARY_ORANGE, size=48),
                                                ft.Text("Mineshield - Screenshot 1", size=12, color=TEXT_GREY),
                                                ft.Text("(Phone Format)", size=10, color=SUBTEXT_GREY),
                                                ft.Container(
                                                    content=ft.Text("Placeholder for app screenshot showing fall detection feature", size=11, color=SUBTEXT_GREY, text_align=ft.TextAlign.CENTER),
                                                    padding=10,
                                                ),
                                            ]
                                        )
                                    ),
                                    ft.Container(
                                        col={"sm": 12, "md": 4},
                                        height=400,
                                        bgcolor=BG_WHITE,
                                        border_radius=8,
                                        border=get_uniform_border(1, BORDER_COLOR),
                                        alignment=ft.Alignment(0, 0),
                                        content=ft.Column(
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                            spacing=10,
                                            controls=[
                                                ft.Icon(ft.Icons.PHOTO, color=PRIMARY_ORANGE, size=48),
                                                ft.Text("Mineshield - Screenshot 2", size=12, color=TEXT_GREY),
                                                ft.Text("(Phone Format)", size=10, color=SUBTEXT_GREY),
                                                ft.Container(
                                                    content=ft.Text("Placeholder for app screenshot showing noise monitoring dashboard", size=11, color=SUBTEXT_GREY, text_align=ft.TextAlign.CENTER),
                                                    padding=10,
                                                ),
                                            ]
                                        )
                                    ),
                                    ft.Container(
                                        col={"sm": 12, "md": 4},
                                        height=400,
                                        bgcolor=BG_WHITE,
                                        border_radius=8,
                                        border=get_uniform_border(1, BORDER_COLOR),
                                        alignment=ft.Alignment(0, 0),
                                        content=ft.Column(
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                            spacing=10,
                                            controls=[
                                                ft.Icon(ft.Icons.PHOTO, color=PRIMARY_ORANGE, size=48),
                                                ft.Text("Mineshield - Screenshot 3", size=12, color=TEXT_GREY),
                                                ft.Text("(Phone Format)", size=10, color=SUBTEXT_GREY),
                                                ft.Container(
                                                    content=ft.Text("Placeholder for app screenshot showing location tracking", size=11, color=SUBTEXT_GREY, text_align=ft.TextAlign.CENTER),
                                                    padding=10,
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
                                ft.Text("Group 16 - Mining Engineering", size=11, color=SUBTEXT_GREY, italic=True),
                                ft.TextButton("View on GitHub", icon=ft.Icons.CODE, url="https://github.com/raunanehale06-png/UNAM-I3691CP-Group-16-Mineshield", style=ft.ButtonStyle(color=ACCENT_ORANGE))
                            ])
                        ],
                    ),
                ),
                
                # MECHANICAL CALCULATOR
                ft.Container(
                    bgcolor=CARD_BG,
                    padding=25,
                    border_radius=10,
                    border=get_uniform_border(1, BORDER_COLOR),
                    content=ft.Column(
                        spacing=12,
                        controls=[
                            ft.Row([
                                ft.Icon(ft.Icons.CALCULATE, color=PRIMARY_ORANGE, size=32),
                                ft.Text("Mechanical Calculator", size=22, weight=ft.FontWeight.BOLD, color=ACCENT_ORANGE),
                            ]),
                            ft.Text("Engineering calculation tool for mechanical design parameters, stress analysis, and material property calculations.", size=14, color=TEXT_GREY),
                            ft.Container(bgcolor=LIGHT_BG, padding=12, border_radius=6, content=ft.Column([
                                ft.Text("CALCULATION FEATURES:", size=12, weight=ft.FontWeight.BOLD, color=DEEP_ORANGE),
                                ft.Text("• Stress and strain calculations (σ = F/A)", size=12, font_family="monospace", color=ACCENT_ORANGE),
                                ft.Text("• Beam deflection analysis", size=12, font_family="monospace", color=ACCENT_ORANGE),
                                ft.Text("• Material property database", size=12, font_family="monospace", color=ACCENT_ORANGE),
                                ft.Text("• Safety factor calculations", size=12, font_family="monospace", color=ACCENT_ORANGE),
                            ])),
                            ft.Row([
                                ft.Container(content=ft.Text("Python", size=11, color=BG_WHITE), bgcolor=PRIMARY_ORANGE, padding=5, border_radius=4),
                                ft.Container(content=ft.Text("NumPy", size=11, color=DEEP_ORANGE), bgcolor=LIGHT_BG, padding=5, border_radius=4),
                                ft.Container(content=ft.Text("MATLAB", size=11, color=DEEP_ORANGE), bgcolor=LIGHT_BG, padding=5, border_radius=4),
                            ]),
                            
                            # 3 Image placeholders for Mechanical Calculator (Square format like MATLAB section)
                            ft.Text("Project Screenshots", size=14, weight=ft.FontWeight.BOLD, color=DEEP_ORANGE),
                            ft.ResponsiveRow(
                                spacing=15,
                                run_spacing=15,
                                controls=[
                                    ft.Container(
                                        col={"sm": 12, "md": 4},
                                        height=200,
                                        bgcolor=BG_WHITE,
                                        border_radius=8,
                                        border=get_uniform_border(1, BORDER_COLOR),
                                        alignment=ft.Alignment(0, 0),
                                        content=ft.Column(
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                            spacing=10,
                                            controls=[
                                                ft.Icon(ft.Icons.IMAGE, color=PRIMARY_ORANGE, size=40),
                                                ft.Text("Calculator - Interface", size=12, color=TEXT_GREY),
                                                ft.Container(
                                                    content=ft.Text("Placeholder for calculator main interface screenshot", size=11, color=SUBTEXT_GREY, text_align=ft.TextAlign.CENTER),
                                                    padding=10,
                                                ),
                                            ]
                                        )
                                    ),
                                    ft.Container(
                                        col={"sm": 12, "md": 4},
                                        height=200,
                                        bgcolor=BG_WHITE,
                                        border_radius=8,
                                        border=get_uniform_border(1, BORDER_COLOR),
                                        alignment=ft.Alignment(0, 0),
                                        content=ft.Column(
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                            spacing=10,
                                            controls=[
                                                ft.Icon(ft.Icons.IMAGE, color=PRIMARY_ORANGE, size=40),
                                                ft.Text("Calculator - Stress Analysis", size=12, color=TEXT_GREY),
                                                ft.Container(
                                                    content=ft.Text("Placeholder for stress calculation output", size=11, color=SUBTEXT_GREY, text_align=ft.TextAlign.CENTER),
                                                    padding=10,
                                                ),
                                            ]
                                        )
                                    ),
                                    ft.Container(
                                        col={"sm": 12, "md": 4},
                                        height=200,
                                        bgcolor=BG_WHITE,
                                        border_radius=8,
                                        border=get_uniform_border(1, BORDER_COLOR),
                                        alignment=ft.Alignment(0, 0),
                                        content=ft.Column(
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                            spacing=10,
                                            controls=[
                                                ft.Icon(ft.Icons.IMAGE, color=PRIMARY_ORANGE, size=40),
                                                ft.Text("Calculator - Results", size=12, color=TEXT_GREY),
                                                ft.Container(
                                                    content=ft.Text("Placeholder for calculation results display", size=11, color=SUBTEXT_GREY, text_align=ft.TextAlign.CENTER),
                                                    padding=10,
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            ft.Divider(color=BORDER_COLOR),
                            ft.TextButton("View on GitHub", icon=ft.Icons.CODE, url="https://github.com/SimonShitana", style=ft.ButtonStyle(color=ACCENT_ORANGE))
                        ],
                    ),
                ),
                
                # EDUCATIONAL WEBSITE
                ft.Container(
                    bgcolor=CARD_BG,
                    padding=25,
                    border_radius=10,
                    border=get_uniform_border(1, BORDER_COLOR),
                    content=ft.Column(
                        spacing=12,
                        controls=[
                            ft.Row([
                                ft.Icon(ft.Icons.SCHOOL, color=PRIMARY_ORANGE, size=32),
                                ft.Text("Educational Website", size=22, weight=ft.FontWeight.BOLD, color=ACCENT_ORANGE),
                            ]),
                            ft.Text("Interactive learning platform for mechanical engineering students featuring tutorials, quizzes, and resource materials.", size=14, color=TEXT_GREY),
                            ft.Container(bgcolor=LIGHT_BG, padding=12, border_radius=6, content=ft.Column([
                                ft.Text("WEBSITE FEATURES:", size=12, weight=ft.FontWeight.BOLD, color=DEEP_ORANGE),
                                ft.Text("• Interactive engineering tutorials", size=12, font_family="monospace", color=ACCENT_ORANGE),
                                ft.Text("• Quiz system with instant feedback", size=12, font_family="monospace", color=ACCENT_ORANGE),
                                ft.Text("• Video lectures and resources", size=12, font_family="monospace", color=ACCENT_ORANGE),
                                ft.Text("• Student progress tracking", size=12, font_family="monospace", color=ACCENT_ORANGE),
                            ])),
                            ft.Row([
                                ft.Container(content=ft.Text("HTML/CSS", size=11, color=BG_WHITE), bgcolor=PRIMARY_ORANGE, padding=5, border_radius=4),
                                ft.Container(content=ft.Text("JavaScript", size=11, color=DEEP_ORANGE), bgcolor=LIGHT_BG, padding=5, border_radius=4),
                                ft.Container(content=ft.Text("React", size=11, color=DEEP_ORANGE), bgcolor=LIGHT_BG, padding=5, border_radius=4),
                            ]),
                            
                            # 3 Image placeholders for Educational Website (Square format like MATLAB section)
                            ft.Text("Project Screenshots", size=14, weight=ft.FontWeight.BOLD, color=DEEP_ORANGE),
                            ft.ResponsiveRow(
                                spacing=15,
                                run_spacing=15,
                                controls=[
                                    ft.Container(
                                        col={"sm": 12, "md": 4},
                                        height=200,
                                        bgcolor=BG_WHITE,
                                        border_radius=8,
                                        border=get_uniform_border(1, BORDER_COLOR),
                                        alignment=ft.Alignment(0, 0),
                                        content=ft.Column(
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                            spacing=10,
                                            controls=[
                                                ft.Icon(ft.Icons.WEB, color=PRIMARY_ORANGE, size=40),
                                                ft.Text("Website - Homepage", size=12, color=TEXT_GREY),
                                                ft.Container(
                                                    content=ft.Text("Placeholder for website homepage screenshot", size=11, color=SUBTEXT_GREY, text_align=ft.TextAlign.CENTER),
                                                    padding=10,
                                                ),
                                            ]
                                        )
                                    ),
                                    ft.Container(
                                        col={"sm": 12, "md": 4},
                                        height=200,
                                        bgcolor=BG_WHITE,
                                        border_radius=8,
                                        border=get_uniform_border(1, BORDER_COLOR),
                                        alignment=ft.Alignment(0, 0),
                                        content=ft.Column(
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                            spacing=10,
                                            controls=[
                                                ft.Icon(ft.Icons.QUIZ, color=PRIMARY_ORANGE, size=40),
                                                ft.Text("Website - Quiz Page", size=12, color=TEXT_GREY),
                                                ft.Container(
                                                    content=ft.Text("Placeholder for interactive quiz interface", size=11, color=SUBTEXT_GREY, text_align=ft.TextAlign.CENTER),
                                                    padding=10,
                                                ),
                                            ]
                                        )
                                    ),
                                    ft.Container(
                                        col={"sm": 12, "md": 4},
                                        height=200,
                                        bgcolor=BG_WHITE,
                                        border_radius=8,
                                        border=get_uniform_border(1, BORDER_COLOR),
                                        alignment=ft.Alignment(0, 0),
                                        content=ft.Column(
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                            spacing=10,
                                            controls=[
                                                ft.Icon(ft.Icons.VIDEO_LIBRARY, color=PRIMARY_ORANGE, size=40),
                                                ft.Text("Website - Resources", size=12, color=TEXT_GREY),
                                                ft.Container(
                                                    content=ft.Text("Placeholder for learning resources page", size=11, color=SUBTEXT_GREY, text_align=ft.TextAlign.CENTER),
                                                    padding=10,
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            ft.Divider(color=BORDER_COLOR),
                            ft.TextButton("View on GitHub", icon=ft.Icons.CODE, url="https://github.com/SimonShitana", style=ft.ButtonStyle(color=ACCENT_ORANGE))
                        ],
                    ),
                ),
                
                # DIGITAL GAME BOARD
                ft.Container(
                    bgcolor=CARD_BG,
                    padding=25,
                    border_radius=10,
                    border=get_uniform_border(1, BORDER_COLOR),
                    content=ft.Column(
                        spacing=12,
                        controls=[
                            ft.Row([
                                ft.Icon(ft.Icons.GAMES, color=PRIMARY_ORANGE, size=32),
                                ft.Text("Digital Game Board", size=22, weight=ft.FontWeight.BOLD, color=ACCENT_ORANGE),
                            ]),
                            ft.Text("Interactive digital board game with multiplayer functionality, real-time updates, and engaging game mechanics.", size=14, color=TEXT_GREY),
                            ft.Container(bgcolor=LIGHT_BG, padding=12, border_radius=6, content=ft.Column([
                                ft.Text("GAME FEATURES:", size=12, weight=ft.FontWeight.BOLD, color=DEEP_ORANGE),
                                ft.Text("• Multiplayer support", size=12, font_family="monospace", color=ACCENT_ORANGE),
                                ft.Text("• Real-time game state updates", size=12, font_family="monospace", color=ACCENT_ORANGE),
                                ft.Text("• Interactive drag-and-drop pieces", size=12, font_family="monospace", color=ACCENT_ORANGE),
                                ft.Text("• Score tracking and leaderboards", size=12, font_family="monospace", color=ACCENT_ORANGE),
                            ])),
                            ft.Row([
                                ft.Container(content=ft.Text("JavaScript", size=11, color=BG_WHITE), bgcolor=PRIMARY_ORANGE, padding=5, border_radius=4),
                                ft.Container(content=ft.Text("Canvas API", size=11, color=DEEP_ORANGE), bgcolor=LIGHT_BG, padding=5, border_radius=4),
                                ft.Container(content=ft.Text("WebSockets", size=11, color=DEEP_ORANGE), bgcolor=LIGHT_BG, padding=5, border_radius=4),
                            ]),
                            
                            # 3 Image placeholders for Digital Game Board (Square format like MATLAB section)
                            ft.Text("Project Screenshots", size=14, weight=ft.FontWeight.BOLD, color=DEEP_ORANGE),
                            ft.ResponsiveRow(
                                spacing=15,
                                run_spacing=15,
                                controls=[
                                    ft.Container(
                                        col={"sm": 12, "md": 4},
                                        height=200,
                                        bgcolor=BG_WHITE,
                                        border_radius=8,
                                        border=get_uniform_border(1, BORDER_COLOR),
                                        alignment=ft.Alignment(0, 0),
                                        content=ft.Column(
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                            spacing=10,
                                            controls=[
                                                ft.Icon(ft.Icons.GAMEPAD, color=PRIMARY_ORANGE, size=40),
                                                ft.Text("Game Board - Main", size=12, color=TEXT_GREY),
                                                ft.Container(
                                                    content=ft.Text("Placeholder for main game board interface", size=11, color=SUBTEXT_GREY, text_align=ft.TextAlign.CENTER),
                                                    padding=10,
                                                ),
                                            ]
                                        )
                                    ),
                                    ft.Container(
                                        col={"sm": 12, "md": 4},
                                        height=200,
                                        bgcolor=BG_WHITE,
                                        border_radius=8,
                                        border=get_uniform_border(1, BORDER_COLOR),
                                        alignment=ft.Alignment(0, 0),
                                        content=ft.Column(
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                            spacing=10,
                                            controls=[
                                                ft.Icon(ft.Icons.PEOPLE, color=PRIMARY_ORANGE, size=40),
                                                ft.Text("Game Board - Multiplayer", size=12, color=TEXT_GREY),
                                                ft.Container(
                                                    content=ft.Text("Placeholder for multiplayer mode screenshot", size=11, color=SUBTEXT_GREY, text_align=ft.TextAlign.CENTER),
                                                    padding=10,
                                                ),
                                            ]
                                        )
                                    ),
                                    ft.Container(
                                        col={"sm": 12, "md": 4},
                                        height=200,
                                        bgcolor=BG_WHITE,
                                        border_radius=8,
                                        border=get_uniform_border(1, BORDER_COLOR),
                                        alignment=ft.Alignment(0, 0),
                                        content=ft.Column(
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                            spacing=10,
                                            controls=[
                                                ft.Icon(ft.Icons.EMOJI_EVENTS, color=PRIMARY_ORANGE, size=40),
                                                ft.Text("Game Board - Scores", size=12, color=TEXT_GREY),
                                                ft.Container(
                                                    content=ft.Text("Placeholder for scores and leaderboard", size=11, color=SUBTEXT_GREY, text_align=ft.TextAlign.CENTER),
                                                    padding=10,
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            ),
                            ft.Divider(color=BORDER_COLOR),
                            ft.TextButton("View on GitHub", icon=ft.Icons.CODE, url="https://github.com/SimonShitana", style=ft.ButtonStyle(color=ACCENT_ORANGE))
                        ],
                    ),
                ),
                
                # Statistics Footer
                ft.Container(
                    bgcolor=SECTION_ORANGE,
                    padding=20,
                    border_radius=10,
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        controls=[
                            ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER, controls=[
                                ft.Text("4+", size=28, weight=ft.FontWeight.BOLD, color=PRIMARY_ORANGE),
                                ft.Text("Major Projects", size=12, color=DEEP_ORANGE),
                            ]),
                            ft.VerticalDivider(color=BORDER_COLOR),
                            ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER, controls=[
                                ft.Text("12", size=28, weight=ft.FontWeight.BOLD, color=PRIMARY_ORANGE),
                                ft.Text("Project Images", size=12, color=DEEP_ORANGE),
                            ]),
                            ft.VerticalDivider(color=BORDER_COLOR),
                            ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER, controls=[
                                ft.Text("19", size=28, weight=ft.FontWeight.BOLD, color=PRIMARY_ORANGE),
                                ft.Text("Team Members", size=12, color=DEEP_ORANGE),
                            ]),
                        ]
                    )
                )
            ],
        ),
    )

    # 7. Technical Blog Section - LESSONS LEARNED
    blog_section = ft.Container(
        key="blog",
        bgcolor=LIGHT_BG,
        padding=40,
        content=ft.Column(
            spacing=25,
            controls=[
                create_section_header("LESSONS LEARNED: MY MINESHIELD JOURNEY", "A 14-week journey in software development, teamwork, and engineering innovation."),
                
                # Introduction Card
                ft.Container(
                    bgcolor=BG_WHITE,
                    padding=25,
                    border_radius=10,
                    border=get_uniform_border(1, BORDER_COLOR),
                    content=ft.Column(
                        spacing=15,
                        controls=[
                            ft.Row([
                                ft.Icon(ft.Icons.SCHOOL, color=PRIMARY_ORANGE, size=40),
                                ft.Text("The Mineshield Experience", size=24, weight=ft.FontWeight.BOLD, color=DEEP_ORANGE),
                            ]),
                            ft.Text(
                                "As the Project Manager for Group 16's Mineshield project, I led a team of 19 engineering students from diverse disciplines to build a mobile safety application for mining environments. This 14-week journey transformed my understanding of software development, team leadership, and engineering problem-solving.",
                                size=15,
                                color=TEXT_GREY,
                                style=ft.TextStyle(height=1.6),
                            ),
                        ],
                    ),
                ),
                
                # Technical Skills Learned
                ft.Container(
                    bgcolor=BG_WHITE,
                    padding=25,
                    border_radius=10,
                    border=get_uniform_border(1, BORDER_COLOR),
                    content=ft.Column(
                        spacing=15,
                        controls=[
                            ft.Row([
                                ft.Icon(ft.Icons.CODE, color=PRIMARY_ORANGE, size=32),
                                ft.Text("Technical Skills Acquired", size=20, weight=ft.FontWeight.BOLD, color=ACCENT_ORANGE),
                            ]),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Text("• React Native & Expo: Learned to build cross-platform mobile apps using JavaScript and React components", size=14, color=TEXT_GREY),
                            ft.Text("• Firebase Integration: Mastered Authentication, Firestore database, Storage, and Cloud Messaging", size=14, color=TEXT_GREY),
                            ft.Text("• Git & GitHub Workflow: Branch management, pull requests, code reviews, and collaboration with 19 members", size=14, color=TEXT_GREY),
                            ft.Text("• Sensor Programming: Implemented accelerometer fall detection and microphone noise monitoring", size=14, color=TEXT_GREY),
                            ft.Text("• Real-time Data Synchronization: Firestore listeners for instant hazard updates", size=14, color=TEXT_GREY),
                        ],
                    ),
                ),
                
                # Project Management Lessons
                ft.Container(
                    bgcolor=BG_WHITE,
                    padding=25,
                    border_radius=10,
                    border=get_uniform_border(1, BORDER_COLOR),
                    content=ft.Column(
                        spacing=15,
                        controls=[
                            ft.Row([
                                ft.Icon(ft.Icons.LEADERBOARD, color=PRIMARY_ORANGE, size=32),
                                ft.Text("Project Management & Leadership", size=20, weight=ft.FontWeight.BOLD, color=ACCENT_ORANGE),
                            ]),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Text("• Daily Stand-ups: Conducted 9 AM meetings (Fri/Sat/Sun) to track progress across 19 members", size=14, color=TEXT_GREY),
                            ft.Text("• Role Distribution: Delegated responsibilities across 6 leads (Firebase, UI/UX, Documentation, GitHub, Lead Dev)", size=14, color=TEXT_GREY),
                            ft.Text("• Timeline Management: Ensured Phase 1-4 deliverables met strict deadlines", size=14, color=TEXT_GREY),
                            ft.Text("• Risk Mitigation: Addressed challenges like GPS limitations underground with last-known-location strategy", size=14, color=TEXT_GREY),
                            ft.Text("• Q&A Moderation: Prepared team for assessor questions on functional requirements and system architecture", size=14, color=TEXT_GREY),
                        ],
                    ),
                ),
                
                # Engineering Challenges Solved
                ft.Container(
                    bgcolor=BG_WHITE,
                    padding=25,
                    border_radius=10,
                    border=get_uniform_border(1, BORDER_COLOR),
                    content=ft.Column(
                        spacing=15,
                        controls=[
                            ft.Row([
                                ft.Icon(ft.Icons.ENGINEERING, color=PRIMARY_ORANGE, size=32),
                                ft.Text("Engineering Challenges & Solutions", size=20, weight=ft.FontWeight.BOLD, color=ACCENT_ORANGE),
                            ]),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Text("• GPS Underground Limitation: Implemented last-known-location tracking stored every 30 seconds before entering mine shaft", size=14, color=TEXT_GREY),
                            ft.Text("• Fall Detection Accuracy: Used 2.5g threshold with 10-reading rolling window achieving 92% accuracy in testing", size=14, color=TEXT_GREY),
                            ft.Text("• Offline Functionality: Added AsyncStorage caching with sync queue for when internet returns", size=14, color=TEXT_GREY),
                            ft.Text("• Real-time Dashboard: Firestore listeners update supervisor dashboard within 2-5 seconds of hazard report", size=14, color=TEXT_GREY),
                            ft.Text("• Safety Score Calculation: Developed formula Safety Score = (Resolved Hazards / Total Hazards) × 100%", size=14, color=TEXT_GREY),
                        ],
                    ),
                ),
                
                # Team Collaboration Insights
                ft.Container(
                    bgcolor=BG_WHITE,
                    padding=25,
                    border_radius=10,
                    border=get_uniform_border(1, BORDER_COLOR),
                    content=ft.Column(
                        spacing=15,
                        controls=[
                            ft.Row([
                                ft.Icon(ft.Icons.GROUP, color=PRIMARY_ORANGE, size=32),
                                ft.Text("Team Collaboration Across Disciplines", size=20, weight=ft.FontWeight.BOLD, color=ACCENT_ORANGE),
                            ]),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Text("• 19 members from Mechanical, Electrical, Mining, Metallurgical, Civil, and Agriculture backgrounds", size=14, color=TEXT_GREY),
                            ft.Text("• Cross-functional communication between Firebase, UI/UX, and development teams", size=14, color=TEXT_GREY),
                            ft.Text("• GitHub PR workflow: feature branches → develop → main with required reviews", size=14, color=TEXT_GREY),
                            ft.Text("• Documentation consistency maintained by Documentation Lead across all phases", size=14, color=TEXT_GREY),
                            ft.Text("• 114 files distributed across 19 members - each received exactly 6 files to complete", size=14, color=TEXT_GREY),
                        ],
                    ),
                ),
                
                # Key Achievements
                ft.Container(
                    bgcolor=SECTION_ORANGE,
                    padding=20,
                    border_radius=10,
                    content=ft.Column(
                        spacing=12,
                        controls=[
                            ft.Text("🏆 Key Achievements as Project Manager", size=18, weight=ft.FontWeight.BOLD, color=DEEP_ORANGE),
                            ft.Text("✓ Successfully delivered Mineshield Phase 3 with all 114 files committed", size=14, color=TEXT_GREY),
                            ft.Text("✓ Coordinated daily stand-ups and ensured all 19 members met their deadlines", size=14, color=TEXT_GREY),
                            ft.Text("✓ Moderated Q&A session, preparing team for 25+ technical questions from assessors", size=14, color=TEXT_GREY),
                            ft.Text("✓ Maintained traceability from SRS functional requirements to implemented code", size=14, color=TEXT_GREY),
                            ft.Text("✓ Built APK via EAS Build and tested on 3 different Android devices", size=14, color=TEXT_GREY),
                        ],
                    ),
                ),
                
                # Personal Reflection
                ft.Container(
                    bgcolor=BG_WHITE,
                    padding=25,
                    border_radius=10,
                    border=get_uniform_border(1, BORDER_COLOR),
                    content=ft.Column(
                        spacing=15,
                        controls=[
                            ft.Row([
                                ft.Icon(ft.Icons.LIGHTBULB, color=PRIMARY_ORANGE, size=32),
                                ft.Text("Personal Reflection", size=20, weight=ft.FontWeight.BOLD, color=ACCENT_ORANGE),
                            ]),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Text(
                                "This project taught me that engineering is fundamentally about solving real problems for real people. Mineshield went from an idea scribbled on paper to a working mobile application that could genuinely improve safety in Namibian mines. I learned that technical skills are important, but communication, patience, and leadership are equally critical when managing diverse teams under tight deadlines. The experience of presenting our work to assessors and defending our technical decisions has prepared me for professional engineering practice.",
                                size=15,
                                color=TEXT_GREY,
                                style=ft.TextStyle(height=1.6),
                            ),
                            ft.Container(height=10),
                            ft.Text(
                                "I am proud of what our team accomplished and grateful for the opportunity to lead Group 16 through this challenging but rewarding journey.",
                                size=15,
                                color=PRIMARY_ORANGE,
                                weight=ft.FontWeight.W_600,
                                style=ft.TextStyle(height=1.6),
                            ),
                        ],
                    ),
                ),
            ],
        ),
    )

    # 8. Experience / Leadership Section
    leadership_section = ft.Container(
        key="experience",
        bgcolor=LIGHT_BG,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("MECHANICAL SOCIETY LEADERSHIP & FIELD EXPERIENCE", "Active contributions to mechanical engineering community and practical industry exposure."),
                ft.Text("Bridging academic mechanical theory with practical industry applications while mentoring aspiring mechanical engineers.", size=15, color=TEXT_GREY),
                ft.ResponsiveRow(
                    spacing=20,
                    controls=[
                        ft.Container(col={"sm": 12, "md": 4}, bgcolor=BG_WHITE, padding=20, border_radius=8, border=get_uniform_border(1, BORDER_COLOR), content=ft.Column([
                            ft.Icon(ft.Icons.GROUP, color=PRIMARY_ORANGE, size=28),
                            ft.Text("Mechanical Engineering Society Chair", size=16, weight=ft.FontWeight.BOLD, color=DEEP_ORANGE),
                            ft.Text("Leading 80+ mechanical engineering students, organizing technical workshops, industry guest lectures, and site visit coordination with local manufacturing operations.", color=TEXT_GREY, size=13),
                        ])),
                        ft.Container(col={"sm": 12, "md": 4}, bgcolor=BG_WHITE, padding=20, border_radius=8, border=get_uniform_border(1, BORDER_COLOR), content=ft.Column([
                            ft.Icon(ft.Icons.CONSTRUCTION, color=PRIMARY_ORANGE, size=28),
                            ft.Text("Intern - Mechanical Design Department", size=16, weight=ft.FontWeight.BOLD, color=DEEP_ORANGE),
                            ft.Text("CAD modeling, thermal system analysis, equipment testing, and assisting senior mechanical engineers with design evaluations.", color=TEXT_GREY, size=13),
                        ])),
                        ft.Container(col={"sm": 12, "md": 4}, bgcolor=BG_WHITE, padding=20, border_radius=8, border=get_uniform_border(1, BORDER_COLOR), content=ft.Column([
                            ft.Icon(ft.Icons.SCHOOL, color=PRIMARY_ORANGE, size=28),
                            ft.Text("Academic Peer Tutoring", size=16, weight=ft.FontWeight.BOLD, color=DEEP_ORANGE),
                            ft.Text("Providing guidance in thermodynamics, fluid mechanics, and mechanical design to undergraduate students, improving pass rates by 25%.", color=TEXT_GREY, size=13),
                        ])),
                    ]
                )
            ]
        )
    )

    # 9. MATLAB Achievement Hub Section
    certificate_data = [
        {"title": "MATLAB Onramp", "file": "MATLAB Onramp.jpg"},
        {"title": "Simulink Fundamentals", "file": "Simulink Oramp.jpg"},
        {"title": "MATLAB Desktop Tools and Troubleshooting Script", "file": "MATLAB Desktop Tools and Troubleshooting Scripts.jpg"},
        {"title": "Make and Manipulate Matrices", "file": "Make and Manipulate Matrices.jpg"},
        {"title": "Calculations with Vectors and Matrices", "file": "Calculations with Vectors and Matrices.jpg"},
        {"title": "Explore Data with MATLAB Plots", "file": "Explore Data with MATLAB Plots.jpg"},
    ]

    cert_cards = []
    for cert in certificate_data:
        if cert["file"]:
            img_control = ft.Image(src=f"/images/{cert['file']}", height=150, fit="contain", scale=1.0, animate_scale=ft.Animation(400, ft.AnimationCurve.EASE_OUT))
        else:
            img_control = ft.Container(height=140, bgcolor=LIGHT_BG, alignment=ft.Alignment(0, 0), content=ft.Column(spacing=6, horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER, controls=[ft.Icon(ft.Icons.UPLOAD_FILE, color=PRIMARY_ORANGE, size=32), ft.Text("Completion proof pending", color=DEEP_ORANGE, size=12, text_align=ft.TextAlign.CENTER)]))

        card_design = ft.Container(
            bgcolor=DARK_CARD_BG, padding=15, border_radius=10, border=get_uniform_border(1, ACCENT_ORANGE),
            on_click=lambda e, title=cert["title"], file=cert["file"]: open_certificate_zoom(title, file) if file else None,
            content=ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER, controls=[
                ft.Container(height=150, width=320, clip_behavior=ft.ClipBehavior.ANTI_ALIAS, border_radius=6, bgcolor=BG_WHITE, alignment=ft.Alignment(0, 0), content=img_control),
                ft.Container(height=6),
                ft.Text(cert["title"], weight=ft.FontWeight.BOLD, color=DARK_TEXT_WHITE, text_align=ft.TextAlign.CENTER, size=13, max_lines=2, overflow=ft.TextOverflow.ELLIPSIS),
                ft.Text("Click to zoom", color="#f0c8a8", size=11, text_align=ft.TextAlign.CENTER),
            ]),
        )

        hover_stack = ft.Stack(height=230, controls=[ft.Container(top=10, left=0, right=0, animate_position=ft.Animation(300, ft.AnimationCurve.EASE_OUT), content=card_design)])

        def make_hover_handler(stack_wrapper, target_img):
            inner_move_container = stack_wrapper.controls[0]
            def handle_hover(e):
                if e.data == "true":
                    inner_move_container.top = 0  
                    inner_move_container.shadow = ft.BoxShadow(blur_radius=12, color=ACCENT_ORANGE)
                    target_img.scale = 1.05  
                else:
                    inner_move_container.top = 10  
                    inner_move_container.shadow = None
                    target_img.scale = 1.0
                inner_move_container.update()
                target_img.update()
            return handle_hover

        if cert["file"]:
            card_design.on_hover = make_hover_handler(hover_stack, img_control)
        cert_cards.append(ft.Container(col={"sm": 12, "md": 4}, content=hover_stack))

    certification_section = ft.Container(
        key="certificates",
        bgcolor=SECTION_DEEP,
        padding=40,
        content=ft.Column(spacing=20, controls=[
            create_section_header("MATLAB ACHIEVEMENT HUB", "Proof of completion for 6 short self-paced courses from the MathWorks Learning Center."),
            ft.Text("Click any certificate to zoom in and inspect the completion proof clearly.", size=13, color=SUBTEXT_GREY),
            ft.ResponsiveRow(spacing=20, run_spacing=10, controls=cert_cards),
        ]),
    )

    # 10. GitHub Evidence & Documentation Section
    github_section = ft.Container(
        key="github",
        bgcolor=LIGHT_BG,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Column([
                            ft.Text("GITHUB EVIDENCE & DOCUMENTATION", size=28, weight=ft.FontWeight.BOLD, color=PRIMARY_ORANGE),
                            ft.Text("Verifiable individual contribution records for a 19-member semester project team.", size=15, color=TEXT_GREY),
                        ]),
                        ft.IconButton(icon=ft.Icons.OPEN_IN_NEW, icon_color=PRIMARY_ORANGE, tooltip="Open GitHub Profile", url="https://github.com/SimonShitana")
                    ]
                ),
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        ft.Container(col={"sm": 12, "md": 4}, content=create_info_card("Commit History", "Screenshots showing commits authored by Simon Shitana in the Mineshield repository, including dates, messages, and linked files.", ft.Icons.COMMIT)),
                        ft.Container(col={"sm": 12, "md": 4}, content=create_info_card("Pull Request Logs", "Documentation of proposed features, reviews performed for team members, comments resolved, and merges completed during the semester project.", ft.Icons.MERGE)),
                        ft.Container(col={"sm": 12, "md": 4}, content=create_info_card("Impact Summary", "My code and documentation improved traceability of calculations and helped explain how engineering module outputs solve Mining and Mechanical engineering problems.", ft.Icons.INSIGHTS)),
                    ],
                ),
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        ft.Container(col={"sm": 12, "md": 6}, bgcolor=BG_WHITE, padding=20, border_radius=10, border=get_uniform_border(1, BORDER_COLOR), content=ft.Column(spacing=12, controls=[
                            ft.Row([ft.Icon(ft.Icons.FOLDER_SPECIAL, color=PRIMARY_ORANGE), ft.Text("Mineshield App", size=16, weight=ft.FontWeight.BOLD, color=DEEP_ORANGE)]),
                            ft.Text("Mobile safety monitoring system with fall detection, noise monitoring, and location tracking for hazardous workplaces.", size=13, color=TEXT_GREY),
                            ft.Row(wrap=True, spacing=5, controls=[
                                ft.Container(content=ft.Text("JavaScript", size=10, color=BG_WHITE), bgcolor=PRIMARY_ORANGE, padding=4, border_radius=4),
                                ft.Container(content=ft.Text("React Native", size=10, color=DEEP_ORANGE), bgcolor=LIGHT_BG, padding=4, border_radius=4),
                                ft.Container(content=ft.Text("Firebase", size=10, color=DEEP_ORANGE), bgcolor=LIGHT_BG, padding=4, border_radius=4),
                            ]),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
                                ft.Text("Active Development", size=11, color=SUBTEXT_GREY),
                                ft.TextButton("View Repository", url="https://github.com/raunanehale06-png/UNAM-I3691CP-Group-16-Mineshield", style=ft.ButtonStyle(color=ACCENT_ORANGE))
                            ])
                        ])),
                        ft.Container(col={"sm": 12, "md": 6}, bgcolor=BG_WHITE, padding=20, border_radius=10, border=get_uniform_border(1, BORDER_COLOR), content=ft.Column(spacing=12, controls=[
                            ft.Row([ft.Icon(ft.Icons.DESCRIPTION, color=PRIMARY_ORANGE), ft.Text("Documentation & Analytics", size=16, weight=ft.FontWeight.BOLD, color=DEEP_ORANGE)]),
                            ft.Text("Engineering calculations, safety metrics, and technical documentation for the Mineshield project.", size=13, color=TEXT_GREY),
                            ft.Row(wrap=True, spacing=5, controls=[
                                ft.Container(content=ft.Text("MATLAB", size=10, color=BG_WHITE), bgcolor=PRIMARY_ORANGE, padding=4, border_radius=4),
                                ft.Container(content=ft.Text("Technical Writing", size=10, color=DEEP_ORANGE), bgcolor=LIGHT_BG, padding=4, border_radius=4),
                            ]),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
                                ft.Text("Phase 3 Complete", size=11, color=SUBTEXT_GREY),
                                ft.TextButton("View Docs", url="https://github.com/raunanehale06-png/UNAM-I3691CP-Group-16-Mineshield/tree/main/docs", style=ft.ButtonStyle(color=ACCENT_ORANGE))
                            ])
                        ])),
                    ],
                ),
            ],
        ),
    )

    # 11. CONTACT SECTION
    name_field = ft.TextField(label="Your Full Name", border_color=PRIMARY_ORANGE, focused_border_color=ACCENT_ORANGE, bgcolor=BG_WHITE, prefix_icon=ft.Icons.PERSON_OUTLINE, filled=True, border_radius=12, text_size=14)
    email_field = ft.TextField(label="Email Address", border_color=PRIMARY_ORANGE, focused_border_color=ACCENT_ORANGE, bgcolor=BG_WHITE, prefix_icon=ft.Icons.EMAIL_OUTLINED, filled=True, border_radius=12, text_size=14)
    subject_field = ft.TextField(label="Subject", border_color=PRIMARY_ORANGE, focused_border_color=ACCENT_ORANGE, bgcolor=BG_WHITE, prefix_icon=ft.Icons.TOPIC, filled=True, border_radius=12, text_size=14)
    message_field = ft.TextField(label="Project Details / Inquiry Message", multiline=True, min_lines=5, max_lines=8, border_color=PRIMARY_ORANGE, focused_border_color=ACCENT_ORANGE, bgcolor=BG_WHITE, prefix_icon=ft.Icons.MESSAGE_OUTLINED, filled=True, border_radius=12, text_size=14)

    def handle_submit_message(e):
        # Just redirect to index.html - no validation, no snackbar
        page.launch_url("/index.html")

    contact_section = ft.Container(
        key="contact",
        bgcolor=LIGHT_BG,
        padding=40,
        content=ft.Column([
            create_section_header("GET IN TOUCH", "Let's collaborate on mechanical engineering projects, research, or career opportunities."),
            ft.ResponsiveRow(spacing=30, run_spacing=30, controls=[
                ft.Column(col={"sm": 12, "md": 5}, spacing=20, controls=[
                    ft.Container(bgcolor=BG_WHITE, padding=25, border_radius=16, shadow=ft.BoxShadow(blur_radius=15, color="#d4a07a", spread_radius=1, offset=ft.Offset(0, 4)), border=ft.Border(left=ft.BorderSide(4, ACCENT_ORANGE)), content=ft.Column(spacing=12, controls=[
                        ft.Row([ft.Container(bgcolor=SECTION_ORANGE, padding=10, border_radius=12, content=ft.Icon(ft.Icons.WORK_OUTLINE, color=PRIMARY_ORANGE, size=28)), ft.Text("Availability", size=20, weight=ft.FontWeight.BOLD, color=DEEP_ORANGE)]),
                        ft.Text("Available for mechanical engineering consultation, thermal system analysis, mechanical design, and research collaborations.", color=TEXT_GREY, size=14),
                        ft.Container(height=5),
                        ft.Container(bgcolor=LIGHT_BG, padding=12, border_radius=10, content=ft.Row([ft.Icon(ft.Icons.CHECK_CIRCLE, color=ACCENT_ORANGE, size=18), ft.Text("Open for internships & graduate positions", color=DEEP_ORANGE, size=13, weight=ft.FontWeight.W_500)])),
                    ])),
                    ft.Container(bgcolor=BG_WHITE, padding=25, border_radius=16, shadow=ft.BoxShadow(blur_radius=15, color="#d4a07a", spread_radius=1, offset=ft.Offset(0, 4)), content=ft.Column(spacing=20, controls=[
                        ft.Text("Contact Information", size=18, weight=ft.FontWeight.BOLD, color=DEEP_ORANGE),
                        ft.Container(on_click=lambda e: page.launch_url("tel:+264817687816"), content=ft.Row([ft.Container(bgcolor=SECTION_ORANGE, padding=8, border_radius=10, content=ft.Icon(ft.Icons.PHONE_ANDROID, color=PRIMARY_ORANGE, size=20)), ft.Column([ft.Text("Phone", size=11, color=SUBTEXT_GREY), ft.Text("+264 81 768 7816", size=15, weight=ft.FontWeight.W_500, color=DEEP_ORANGE)])], spacing=12)),
                        ft.Container(on_click=lambda e: page.launch_url("mailto:simonshitana21@gmail.com"), content=ft.Row([ft.Container(bgcolor=SECTION_ORANGE, padding=8, border_radius=10, content=ft.Icon(ft.Icons.EMAIL, color=PRIMARY_ORANGE, size=20)), ft.Column([ft.Text("Email", size=11, color=SUBTEXT_GREY), ft.Text("simonshitana21@gmail.com", size=14, weight=ft.FontWeight.W_500, color=DEEP_ORANGE)])], spacing=12)),
                        ft.Container(on_click=lambda e: page.launch_url("https://github.com/SimonShitana"), content=ft.Row([ft.Container(bgcolor=SECTION_ORANGE, padding=8, border_radius=10, content=ft.Icon(ft.Icons.CODE, color=PRIMARY_ORANGE, size=20)), ft.Column([ft.Text("GitHub", size=11, color=SUBTEXT_GREY), ft.Text("github.com/SimonShitana", size=13, weight=ft.FontWeight.W_500, color=DEEP_ORANGE)])], spacing=12)),
                        ft.Container(content=ft.Row([ft.Container(bgcolor=SECTION_ORANGE, padding=8, border_radius=10, content=ft.Icon(ft.Icons.LOCATION_ON, color=PRIMARY_ORANGE, size=20)), ft.Column([ft.Text("Location", size=11, color=SUBTEXT_GREY), ft.Text("Ongwediva, Namibia", size=14, weight=ft.FontWeight.W_500, color=DEEP_ORANGE)])], spacing=12)),
                    ])),
                    ft.Container(bgcolor=PRIMARY_ORANGE, padding=20, border_radius=16, shadow=ft.BoxShadow(blur_radius=15, color="#d4a07a", spread_radius=1, offset=ft.Offset(0, 4)), content=ft.Column(spacing=12, controls=[
                        ft.Text("Quick Connect", size=16, weight=ft.FontWeight.BOLD, color=BG_WHITE),
                        ft.Row(spacing=12, controls=[
                            ft.IconButton(icon=ft.Icons.MAIL, icon_color=BG_WHITE, bgcolor="#e8650a", on_click=lambda e: page.launch_url("mailto:simonshitana21@gmail.com"), style=ft.ButtonStyle(shape=ft.CircleBorder())),
                            ft.IconButton(icon=ft.Icons.CODE, icon_color=BG_WHITE, bgcolor="#e8650a", on_click=lambda e: page.launch_url("https://github.com/SimonShitana"), style=ft.ButtonStyle(shape=ft.CircleBorder())),
                            ft.IconButton(icon=ft.Icons.CHAT, icon_color=BG_WHITE, bgcolor="#e8650a", on_click=lambda e: page.launch_url("https://wa.me/264817687816"), style=ft.ButtonStyle(shape=ft.CircleBorder())),
                            ft.IconButton(icon=ft.Icons.INSERT_DRIVE_FILE, icon_color=BG_WHITE, bgcolor="#e8650a", on_click=lambda e: page.launch_url("/CV_2026.pdf.pdf"), style=ft.ButtonStyle(shape=ft.CircleBorder())),
                        ]),
                    ])),
                ]),
                ft.Container(col={"sm": 12, "md": 7}, bgcolor=BG_WHITE, padding=30, border_radius=16, shadow=ft.BoxShadow(blur_radius=15, color="#d4a07a", spread_radius=1, offset=ft.Offset(0, 4)), content=ft.Column(spacing=20, controls=[
                    ft.Row([ft.Icon(ft.Icons.SEND, color=PRIMARY_ORANGE, size=28), ft.Text("Send a Message", size=22, weight=ft.FontWeight.BOLD, color=DEEP_ORANGE)]),
                    ft.Text("I'll get back to you within 24-48 hours", size=13, color=SUBTEXT_GREY),
                    ft.Divider(color=BORDER_COLOR),
                    name_field, email_field, subject_field, message_field,
                    ft.Container(height=5),
                    ft.ElevatedButton("Send Message", icon=ft.Icons.SEND, bgcolor=PRIMARY_ORANGE, color=BG_WHITE, on_click=handle_submit_message, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12), padding=ft.Padding(25, 12, 25, 12)), expand=True),
                ])),
            ]),
        ]),
    )

    portfolio_pages = {
        "overview": hero_section,
        "about": about_section,
        "skills": skills_section,
        "contribution": contribution_section,
        "timeline": timeline_section,
        "projects": project_section,
        "blog": blog_section,
        "experience": leadership_section,
        "certificates": certification_section,
        "github": github_section,
        "contact": contact_section,
    }

    page_switcher = ft.AnimatedSwitcher(
        content=build_page_view(hero_section, "overview"),
        duration=220,
        reverse_duration=160,
        switch_in_curve=ft.AnimationCurve.EASE_OUT,
        switch_out_curve=ft.AnimationCurve.EASE_IN,
        transition=ft.AnimatedSwitcherTransition.FADE,
        expand=True,
    )

    def make_nav_button(label, page_key):
        button = ft.TextButton(label, style=ft.ButtonStyle(color=BG_WHITE if page_key == current_page_key["value"] else "#f0c8a8", overlay_color="#e8650a"), on_click=lambda e, target=page_key: navigate_to(target))
        nav_buttons[page_key] = button
        return button

    header_navbar = ft.Container(
        bgcolor=PRIMARY_ORANGE,
        padding=ft.Padding(40, 15, 40, 15),
        border=ft.Border(bottom=ft.BorderSide(1, ACCENT_ORANGE)),
        shadow=ft.BoxShadow(blur_radius=10, color="#d4a07a", offset=ft.Offset(0, 2)),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Row([ft.Container(width=12, height=12, bgcolor=BG_WHITE, border_radius=6), ft.Text("SIMON SHITANA", weight=ft.FontWeight.BOLD, size=16, color=BG_WHITE, style=ft.TextStyle(letter_spacing=1.1))], spacing=10),
                ft.Row([
                    make_nav_button("Overview", "overview"),
                    make_nav_button("About", "about"),
                    make_nav_button("Skills", "skills"),
                    make_nav_button("Portfolio", "contribution"),
                    make_nav_button("Timeline", "timeline"),
                    make_nav_button("Projects", "projects"),
                    make_nav_button("Blog", "blog"),
                    make_nav_button("Experience", "experience"),
                    make_nav_button("MATLAB Hub", "certificates"),
                    make_nav_button("GitHub", "github"),
                    make_nav_button("Contact", "contact"),
                ], spacing=10, wrap=True)
            ]
        )
    )

    page.add(
        ft.Column(
            expand=True,
            spacing=0,
            controls=[header_navbar, page_switcher]
        )
    )

# =========================================================
# MAIN ENTRY POINT - CORRECTED FOR RENDER DEPLOYMENT
# =========================================================
if __name__ == "__main__":
    ft.app(
        target=main,
        view=ft.AppView.WEB_BROWSER,
        assets_dir="assets",
        port=int(os.environ.get("PORT", 8000))
    )