"""LI.FI-tailored CV PDF — Web3 / Checkout positioning. Separate from the
   primary tailored CV; fits on 2 pages, Unicode-safe."""

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

OUT_PATH = "/Users/anhnd/Documents/mycv/public/CV_Nguyen_Duc_Anh_Aldric_LiFi.pdf"

# Register a Unicode-capable font (Arial on macOS supports full diacritics).
ARIAL = "/System/Library/Fonts/Supplemental/Arial.ttf"
ARIAL_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
ARIAL_ITALIC = "/System/Library/Fonts/Supplemental/Arial Italic.ttf"
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
    "title": "Senior Full-Stack Engineer — TypeScript · Node.js · React · Web3",
    "tagline": "Backend-heavy full-stack engineer with deep Web3 experience. Building provider integrations, DEX/launchpad/NFT systems, and long-running on-chain flows on the exact stack LI.FI runs — Node.js/TypeScript, React + viem/wagmi, MongoDB, Redis, Kubernetes on AWS.",
    "location": "Remote",
    "email": "anhnd350309@gmail.com",
    "github": "github.com/0xaldric",
    "linkedin": "linkedin.com/in/anhnd350309",
}

SUMMARY = (
    "Senior full-stack engineer with 5+ years shipping production backend systems and 3+ years building Web3 products "
    "end to end — DEX routing, launchpads, NFT execution engines, and cross-chain tooling. Comfortable across the "
    "exact LI.FI stack: TypeScript/Node.js, React with viem/wagmi, MongoDB/Redis, ethers.js, Docker/Kubernetes on AWS. "
    "Strong instincts around provider integrations, async flows, retries/idempotency, observability, and recovery — "
    "the exact failure modes a Checkout product has to absorb."
)

EXPERIENCE = [
    {
        "title": "Senior Web3 Engineer (Freelance)",
        "company": "Independent",
        "period": "05/2025 — Present",
        "location": "Remote",
        "summary": "Shipping production crypto products end to end across multiple teams — token launchpads, NFT execution engines, DEX and bridge tooling — on TypeScript / Node.js / React / Solidity.",
        "highlights": [
            "Buy launchpad — full-stack token launch platform on EVM with bonding-curve pricing, anti-bot guards, and partner-configurable rules. React + viem/wagmi on the client; Node.js workers on ethers.js; MongoDB + Redis for sessions, quotes, and idempotent state.",
            "NFT Strategy (nftstrategy) — automated NFT execution engine on top of Seaport/Reservoir with floor-sweep, strategy backtests, and robust partial-fill recovery. Lifecycle state tracked mempool → confirmation → reorg.",
            "Provider integration patterns — normalized DEX aggregators, NFT marketplaces, and price oracles behind a single client-facing API; absorbed provider-specific edge cases (rate limits, slippage drift, eventually-consistent quotes).",
            "Long-running flow hardening — idempotent quote refresh, webhook + reconciliation jobs, retry/backoff with circuit breakers, and on-chain recovery flows for stuck cross-chain transactions.",
            "Observability stack — structured logs, traces, and per-provider metrics dashboards; alerts wired to incident response.",
        ],
        "stack": ["TypeScript", "Node.js", "React", "viem", "wagmi", "ethers.js", "Solidity", "MongoDB", "Redis", "Docker", "AWS"],
    },
    {
        "title": "Open-source Contributor",
        "company": "Mojave · 1sixtech",
        "period": "04/2025 — 07/2025",
        "location": "Remote · Open Source",
        "summary": "Bitcoin / zk infrastructure — Rust workspace for full-node, sequencer, prover, and cryptographic utilities.",
        "highlights": [
            "Implemented block signing and verification (PR #17) — cryptographic identity guarantees for produced blocks.",
            "Built automatic ethrex upgrade tooling (PR #20) — keeping the workspace in lockstep with upstream changes.",
            "Worked across a multi-crate Rust workspace covering full node, sequencer, prover, and cryptographic primitives.",
        ],
        "stack": ["Rust", "Cryptography", "ZK", "Bitcoin", "ethrex"],
    },
    {
        "title": "Senior Software Engineer",
        "company": "Topology Foundation",
        "period": "12/2024 — 03/2025",
        "location": "Remote (distributed: Germany · France · Korea)",
        "summary": "Decentralized Realtime Program (DRP) — open-source primitives for real-time collaborative apps. Worked daily with teammates across CET (Germany, France) and APAC (Korea); standups, pair-programming, and on-call all built around a shared European afternoon overlap.",
        "highlights": [
            "Improved build processes and CI/CD workflows for the DRP runtime, supporting modular code evolution.",
            "Authored high-coverage test suites — lifted code coverage to 90% across distributed components.",
            "Integrated performance metrics for network latency and CPU time, enabling real-time profiling and observability in decentralized environments.",
            "Operated effectively across a CET/APAC team split — proof point for any EMEA-leaning role considering an APAC contributor.",
        ],
        "stack": ["TypeScript", "Node.js", "Vitest", "GitHub Actions", "Distributed Systems"],
    },
    {
        "title": "Head of Engineering",
        "company": "AnyAxis Labs",
        "period": "02/2024 — 12/2024",
        "location": "Remote",
        "summary": "Led the engineering org behind multiple Web3 products across the TON ecosystem — DEX, launchpad, and token issuance.",
        "highlights": [
            "AytuDex — engineered algorithmic routing optimizations 50–100% faster than peer DEXes on the same pairs (directly applicable to bridge / DEX-aggregator routing logic).",
            "TonPad — designed launchpad smart contracts and system architecture: allocation, vesting, treasury, partner-configurable rules.",
            "Pump.fun-style platform — separated read / write / socket layers for predictable scaling under bursty long-running flows.",
            "Led a high-availability backend supporting 50,000+ active users at 99.9% uptime; standardized deploys, observability, and incident response on K8s.",
            "Built and directed a backend + blockchain team; owned hiring, technical roadmaps, and security posture.",
        ],
        "stack": ["TypeScript", "NestJS", "Solidity", "TON / FunC", "PostgreSQL", "Redis", "Kafka", "Kubernetes"],
    },
    {
        "title": "Software Engineer (Part-time)",
        "company": "WispSwap Lab",
        "period": "03/2023 — 01/2024",
        "location": "Remote",
        "summary": "Off-chain infrastructure for a DeFi DEX — the same kind of provider/indexer layer that sits behind a Checkout product.",
        "highlights": [
            "Designed and shipped the off-chain indexing + quote service for WispSwap; operated services for ~20,000 users and 1,000+ concurrent on peak days.",
            "Built idempotent quote refresh, retry/backoff, and reconciliation against on-chain truth.",
        ],
        "stack": ["TypeScript", "Node.js", "PostgreSQL", "Redis", "ethers.js"],
    },
    {
        "title": "Software Engineer L3",
        "company": "Teko",
        "period": "12/2021 — 06/2023",
        "location": None,
        "summary": "Enterprise CRM and merchant tooling for a major retail tech group — production backend foundations.",
        "highlights": [
            "Built enterprise CRM apps on FastAPI, ElasticSearch, Redis, MySQL, and Kafka — cut API latency by 60% via targeted caching.",
            "Maintained legacy systems while upgrading with SOLID + design patterns; kept test coverage above 95%.",
            "Mentored four new team members through code reviews and on-the-job guidance.",
        ],
        "stack": ["Python", "FastAPI", "MySQL", "Redis", "Elasticsearch", "Kafka"],
    },
]

