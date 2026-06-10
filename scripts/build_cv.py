"""Tailored CV PDF — mirrors the website content, fits on 2 pages, Unicode-safe."""

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    KeepTogether,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

import os

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_PATH = os.path.join(REPO_ROOT, "public", "CV_Nguyen_Duc_Anh_Aldric_Tailored.pdf")


def _first_existing(paths):
    for p in paths:
        if os.path.exists(p):
            return p
    raise FileNotFoundError(f"No usable font found among: {paths}")


# Register a Unicode-capable font with full Vietnamese diacritics.
# Arial on macOS; Liberation Sans (Arial-metric-compatible) on Linux.
ARIAL = _first_existing([
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
])
ARIAL_BOLD = _first_existing([
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
])
ARIAL_ITALIC = _first_existing([
    "/System/Library/Fonts/Supplemental/Arial Italic.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf",
])
pdfmetrics.registerFont(TTFont("Body", ARIAL))
pdfmetrics.registerFont(TTFont("Body-Bold", ARIAL_BOLD))
pdfmetrics.registerFont(TTFont("Body-Italic", ARIAL_ITALIC))

FONT = "Body"
FONT_B = "Body-Bold"
FONT_I = "Body-Italic"

# Palette
INK = colors.HexColor("#0f172a")
SUB = colors.HexColor("#475569")
MUTED = colors.HexColor("#64748b")
ACCENT = colors.HexColor("#047857")
RULE = colors.HexColor("#cbd5e1")

PAGE_W, PAGE_H = A4
MARGIN_X = 14 * mm
MARGIN_TOP = 12 * mm
MARGIN_BOTTOM = 12 * mm

styles = getSampleStyleSheet()

name_style = ParagraphStyle(
    "Name",
    parent=styles["Title"],
    fontName=FONT_B,
    fontSize=20,
    leading=23,
    textColor=INK,
    spaceAfter=1,
    alignment=TA_LEFT,
)
title_style = ParagraphStyle(
    "Tagline",
    parent=styles["Normal"],
    fontName=FONT,
    fontSize=9.5,
    leading=12,
    textColor=SUB,
    spaceAfter=2,
)
contact_style = ParagraphStyle(
    "Contact",
    parent=styles["Normal"],
    fontName=FONT,
    fontSize=8.5,
    leading=11,
    textColor=MUTED,
    spaceAfter=4,
)
section_style = ParagraphStyle(
    "Section",
    parent=styles["Heading2"],
    fontName=FONT_B,
    fontSize=10,
    leading=12,
    textColor=ACCENT,
    spaceBefore=8,
    spaceAfter=3,
)
role_title_style = ParagraphStyle(
    "RoleTitle",
    parent=styles["Normal"],
    fontName=FONT_B,
    fontSize=10,
    leading=12,
    textColor=INK,
)
role_meta_style = ParagraphStyle(
    "RoleMeta",
    parent=styles["Normal"],
    fontName=FONT_I,
    fontSize=8.5,
    leading=11,
    textColor=MUTED,
)
role_period_style = ParagraphStyle(
    "RolePeriod",
    parent=styles["Normal"],
    fontName=FONT,
    fontSize=8.5,
    leading=11,
    textColor=MUTED,
    alignment=2,
)
summary_style = ParagraphStyle(
    "Summary",
    parent=styles["Normal"],
    fontName=FONT_I,
    fontSize=9,
    leading=12,
    textColor=SUB,
    spaceBefore=1,
    spaceAfter=2,
)
body_style = ParagraphStyle(
    "Body",
    parent=styles["Normal"],
    fontName=FONT,
    fontSize=9,
    leading=12,
    textColor=INK,
)
bullet_style = ParagraphStyle(
    "Bullet",
    parent=styles["Normal"],
    fontName=FONT,
    fontSize=9,
    leading=12,
    textColor=INK,
    leftIndent=9,
    spaceAfter=1,
)
chip_style = ParagraphStyle(
    "Chip",
    parent=styles["Normal"],
    fontName=FONT,
    fontSize=8,
    leading=11,
    textColor=SUB,
)
skill_label_style = ParagraphStyle(
    "SkillLabel",
    parent=styles["Normal"],
    fontName=FONT_B,
    fontSize=9,
    leading=11,
    textColor=ACCENT,
)


