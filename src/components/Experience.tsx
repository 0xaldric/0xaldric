import { ExternalLink, MapPin } from "lucide-react";
import { experience } from "../data/cv";
import { SectionHeading } from "./SectionHeading";

export function Experience() {
  return (
    <section
      id="experience"
      className="border-y border-zinc-800/60 bg-zinc-950/40"
    >
      <div className="mx-auto max-w-5xl px-4 py-20 sm:px-6 sm:py-28">
        <SectionHeading
          eyebrow="02 · Experience"
          title="Where I've shipped"
          description="From early intern at Teko to Head of Engineering — owning delivery and uptime across consumer, enterprise, and Web3."
        />

        <ol className="relative space-y-12 border-l border-zinc-800 pl-6 sm:pl-8">
          {experience.map((role) => (
            <li key={`${role.company}-${role.period}`} className="relative">
              <span className="absolute -left-[31px] top-2 flex h-3 w-3 items-center justify-center sm:-left-[37px]">
                <span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-emerald-400/40" />
                <span className="relative inline-flex h-3 w-3 rounded-full bg-emerald-400" />
              </span>

              <div className="flex flex-wrap items-baseline justify-between gap-x-4">
                <h3 className="text-lg font-semibold text-zinc-100">
                  {role.title}{" "}
                  <span className="text-zinc-500">· {role.company}</span>
                </h3>
                <span className="font-mono text-xs uppercase tracking-wider text-zinc-500">
                  {role.period}
                </span>
              </div>

              {role.location ? (
                <p className="mt-1 inline-flex items-center gap-1 text-xs text-zinc-500">
                  <MapPin className="h-3 w-3" /> {role.location}
                </p>
              ) : null}

              {role.summary ? (
                <p className="mt-3 text-sm text-zinc-300">{role.summary}</p>
              ) : null}

              <ul className="mt-4 space-y-2 text-sm text-zinc-400">
                {role.highlights.map((h, i) => (
                  <li key={i} className="flex gap-2 leading-relaxed">
                    <span
                      aria-hidden
                      className="mt-2 inline-block h-1 w-1 shrink-0 rounded-full bg-emerald-500/80"
                    />
                    <span>{h}</span>
                  </li>
                ))}
              </ul>

              {role.stack ? (
                <ul className="mt-4 flex flex-wrap gap-1.5">
                  {role.stack.map((s) => (
                    <li
                      key={s}
                      className="rounded-full border border-zinc-800 bg-zinc-900/60 px-2.5 py-0.5 font-mono text-[11px] text-zinc-400"
                    >
                      {s}
                    </li>
                  ))}
                </ul>
              ) : null}

              {role.links ? (
                <div className="mt-3 flex flex-wrap gap-3">
                  {role.links.map((l) => (
                    <a
                      key={l.href}
                      href={l.href}
                      target="_blank"
                      rel="noreferrer"
                      className="inline-flex items-center gap-1 text-xs text-emerald-400 hover:text-emerald-300"
                    >
                      {l.label} <ExternalLink className="h-3 w-3" />
                    </a>
                  ))}
                </div>
              ) : null}
            </li>
          ))}
        </ol>
      </div>
    </section>
  );
}
