export type Link = { label: string; href: string };

export type Role = {
  company: string;
  title: string;
  period: string;
  location?: string;
  summary?: string;
  highlights: string[];
  stack?: string[];
  links?: Link[];
};

export type ProjectItem = {
  name: string;
  description: string;
  tags: string[];
  href?: string;
};

export type SkillGroup = {
  label: string;
  items: string[];
};

export const profile = {
  name: "Nguyễn Đức Anh",
  alias: "Aldric",
  title: "Software Engineer · TypeScript · Python · Node.js",
  location: "Hà Nội, Việt Nam · Remote",
  email: "anhnd350309@gmail.com",
  github: "https://github.com/0xaldric",
  linkedin: "https://www.linkedin.com/in/anhnd350309",
  twitter: "https://x.com/0xaldric",
  resume: "/CV_Nguyen_Duc_Anh_Aldric_Tailored.pdf",
  // Tailored bio for product-led, AI-assisted, cloud-native engineering roles.
  tagline:
    "Product-minded engineer shipping end-to-end — from planning to production. Backend and full-stack across TypeScript, Python, and Node.js, with hands-on CI/CD, observability, and cloud delivery at startup pace.",
};

export const about = {
  paragraphs: [
    "I'm a software engineer who treats every system as a product. For 5+ years I've shipped customer-facing features and the backbone they run on — leading teams, owning delivery, and operating in fast-changing environments where speed, quality, and customer impact have to coexist.",
    "I work primarily in TypeScript and Python (Node.js, NestJS, FastAPI), with deep experience in microservices, distributed systems, smart contracts, and event-driven architecture (Kafka, RabbitMQ). I've scaled platforms to 50,000+ active users, sustained 99.9% uptime, and cut API latency by 60% through targeted caching and profiling.",
    "I'm comfortable across the stack and across the org — collaborating with Product and Design, owning incidents, contributing to code reviews and engineering discussions, and adopting AI-assisted workflows to ship faster without sacrificing reliability.",
  ],
  facts: [
    { label: "Years shipping production", value: "5+" },
    { label: "Peak monthly active users", value: "50K+" },
    { label: "Uptime sustained", value: "99.9%" },
    { label: "Latency reduction", value: "60%" },
  ],
};