def rule():
    return HRFlowable(width="100%", thickness=0.4, color=RULE, spaceBefore=2, spaceAfter=4)


def bullet(text):
    # Use a typographic bullet that renders identically in any reader.
    return Paragraph(f"&#8226;&nbsp; {text}", bullet_style)


def role_header(title, company, period, location):
    title_html = f"<font name='{FONT_B}'>{title}</font> · <font color='#475569'>{company}</font>"
    data = [[Paragraph(title_html, role_title_style), Paragraph(period, role_period_style)]]
    t = Table(data, colWidths=[125 * mm, 50 * mm])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    flowables = [t]
    if location:
        flowables.append(Paragraph(location, role_meta_style))
    return flowables


def role_block(role):
    parts = role_header(role["title"], role["company"], role["period"], role.get("location"))
    if role.get("summary"):
        parts.append(Spacer(1, 1))
        parts.append(Paragraph(role["summary"], summary_style))
    parts.append(Spacer(1, 1))
    for h in role["highlights"]:
        parts.append(bullet(h))
    if role.get("stack"):
        parts.append(Spacer(1, 1))
        parts.append(Paragraph(
            f"<font color='#64748b'>Stack — </font>{', '.join(role['stack'])}",
            chip_style,
        ))
    parts.append(Spacer(1, 5))
    return KeepTogether(parts)


PROFILE = {
    "name": "Nguyễn Đức Anh (Aldric)",
    "title": "Software Engineer · TypeScript · Python · Node.js",
    "tagline": "Product-minded engineer shipping end-to-end — from planning to production. Backend and full-stack across TypeScript, Python, and Node.js, with hands-on CI/CD, observability, and cloud delivery at startup pace.",
    "location": "Remote",
    "email": "anhnd350309@gmail.com",
    "github": "github.com/0xaldric",
    "linkedin": "linkedin.com/in/0xaldric",
}

SUMMARY = (
    "Software engineer with 5+ years building and shipping production systems — from enterprise CRM at Teko "
    "to Web3 platforms supporting 50,000+ active users at 99.9% uptime. Strong product mindset, end-to-end "
    "ownership, and pragmatic judgment in fast-changing environments. Comfortable in modern AI-assisted "
    "engineering workflows, with deep experience across testing, CI/CD, observability, and cloud."
)

