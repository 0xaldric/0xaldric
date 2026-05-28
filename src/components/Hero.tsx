import { ArrowDown, Download, Mail, MapPin } from "lucide-react";
import { GithubIcon, LinkedinIcon } from "./BrandIcons";
import { profile } from "../data/cv";

export function Hero() {
  return (
    <section
      id="top"
      className="relative overflow-hidden border-b border-zinc-800/60"
    >
      <div className="pointer-events-none absolute inset-0 -z-10">
        <div className="absolute -top-32 left-1/2 h-[34rem] w-[34rem] -translate-x-1/2 rounded-full bg-emerald-500/10 blur-3xl" />
        <div className="absolute right-[-6rem] top-40 h-72 w-72 rounded-full bg-cyan-500/10 blur-3xl" />
      </div>

      <div className="mx-auto max-w-5xl px-4 pt-24 pb-20 sm:px-6 sm:pt-32 sm:pb-28">
        <div className="flex items-center gap-2 font-mono text-xs uppercase tracking-[0.2em] text-emerald-400/80">
          <span className="h-1.5 w-1.5 rounded-full bg-emerald-400" />
          Available for new opportunities
        </div>

        <h1 className="mt-6 text-4xl font-semibold tracking-tight text-zinc-100 sm:text-6xl">
          {profile.name}{" "}
          <span className="text-zinc-500">({profile.alias})</span>
        </h1>

        <p className="mt-4 text-lg text-zinc-300 sm:text-xl">{profile.title}</p>

        <p className="mt-6 max-w-2xl text-base text-zinc-400 sm:text-lg">
          {profile.tagline}
        </p>

        <div className="mt-6 flex flex-wrap items-center gap-x-5 gap-y-2 text-sm text-zinc-500">
          <span className="inline-flex items-center gap-1.5">
            <MapPin className="h-4 w-4" /> {profile.location}
          </span>
          <a
            className="inline-flex items-center gap-1.5 hover:text-zinc-200"
            href={`mailto:${profile.email}`}
          >
            <Mail className="h-4 w-4" /> {profile.email}
          </a>
        </div>

        <div className="mt-10 flex flex-wrap items-center gap-3">
          <a
            href="#contact"
            className="inline-flex items-center gap-2 rounded-full bg-emerald-500 px-5 py-2.5 text-sm font-medium text-zinc-950 transition hover:bg-emerald-400"
          >
            <Mail className="h-4 w-4" />
            Get in touch
          </a>
          <a
            href={profile.resume}
            download
            className="inline-flex items-center gap-2 rounded-full border border-zinc-700 bg-zinc-900/50 px-5 py-2.5 text-sm font-medium text-zinc-200 transition hover:border-zinc-500 hover:bg-zinc-800"
          >
            <Download className="h-4 w-4" />
            Download CV
          </a>
          <a
            href={profile.github}
            target="_blank"
            rel="noreferrer"
            className="inline-flex items-center gap-2 rounded-full border border-zinc-800 px-5 py-2.5 text-sm font-medium text-zinc-300 transition hover:border-zinc-600 hover:text-zinc-100"
          >
            <GithubIcon className="h-4 w-4" /> GitHub
          </a>
          <a
            href={profile.linkedin}
            target="_blank"
            rel="noreferrer"
            className="inline-flex items-center gap-2 rounded-full border border-zinc-800 px-5 py-2.5 text-sm font-medium text-zinc-300 transition hover:border-zinc-600 hover:text-zinc-100"
          >
            <LinkedinIcon className="h-4 w-4" /> LinkedIn
          </a>
        </div>

        <a
          href="#about"
          className="mt-16 inline-flex items-center gap-2 text-xs font-mono uppercase tracking-[0.2em] text-zinc-500 transition hover:text-zinc-300"
        >
          Scroll <ArrowDown className="h-3 w-3 animate-bounce" />
        </a>
      </div>
    </section>
  );
}
