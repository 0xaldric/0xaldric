import { ArrowUpRight, GraduationCap, Trophy } from "lucide-react";
import { achievements, education, projects } from "../data/cv";
import { SectionHeading } from "./SectionHeading";

export function Projects() {
  return (
    <section
      id="projects"
      className="border-t border-zinc-800/60 bg-zinc-950/40"
    >
      <div className="mx-auto max-w-5xl px-4 py-20 sm:px-6 sm:py-28">
        <SectionHeading
          eyebrow="04 · Projects"
          title="Selected work"
          description="A mix of Web3 systems, open source, and product work I'm proud of."
        />

        <ul className="grid gap-4 sm:grid-cols-2">
          {projects.map((p) => {
            const Wrapper: React.ElementType = p.href ? "a" : "div";
            const wrapperProps = p.href
              ? { href: p.href, target: "_blank", rel: "noreferrer" }
              : {};
            return (
              <li key={p.name}>
                <Wrapper
                  {...wrapperProps}
                  className="group block h-full rounded-2xl border border-zinc-800/80 bg-zinc-900/40 p-5 transition hover:border-emerald-500/40 hover:bg-zinc-900/70"
                >
                  <div className="flex items-start justify-between gap-3">
                    <h3 className="text-base font-semibold text-zinc-100 group-hover:text-emerald-300">
                      {p.name}
                    </h3>
                    {p.href ? (
                      <ArrowUpRight className="h-4 w-4 shrink-0 text-zinc-500 transition group-hover:-translate-y-0.5 group-hover:translate-x-0.5 group-hover:text-emerald-400" />
                    ) : null}
                  </div>
                  <p className="mt-2 text-sm leading-relaxed text-zinc-400">
                    {p.description}
                  </p>
                  <ul className="mt-4 flex flex-wrap gap-1.5">
                    {p.tags.map((t) => (
                      <li
                        key={t}
                        className="rounded-full border border-zinc-800 px-2 py-0.5 font-mono text-[11px] text-zinc-400"
                      >
                        {t}
                      </li>
                    ))}
                  </ul>
                </Wrapper>
              </li>
            );
          })}
        </ul>

        <div className="mt-14 grid gap-6 sm:grid-cols-2">
          <div className="rounded-2xl border border-zinc-800/80 bg-zinc-900/40 p-5">
            <div className="flex items-center gap-2 text-sm font-semibold uppercase tracking-wider text-emerald-400">
              <GraduationCap className="h-4 w-4" /> Education
            </div>
            <ul className="mt-4 space-y-3">
              {education.map((e) => (
                <li key={e.school}>
                  <p className="text-sm font-medium text-zinc-100">{e.school}</p>
                  <p className="text-sm text-zinc-400">{e.degree}</p>
                  <p className="font-mono text-xs text-zinc-500">{e.period}</p>
                </li>
              ))}
            </ul>
          </div>

          <div className="rounded-2xl border border-zinc-800/80 bg-zinc-900/40 p-5">
            <div className="flex items-center gap-2 text-sm font-semibold uppercase tracking-wider text-emerald-400">
              <Trophy className="h-4 w-4" /> Achievements
            </div>
            <ul className="mt-4 space-y-2 text-sm text-zinc-400">
              {achievements.map((a) => (
                <li key={a} className="flex gap-2">
                  <span
                    aria-hidden
                    className="mt-2 inline-block h-1 w-1 shrink-0 rounded-full bg-emerald-500/80"
                  />
                  <span>{a}</span>
                </li>
              ))}
            </ul>
          </div>
        </div>
      </div>
    </section>
  );
}
