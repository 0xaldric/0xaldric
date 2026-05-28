import { useEffect, useState } from "react";
import { Mail } from "lucide-react";
import { GithubIcon, LinkedinIcon } from "./BrandIcons";
import { profile } from "../data/cv";

const links = [
  { href: "#about", label: "About" },
  { href: "#experience", label: "Experience" },
  { href: "#skills", label: "Skills" },
  { href: "#projects", label: "Projects" },
  { href: "#contact", label: "Contact" },
];

export function Navbar() {
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 12);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  return (
    <header
      className={`sticky top-0 z-40 transition-all ${
        scrolled
          ? "border-b border-zinc-800/80 bg-zinc-950/70 backdrop-blur"
          : "border-b border-transparent bg-transparent"
      }`}
    >
      <nav className="mx-auto flex h-16 max-w-5xl items-center justify-between px-4 sm:px-6">
        <a
          href="#top"
          className="font-mono text-sm font-medium text-zinc-100 hover:text-emerald-400"
        >
          <span className="text-emerald-400">~/</span>aldric
        </a>

        <ul className="hidden gap-8 md:flex">
          {links.map((l) => (
            <li key={l.href}>
              <a
                href={l.href}
                className="text-sm text-zinc-400 transition hover:text-zinc-100"
              >
                {l.label}
              </a>
            </li>
          ))}
        </ul>

        <div className="flex items-center gap-2">
          <a
            href={profile.github}
            target="_blank"
            rel="noreferrer"
            aria-label="GitHub"
            className="rounded-full p-2 text-zinc-400 transition hover:bg-zinc-800/60 hover:text-zinc-100"
          >
            <GithubIcon className="h-4 w-4" />
          </a>
          <a
            href={profile.linkedin}
            target="_blank"
            rel="noreferrer"
            aria-label="LinkedIn"
            className="rounded-full p-2 text-zinc-400 transition hover:bg-zinc-800/60 hover:text-zinc-100"
          >
            <LinkedinIcon className="h-4 w-4" />
          </a>
          <a
            href={`mailto:${profile.email}`}
            aria-label="Email"
            className="rounded-full p-2 text-zinc-400 transition hover:bg-zinc-800/60 hover:text-zinc-100"
          >
            <Mail className="h-4 w-4" />
          </a>
        </div>
      </nav>
    </header>
  );
}
