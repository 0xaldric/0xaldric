type Props = {
  eyebrow: string;
  title: string;
  description?: string;
};

export function SectionHeading({ eyebrow, title, description }: Props) {
  return (
    <div className="mb-10 sm:mb-14">
      <p className="text-xs font-mono uppercase tracking-[0.2em] text-emerald-400/80">
        {eyebrow}
      </p>
      <h2 className="mt-2 text-3xl font-semibold tracking-tight text-zinc-100 sm:text-4xl">
        {title}
      </h2>
      {description ? (
        <p className="mt-3 max-w-2xl text-base text-zinc-400">{description}</p>
      ) : null}
    </div>
  );
}
