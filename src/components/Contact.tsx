import { Mail } from "lucide-react";
import { GithubIcon, LinkedinIcon } from "./BrandIcons";
import { profile } from "../data/cv";
import { SectionHeading } from "./SectionHeading";

export function Contact() {
  return (
    <section id="contact" className="mx-auto max-w-5xl px-4 py-20 sm:px-6 sm:py-28">
      <SectionHeading
        eyebrow="05 · Contact"
        title="Let's build something"
        description="I'm open to remote, product-focused engineering roles — especially teams shipping fast in modern, AI-assisted environments."
      />

      <div className="rounded-3xl border border-zinc-800/80 bg-gradient-to-br from-zinc-900/80 to-zinc-950 p-8 sm:p-10">
        <p className="max-w-2xl text-base text-zinc-300">
          The fastest way to reach me is email. Drop a line and I'll usually
          reply within a day.
        </p>

        <div className="mt-6 flex flex-wrap items-center gap-3">
          <a
            href={`mailto:${profile.email}`}
            className="inline-flex items-center gap-2 rounded-full bg-emerald-500 px-5 py-2.5 text-sm font-medium text-zinc-950 transition hover:bg-emerald-400"
          >
            <Mail className="h-4 w-4" /> {profile.email}
          </a>
          <a
            href={profile.github}
            target="_blank"
            rel="noreferrer"
            className="inline-flex items-center gap-2 rounded-full border border-zinc-700 px-5 py-2.5 text-sm font-medium text-zinc-200 transition hover:border-zinc-500"
          >
            <GithubIcon className="h-4 w-4" /> GitHub
          </a>
          <a
            href={profile.linkedin}
            target="_blank"
            rel="noreferrer"
            className="inline-flex items-center gap-2 rounded-full border border-zinc-700 px-5 py-2.5 text-sm font-medium text-zinc-200 transition hover:border-zinc-500"
          >
            <LinkedinIcon className="h-4 w-4" /> LinkedIn
          </a>
        </div>
      </div>
    </section>
  );
}
