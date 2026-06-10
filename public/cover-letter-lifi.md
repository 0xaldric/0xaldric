# Cover letter — LI.FI · Senior Full-Stack Engineer (Checkout)

Hi LI.FI team,

I'm applying for the Senior Full-Stack Engineer (Checkout) role. Two
things to put on the table upfront.

**On the EMEA requirement.** I'm currently in APAC (UTC+7), but I've
already been running exactly this rhythm in production. At **Topology
Foundation (12/2024 – 03/2025)** my immediate teammates were in
**Germany, France, and Korea** — daily standups, pair-programming, and
on-call rotations all worked because we built our cadence around the
European afternoon block, a 6–7h overlap window I'm happy to keep. I'm
also open to relocating to EMEA if the role progresses. If that's a
strict filter for HR, I'd love the chance to be considered on the work
itself; I think it stands up.

**On the work.** Checkout's product surface — provider integrations,
routing intelligence, lifecycle state across long-running flows, and the
recovery posture all of that needs — is the exact shape of what I've been
shipping:

- **BinkOS** (freelance, 2025) — a DeFi execution layer that normalizes
  10+ swap, bridge, and lending providers (deBridge for cross-chain,
  plus PancakeSwap, KyberSwap, OKX DEX, Jupiter, Venus) behind a single
  provider-agnostic plugin interface. This is the same
  provider-normalization and routing thesis LI.FI is built on — I've
  already built it once, in TypeScript on ethers + viem.
- **Token launchpad tooling** (freelance, 2025) — launch and buy/sell
  flows on Solana (LetsBonk) and EVM, with on-chain execution via
  ethers.js, IPFS metadata, and idempotent state — the funding-flow edge
  cases (slippage, retries, partial fills) a Checkout has to absorb.
- **On-chain oracle** (freelance, 2025) — a real-time pipeline producing
  commit-reveal attestations signed and verified on-chain, with
  orphan/recovery handling for long-running, failure-prone rounds.
- **AytuDex** (Head of Engineering, AnyAxis Labs) — algorithmic routing
  delivering 50–100% faster execution than peer DEXes; the routing
  intelligence story at a deeper layer.

Stack overlap with what LI.FI runs is direct and current:
**TypeScript / Node.js**, **React + viem**, **ethers.js**,
**MongoDB / Redis**, **Docker / Kubernetes on AWS**, **GitHub Actions /
GitOps CD**, structured observability.

I'd be glad to do a take-home or technical screen at your convenience.
CV attached.

Best,
Aldric (Nguyễn Đức Anh)
github.com/0xaldric · linkedin.com/in/0xaldric · anhnd350309@gmail.com
