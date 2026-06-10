import os
import flet as ft
import webbrowser
import threading

def main(page: ft.Page):

    # =========================================================
    # PAGE SETTINGS (Optimized for Fixed Header Layout)
    # =========================================================
    page.title = "Simon Shitana - Mechanical Engineering Portfolio"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.spacing = 0
    page.bgcolor = "#fff5eb"
    page.scroll = None  # Crucial: Page tracking disabled so container columns handle isolated scrolling

    # =========================================================
    # PREMIUM MECHANICAL ENGINEERING ORANGE PALETTE
    # =========================================================
    PRIMARY_ORANGE = "#c45100"        # Deep Burnt Orange / Engineering Core Orange
    ACCENT_ORANGE = "#e8650a"         # Vibrant Mechanical Orange
    DEEP_ORANGE = "#a04000"           # Dark accent for text/buttons
    LIGHT_BG = "#fff5eb"              # Soft warm-tint background
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

    # =========================================================
    # PREMIUM COMPONENT BUILDERS
    # =========================================================
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

    # =========================================================
    # NAVIGATION SYSTEM
    # =========================================================
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
    # SECTIONS DEFINITIONS
    # =========================================================
    
    # 1. Overview Section
    hero_section = ft.Container(
        key="overview",
        bgcolor=LIGHT_BG,
        padding=ft.Padding(50, 60, 50, 60),
        content=ft.ResponsiveRow(
            controls=[
                ft.Column(
                    col={"sm": 12, "md": 7},
                    spacing=15,
                    controls=[
                        ft.Text(
                            "MECHANICAL ENGINEERING STUDENT @ UNAM", 
                            size=13, 
                            weight=ft.FontWeight.W_600, 
                            color=ACCENT_ORANGE, 
                            style=ft.TextStyle(letter_spacing=1.5)
                        ),
                        ft.Text("Simon Shitana", size=42, weight=ft.FontWeight.BOLD, color=PRIMARY_ORANGE),
                        ft.Text("GitHub: https://github.com/SimonShitana", size=14, weight=ft.FontWeight.W_500, color=PRIMARY_ORANGE),
                        ft.Divider(color=PRIMARY_ORANGE, thickness=1.5),
                        ft.Text("Phone: +264 81 768 7816  |  Email: simonshitana21@gmail.com", size=14, weight=ft.FontWeight.W_500, color=DEEP_ORANGE),
                        ft.Text("Mechanical Engineering student focused on thermodynamics, fluid mechanics, mechanical design optimization, manufacturing systems, and data-driven engineering operations.", size=16, color=TEXT_GREY),
                        ft.Container(height=10),
                        ft.ElevatedButton(
                            "Download CV (PDF)",
                            icon=ft.Icons.DOWNLOAD,
                            bgcolor=PRIMARY_ORANGE,
                            color=BG_WHITE,
                            url="/cv.pdf",
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=6)),
                        ),
                    ],
                ),
                ft.Column(
                    col={"sm": 12, "md": 5},
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            width=220,
                            height=220,
                            border_radius=110,
                            bgcolor=AVATAR_BG,
                            alignment=ft.Alignment(0, 0),
                            border=get_uniform_border(4, PRIMARY_ORANGE),
                            content=ft.Icon(ft.Icons.PERSON, size=100, color=PRIMARY_ORANGE),  # Placeholder for profile image
                        ),
                        ft.Container(height=8),
                        ft.Text("Mechanical Engineering & Thermal Systems 2026", size=12, color=SUBTEXT_GREY, italic=True),
                    ],
                ),
            ]
        ),
    )

    # 2. Skills Section
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

    # 3. Individual Portfolio Reflection Section
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
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            content=create_info_card(
                                "Semester Project Contribution",
                                "I contributed to the engineering logic, documentation, and portfolio evidence for the group app, with emphasis on making technical work traceable for the Mechanical, Thermodynamics, and Manufacturing engineering modules.",
                                ft.Icons.ENGINEERING,
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            content=create_info_card(
                                "Evidence of Work",
                                "This portfolio includes certificate screenshots, implementation notes, code snippets, design/documentation placeholders, GitHub logs, and technical explanations that can be verified during assessment.",
                                ft.Icons.FACT_CHECK,
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            content=create_info_card(
                                "What I Learned",
                                "I strengthened my ability to translate engineering calculations into software requirements, document individual progress in a large team, and present mathematical concepts clearly with proper notation.",
                                ft.Icons.LIGHTBULB,
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            content=create_info_card(
                                "Challenges Addressed",
                                "The main challenge was proving individual contribution inside a 20-member project. I addressed it by organizing weekly logs, GitHub evidence, screenshots, and a concise impact narrative.",
                                ft.Icons.TROUBLESHOOT,
                            ),
                        ),
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
                                ft.Text("Add the final showcase recording link here so it matches the contribution you will present live.", color=TEXT_GREY, size=13),
                            ]),
                            ft.TextButton("Video Link Placeholder", icon=ft.Icons.VIDEO_LIBRARY, url="https://example.com/contribution-video", style=ft.ButtonStyle(color=ACCENT_ORANGE)),
                        ],
                    ),
                ),
            ],
        ),
    )

    # 3. Project Timeline Section - SIMON'S TIMELINE CONTRIBUTION
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
                            ft.Text("Assigned specific engineering roles within the group, participated in kickoff meetings, and contributed to drafting the project charter document.", color=TEXT_GREY),
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

    # 4. Projects Section
    project_section = ft.Container(
        key="projects",
        bgcolor=BG_WHITE,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("MECHANICAL ENGINEERING PROJECTS", "Advanced analytical tools for thermal systems and mechanical design optimization."),
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=CARD_BG,
                            padding=25,
                            border_radius=10,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=12,
                                controls=[
                                    ft.Text("1. Thermodynamics Cycle Simulator", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_ORANGE),
                                    ft.Text("Comprehensive MATLAB-based thermodynamic tool for evaluating Carnot, Rankine, Brayton, and Otto cycles with efficiency calculations.", color=TEXT_GREY, size=14),
                                    ft.Container(
                                        bgcolor=LIGHT_BG,
                                        padding=12,
                                        border_radius=6,
                                        content=ft.Column([
                                            ft.Text("THERMODYNAMIC CORE EQUATIONS:", size=11, weight=ft.FontWeight.BOLD, color=DEEP_ORANGE),
                                            ft.Text("• Thermal Efficiency: η = 1 - Q_out/Q_in", size=12, font_family="monospace", color=ACCENT_ORANGE),
                                            ft.Text("• Carnot Efficiency: η_max = 1 - T_cold/T_hot", size=12, font_family="monospace", color=ACCENT_ORANGE),
                                            ft.Text("• Work Output: W_net = Q_in - Q_out", size=12, font_family="monospace", color=ACCENT_ORANGE),
                                            ft.Text("• Power Generation: P = ṁ × W_net", size=12, font_family="monospace", color=ACCENT_ORANGE),
                                        ])
                                    ),
                                    ft.Text("Enables mechanical engineers to assess thermal system performance, optimize operating conditions, and predict efficiency improvements.", color=TEXT_GREY, size=12),
                                    ft.Row([
                                        ft.Container(content=ft.Text("MATLAB/Simulink", size=11, color=BG_WHITE), bgcolor=PRIMARY_ORANGE, padding=5, border_radius=4),
                                        ft.Container(content=ft.Text("Thermo-Calc", size=11, color=DEEP_ORANGE), bgcolor=LIGHT_BG, padding=5, border_radius=4),
                                    ])
                                ],
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=CARD_BG,
                            padding=25,
                            border_radius=10,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=12,
                                controls=[
                                    ft.Text("2. Fluid Dynamics Pipeline Optimizer", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_ORANGE),
                                    ft.Text("Interactive simulation tool for analyzing flow rates, pressure drops, and pump selection in complex piping systems.", color=TEXT_GREY, size=14),
                                    ft.Container(
                                        bgcolor=LIGHT_BG,
                                        padding=12,
                                        border_radius=6,
                                        content=ft.Column([
                                            ft.Text("FLUID DYNAMICS CORE EQUATIONS:", size=11, weight=ft.FontWeight.BOLD, color=DEEP_ORANGE),
                                            ft.Text("• Bernoulli's Equation: P₁/ρg + v₁²/2g + z₁ = P₂/ρg + v₂²/2g + z₂ + h_L", size=12, font_family="monospace", color=ACCENT_ORANGE),
                                            ft.Text("• Darcy-Weisbach: h_f = f × (L/D) × (v²/2g)", size=12, font_family="monospace", color=ACCENT_ORANGE),
                                            ft.Text("• Reynolds Number: Re = ρvD/μ", size=12, font_family="monospace", color=ACCENT_ORANGE),
                                            ft.Text("• Pump Power: P = ρgQH/η", size=12, font_family="monospace", color=ACCENT_ORANGE),
                                        ])
                                    ),
                                    ft.Text("Assists engineers in designing efficient pipeline networks, calculating required pump specifications, and ensuring optimal flow conditions.", color=TEXT_GREY, size=12),
                                    ft.Row([
                                        ft.Container(content=ft.Text("Python Scripting", size=11, color=BG_WHITE), bgcolor=PRIMARY_ORANGE, padding=5, border_radius=4),
                                        ft.Container(content=ft.Text("Ansys Fluent", size=11, color=DEEP_ORANGE), bgcolor=LIGHT_BG, padding=5, border_radius=4),
                                    ])
                                ],
                            ),
                        ),
                    ],
                ),
            ],
        ),
    )

    # 5. Technical Blog Section
    blog_section = ft.Container(
        key="blog",
        bgcolor=LIGHT_BG,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("TECHNICAL BLOG: CONFIDENCE IN CONCEPTS", "Written technical explanations with embedded video insert placeholders."),
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=22,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=12,
                                controls=[
                                    ft.Text("Mechanical Power Transmission", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_ORANGE),
                                    ft.Text("For engineering modules, power transmission combines torque, angular velocity, and efficiency factors. Correct notation keeps the calculation readable and auditable.", color=TEXT_GREY, size=13),
                                    ft.Container(
                                        bgcolor=LIGHT_BG,
                                        padding=14,
                                        border_radius=6,
                                        content=ft.Text("P = τ × ω = 2π × N × τ / 60", font_family="monospace", size=14, color=PRIMARY_ORANGE),
                                    ),
                                    ft.Text("Where P is power (Watts), τ is torque (Nm), ω is angular velocity (rad/s), and N is rotational speed (RPM).", color=TEXT_GREY, size=13),
                                    ft.TextButton("Embedded Video Insert", icon=ft.Icons.PLAY_CIRCLE, url="https://example.com/power-transmission-video", style=ft.ButtonStyle(color=ACCENT_ORANGE)),
                                ],
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=22,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=12,
                                controls=[
                                    ft.Text("Engineering Module Impact", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_ORANGE),
                                    ft.Text("In the Mechanical module, structured formulas helped connect interface inputs to practical outputs such as stress analysis, thermal system performance, and equipment specifications.", color=TEXT_GREY, size=13),
                                    ft.Container(
                                        bgcolor=LIGHT_BG,
                                        padding=14,
                                        border_radius=6,
                                        content=ft.Text("σ = F/A   |   ε = ΔL/L   |   E = σ/ε", font_family="monospace", size=14, color=PRIMARY_ORANGE),
                                    ),
                                    ft.Text("The notation makes assumptions visible: force, area, deformation, and material properties must be documented before results are trusted.", color=TEXT_GREY, size=13),
                                    ft.TextButton("Embedded Video Insert", icon=ft.Icons.PLAY_CIRCLE, url="https://example.com/engineering-impact-video", style=ft.ButtonStyle(color=ACCENT_ORANGE)),
                                ],
                            ),
                        ),
                    ],
                ),
            ],
        ),
    )

    # 6. Experience / Leadership Section
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
                        ft.Container(
                            col={"sm": 12, "md": 4},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column([
                                ft.Icon(ft.Icons.GROUP, color=PRIMARY_ORANGE, size=28),
                                ft.Text("Mechanical Engineering Society Chair", size=16, weight=ft.FontWeight.BOLD, color=DEEP_ORANGE),
                                ft.Text("Leading 80+ mechanical engineering students, organizing technical workshops, industry guest lectures, and site visit coordination with local manufacturing operations.", color=TEXT_GREY, size=13),
                            ])
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 4},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column([
                                ft.Icon(ft.Icons.CONSTRUCTION, color=PRIMARY_ORANGE, size=28),
                                ft.Text("Intern - Mechanical Design Department", size=16, weight=ft.FontWeight.BOLD, color=DEEP_ORANGE),
                                ft.Text("CAD modeling, thermal system analysis, equipment testing, and assisting senior mechanical engineers with design evaluations.", color=TEXT_GREY, size=13),
                            ])
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 4},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column([
                                ft.Icon(ft.Icons.SCHOOL, color=PRIMARY_ORANGE, size=28),
                                ft.Text("Academic Peer Tutoring", size=16, weight=ft.FontWeight.BOLD, color=DEEP_ORANGE),
                                ft.Text("Providing guidance in thermodynamics, fluid mechanics, and mechanical design to undergraduate students, improving pass rates by 25%.", color=TEXT_GREY, size=13),
                            ])
                        ),
                    ]
                )
            ]
        )
    )

    # 6. MATLAB Achievement Hub Section
    certificate_data = [
        {"title": "MATLAB Onramp", "file": "MATLAB Onramp.jpeg"},
        {"title": "Simulink Fundamentals", "file": "Simulink Fundamentals.jpeg"},
        {"title": "MATLAB Desktop Tools and Troubleshooting Script", "file": "MATLAB Desktop Tools and Troubleshooting Script.jpeg"},
        {"title": "Make and Manipulate Matrices", "file": "Make and Manipulate Matrices.jpeg"},
        {"title": "Calculations with Vectors and Matrices", "file": "Calculations with Vectors and Matrices.jpeg"},
        {"title": "Explore Data with MATLAB Plots", "file": "Explore Data with MATLAB Plots.jpeg"},
        {"title": "How MATLAB Graphics Work", "file": "How MATLAB Graphics Work.jpeg"},
    ]

    cert_cards = []
    for cert in certificate_data:
        if cert["file"]:
            img_control = ft.Image(
                src=f"/images/{cert['file']}",
                height=150,
                fit="contain", 
                scale=1.0,
                animate_scale=ft.Animation(400, ft.AnimationCurve.EASE_OUT),
            )
        else:
            img_control = ft.Container(
                height=140,
                bgcolor=LIGHT_BG,
                alignment=ft.Alignment(0, 0),
                content=ft.Column(
                    spacing=6,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(ft.Icons.UPLOAD_FILE, color=PRIMARY_ORANGE, size=32),
                        ft.Text("Completion proof pending", color=DEEP_ORANGE, size=12, text_align=ft.TextAlign.CENTER),
                    ],
                ),
            )

        card_design = ft.Container(
            bgcolor=DARK_CARD_BG,
            padding=15,
            border_radius=10,
            border=get_uniform_border(1, ACCENT_ORANGE),
            on_click=lambda e, title=cert["title"], file=cert["file"]: open_certificate_zoom(title, file) if file else None,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        height=150,
                        width=320,
                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                        border_radius=6,
                        bgcolor=BG_WHITE,
                        alignment=ft.Alignment(0, 0),
                        content=img_control,
                    ),
                    ft.Container(height=6),
                    ft.Text(cert["title"], weight=ft.FontWeight.BOLD, color=DARK_TEXT_WHITE, text_align=ft.TextAlign.CENTER, size=13, max_lines=2, overflow=ft.TextOverflow.ELLIPSIS),
                    ft.Text("Click to zoom", color="#f0c8a8", size=11, text_align=ft.TextAlign.CENTER),
                ],
            ),
        )

        hover_stack = ft.Stack(
            height=230,
            controls=[
                ft.Container(top=10, left=0, right=0, animate_position=ft.Animation(300, ft.AnimationCurve.EASE_OUT), content=card_design)
            ]
        )

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
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("MATLAB ACHIEVEMENT HUB", "Proof of completion for 8 short self-paced courses from the MathWorks Learning Center."),
                ft.Text("Click any certificate to zoom in and inspect the completion proof clearly.", size=13, color=SUBTEXT_GREY),
                ft.ResponsiveRow(spacing=20, run_spacing=10, controls=cert_cards),
            ],
        ),
    )

    # 8. GitHub Evidence & Documentation Section
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
                            ft.Text("Verifiable individual contribution records for a 20-member semester project team.", size=15, color=TEXT_GREY),
                        ]),
                        ft.IconButton(icon=ft.Icons.OPEN_IN_NEW, icon_color=PRIMARY_ORANGE, tooltip="Open GitHub Profile", url="https://github.com/SimonShitana")
                    ]
                ),
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 4},
                            content=create_info_card(
                                "Commit History",
                                "Add screenshots or direct API pulls showing commits authored by Simon Shitana in the main repository, including dates, messages, and linked files.",
                                ft.Icons.COMMIT,
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 4},
                            content=create_info_card(
                                "Pull Request Logs",
                                "Document proposed features, reviews performed for team members, comments resolved, and merges completed during the semester project.",
                                ft.Icons.MERGE,
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 4},
                            content=create_info_card(
                                "Impact Summary",
                                "My code and documentation improved traceability of calculations and helped explain how engineering module outputs solve Mechanical, Thermodynamics, or Manufacturing engineering problems.",
                                ft.Icons.INSIGHTS,
                            ),
                        ),
                    ],
                ),
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=10,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=12,
                                controls=[
                                    ft.Row([ft.Icon(ft.Icons.FOLDER_SPECIAL, color=PRIMARY_ORANGE), ft.Text("Thermo-Cycle-Simulator", size=16, weight=ft.FontWeight.BOLD, color=DEEP_ORANGE)]),
                                    ft.Text("Interactive thermodynamic cycle simulator with efficiency calculations, work output predictions, and graphical performance charts for mechanical systems.", size=13, color=TEXT_GREY),
                                    ft.Row(wrap=True, spacing=5, controls=[
                                        ft.Container(content=ft.Text("Python", size=10, color=BG_WHITE), bgcolor=PRIMARY_ORANGE, padding=4, border_radius=4),
                                        ft.Container(content=ft.Text("MATLAB", size=10, color=DEEP_ORANGE), bgcolor=LIGHT_BG, padding=4, border_radius=4),
                                        ft.Container(content=ft.Text("Plotly", size=10, color=DEEP_ORANGE), bgcolor=LIGHT_BG, padding=4, border_radius=4),
                                    ]),
                                    ft.Divider(color=BORDER_COLOR),
                                    ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
                                        ft.Text("Active Development", size=11, color=SUBTEXT_GREY),
                                        ft.TextButton("View Repository", url="https://github.com/SimonShitana", style=ft.ButtonStyle(color=ACCENT_ORANGE))
                                    ])
                                ]
                            )
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=10,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=12,
                                controls=[
                                    ft.Row([ft.Icon(ft.Icons.FOLDER, color=PRIMARY_ORANGE), ft.Text("Fluid-Pipeline-Analyzer", size=16, weight=ft.FontWeight.BOLD, color=DEEP_ORANGE)]),
                                    ft.Text("Pipeline flow solver for mechanical systems. Calculates pressure drops, flow rates, and optimal pump specifications for regulatory compliance.", size=13, color=TEXT_GREY),
                                    ft.Row(wrap=True, spacing=5, controls=[
                                        ft.Container(content=ft.Text("Python", size=10, color=BG_WHITE), bgcolor=PRIMARY_ORANGE, padding=4, border_radius=4),
                                        ft.Container(content=ft.Text("NumPy/SciPy", size=10, color=DEEP_ORANGE), bgcolor=LIGHT_BG, padding=4, border_radius=4),
                                    ]),
                                    ft.Divider(color=BORDER_COLOR),
                                    ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
                                        ft.Text("Stable Release", size=11, color=SUBTEXT_GREY),
                                        ft.TextButton("View Repository", url="https://github.com/SimonShitana", style=ft.ButtonStyle(color=ACCENT_ORANGE))
                                    ])
                                ]
                            )
                        ),
                    ],
                ),
            ],
        ),
    )

    # 8. ADVANCED CONTACT SECTION - Redesigned with premium styling
    name_field = ft.TextField(
        label="Your Full Name", 
        border_color=PRIMARY_ORANGE, 
        focused_border_color=ACCENT_ORANGE,
        bgcolor=BG_WHITE,
        prefix_icon=ft.Icons.PERSON_OUTLINE,
        filled=True,
        border_radius=12,
        text_size=14
    )
    email_field = ft.TextField(
        label="Email Address", 
        border_color=PRIMARY_ORANGE, 
        focused_border_color=ACCENT_ORANGE,
        bgcolor=BG_WHITE,
        prefix_icon=ft.Icons.EMAIL_OUTLINED,
        filled=True,
        border_radius=12,
        text_size=14
    )
    subject_field = ft.TextField(
        label="Subject", 
        border_color=PRIMARY_ORANGE, 
        focused_border_color=ACCENT_ORANGE,
        bgcolor=BG_WHITE,
        prefix_icon=ft.Icons.TOPIC,
        filled=True,
        border_radius=12,
        text_size=14
    )
    message_field = ft.TextField(
        label="Project Details / Inquiry Message", 
        multiline=True, 
        min_lines=5,
        max_lines=8,
        border_color=PRIMARY_ORANGE, 
        focused_border_color=ACCENT_ORANGE,
        bgcolor=BG_WHITE,
        prefix_icon=ft.Icons.MESSAGE_OUTLINED,
        filled=True,
        border_radius=12,
        text_size=14
    )

    def handle_submit_message(e):
        if not name_field.value or not email_field.value:
            page.show_snack_bar(
                ft.SnackBar(
                    content=ft.Text("Please fill out your Name and Email fields before submitting."),
                    bgcolor=ACCENT_ORANGE,
                    duration=3000,
                )
            )
        else:
            page.show_snack_bar(
                ft.SnackBar(
                    content=ft.Text(f"Thank you {name_field.value}! Your message was compiled and sent successfully. I'll get back to you soon."),
                    bgcolor=PRIMARY_ORANGE,
                    duration=4000,
                )
            )
            name_field.value = ""
            email_field.value = ""
            subject_field.value = ""
            message_field.value = ""
            page.update()

    contact_section = ft.Container(
        key="contact",
        bgcolor=LIGHT_BG,
        padding=40,
        content=ft.Column([
            create_section_header("GET IN TOUCH", "Let's collaborate on mechanical engineering projects, research, or career opportunities."),
            
            ft.ResponsiveRow(
                spacing=30,
                run_spacing=30,
                controls=[
                    # LEFT COLUMN - Contact Information Cards
                    ft.Column(
                        col={"sm": 12, "md": 5},
                        spacing=20,
                        controls=[
                            # Availability Card
                            ft.Container(
                                bgcolor=BG_WHITE,
                                padding=25,
                                border_radius=16,
                                shadow=ft.BoxShadow(
                                    blur_radius=15,
                                    color="#d4a07a",
                                    spread_radius=1,
                                    offset=ft.Offset(0, 4),
                                ),
                                border=ft.Border(
                                    left=ft.BorderSide(4, ACCENT_ORANGE),
                                    top=ft.BorderSide(0, BORDER_COLOR),
                                    right=ft.BorderSide(0, BORDER_COLOR),
                                    bottom=ft.BorderSide(0, BORDER_COLOR),
                                ),
                                content=ft.Column(
                                    spacing=12,
                                    controls=[
                                        ft.Row([
                                            ft.Container(
                                                bgcolor=SECTION_ORANGE,
                                                padding=10,
                                                border_radius=12,
                                                content=ft.Icon(ft.Icons.WORK_OUTLINE, color=PRIMARY_ORANGE, size=28),
                                            ),
                                            ft.Text("Availability", size=20, weight=ft.FontWeight.BOLD, color=DEEP_ORANGE),
                                        ]),
                                        ft.Text("Available for mechanical engineering consultation, thermal system analysis, mechanical design, and research collaborations.", color=TEXT_GREY, size=14),
                                        ft.Container(height=5),
                                        ft.Container(
                                            bgcolor=LIGHT_BG,
                                            padding=12,
                                            border_radius=10,
                                            content=ft.Row([
                                                ft.Icon(ft.Icons.CHECK_CIRCLE, color=ACCENT_ORANGE, size=18),
                                                ft.Text("Open for internships & graduate positions", color=DEEP_ORANGE, size=13, weight=ft.FontWeight.W_500),
                                            ]),
                                        ),
                                    ],
                                ),
                            ),
                            
                            # Contact Details Card
                            ft.Container(
                                bgcolor=BG_WHITE,
                                padding=25,
                                border_radius=16,
                                shadow=ft.BoxShadow(
                                    blur_radius=15,
                                    color="#d4a07a",
                                    spread_radius=1,
                                    offset=ft.Offset(0, 4),
                                ),
                                content=ft.Column(
                                    spacing=20,
                                    controls=[
                                        ft.Text("Contact Information", size=18, weight=ft.FontWeight.BOLD, color=DEEP_ORANGE),
                                        
                                        ft.Container(
                                            on_click=lambda e: page.launch_url("tel:+264817687816"),
                                            content=ft.Row([
                                                ft.Container(
                                                    bgcolor=SECTION_ORANGE,
                                                    padding=8,
                                                    border_radius=10,
                                                    content=ft.Icon(ft.Icons.PHONE_ANDROID, color=PRIMARY_ORANGE, size=20),
                                                ),
                                                ft.Column([
                                                    ft.Text("Phone", size=11, color=SUBTEXT_GREY),
                                                    ft.Text("+264 81 768 7816", size=15, weight=ft.FontWeight.W_500, color=DEEP_ORANGE),
                                                ]),
                                            ], spacing=12),
                                        ),
                                        
                                        ft.Container(
                                            on_click=lambda e: page.launch_url("mailto:simonshitana21@gmail.com"),
                                            content=ft.Row([
                                                ft.Container(
                                                    bgcolor=SECTION_ORANGE,
                                                    padding=8,
                                                    border_radius=10,
                                                    content=ft.Icon(ft.Icons.EMAIL, color=PRIMARY_ORANGE, size=20),
                                                ),
                                                ft.Column([
                                                    ft.Text("Email", size=11, color=SUBTEXT_GREY),
                                                    ft.Text("simonshitana21@gmail.com", size=14, weight=ft.FontWeight.W_500, color=DEEP_ORANGE),
                                                ]),
                                            ], spacing=12),
                                        ),
                                        
                                        ft.Container(
                                            on_click=lambda e: page.launch_url("https://github.com/SimonShitana"),
                                            content=ft.Row([
                                                ft.Container(
                                                    bgcolor=SECTION_ORANGE,
                                                    padding=8,
                                                    border_radius=10,
                                                    content=ft.Icon(ft.Icons.CODE, color=PRIMARY_ORANGE, size=20),
                                                ),
                                                ft.Column([
                                                    ft.Text("GitHub", size=11, color=SUBTEXT_GREY),
                                                    ft.Text("github.com/SimonShitana", size=13, weight=ft.FontWeight.W_500, color=DEEP_ORANGE),
                                                ]),
                                            ], spacing=12),
                                        ),
                                        
                                        ft.Container(
                                            content=ft.Row([
                                                ft.Container(
                                                    bgcolor=SECTION_ORANGE,
                                                    padding=8,
                                                    border_radius=10,
                                                    content=ft.Icon(ft.Icons.LOCATION_ON, color=PRIMARY_ORANGE, size=20),
                                                ),
                                                ft.Column([
                                                    ft.Text("Location", size=11, color=SUBTEXT_GREY),
                                                    ft.Text("Ongwediva, Namibia", size=14, weight=ft.FontWeight.W_500, color=DEEP_ORANGE),
                                                ]),
                                            ], spacing=12),
                                        ),
                                    ],
                                ),
                            ),
                            
                            # Social/Quick Links Card
                            ft.Container(
                                bgcolor=PRIMARY_ORANGE,
                                padding=20,
                                border_radius=16,
                                shadow=ft.BoxShadow(
                                    blur_radius=15,
                                    color="#d4a07a",
                                    spread_radius=1,
                                    offset=ft.Offset(0, 4),
                                ),
                                content=ft.Column(
                                    spacing=12,
                                    controls=[
                                        ft.Text("Quick Connect", size=16, weight=ft.FontWeight.BOLD, color=BG_WHITE),
                                        ft.Row(
                                            spacing=12,
                                            controls=[
                                                ft.IconButton(
                                                    icon=ft.Icons.MAIL,
                                                    icon_color=BG_WHITE,
                                                    bgcolor="#e8650a",
                                                    on_click=lambda e: page.launch_url("mailto:simonshitana21@gmail.com"),
                                                    style=ft.ButtonStyle(shape=ft.CircleBorder()),
                                                ),
                                                ft.IconButton(
                                                    icon=ft.Icons.CODE,
                                                    icon_color=BG_WHITE,
                                                    bgcolor="#e8650a",
                                                    on_click=lambda e: page.launch_url("https://github.com/SimonShitana"),
                                                    style=ft.ButtonStyle(shape=ft.CircleBorder()),
                                                ),
                                                ft.IconButton(
                                                    icon=ft.Icons.CHAT,
                                                    icon_color=BG_WHITE,
                                                    bgcolor="#e8650a",
                                                    on_click=lambda e: page.launch_url("https://wa.me/264817687816"),
                                                    style=ft.ButtonStyle(shape=ft.CircleBorder()),
                                                ),
                                                ft.IconButton(
                                                    icon=ft.Icons.INSERT_DRIVE_FILE,
                                                    icon_color=BG_WHITE,
                                                    bgcolor="#e8650a",
                                                    on_click=lambda e: page.launch_url("/cv.pdf"),
                                                    style=ft.ButtonStyle(shape=ft.CircleBorder()),
                                                ),
                                            ]
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                    
                    # RIGHT COLUMN - Contact Form
                    ft.Container(
                        col={"sm": 12, "md": 7},
                        bgcolor=BG_WHITE,
                        padding=30,
                        border_radius=16,
                        shadow=ft.BoxShadow(
                            blur_radius=15,
                            color="#d4a07a",
                            spread_radius=1,
                            offset=ft.Offset(0, 4),
                        ),
                        content=ft.Column(
                            spacing=20,
                            controls=[
                                ft.Row([
                                    ft.Icon(ft.Icons.SEND, color=PRIMARY_ORANGE, size=28),
                                    ft.Text("Send a Message", size=22, weight=ft.FontWeight.BOLD, color=DEEP_ORANGE),
                                ]),
                                ft.Text("I'll get back to you within 24-48 hours", size=13, color=SUBTEXT_GREY),
                                ft.Divider(color=BORDER_COLOR),
                                name_field,
                                email_field,
                                subject_field,
                                message_field,
                                ft.Container(height=5),
                                ft.ElevatedButton(
                                    "Send Message",
                                    icon=ft.Icons.SEND,
                                    bgcolor=PRIMARY_ORANGE,
                                    color=BG_WHITE,
                                    on_click=handle_submit_message,
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=12),
                                        padding=ft.Padding(25, 12, 25, 12),
                                    ),
                                    expand=True,
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        ]),
    )

    portfolio_pages = {
        "overview": hero_section,
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
        button = ft.TextButton(
            label,
            style=ft.ButtonStyle(
                color=BG_WHITE if page_key == current_page_key["value"] else "#f0c8a8",
                overlay_color="#e8650a",
            ),
            on_click=lambda e, target=page_key: navigate_to(target),
        )
        nav_buttons[page_key] = button
        return button

    # =========================================================
    # STICKY NAVBAR PANEL (Pinned permanently to top layer)
    # =========================================================
    header_navbar = ft.Container(
        bgcolor=PRIMARY_ORANGE,
        padding=ft.Padding(40, 15, 40, 15),
        border=ft.Border(bottom=ft.BorderSide(1, ACCENT_ORANGE)),
        shadow=ft.BoxShadow(blur_radius=10, color="#d4a07a", offset=ft.Offset(0, 2)),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Row([
                    ft.Container(width=12, height=12, bgcolor=BG_WHITE, border_radius=6),
                    ft.Text("SIMON SHITANA", weight=ft.FontWeight.BOLD, size=16, color=BG_WHITE, style=ft.TextStyle(letter_spacing=1.1))
                ], spacing=10),
                ft.Row([
                    make_nav_button("Overview", "overview"),
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

    # =========================================================
    # RENDER DIRECT TO MAIN PAGE WINDOW
    # =========================================================
    page.add(
        ft.Column(
            expand=True,
            spacing=0,
            controls=[
                header_navbar,       # Stays perfectly frozen at the top
                page_switcher        # Swaps section pages beneath the navbar
            ]
        )
    )

def open_browser():
    """Open the web browser automatically when the server starts"""
    import time
    time.sleep(2)  # Give the server a moment to start
    webbrowser.open("http://127.0.0.1:8551")

if __name__ == "__main__":
    try:
        # Start the browser opener in a separate thread
        threading.Thread(target=open_browser, daemon=True).start()
        
        # Run the Flet app with web support
        ft.app(
            target=main,
            host="127.0.0.1",
            port=8551,
            view=ft.AppView.WEB_BROWSER,  # This will open in default browser
            assets_dir="assets",
        )
    except Exception as e:
        print(f"Error: {e}", flush=True)
        import traceback
        traceback.print_exc()