export const experience: Role[] = [
  {
    company: "5Solution",
    title: "Senior Software Engineer",
    period: "04/2025 — Present",
    location: "Remote · Vietnam",
    summary:
      "Owning backend and full-stack delivery across a multi-product event-tech platform — 5sport, 5bib, 5ticket, 5pix — used by race organizers, athletes, and photographers.",
    highlights: [
      "Lead end-to-end delivery for 5sport and 5bib: race registration, bib-to-photo matching, and live leaderboards — partnering with Product and Design from discovery to production.",
      "Designed the 5ticket event ticketing flow (QR check-in, anti-fraud, refunds) on a Node.js/NestJS + PostgreSQL stack, hardened with idempotent APIs and integration tests.",
      "Built the 5pix high-throughput photo distribution pipeline — ingest, face/bib detection, CDN delivery — handling burst traffic on race days with autoscaling on Kubernetes.",
      "Hardened CI/CD with GitHub Actions, ephemeral preview environments, and structured logging + tracing for fast debugging and incident response.",
      "Adopted AI-assisted workflows (code review, scaffolding, test generation) across the team — measurably faster cycle times without dropping coverage.",
    ],
    stack: [
      "TypeScript",
      "NestJS",
      "Node.js",
      "PostgreSQL",
      "Redis",
      "Kafka",
      "Kubernetes",
      "GitHub Actions",
      "OpenTelemetry",
    ],
  },
  {
    company: "Mojave · 1sixtech",
    title: "Open-source Contributor",
    period: "04/2025 — 07/2025",
    location: "Remote · Open Source",
    summary:
      "Bitcoin / zk infrastructure — Rust workspace for full-node, sequencer, prover, and cryptographic utilities.",
    highlights: [
      "Implemented block signing and verification (PR #17) — cryptographic identity guarantees for produced blocks.",
      "Built automatic ethrex upgrade tooling (PR #20) — keeping the workspace in lockstep with upstream changes.",
      "Worked across a multi-crate Rust workspace covering full node, sequencer, prover, and cryptographic primitives.",
    ],
    stack: ["Rust", "Cryptography", "ZK", "Bitcoin", "ethrex"],
    links: [{ label: "Mojave on GitHub", href: "https://github.com/1sixtech/mojave" }],
  },
  {
    company: "Topology Foundation",
    title: "Senior Software Engineer",
    period: "12/2024 — 03/2025",
    location: "Remote",
    summary:
      "Decentralized Realtime Program (DRP) — open-source primitives for real-time collaborative apps.",
    highlights: [
      "Planned and improved build processes for the DRP runtime, enhancing CI/CD workflows and supporting modular code evolution.",
      "Authored high-coverage test suites that lifted code coverage to 90%, ensuring robust validation across distributed components.",
      "Integrated performance metrics for network latency and CPU time — enabling real-time profiling and observability in decentralized environments.",
    ],
    stack: ["TypeScript", "Node.js", "Vitest", "GitHub Actions", "Distributed Systems"],
    links: [{ label: "ts-drp on GitHub", href: "https://github.com/0xaldric/ts-drp" }],
  },
  {
    company: "AnyAxis Labs",
    title: "Head of Engineering",
    period: "02/2024 — 12/2024",
    location: "Hà Nội · Remote",
    summary:
      "Led the engineering org behind multiple Web3 products across the TON ecosystem.",
    highlights: [
      "Led development of a high-availability backend supporting 50,000+ active users with 99.9% uptime.",
      "Assembled and directed a backend + blockchain team; owned hiring, technical roadmaps, and security posture.",
      "Rolled out microservice architecture, DevOps practices, and CI/CD pipelines — standardizing deploys, observability, and incident response.",
      "TonPad — designed smart-contract logic and system architecture for a TON-native launchpad.",
      "AytuDex — engineered algorithmic optimizations delivering 50–100% faster execution than peer DEXes.",
      "Pump.fun-style platform — full-stack ecosystem with separated read / write / socket paths for predictable scaling.",
    ],
    stack: [
      "TypeScript",
      "NestJS",
      "Solidity",
      "TON / FunC",
      "PostgreSQL",
      "Redis",
      "Kafka",
      "Kubernetes",
    ],
  },
  {
    company: "Vector Education",
    title: "Co-founder · Engineering",
    period: "04/2023 — 04/2024",
    location: "Hà Nội",
    summary:
      "Co-founded an educational publishing app shipped to iOS and Android.",
    highlights: [
      "Built and deployed server-side services for Vector, an educational publishing app available on Android and iOS.",
      "Onboarded 400 users onto the platform; owned everything from infra to release engineering.",
    ],
    stack: ["Node.js", "TypeScript", "MongoDB", "AWS"],
    links: [
      { label: "iOS", href: "https://apps.apple.com/vn/app/vector/id6450834400" },
      {
        label: "Android",
        href: "https://play.google.com/store/apps/details?id=com.app.vector",
      },
    ],
  },
  {
    company: "WispSwap Lab",
    title: "Software Engineer (Part-time)",
    period: "03/2023 — 01/2024",
    location: "Remote",
    summary: "Off-chain infrastructure for a DeFi DEX.",
    highlights: [
      "Designed an efficient off-chain system to improve data processing and scalability inside the WispSwap DeFi ecosystem.",
      "Operated backend services for ~20,000 users; scaled infrastructure to 1,000+ concurrent active users in a single day.",
    ],
    stack: ["TypeScript", "Node.js", "PostgreSQL", "Redis"],
  },
  {
    company: "Teko Vietnam",
    title: "Software Engineer L3",
    period: "12/2021 — 06/2023",
    location: "Hà Nội",
    summary:
      "Enterprise CRM and merchant tooling for one of Vietnam's largest retail tech groups.",
    highlights: [
      "Built enterprise CRM applications on FastAPI, ElasticSearch, Redis, MySQL, and Apache Kafka.",
      "Cut API response latency by 60% via targeted caching strategies.",
      "Maintained legacy systems while upgrading the codebase with SOLID principles, clean-code practices, and design patterns — keeping test coverage above 95%.",
      "Mentored and trained four new team members through code reviews and on-the-job guidance.",
    ],
    stack: ["Python", "FastAPI", "MySQL", "Redis", "Elasticsearch", "Kafka"],
  },
  {
    company: "Teko Vietnam",
    title: "Software Engineer · Intern",
    period: "04/2021 — 11/2021",
    location: "Hà Nội",
    highlights: [
      "Built two core services in a microservice architecture using FastAPI, PostgreSQL, and Redis caching — serving 500 users.",
      "Integrated multiple core services to cut VNPAY merchant declaration time by 50%.",
    ],
    stack: ["Python", "FastAPI", "PostgreSQL", "Redis"],
  },
  {
    company: "VNIST",
    title: "Software Engineer · Intern",
    period: "01/2020 — 01/2021",
    location: "Hà Nội",
    highlights: [
      "First professional engineering role — contributed to internal tooling and security research projects.",
    ],
  },
];

