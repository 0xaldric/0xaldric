import { profile } from "../data/cv";

export function Footer() {
  return (
    <footer className="border-t border-zinc-800/60">
      <div className="mx-auto flex max-w-5xl flex-col items-start justify-between gap-2 px-4 py-8 text-xs text-zinc-500 sm:flex-row sm:items-center sm:px-6">
        <p>
          © {new Date().getFullYear()} {profile.name} ({profile.alias}). Built
          with React, Vite, Tailwind.
        </p>
        <p className="font-mono">
          <span className="text-emerald-400">$</span> kept simple, shipped fast.
        </p>
      </div>
    </footer>
  );
}
