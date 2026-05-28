import { about } from "../data/cv";
import { SectionHeading } from "./SectionHeading";

export function About() {
  return (
    <section id="about" className="mx-auto max-w-5xl px-4 py-20 sm:px-6 sm:py-28">
      <SectionHeading
        eyebrow="01 · About"
        title="Product-minded engineer. End-to-end ownership."
        description="I care about customer outcomes as much as the code. Here's the lens I bring."
      />

      <div className="grid gap-10 lg:grid-cols-3">
        <div className="space-y-5 text-base leading-relaxed text-zinc-300 lg:col-span-2">
          {about.paragraphs.map((p, i) => (
            <p key={i}>{p}</p>
          ))}
        </div>

        <dl className="grid grid-cols-2 gap-3 self-start">
          {about.facts.map((fact) => (
            <div
              key={fact.label}
              className="rounded-xl border border-zinc-800/80 bg-zinc-900/40 p-4"
            >
              <dt className="text-xs uppercase tracking-wide text-zinc-500">
                {fact.label}
              </dt>
              <dd className="mt-1 text-2xl font-semibold text-emerald-400">
                {fact.value}
              </dd>
            </div>
          ))}
        </dl>
      </div>
    </section>
  );
}