EXPERIENCE = [
    {
        "title": "Senior Software Engineer",
        "company": "5Solution",
        "period": "04/2025 — Present",
        "location": "Remote",
        "summary": "Backend and full-stack delivery across a multi-product event-tech platform — 5sport, 5bib, 5ticket, 5pix — used by race organizers, athletes, and photographers.",
        "highlights": [
            "Lead end-to-end delivery for 5sport and 5bib: race registration, bib-to-photo matching, and live leaderboards — partnering with Product and Design from discovery to production.",
            "Designed the 5ticket event ticketing flow (QR check-in, anti-fraud, refunds) on Node.js/NestJS + PostgreSQL, hardened with idempotent APIs and integration tests.",
            "Built the 5pix high-throughput photo distribution pipeline — ingest, face/bib detection, CDN delivery — handling burst traffic on race days with autoscaling on Kubernetes.",
            "Hardened CI/CD with GitHub Actions, ephemeral preview environments, and structured logging + tracing for fast debugging and incident response.",
            "Adopted AI-assisted workflows (code review, scaffolding, test generation) — measurably faster cycle times without dropping coverage.",
        ],
        "stack": ["TypeScript", "NestJS", "Node.js", "PostgreSQL", "Redis", "Kafka", "Kubernetes", "GitHub Actions", "OpenTelemetry"],
    },
    {
        "title": "Senior Software Engineer",
        "company": "Topology Foundation",
        "period": "12/2024 — 03/2025",
        "location": "Remote",
        "summary": "Decentralized Realtime Program (DRP) — open-source primitives for real-time collaborative apps.",
        "highlights": [
            "Improved build processes and CI/CD workflows for the DRP runtime, supporting modular code evolution.",
            "Authored high-coverage test suites — lifted code coverage to 90% across distributed components.",
            "Integrated performance metrics for network latency and CPU time, enabling real-time profiling and observability in decentralized environments.",
        ],
        "stack": ["TypeScript", "Node.js", "Vitest", "GitHub Actions", "Distributed Systems"],
    },
    {
        "title": "Head of Engineering",
        "company": "AnyAxis Labs",
        "period": "02/2024 — 12/2024",
        "location": "Remote",
        "summary": "Led the engineering org behind multiple Web3 products across the TON ecosystem.",
        "highlights": [
            "Led a high-availability backend supporting 50,000+ active users with 99.9% uptime.",
            "Built and directed a backend + blockchain team; owned hiring, technical roadmaps, and security posture.",
            "Rolled out microservices, DevOps practices, and CI/CD — standardizing deploys, observability, and incident response.",
            "Shipped TonPad (TON launchpad), AytuDex (50–100% faster execution than peer DEXes), and a Pump.fun-style platform with separated read/write/socket layers.",
        ],
        "stack": ["TypeScript", "NestJS", "Solidity", "TON / FunC", "PostgreSQL", "Redis", "Kafka", "Kubernetes"],
    },
    {
        "title": "Co-founder · Engineering",
        "company": "Vector Education",
        "period": "04/2023 — 04/2024",
        "location": None,
        "highlights": [
            "Built and deployed backend services for Vector — an educational publishing app shipped to iOS and Android; onboarded 400 users.",
        ],
        "stack": ["Node.js", "TypeScript", "MongoDB", "AWS"],
    },
    {
        "title": "Software Engineer (Part-time)",
        "company": "WispSwap Lab",
        "period": "03/2023 — 01/2024",
        "location": "Remote",
        "highlights": [
            "Designed an efficient off-chain system for the WispSwap DeFi ecosystem; operated services for ~20,000 users; scaled to 1,000+ concurrent users in a single day.",
        ],
        "stack": ["TypeScript", "Node.js", "PostgreSQL", "Redis"],
    },
    {
        "title": "Software Engineer L3",
        "company": "Teko",
        "period": "12/2021 — 06/2023",
        "location": None,
        "summary": "Enterprise CRM and merchant tooling for a major retail tech group.",
        "highlights": [
            "Built enterprise CRM apps on FastAPI, ElasticSearch, Redis, MySQL, and Kafka — cut API latency by 60% via targeted caching.",
            "Maintained legacy systems while upgrading the codebase with SOLID principles and design patterns; kept test coverage above 95%.",
            "Mentored four new team members through code reviews and on-the-job guidance.",
        ],
        "stack": ["Python", "FastAPI", "MySQL", "Redis", "Elasticsearch", "Kafka"],
    },
    {
        "title": "Software Engineer · Intern",
        "company": "Teko · VNIST",
        "period": "01/2020 — 11/2021",
        "location": None,
        "highlights": [
            "Built two core microservices on FastAPI / PostgreSQL / Redis (500 users); integrated services to cut VNPAY merchant declaration time by 50%. Prior internship at VNIST.",
        ],
    },
]

SKILLS = [
    ("Languages", "TypeScript, Python, Go (learning), Solidity, Rust, C++, SQL"),
    ("Backend & frameworks", "Node.js, NestJS, FastAPI, microservices, REST, gRPC, WebSockets"),
    ("Data & messaging", "PostgreSQL, MySQL, Redis, Elasticsearch, MongoDB, Kafka, RabbitMQ"),
    ("Cloud, CI/CD & observability", "Docker, Kubernetes, GitHub Actions, AWS, OpenTelemetry, Prometheus / Grafana, structured logging"),
    ("Web3", "EVM, Solidity, TON / FunC, Sui, Solana, smart-contract design"),
    ("Testing & practices", "Unit + integration testing, TDD, code review, incident response, AI-assisted workflows, OOP & design patterns"),
]

