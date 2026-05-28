import { skills } from "../data/cv";
import { SectionHeading } from "./SectionHeading";

export function Skills() {
  return (
    <section id="skills" className="mx-auto max-w-5xl px-4 py-20 sm:px-6 sm:py-28">
      <SectionHeading
        eyebrow="03 · Skills"
        title="My stack"
        description="The tools I reach for when shipping production systems."
      />

      <div className="grid gap-5 sm:grid-cols-2">
        {skills.map((group) => (
          <div
            key={group.label}
            className="rounded-2xl border border-zinc-800/80 bg-zinc-900/40 p-5"
          >
            <h3 className="text-sm font-semibold uppercase tracking-wider text-emerald-400">
              {group.label}
            </h3>
            <ul className="mt-4 flex flex-wrap gap-2">
              {group.items.map((item) => (
                <li
                  key={item}
                  className="rounded-lg border border-zinc-800 bg-zinc-950/60 px-2.5 py-1 text-sm text-zinc-300 transition hover:border-emerald-500/40 hover:text-emerald-300"
                >
                  {item}
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </section>
  );
}