SKILLS = [
    ("Languages", "TypeScript, Solidity, Rust, Python, Go (learning), SQL"),
    ("Backend", "Node.js, NestJS, Express, FastAPI, microservices, REST, WebSockets"),
    ("Web3 / on-chain", "viem, wagmi, ethers.js, web3.js, Hardhat, Foundry, EVM, Solidity, TON / FunC, Sui, Solana"),
    ("Frontend", "React, TypeScript, Tailwind, viem + wagmi for Web3 UI"),
    ("Data & messaging", "MongoDB, PostgreSQL, MySQL, Redis, Elasticsearch, Kafka, RabbitMQ"),
    ("Cloud & DevOps", "Docker, Kubernetes, AWS, CloudFlare, GitHub Actions, GitOps CD, OpenTelemetry, Prometheus / Grafana"),
    ("Integration patterns", "Provider normalization, idempotent quotes, async retries, webhooks, reconciliation, recovery flows, circuit breakers"),
]

PROJECTS = [
    ("Buy launchpad (freelance)",
     "Full-stack EVM token launch platform with bonding-curve pricing, anti-bot guards, and partner-configurable rules. React + viem/wagmi UI, Node.js + ethers.js workers, MongoDB / Redis state."),
    ("NFT Strategy · nftstrategy (freelance)",
     "Automated NFT execution engine on Seaport/Reservoir: floor sweeps, strategy backtests, partial-fill recovery, mempool → reorg lifecycle tracking."),
    ("AytuDex / TonPad / Pump.fun-style platform",
     "Web3 systems shipped via AnyAxis Labs: custom DEX routing (50–100% faster), launchpad smart contracts, scalable token issuance with separated read/write/socket layers."),
    ("Mojave · Bitcoin / zk infrastructure",
     "Rust workspace for full-node, sequencer, prover, and cryptographic utilities. Contributed block signing & verification (PR #17) and automatic ethrex upgrade tooling (PR #20). github.com/1sixtech/mojave"),
    ("ts-drp · Decentralized Realtime Program",
     "TypeScript runtime for decentralized real-time collaboration — contributed CI/CD, test infrastructure (→ 90% coverage), and performance instrumentation. github.com/0xaldric/ts-drp"),
]

EDUCATION = {
    "school": "Hanoi University of Science and Technology (HUST)",
    "degree": "B.Sc., Computer Science",
    "period": "09/2017 — 09/2022",
}

ACHIEVEMENTS = [
    'UAVS Hackatrix — Top 7, "Application for job management and salary payment" (07/2021)',
    "KPMG Challenge — solutions to help businesses overcome pandemic impact",
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