export const skills: SkillGroup[] = [
  {
    label: "Languages",
    items: ["TypeScript", "Python", "Go (learning)", "Solidity", "Rust", "C++", "SQL"],
  },
  {
    label: "Backend & Frameworks",
    items: ["Node.js", "NestJS", "FastAPI", "Microservices", "REST", "gRPC", "WebSockets"],
  },
  {
    label: "Data & Messaging",
    items: ["PostgreSQL", "MySQL", "Redis", "Elasticsearch", "MongoDB", "Kafka", "RabbitMQ"],
  },
  {
    label: "Cloud, CI/CD & Observability",
    items: [
      "Docker",
      "Kubernetes",
      "GitHub Actions",
      "AWS",
      "OpenTelemetry",
      "Prometheus / Grafana",
      "Structured logging",
    ],
  },
  {
    label: "Web3",
    items: ["EVM", "Solidity", "TON / FunC", "Sui", "Solana", "Smart-contract design"],
  },
  {
    label: "Testing & Practices",
    items: [
      "Unit + integration testing",
      "TDD",
      "Code review",
      "Incident response",
      "AI-assisted workflows",
      "OOP & design patterns",
    ],
  },
];

export const projects: ProjectItem[] = [
  {
    name: "ts-drp · Decentralized Realtime Program",
    description:
      "TypeScript runtime for decentralized real-time collaboration. Contributed CI/CD, test infrastructure (→ 90% coverage), and performance instrumentation.",
    tags: ["TypeScript", "Distributed Systems", "Open Source"],
    href: "https://github.com/0xaldric/ts-drp",
  },
  {
    name: "Mojave · Bitcoin / zk infrastructure",
    description:
      "Rust workspace for Mojave's full-node, sequencer, prover, and cryptographic utilities. Contributed block signing & verification (PR #17) and automatic ethrex upgrade tooling (PR #20).",
    tags: ["Rust", "Bitcoin", "ZK", "Cryptography", "Open Source"],
    href: "https://github.com/1sixtech/mojave",
  },
  {
    name: "AytuDex — Algorithmic DEX",
    description:
      "On-chain DEX with custom routing and matching optimizations measured 50–100% faster than peer DEXes on the same pairs.",
    tags: ["Solidity", "DeFi", "Performance"],
  },
  {
    name: "TonPad — TON Launchpad",
    description:
      "Smart-contract logic and system design for a launchpad on the TON blockchain — handled allocation, vesting, and treasury flows.",
    tags: ["TON", "FunC", "Smart Contracts"],
  },
  {
    name: "Pump.fun-style Token Platform",
    description:
      "Full-stack token-issuance platform with separated read / write / socket layers for predictable horizontal scaling.",
    tags: ["TypeScript", "System Design", "Web3"],
  },
  {
    name: "Vector — Educational Publishing",
    description:
      "Co-founded and built the backend for an educational publishing app live on iOS and Android.",
    tags: ["Node.js", "Mobile Backend", "Startup"],
    href: "https://apps.apple.com/vn/app/vector/id6450834400",
  },
  {
    name: "FastAPI Boilerplate",
    description:
      "Opinionated FastAPI starter with dependency injection and a test-first layout — easy to extend, easy to test.",
    tags: ["Python", "FastAPI", "Open Source"],
    href: "https://github.com/0xaldric",
  },
  {
    name: "Telegram Bot Boilerplate",
    description:
      "Modular NestJS Telegram bot scaffold — separate modules, maintainable structure, production-ready.",
    tags: ["NestJS", "TypeScript", "Open Source"],
    href: "https://github.com/0xaldric",
  },
];

export const education = [
  {
    school: "Hà Nội University of Science and Technology",
    degree: "B.Sc., Computer Science",
    period: "09/2017 — 09/2022",
    location: "Hà Nội, Vietnam",
  },
];

export const achievements = [
  'UAVS Hackatrix — Top 7, "Application for job management and salary payment" (07/2021)',
  "KPMG Challenge — solutions to help businesses overcome pandemic impact",
  "HackerRank — Problem-Solving Certificate",
];