PROJECTS = [
    ("ts-drp · Decentralized Realtime Program",
     "TypeScript runtime for decentralized real-time collaboration — contributed CI/CD, test infrastructure (→ 90% coverage), and performance instrumentation. github.com/0xaldric/ts-drp"),
    ("Mojave · Bitcoin / zk infrastructure",
     "Rust workspace for full-node, sequencer, prover, and cryptographic utilities — contributed block signing/verification and ethrex upgrade tooling. github.com/1sixtech/mojave"),
    ("Zora Protocol — open-source contribution",
     "Merged upstream PR adding username + Farcaster support to the socialAccounts API. github.com/ourzora/zora-protocol/pull/525"),
    ("AytuDex / TonPad / Pump.fun-style platform",
     "Web3 systems: custom DEX routing (50–100% faster), TON launchpad smart contracts, scalable token issuance with separated read/write/socket layers."),
    ("NestJS backend & Telegram bot starters",
     "Open-source TypeScript starters — NestJS/TypeORM/Redis backend template and a Telegraf bot scaffold. github.com/0xaldric/template · github.com/0xaldric/telegram-bot-study"),
]

EDUCATION = {
    "school": "Hanoi University of Science and Technology (HUST)",
    "degree": "B.Sc., Computer Science",
    "period": "09/2017 — 09/2022",
}

ACHIEVEMENTS = [
    "HackerRank — Problem-Solving Certificate",
]


def build():
    doc = BaseDocTemplate(
        OUT_PATH,
        pagesize=A4,
        leftMargin=MARGIN_X,
        rightMargin=MARGIN_X,
        topMargin=MARGIN_TOP,
        bottomMargin=MARGIN_BOTTOM,
        title=f"CV — {PROFILE['name']}",
        author=PROFILE["name"],
    )
    frame = Frame(
        MARGIN_X, MARGIN_BOTTOM,
        PAGE_W - 2 * MARGIN_X,
        PAGE_H - MARGIN_TOP - MARGIN_BOTTOM,
        id="main", showBoundary=0,
    )
    doc.addPageTemplates([PageTemplate(id="main", frames=[frame])])

    story = []
    story.append(Paragraph(PROFILE["name"], name_style))
    story.append(Paragraph(PROFILE["title"], title_style))
    story.append(Paragraph(PROFILE["tagline"], title_style))
    contact_line = (
        f"{PROFILE['location']}  ·  "
        f"<a href='mailto:{PROFILE['email']}' color='#047857'>{PROFILE['email']}</a>  ·  "
        f"<a href='https://{PROFILE['github']}' color='#047857'>{PROFILE['github']}</a>  ·  "
        f"<a href='https://{PROFILE['linkedin']}' color='#047857'>{PROFILE['linkedin']}</a>"
    )
    story.append(Paragraph(contact_line, contact_style))
    story.append(rule())

    story.append(Paragraph("Summary", section_style))
    story.append(Paragraph(SUMMARY, body_style))

    story.append(Paragraph("Experience", section_style))
    for role in EXPERIENCE:
        story.append(role_block(role))

    story.append(Paragraph("Skills", section_style))
    skill_rows = [
        [Paragraph(label, skill_label_style), Paragraph(items, body_style)]
        for label, items in SKILLS
    ]
    skill_tbl = Table(skill_rows, colWidths=[50 * mm, 125 * mm])
    skill_tbl.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 1),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
    ]))
    story.append(skill_tbl)

    story.append(Paragraph("Selected projects", section_style))
    for name, desc in PROJECTS:
        story.append(Paragraph(f"<font name='{FONT_B}'>{name}</font> — <font color='#475569'>{desc}</font>", body_style))
        story.append(Spacer(1, 2))

    story.append(Paragraph("Education", section_style))
    story.append(Paragraph(
        f"<font name='{FONT_B}'>{EDUCATION['school']}</font> — {EDUCATION['degree']}  "
        f"<font color='#64748b'>· {EDUCATION['period']}</font>",
        body_style,
    ))

    story.append(Paragraph("Achievements", section_style))
    for a in ACHIEVEMENTS:
        story.append(bullet(a))

    doc.build(story)
    print(f"Built {OUT_PATH}")


if __name__ == "__main__":
    build()
